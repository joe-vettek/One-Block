package xueluoanping.oneblock.handler;

import com.mojang.brigadier.exceptions.CommandSyntaxException;
import net.minecraft.ResourceLocationException;
import net.minecraft.commands.arguments.coordinates.BlockPosArgument;
import net.minecraft.core.BlockPos;
import net.minecraft.core.SectionPos;
import net.minecraft.core.particles.ParticleTypes;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.core.registries.Registries;
import net.minecraft.network.chat.Component;
import net.minecraft.resources.ResourceKey;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.server.MinecraftServer;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.util.AbortableIterationConsumer;
import net.minecraft.world.entity.Entity;
import net.minecraft.world.entity.EntityType;
import net.minecraft.world.entity.MoverType;
import net.minecraft.world.entity.decoration.ArmorStand;
import net.minecraft.world.entity.item.ItemEntity;
import net.minecraft.world.level.ChunkPos;
import net.minecraft.world.level.block.Blocks;
import net.minecraft.world.level.block.StructureBlock;
import net.minecraft.world.level.chunk.ChunkGenerator;
import net.minecraft.world.level.levelgen.structure.BoundingBox;
import net.minecraft.world.level.levelgen.structure.BuiltinStructures;
import net.minecraft.world.level.levelgen.structure.Structure;
import net.minecraft.world.level.levelgen.structure.StructureStart;
import net.minecraft.world.level.levelgen.structure.templatesystem.StructureTemplate;
import net.minecraft.world.phys.AABB;
import net.minecraft.world.phys.Vec3;
import net.minecraftforge.event.TickEvent;
import net.minecraftforge.event.level.LevelEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import xueluoanping.oneblock.OneBlock;
import xueluoanping.oneblock.config.General;
import xueluoanping.oneblock.util.ClientUtils;
import xueluoanping.oneblock.util.PlaceUtil;
import xueluoanping.oneblock.util.RegisterFinderUtil;

import java.util.ConcurrentModificationException;
import java.util.HashMap;
import java.util.Map;
import java.util.Optional;
import java.util.stream.Collectors;

// @Mod.EventBusSubscriber(bus = Mod.EventBusSubscriber.Bus.FORGE, value = Dist.DEDICATED_SERVER)
public class Levelhandler {
    public static Levelhandler instance = new Levelhandler();

    // public static OneBlockSave oneBlockSave;
    public static final Map<ServerLevel, OneBlockSave> oneBlockSaveHolder = new HashMap<>();

    @SubscribeEvent
    public void onLevelLoad(LevelEvent.Load event) {
        if (!event.getLevel().isClientSide())
            for (ServerLevel allLevel : event.getLevel().getServer().getAllLevels()) {
                oneBlockSaveHolder.put(allLevel, OneBlockSave.get(event.getLevel().getServer().overworld()));
            }
    }


    @SubscribeEvent
    public void onLevelSave(LevelEvent.Unload event) {
        if (!event.getLevel().isClientSide())
            oneBlockSaveHolder.clear();
        // oneBlockSave = null;
    }

    // 只需要保持item位置即可
    @SubscribeEvent
    public void onTick(TickEvent.ServerTickEvent event) {
        // OneBlock.logger(System.currentTimeMillis());
        var server = event.getServer();
        for (ServerLevel level : server.getAllLevels()) {
            var oneBlockSave = oneBlockSaveHolder.get(level);
            for (BlockPos pos : oneBlockSave.getBlockPos()) {
                if (level.isLoaded(pos))
                    generateBlock(server, oneBlockSave, level, pos);
            }
        }
        // ServerLevel level = server.overworld();

    }

    private boolean add = false;

    private void generateBlock(MinecraftServer server, OneBlockSave oneBlockSave, ServerLevel level, BlockPos pos) {

        ClientUtils.playASHParticles(level, pos);
        if (level.isEmptyBlock(pos)) {
            var nowProgress = oneBlockSave.get(pos);
            var stageHolder = network.getStage(nowProgress.counter);
            var stage = stageHolder.data();
            nowProgress.name = stage.getResName();
            boolean has_gift = stage.getEnd_gift() != null;
            boolean set_gift = has_gift && stageHolder.stageRemainCount() == 1;
            if (stageHolder.isEnd()) {
                network.setBedrock(level, pos);
                nowProgress.setBedrockLastTime(stage.getCount());
            } else if (set_gift) {
                network.setGif(level, pos, stage.getEnd_gift());
            } else {
                if (stageHolder.isBegin()) {
                    ClientUtils.tittlePlayerClean(server);
                    ClientUtils.informNewStage(server, stage.getResName());
                    // reset the record when a new stage
                    nowProgress.cleanRemain();
                    for (StageData.BlockEntry blockEntry : stage.getList()) {
                        if (blockEntry.getMin_times() > 0) {
                            nowProgress.addRemain(blockEntry.getType(), blockEntry.getGlobalId(), blockEntry.getMin_times());
                        }
                        if (blockEntry.getMax_times() > 0) {
                            nowProgress.addQuota(blockEntry.getType(), blockEntry.getGlobalId(), blockEntry.getMin_times());
                        }
                    }
                }
                // the last is a gift,so we need to prepare
                int remainCount = has_gift ? stageHolder.stageRemainCount() - 1 : stageHolder.stageRemainCount();
                var select = network.setNewBlock(level, pos, stage, remainCount, nowProgress);
                nowProgress.updateRemain(select.getType(), select.getGlobalId());
                nowProgress.updateQuota(select.getType(), select.getGlobalId());
            }
            nowProgress.updateCounter();
            oneBlockSave.update(pos, nowProgress);
            for (ServerPlayer player : level.players()) {
                level.sendParticles(player, ParticleTypes.CLOUD, false, pos.getX() + 0.5, pos.getY() + 0.8, pos.getZ() + 0.5, 3, 0.5, 0.7, 0.5, 0.025);
            }
            // for debug
            if (General.debug.get())
                ClientUtils.informPlayerProgress(server, nowProgress.name, nowProgress.counter);

        } else if (level.getBlockState(pos).is(Blocks.BEDROCK)) {
            var oneBlockSaveInstance = oneBlockSave.get(pos);
            if (oneBlockSaveInstance.bedrockLastTime <= 0) {
                level.removeBlock(pos, false);
            } else {
                int i = oneBlockSaveInstance.bedrockLastTime / 50;
                if (oneBlockSaveInstance.bedrockLastTime % 50 == 0)
                    ClientUtils.tittlePlayer(server, String.valueOf(i));
                oneBlockSaveInstance.updateBedrockLastTime();
                oneBlockSave.update(pos, oneBlockSaveInstance);
            }
        }
        if (General.collectItemNearby.get()) {
            try {
                double x = pos.getX() + 0.5;
                double y = pos.getY() + 1;
                double z = pos.getZ() + 0.5;
                var aabb = new AABB(new Vec3(x - 1.5, y - 1, z - 1.5), new Vec3(x + 1.5, y + 1.25, z + 1.5));
                level.getEntities().get(EntityType.ITEM, aabb, itemEntity -> {
                    // if (entity instanceof ItemEntity itemEntity)
                    {
                        itemEntity.syncPacketPositionCodec(x, y, z);
                        itemEntity.moveTo(new Vec3(x, y, z));
                    }
                    return AbortableIterationConsumer.Continuation.CONTINUE;
                });
            } catch (ConcurrentModificationException e) {
                e.printStackTrace();
            }
        }

    }
}
