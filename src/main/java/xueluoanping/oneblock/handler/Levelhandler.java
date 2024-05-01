package xueluoanping.oneblock.handler;

import net.minecraft.core.BlockPos;
import net.minecraft.core.particles.ParticleTypes;
import net.minecraft.server.MinecraftServer;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.util.AbortableIterationConsumer;
import net.minecraft.world.entity.EntityType;
import net.minecraft.world.level.block.Blocks;
import net.minecraft.world.phys.AABB;
import net.minecraft.world.phys.Vec3;
import net.minecraftforge.event.TickEvent;
import net.minecraftforge.event.level.LevelEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import xueluoanping.oneblock.OneBlock;
import xueluoanping.oneblock.config.General;
import xueluoanping.oneblock.util.ClientUtils;

import java.util.ConcurrentModificationException;
import java.util.HashMap;
import java.util.Map;

// @Mod.EventBusSubscriber(bus = Mod.EventBusSubscriber.Bus.FORGE, value = Dist.DEDICATED_SERVER)
public class Levelhandler {
    public static Levelhandler instance = new Levelhandler();

    // public static OneBlockSave oneBlockSave;
    public static final Map<ServerLevel, OneBlockSave> oneBlockSaveHolder = new HashMap<>();


    public static OneBlockSave getSaveData(ServerLevel level) {
        return oneBlockSaveHolder.get(level);
    }

    @SubscribeEvent
    public void onLevelLoad(LevelEvent.Load event) {
        if (!event.getLevel().isClientSide())
            for (ServerLevel allLevel : event.getLevel().getServer().getAllLevels()) {
                oneBlockSaveHolder.put(allLevel, OneBlockSave.get(allLevel));
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
            var oneBlockSave = getSaveData(level);
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
        // Player always dig it and we not get
        if (level.isEmptyBlock(pos)) {
            if (General.debug.get())
                OneBlock.logger("Start Set at ", System.currentTimeMillis());
            var nowProgress = oneBlockSave.getOrDefault(pos);
            var stageHolder = network.getStage(nowProgress.counter);
            var stage = stageHolder.data();
            nowProgress.name = stage.getResName();
            boolean has_gift = stage.getEnd_gift() != null;
            boolean set_gift = has_gift && stageHolder.stageRemainCount() == 1;
            if (stageHolder.isEnd()) {
                network.setBedrock(level, pos);
                nowProgress.setBedrockLastTime(stage.getCount() > 0 ? stage.getCount() : 50 * 60);
            } else if (set_gift) {
                network.setGif(level, pos, stage.getEnd_gift());
            } else {
                if (stageHolder.isBegin()) {
                    ClientUtils.tittlePlayerClean(server);
                    ClientUtils.informNewStage(server, stage.getResName());
                    // reset the record when a new stage
                    nowProgress.cleanLocalCounter();
                    for (StageData.BlockEntry blockEntry : stage.getList()) {
                        if (blockEntry.getMin_times() > 0) {
                            nowProgress.addRemain(blockEntry.getType(), blockEntry.getGlobalId(), blockEntry.getMin_times());
                        }
                        if (blockEntry.getMax_times() > 0) {
                            nowProgress.addQuota(blockEntry.getType(), blockEntry.getGlobalId(), blockEntry.getMin_times());
                        }
                        if (blockEntry.getTimes() > 0) {
                            nowProgress.addRemain(blockEntry.getType(), blockEntry.getGlobalId(), blockEntry.getMin_times());
                            nowProgress.addQuota(blockEntry.getType(), blockEntry.getGlobalId(), blockEntry.getMin_times());
                        }
                        if (blockEntry.getPrecedence_start() != 0 || blockEntry.getPrecedence_end() != 0) {
                            int start = blockEntry.getPrecedence_start() >= 0 ? blockEntry.getPrecedence_start() : stage.getCount() + blockEntry.getPrecedence_start() + 1;
                            int end = blockEntry.getPrecedence_end() >= 0 ? blockEntry.getPrecedence_end() : stage.getCount() + blockEntry.getPrecedence_end() + 1;
                            nowProgress.addPrecedence(blockEntry.getType(), blockEntry.getGlobalId(), start, end);
                        }
                        if (blockEntry.getPrecedence() != 0) {
                            int precedence = blockEntry.getPrecedence() > 0 ? blockEntry.getPrecedence() : stage.getCount() + blockEntry.getPrecedence() + 1;
                            nowProgress.addPrecedence(blockEntry.getType(), blockEntry.getGlobalId(), precedence, precedence);
                        }
                    }
                }
                // the last is a gift,so we need to prepare
                int remainCount = has_gift ? stageHolder.stageRemainCount() - 1 : stageHolder.stageRemainCount();
                var select = network.setNewBlock(level, pos, stage, remainCount, nowProgress);

                nowProgress.updateLocalCounter(select.getType(), select.getGlobalId());
            }
            nowProgress.updateCounter();
            oneBlockSave.update(pos, nowProgress);
            for (ServerPlayer player : level.players()) {
                level.sendParticles(player, ParticleTypes.CLOUD, false, pos.getX() + 0.5, pos.getY() + 0.8, pos.getZ() + 0.5, 3, 0.5, 0.7, 0.5, 0.025);
            }
            // for debug
            if (General.debug.get())
                ClientUtils.informPlayerProgress(server, nowProgress.name, nowProgress.counter);

            if (General.debug.get())
                OneBlock.logger("End Set at ", System.currentTimeMillis());
        } else if (level.getBlockState(pos).is(Blocks.BEDROCK)) {
            var oneBlockSaveInstance = oneBlockSave.getOrDefault(pos);
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
