package xueluoanping.oneblock;

import net.minecraft.world.item.CreativeModeTabs;
import net.minecraft.world.item.Item;

import net.minecraft.world.level.block.entity.BlockEntityType;
import net.minecraftforge.event.BuildCreativeModeTabContentsEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;
import net.minecraft.world.level.block.Block;
import net.minecraftforge.registries.RegistryObject;
import xueluoanping.oneblock.Item.FantasyBraceletItem;

@Mod.EventBusSubscriber(bus = Mod.EventBusSubscriber.Bus.MOD)
public class ModContents {
    public static final DeferredRegister<Item> ITEM_DEFERRED_REGISTER = DeferredRegister.create(ForgeRegistries.ITEMS, OneBlock.MOD_ID);
    public static final DeferredRegister<Block> BLOCK_DEFERRED_REGISTER = DeferredRegister.create(ForgeRegistries.BLOCKS, OneBlock.MOD_ID);
    public static final DeferredRegister<BlockEntityType<?>> BLOCK_ENTITY_TYPE_DEFERRED_REGISTER = DeferredRegister.create(ForgeRegistries.BLOCK_ENTITY_TYPES, OneBlock.MOD_ID);

    // public static final RegistryObject<Block> fluiddrawer = DREntityBlocks.register("one", () -> new BlockOne(BlockBehaviour.Properties.copy(Blocks.GLASS)
    //         .sound(SoundType.GLASS).strength(5.0F)
    //         .noOcclusion()));
    // public static final RegistryObject<Item> itemBlock = DREntityBlockItems.register("one", () -> new BlockItem(fluiddrawer.get(), new Item.Properties()));
    // public static final RegistryObject<BlockEntityType<BlockEntityOne>> tankTileEntityType = DRBlockEntities.register("one",
    //         () ->  BlockEntityType.Builder.of(BlockEntityOne::new, fluiddrawer.get()).build( null));
    public static final RegistryObject<Item> item = ITEM_DEFERRED_REGISTER.register("fantasy_bracelet",
            () -> new FantasyBraceletItem(new Item.Properties().durability(1)));


}
