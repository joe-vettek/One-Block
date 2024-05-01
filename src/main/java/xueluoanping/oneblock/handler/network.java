package xueluoanping.oneblock.handler;

import java.util.*;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonElement;


import net.minecraft.core.BlockPos;
import net.minecraft.core.Direction;
import net.minecraft.network.chat.Component;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.server.packs.resources.ResourceManager;
import net.minecraft.server.packs.resources.SimpleJsonResourceReloadListener;
import net.minecraft.util.profiling.ProfilerFiller;
import net.minecraft.world.level.block.Blocks;
import net.minecraft.world.level.block.ChestBlock;
import net.minecraft.world.level.block.entity.RandomizableContainerBlockEntity;
import xueluoanping.oneblock.OneBlock;
import xueluoanping.oneblock.config.General;
import xueluoanping.oneblock.util.ClientUtils;
import xueluoanping.oneblock.util.PlaceUtil;


// https://github.com/teaconmc/SignMeUp/blob/1.18-forge/src/main/java/org/teacon/signin/data/GuideMapManager.java
public class network extends SimpleJsonResourceReloadListener {
    private static final Gson GSON = new GsonBuilder().setLenient()
            .registerTypeHierarchyAdapter(Component.class, new Component.Serializer())
            .create();

    // public static final network instance = new network(GSON, "stages.config");
    public static final network instance2 = new network(GSON, "oneblock");
    public static final List<StageData> STAGE_DATA_LIST = new ArrayList<>();

    // public static OneBlockConfig oneBlockConfig = new OneBlockConfig();

    record StageHolder(StageData data, boolean isBegin, boolean isEnd, int stageRemainCount) {
    }

    public static int getStageStartPos(ResourceLocation resourceLocation) {
        // it means we set the first block
        int pos = 0;
        int size = STAGE_DATA_LIST.size();
        for (int i = 0; i < size; i++) {
            StageData stageData = STAGE_DATA_LIST.get(i);
            if (i == size - 1 || stageData.getResourceLocation().compareTo(resourceLocation) == 0) {

                break;
            } else {
                pos += stageData.getCount();
                // because a bedrock cost a counter, so we need to +1 if we have set the bedrock
                pos++;
            }
        }
        return pos;
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
            if (i < size - 1 && data.getCount() > 0) {
                int count = data.getCount();
                count = Math.max(count, 0);
                progress -= data.getCount();
                if (progress < 0) {
                    stageData = data;
                    is_begin = (count + progress == 0 || lastProgress == 0) && count != 0;
                    is_end = lastProgress > 1 && count + progress + 1 == 0;
                    stageRemainCount = -progress;
                    break;
                }
                // because a bedrock cost a counter, so we need to -1 if we have set the bedrock
                progress--;

            } else {
                // a bedrock is set before the stage so we need
                if (progress == -1) {
                    is_end = true;
                } else if (progress == 0) {
                    is_begin = true;
                }
                stageData = data;
                if (data.getCount() < 0) {
                    // due to it was set -1 to go endless so we need update the remain to get the local progress
                    stageRemainCount = -(progress - data.getCount())-1;
                }else{
                    progress -= data.getCount();
                    stageRemainCount = -progress;
                }
                break;
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

    public static StageData.BlockEntry setNewBlock(ServerLevel level, BlockPos basePos, StageData stage, int remain, OneBlockProgress nowProgress) {
        // remain less than 0 if endless stage
        var select = stage.selectRandomByWeight(level.getRandom(), nowProgress, nowProgress.getRemainAmount() >= remain&&remain>0, stage.getCount() - remain);
        PlaceUtil.placeSelect(level, basePos, select);
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
        var subStageDataList = new ArrayList<StageData>();
        objects.forEach((res, json) -> {
            OneBlock.logger(json.toString(), res);
            if (res.toString().contains("phases")) {
                StageData stageData = gson.fromJson(json, StageData.class);
                stageData.setResourceLocation(res);
                if (stageData.getTarget() == null)
                    STAGE_DATA_LIST.add(stageData);
                else subStageDataList.add(stageData);
            }
            // Cuisine.logger(Minecraft.getInstance().isLocalServer());
        });
        // clean extra data
        var oneBlockConfig = General.getOrder();
        var removeList = new ArrayList<StageData>();
        for (StageData s : STAGE_DATA_LIST) {
            if (!oneBlockConfig.contains(s.getResourceLocation().toString())) {
                removeList.add(s);
            }
        }
        STAGE_DATA_LIST.removeAll(removeList);

        // sort
        STAGE_DATA_LIST.sort(Comparator.comparing(
                e -> oneBlockConfig.indexOf(e.getResourceLocation().toString())
        ));


        // add sub target
        for (StageData subData : subStageDataList) {
            for (int i = 0; i < STAGE_DATA_LIST.size(); i++) {
                var data = STAGE_DATA_LIST.get(i);
                if (data.getResourceLocation().toString().equals(subData.getTarget())) {
                    data.getList().addAll(subData.getList());
                    break;
                }
            }
        }
    }


}
