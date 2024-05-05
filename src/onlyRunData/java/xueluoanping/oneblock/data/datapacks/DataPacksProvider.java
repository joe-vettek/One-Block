package xueluoanping.oneblock.data.datapacks;

import com.google.common.collect.Maps;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.mojang.logging.LogUtils;
import com.simibubi.create.AllBlocks;
import net.minecraft.data.CachedOutput;
import net.minecraft.data.DataGenerator;
import net.minecraft.data.DataProvider;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.world.level.storage.loot.LootTable;
import org.jetbrains.annotations.NotNull;
import org.slf4j.Logger;
import xueluoanping.oneblock.ModConstants;
import xueluoanping.oneblock.OneBlock;
import xueluoanping.oneblock.handler.StageData;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.CompletableFuture;
import java.util.function.Supplier;



public class DataPacksProvider implements DataProvider {
    private static final Logger LOGGER = LogUtils.getLogger();
    private static final Gson GSON = new GsonBuilder().setPrettyPrinting().disableHtmlEscaping().create();
    private static final Map<String, Map<ResourceLocation, Supplier<LootTable.Builder>>> BLOCK_LOOTS = new HashMap<>();
    private final DataGenerator generator;
    
    public DataPacksProvider(DataGenerator generator) {
        this.generator = generator;
    }
    
    @Override
    public @NotNull CompletableFuture<?> run(@NotNull CachedOutput cache) {
        Path outputFolder = this.generator.getPackOutput().getOutputFolder();
        String modid="oneblock-extra-" + "create";
        Path datapackFolder = outputFolder.resolve("datapacks/"+modid);
        Map<ResourceLocation, StageData> map = Maps.newHashMap();
        var s=new StageData();
        s.setResourceLocation(new ResourceLocation(modid,"phases/test"));
        s.setList(new ArrayList<>());
        var be = new StageData.BlockEntry(ModConstants.TYPE_BLOCK, AllBlocks.ZINC_ORE.getId().toString());
        s.getList().add(be);
        map.put(s.getResourceLocation(),s);
        // need clean cache
        map.forEach((id, stageData) -> {
            Path path = createPhasesPath(datapackFolder, stageData.getResourceLocation());
            stageData.setResourceLocation(null);
            DataProvider.saveStable(cache, stageData.toJson(), path);
        });
        DataProvider.saveStable(cache,new ResourcePackInfo().toJson(),createMetaPath(datapackFolder));
        return CompletableFuture.runAsync(() -> {
        });
    }

    @Override
    public String getName() {
        return "Datapacks: " + OneBlock.MOD_ID;
    }

    protected static Path createPhasesPath(Path path, ResourceLocation id) {
        return path.resolve("data/" + id.getNamespace() + "/oneblock/" + id.getPath() + ".json");
    }

    protected static Path createMetaPath(Path path) {
        return path.resolve("pack.mcmeta");
    }

    public static void writeToFile(String filePath, String content) {
        try {
            BufferedWriter writer = new BufferedWriter(new FileWriter(filePath));
            writer.write(content);
            writer.close();
        } catch (IOException e) {
        }
    }

}
