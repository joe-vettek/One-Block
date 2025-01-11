package xueluoanping.oneblock.client;


import net.minecraft.client.renderer.RenderType;
import net.minecraft.world.item.CreativeModeTabs;
import net.minecraft.world.item.ItemStack;
import net.minecraftforge.api.distmarker.Dist;
import net.minecraftforge.api.distmarker.OnlyIn;
import net.minecraftforge.client.event.EntityRenderersEvent;
import net.minecraftforge.event.BuildCreativeModeTabContentsEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.event.lifecycle.FMLClientSetupEvent;
import xueluoanping.oneblock.ModContents;
import xueluoanping.oneblock.OneBlock;

@Mod.EventBusSubscriber(bus = Mod.EventBusSubscriber.Bus.MOD, value = Dist.CLIENT)
public class ClientSetup {

    @SubscribeEvent
    public static void onClientEvent(FMLClientSetupEvent event) {
        OneBlock.logger("Register Client");
        event.enqueueWork(() -> {

        });
    }


    @SubscribeEvent
    public static void onBuildCreativeModeTabContentsEvent(BuildCreativeModeTabContentsEvent event) {
        if (event.getTabKey() == CreativeModeTabs.TOOLS_AND_UTILITIES) {
            event.accept(ModContents.fantasy_bracelet.get());
            ItemStack stack = ModContents.fantasy_bracelet.get().getDefaultInstance();
            stack.setDamageValue(1);
            event.accept(stack);
        }
    }
}
