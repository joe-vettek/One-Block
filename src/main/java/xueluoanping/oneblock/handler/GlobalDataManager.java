package xueluoanping.oneblock.handler;

import net.minecraft.core.BlockPos;
import net.minecraft.nbt.CompoundTag;
import net.minecraft.nbt.ListTag;
import net.minecraft.nbt.Tag;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.level.Level;
import net.minecraft.world.level.saveddata.SavedData;
import net.minecraft.world.level.storage.DimensionDataStorage;
import org.jetbrains.annotations.NotNull;
import xueluoanping.oneblock.api.StageProgress;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;


// Todo: clean remain counter in future
public class GlobalDataManager extends SavedData {

    private final Map<BlockPos, StageProgress> chunkPosData = new HashMap<>();

    private String hashStageVersion="";

    public GlobalDataManager() {
    }

    public GlobalDataManager(CompoundTag tag) {

        ListTag list = tag.getList("oneblock", Tag.TAG_COMPOUND);
        for (Tag t : list) {
            CompoundTag manaTag = (CompoundTag) t;
            BlockPos chunkPos = new BlockPos(manaTag.getInt("x"), manaTag.getInt("y"), manaTag.getInt("z"));
            var p = new StageProgress
                    (manaTag.getString("name"), manaTag.getInt("counter"));
            if (manaTag.contains("bedrockLastTime"))
                p.counter = manaTag.getInt("bedrockLastTime");
            if (manaTag.contains("remainCounter"))
                p.remainCounter = manaTag.getList("remainCounter", ListTag.TAG_COMPOUND);
            if (manaTag.contains("quotaCounter"))
                p.quotaCounter = manaTag.getList("quotaCounter", ListTag.TAG_COMPOUND);
            if (manaTag.contains("precedenceCounter"))
                p.precedenceCounter = manaTag.getList("precedenceCounter", ListTag.TAG_COMPOUND);
            chunkPosData.put(chunkPos, p);
        }

        if (tag.contains("oneblockVersion")){
            hashStageVersion=tag.getString("oneblockVersion");
        }
    }

    // public void update(BlockPos blockPos) {
    //     // if(fluidDrawerControllerSave!=null){
    //     var p = get(blockPos);
    //     p.counter++;
    //     chunkPosData.put(blockPos, p);
    //     setDirty();
    //     // }else fluidDrawerControllerSave=new FluidDrawerControllerSave();
    // }

    public void update(BlockPos blockPos, StageProgress progress) {
        chunkPosData.put(blockPos, progress);
        setDirty();
    }

    public StageProgress getOrDefault(BlockPos pos) {
        return chunkPosData.getOrDefault(pos, new StageProgress());
    }

    public StageProgress get(BlockPos pos) {
        return chunkPosData.get(pos);
    }

    public BlockPos remove(BlockPos blockPos) {
        var remove = chunkPosData.remove(blockPos);
        setDirty();
        return remove == null ? null : blockPos;
    }

    public Set<BlockPos> getBlockPos() {
        return chunkPosData.keySet();
    }

    @Override
    public @NotNull CompoundTag save(CompoundTag tag) {
        ListTag list = new ListTag();
        chunkPosData.forEach((chunkPos, mana) -> {
            CompoundTag manaTag = new CompoundTag();
            manaTag.putInt("x", chunkPos.getX());
            manaTag.putInt("y", chunkPos.getY());
            manaTag.putInt("z", chunkPos.getZ());
            manaTag.putString("name", mana.name);
            manaTag.putInt("counter", mana.counter);
            manaTag.put("remainCounter", mana.remainCounter);
            manaTag.put("quotaCounter", mana.quotaCounter);
            manaTag.put("precedenceCounter", mana.precedenceCounter);
            list.add(manaTag);
        });
        tag.put("oneblock", list);
        tag.putString("hashStageVersion","");
        return tag;
    }

    public static GlobalDataManager get(Level worldIn) {
        if (!(worldIn instanceof ServerLevel)) {
            throw new RuntimeException("Attempted to get the data from a client world. This is wrong.");
        }
        // ServerLevel world = worldIn.getServer().getLevel(Level.OVERWORLD);
        ServerLevel world = (ServerLevel) worldIn;

        DimensionDataStorage storage = world.getDataStorage();
        return storage.computeIfAbsent(GlobalDataManager::new, GlobalDataManager::new, "oneblock");
    }


}
