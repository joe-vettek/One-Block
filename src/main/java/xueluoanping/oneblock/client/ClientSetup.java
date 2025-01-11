package xueluoanping.oneblock.client;



import net.minecraft.client.renderer.RenderType;
import net.minecraft.world.item.CreativeModeTabs;
import net.minecraft.world.item.ItemStack;
import net.neoforged.api.distmarker.Dist;
import net.neoforged.bus.api.SubscribeEvent;
import net.neoforged.fml.common.EventBusSubscriber;
import net.neoforged.fml.event.lifecycle.FMLClientSetupEvent;
import net.neoforged.neoforge.client.event.EntityRenderersEvent;
import net.neoforged.neoforge.event.BuildCreativeModeTabContentsEvent;
import xueluoanping.oneblock.ModContents;
import xueluoanping.oneblock.OneBlock;

@EventBusSubscriber(bus = EventBusSubscriber.Bus.MOD, value = Dist.CLIENT)
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
