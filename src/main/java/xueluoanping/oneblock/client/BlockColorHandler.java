package xueluoanping.oneblock.client;


import net.minecraftforge.api.distmarker.Dist;
import net.minecraftforge.fml.common.Mod;

@Mod.EventBusSubscriber(bus = Mod.EventBusSubscriber.Bus.MOD, value = Dist.CLIENT)
public class BlockColorHandler {

    // // Need to wait
    // @SubscribeEvent
    // public static void handleBlockColor(FMLClientSetupEvent event) {
    //     event.enqueueWork(() -> {
    //         BlockState birchLeaves = Blocks.BIRCH_LEAVES.defaultBlockState();
    //
    //         Minecraft.getInstance().getBlockColors().register((state, worlds, poss, i) -> {
    //             if (i == 0) {
    //                 Block block = state.getBlock();
    //                 if (block == REDLOVE_LEAVES.get())
    //                     return -1;
    //                 if (block == CHERRY_LEAVES.get())
    //                     return -1;
    //                 return Minecraft.getInstance().getBlockColors().getColor(birchLeaves, worlds, poss, i);
    //             }
    //             if (i == 1) {
    //                 int stage = state.getValue(FruitLeavesBlock.AGE);
    //                 if (stage < 3) {
    //                     return Minecraft.getInstance().getBlockColors().getColor(birchLeaves, worlds, poss, i);
    //                 }
    //                 Block block = state.getBlock();
    //                 if (block == CITRON_LEAVES.get())
    //                     return 0xDDCC58;
    //                 if (block == GRAPEFRUIT_LEAVES.get())
    //                     return 0xF4502B;
    //                 if (block == LEMON_LEAVES.get())
    //                     return 0xEBCA4B;
    //                 if (block == LIME_LEAVES.get())
    //                     return 0xCADA76;
    //                 if (block == TANGERINE_LEAVES.get())
    //                     return 0xF08A19;
    //                 if (block == ORANGE_LEAVES.get())
    //                     return 0xF08A19;
    //                 if (block == POMEGRANATE_LEAVES.get())
    //                     return 0xB23733;
    //                 if (block == POMELO_LEAVES.get())
    //                     return 0xF7F67E;
    //                 if (block == REDLOVE_LEAVES.get())
    //                     return 0xC22626;
    //                 if (block == CHERRY_LEAVES.get() )
    //                     return 0xE45B55;
    //             }
    //             return FoliageColor.getEvergreenColor();
    //         }, CHERRY_LEAVES.get(), TANGERINE_LEAVES.get(), LIME_LEAVES.get(), CITRON_LEAVES.get(), POMEGRANATE_LEAVES.get(), POMELO_LEAVES.get(), ORANGE_LEAVES.get(), LEMON_LEAVES.get(), GRAPEFRUIT_LEAVES.get(), REDLOVE_LEAVES.get());
    //
    //         Minecraft.getInstance().getBlockColors().register((state, worlds, poss, i) -> {
    //
    //
    //             Block block = state.getValue(BlockStateProperties.AGE_3) == 0 ?
    //                     Blocks.AIR : state.getBlock();
    //
    //             if (block == CHERRY.get() && i == 0)
    //                 return 0xE45B55;
    //             // if (i == 0)
    //             {
    //                 if (block == CITRON.get())
    //                     return 0xDDCC58;
    //                 if (block == GRAPEFRUIT.get())
    //                     return 0xF4502B;
    //                 if (block == LEMON.get())
    //                     return 0xEBCA4B;
    //                 if (block == LIME.get())
    //                     return 0xCADA76;
    //                 if (block == TANGERINE.get())
    //                     return 0xF08A19;
    //                 if (block == ORANGE.get())
    //                     return 0xF08A19;
    //                 if (block == POMEGRANATE.get())
    //                     return 0xB23733;
    //                 if (block == POMELO.get())
    //                     return 0xF7F67E;
    //                 if (block == REDLOVE.get())
    //                     return 0xC22626;
    //             }
    //             // else
    //             //     return FoliageColors.getBirchColor();
    //
    //             return -1;
    //         }, CHERRY.get(), TANGERINE.get(), LIME.get(), CITRON.get(), POMEGRANATE.get(), POMELO.get(), ORANGE.get(), LEMON.get(), GRAPEFRUIT.get(), REDLOVE.get());
    //
    //     });
    //
    //
    // }


  }
