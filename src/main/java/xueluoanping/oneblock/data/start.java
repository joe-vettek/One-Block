package xueluoanping.oneblock.data;

import net.minecraft.core.HolderLookup;
import net.minecraft.data.DataGenerator;
import net.minecraft.data.PackOutput;
import net.minecraftforge.common.data.ExistingFileHelper;
import net.minecraftforge.data.event.GatherDataEvent;
import xueluoanping.oneblock.OneBlock;
import xueluoanping.oneblock.data.blockstate.ItemModelProvider;
import xueluoanping.oneblock.data.lang.Lang_EN;
import xueluoanping.oneblock.data.lang.Lang_ZH;
import xueluoanping.oneblock.data.loot.GLMProvider;

import java.util.concurrent.CompletableFuture;


public class start {
    public final static String MODID = OneBlock.MOD_ID;

    public static void dataGen(GatherDataEvent event) {
        DataGenerator generator = event.getGenerator();
        ExistingFileHelper helper = event.getExistingFileHelper();
        PackOutput packOutput = generator.getPackOutput();
        CompletableFuture<HolderLookup.Provider> lookupProvider = event.getLookupProvider();
        if (event.includeServer()) {
            OneBlock.logger("Generate We Data!!!");

            // TagsDataProvider blockTags = new TagsDataProvider(packOutput,lookupProvider, MODID, helper);
            // generator.addProvider(event.includeServer(),blockTags);
            // generator.addProvider(event.includeServer(),new FDLItemTagsProvider(packOutput, lookupProvider, blockTags.contentsGetter()));
            //
            // generator.addProvider(event.includeServer(),new LFTLootTableProvider(packOutput));
            // generator.addProvider(event.includeServer(),new GLMProvider(packOutput, MODID));
        }
        if (event.includeClient()) {
            generator.addProvider(event.includeClient(),new ItemModelProvider(packOutput,helper));
            generator.addProvider(event.includeClient(),new Lang_EN(packOutput,helper));
            generator.addProvider(event.includeClient(),new Lang_ZH(packOutput,helper));
        }


    }
}
