package xueluoanping.oneblock.handler;

import net.minecraft.core.BlockPos;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.server.packs.resources.PreparableReloadListener;
import net.minecraft.server.packs.resources.ResourceManager;
import net.minecraft.tags.BlockTags;
import net.minecraft.util.profiling.ProfilerFiller;
import net.minecraft.world.item.CreativeModeTabs;
import net.minecraft.world.level.block.Block;
import net.minecraftforge.event.AddReloadListenerEvent;
import net.minecraftforge.event.BuildCreativeModeTabContentsEvent;
import net.minecraftforge.event.RegisterCommandsEvent;
import net.minecraftforge.event.TickEvent;
import net.minecraftforge.event.level.LevelEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import xueluoanping.oneblock.ModContents;

import java.util.concurrent.CompletableFuture;
import java.util.concurrent.Executor;
import java.util.stream.Collectors;

// @Mod.EventBusSubscriber(bus = Mod.EventBusSubscriber.Bus.FORGE, value = Dist.DEDICATED_SERVER)
public class ReloadHandler {
    public static ReloadHandler instance = new ReloadHandler();

    // @SubscribeEvent
    // public void onLevelLoad(LevelEvent.Load event) {
    // }
    //
    // @SubscribeEvent
    // public void onLevelSave(LevelEvent.Save event) {
    //
    // }

    @SubscribeEvent
    public void onAddReloadListener(AddReloadListenerEvent event) {
        // event.addListener(network.instance);
        event.addListener(network.instance2);

    }

    @SubscribeEvent
    public void onRegisterCommands(RegisterCommandsEvent event) {
    }



}
