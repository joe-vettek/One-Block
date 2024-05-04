package xueluoanping.oneblock;


import net.minecraft.resources.ResourceLocation;
import net.minecraftforge.common.MinecraftForge;
import net.minecraftforge.data.event.GatherDataEvent;
import net.minecraftforge.fml.ModLoadingContext;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.config.ModConfig;
import net.minecraftforge.fml.event.lifecycle.FMLClientSetupEvent;
import net.minecraftforge.fml.event.lifecycle.FMLCommonSetupEvent;
import net.minecraftforge.fml.event.lifecycle.InterModEnqueueEvent;
import net.minecraftforge.fml.event.lifecycle.InterModProcessEvent;
import net.minecraftforge.fml.javafmlmod.FMLJavaModLoadingContext;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import xueluoanping.oneblock.config.General;
import xueluoanping.oneblock.data.start;
import xueluoanping.oneblock.handler.Levelhandler;
import xueluoanping.oneblock.handler.ReloadHandler;

import java.util.Objects;

// The value here should match an entry in the META-INF/mods.toml file
@Mod(OneBlock.MOD_ID)
public class OneBlock {
    public static final String MOD_ID = "oneblock";
    // Directly reference a log4j logger.
    public static final Logger LOGGER = LogManager.getLogger();

    public static final boolean useLogger = Objects.equals(System.getProperty("forgegradle.runs.dev"), "true");

    public OneBlock() {
        // Register the setup method for modloading
        FMLJavaModLoadingContext.get().getModEventBus().addListener(this::setup);
        // Register the enqueueIMC method for modloading
        FMLJavaModLoadingContext.get().getModEventBus().addListener(this::enqueueIMC);
        // Register the processIMC method for modloading
        FMLJavaModLoadingContext.get().getModEventBus().addListener(this::processIMC);
        // Register the doClientStuff method for modloading
        FMLJavaModLoadingContext.get().getModEventBus().addListener(this::doClientStuff);

        FMLJavaModLoadingContext.get().getModEventBus().addListener(this::gatherData);

        // Register ourselves for server and other game events we are interested in
        MinecraftForge.EVENT_BUS.register(this);
        // MinecraftForge.EVENT_BUS.register(TreeGrowHandler.instance);
        ModContents.BLOCK_DEFERRED_REGISTER.register(FMLJavaModLoadingContext.get().getModEventBus());
        ModContents.ITEM_DEFERRED_REGISTER.register(FMLJavaModLoadingContext.get().getModEventBus());
        ModContents.BLOCK_ENTITY_TYPE_DEFERRED_REGISTER.register(FMLJavaModLoadingContext.get().getModEventBus());
        ModContents.LOOT_MODIFIERS.register(FMLJavaModLoadingContext.get().getModEventBus());


        MinecraftForge.EVENT_BUS.register(Levelhandler.instance);
        MinecraftForge.EVENT_BUS.register(ReloadHandler.instance);
        MinecraftForge.EVENT_BUS.register(ReloadHandler.instance);

        ModLoadingContext.get().registerConfig(ModConfig.Type.COMMON, General.COMMON_CONFIG);
        FMLJavaModLoadingContext.get().getModEventBus().addListener(ReloadHandler::onAddPackFindersEvent);

    }


    private void setup(final FMLCommonSetupEvent event) {
        // some preinit code
        //        LOGGER.info("HELLO FROM PREINIT");
        //        LOGGER.info("DIRT BLOCK >> {}", Blocks.DIRT.getRegistryName());
    }

    private void doClientStuff(final FMLClientSetupEvent event) {
        // do something that can only be done on the client
        //        LOGGER.info("Got game settings {}", event.getMinecraftSupplier().get().options);
    }

    private void enqueueIMC(final InterModEnqueueEvent event) {
        // some example code to dispatch IMC to another mod
        //        InterModComms.sendTo("examplemod", "helloworld", () -> { LOGGER.info("Hello world from the MDK"); return "Hello world";});
    }

    private void processIMC(final InterModProcessEvent event) {
        // some example code to receive and process InterModComms from other mods
        //        LOGGER.info("Got IMC {}", event.getIMCStream().
        //                map(m->m.getMessageSupplier().get()).
        //                collect(Collectors.toList()));

    }


    // You can use EventBusSubscriber to automatically subscribe events on the contained class (this is subscribing to the MOD
    // Event bus for receiving Registry Events)
    // @Mod.EventBusSubscriber(bus = Mod.EventBusSubscriber.Bus.MOD)
    // public static class RegistryEvents {
    //     @SubscribeEvent
    //     public static void onBlocksRegistry(final RegistryEvent.Register<Block> blockRegistryEvent) {
    //         // register a new block here
    //         //            LOGGER.info("HELLO from Register Block");
    //     }
    // }

    public void gatherData(final GatherDataEvent event) {
        // Resources.MANAGER.gatherData();

        // GatherDataHelper.gatherAllData(
        //         MOD_ID,
        //         event,
        //         SoilProperties.REGISTRY,
        //         Family.REGISTRY,
        //         Species.REGISTRY,
        //         LeavesProperties.REGISTRY
        // );
        start.dataGen(event);
    }

    public static void logger(Object... x) {
        if (useLogger) {
            LOGGER.info(getStr(x));
        }
    }

    public static String getStr(Object... x) {
        StringBuilder output = new StringBuilder();
        for (Object i : x) {
            output.append(i).append(" ");
        }
        return output.toString();
    }

    public static void error(Object... x) {
        LOGGER.error(getStr(x));
    }

    public static ResourceLocation rl(String name) {
        return new ResourceLocation(OneBlock.MOD_ID, name);
    }
}
