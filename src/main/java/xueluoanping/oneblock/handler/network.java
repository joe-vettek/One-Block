package xueluoanping.oneblock.handler;

import java.util.*;
import java.util.concurrent.atomic.AtomicReference;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonElement;


import net.minecraft.core.BlockPos;
import net.minecraft.core.Direction;
import net.minecraft.core.particles.ParticleTypes;
import net.minecraft.network.chat.Component;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.server.packs.resources.ResourceManager;
import net.minecraft.server.packs.resources.SimpleJsonResourceReloadListener;
import net.minecraft.util.profiling.ProfilerFiller;
import net.minecraft.world.entity.MobSpawnType;
import net.minecraft.world.level.block.Blocks;
import net.minecraft.world.level.block.ChestBlock;
import net.minecraft.world.level.block.entity.BrushableBlockEntity;
import net.minecraft.world.level.block.entity.RandomizableContainerBlockEntity;
import xueluoanping.oneblock.ModConstants;
import xueluoanping.oneblock.OneBlock;
import xueluoanping.oneblock.client.OneBlockTranslator;
import xueluoanping.oneblock.util.ClientUtils;
import xueluoanping.oneblock.util.CommandUtils;
import xueluoanping.oneblock.util.PlaceUtil;
import xueluoanping.oneblock.util.RegisterFinderUtil;


// https://github.com/teaconmc/SignMeUp/blob/1.18-forge/src/main/java/org/teacon/signin/data/GuideMapManager.java
public class network extends SimpleJsonResourceReloadListener {
    private static final Gson GSON = new GsonBuilder().setLenient()
            .registerTypeHierarchyAdapter(Component.class, new Component.Serializer())
            .create();

    // public static final network instance = new network(GSON, "stages.config");
    public static final network instance2 = new network(GSON, "oneblock");
    public static final List<StageData> STAGE_DATA_LIST = new ArrayList<>();

    public static OneBlockConfig oneBlockConfig = new OneBlockConfig();

    record StageHolder(StageData data, boolean isBegin, boolean isEnd, int stageRemainCount) {
    }

    public static StageHolder getStage(int lastProgress) {
        StageData stageData = null;
        boolean is_begin = false;
        boolean is_end = false;
        int stageRemainCount = 0;

        int progress = lastProgress;
        int size = STAGE_DATA_LIST.size();
        for (int i = 0; i < size; i++) {
            StageData data = STAGE_DATA_LIST.get(i);
            if (i < size - 1) {
                progress -= data.getCount();
                if (progress < 0) {
                    stageData = data;
                    is_begin = stageData.getCount() + progress == 0 || lastProgress == 0;
                    is_end = lastProgress > 1 && stageData.getCount() + progress + 1 == 0;
                    stageRemainCount = -progress;
                    break;
                }
                // because a bedrock cost a counter, so we need to -1 if we have set the bedrock
                progress--;

            } else {
                // a bedrock is set before the stage so we need
                if (progress == 1) {
                    is_begin = true;
                }
                stageData = data;
                stageRemainCount = Integer.MAX_VALUE;
            }

        }

        return new StageHolder(stageData, is_begin, is_end, stageRemainCount);
    }

    public static void setBedrock(ServerLevel level, BlockPos pos) {
        level.setBlockAndUpdate(pos, Blocks.BEDROCK.defaultBlockState());
    }

    public static void setGif(ServerLevel level, BlockPos pos, String lootTable) {
        var block = Blocks.CHEST;
        level.setBlockAndUpdate(pos, block.defaultBlockState().setValue(ChestBlock.FACING, Direction.EAST));
        if (level.getBlockEntity(pos) instanceof RandomizableContainerBlockEntity entity)
            entity.setLootTable(new ResourceLocation(lootTable), level.getSeed());
        ClientUtils.playHEARTParticles(level, pos);
    }

    public static StageData.BlockEntry setNewBlock(ServerLevel level, BlockPos pos, StageData stage, int remain, OneBlockProgress nowProgress) {
        var select = stage.selectRandomByWeight(level.getRandom(), nowProgress, nowProgress.getRemainAmount() >= remain);
        if (Objects.equals(select.getType(), ModConstants.TYPE_BLOCK)) {
            var block = RegisterFinderUtil.getBlock(select.getId());
            level.setBlockAndUpdate(pos, block.defaultBlockState());
        } else if (Objects.equals(select.getType(), ModConstants.TYPE_GIFT)) {
            // to avoid some problem the gift use id as res
            var block = Blocks.CHEST;
            level.setBlockAndUpdate(pos, block.defaultBlockState().setValue(ChestBlock.FACING, Direction.EAST));
            if (level.getBlockEntity(pos) instanceof RandomizableContainerBlockEntity containerBlockEntity)
                containerBlockEntity.setLootTable(new ResourceLocation(select.getId()), level.getSeed());
        } else if (Objects.equals(select.getType(), ModConstants.TYPE_ARCHAEOLOGY)) {
            var block = RegisterFinderUtil.getBlock(select.getId());
            level.setBlockAndUpdate(pos, block.defaultBlockState());
            if (level.getBlockEntity(pos) instanceof BrushableBlockEntity brushableBlockEntity)
                brushableBlockEntity.setLootTable(new ResourceLocation(select.getLoot_table()), level.getSeed());
        } else if (Objects.equals(select.getType(), ModConstants.TYPE_MOB)) {
            var mob = RegisterFinderUtil.getEntity(select.getId());
            for (int i = 0; i < select.getCount(); i++) {
                var entity = mob.spawn(level, pos.above(2), MobSpawnType.NATURAL);
                if (entity != null) {
                    entity.moveTo(pos.getX() + 0.5 + 0.05 * i, pos.getY() + 1.6, pos.getZ() + 0.5 + 0.05 * i);
                    entity.setCustomName(Component.translatable(OneBlockTranslator.getCustomName("mob")));
                }
            }
            ClientUtils.playSpawnSound(level, pos);
            ClientUtils.playCloudParticles(level, pos);
        } else if (Objects.equals(select.getType(), ModConstants.TYPE_TEMPLATE)) {
            PlaceUtil.placeTemplate(level, pos, new ResourceLocation(select.getId()));
        } else if (Objects.equals(select.getType(), ModConstants.TYPE_STRUCTURE)) {
            PlaceUtil.placeStructure(level, pos, new ResourceLocation(select.getId()));
        } else if (Objects.equals(select.getType(), ModConstants.TYPE_CONFIGURED_FEATURE)) {
            PlaceUtil.placeFeature(level, pos, new ResourceLocation(select.getId()));
        } else if (Objects.equals(select.getType(), ModConstants.TYPE_COMMAND)) {
            CommandUtils.performCommand(level.getServer(), pos, select.getId());
        }
        return select;
    }

    public network(Gson json, String s) {
        super(json, s);
        OneBlock.logger("data init");
    }

    @Override
    protected void apply(Map<ResourceLocation, JsonElement> objects, ResourceManager manager, ProfilerFiller profiler) {
        OneBlock.logger("Hello Profile");
        STAGE_DATA_LIST.clear();
        Gson gson = new GsonBuilder().create();
        AtomicReference<OneBlockConfig> config = new AtomicReference<>();
        var subStageDataList = new ArrayList<StageData>();
        objects.forEach((res, json) -> {
            OneBlock.logger(json.toString(), res);
            if (res.toString().contains("phases")) {
                StageData stageData = gson.fromJson(json, StageData.class);
                stageData.setResourceLocation(res);
                if (stageData.getSub_target() == null)
                    STAGE_DATA_LIST.add(stageData);
                else subStageDataList.add(stageData);
            } else if (res.toString().contains("config")) {
                config.set(gson.fromJson(json, OneBlockConfig.class));
            }
            // Cuisine.logger(Minecraft.getInstance().isLocalServer());
        });
        // clean extra data
        oneBlockConfig = config.get();
        var removeList = new ArrayList<StageData>();
        for (StageData s : STAGE_DATA_LIST) {
            if (!oneBlockConfig.getOrder().contains(s.getResourceLocation().toString())) {
                removeList.add(s);
            }
        }
        STAGE_DATA_LIST.removeAll(removeList);

        // sort
        STAGE_DATA_LIST.sort(Comparator.comparing(
                e -> oneBlockConfig.getOrder().indexOf(e.getResourceLocation().toString())
        ));


        // add sub target
        for (StageData subData : subStageDataList) {
            for (int i = 0; i < STAGE_DATA_LIST.size(); i++) {
                var data = STAGE_DATA_LIST.get(i);
                if (data.getResourceLocation().toString().equals(subData.getSub_target())) {
                    data.getList().addAll(subData.getList());
                    break;
                }
            }
        }
    }


}
