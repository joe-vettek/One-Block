package xueluoanping.oneblock.data;

import net.minecraft.core.HolderLookup;
import net.minecraft.data.DataGenerator;
import net.minecraft.data.PackOutput;
import net.minecraftforge.common.data.ExistingFileHelper;
import net.minecraftforge.data.event.GatherDataEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;
import xueluoanping.oneblock.OneBlock;
import xueluoanping.oneblock.data.datapacks.DataPacksProvider;

import java.util.concurrent.CompletableFuture;


@Mod.EventBusSubscriber(bus = Mod.EventBusSubscriber.Bus.MOD)
public class start_d {
    public final static String MODID = OneBlock.MOD_ID;

    @SubscribeEvent
    public static void dataGen(GatherDataEvent event) {
        DataGenerator generator = event.getGenerator();
        ExistingFileHelper helper = event.getExistingFileHelper();
        PackOutput packOutput = generator.getPackOutput();
        CompletableFuture<HolderLookup.Provider> lookupProvider = event.getLookupProvider();
        if (event.includeServer()) {
            OneBlock.logger("Generate We Data!!!");
            generator.addProvider(event.includeServer(), new DataPacksProvider(generator));
        }
        if (event.includeClient()) {
        }


    }
}
