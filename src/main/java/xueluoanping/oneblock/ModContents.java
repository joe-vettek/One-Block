package xueluoanping.oneblock;

import com.mojang.serialization.Codec;
import net.minecraft.world.item.Item;

import net.minecraft.world.level.block.Blocks;
import net.minecraft.world.level.block.SoundType;
import net.minecraft.world.level.block.entity.BlockEntityType;
import net.minecraft.world.level.block.state.BlockBehaviour;
import net.minecraft.world.level.material.PushReaction;
import net.minecraftforge.common.loot.IGlobalLootModifier;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;
import net.minecraft.world.level.block.Block;
import net.minecraftforge.registries.RegistryObject;
import xueluoanping.oneblock.Item.FantasyBraceletItem;
import xueluoanping.oneblock.block.BlockOne;
import xueluoanping.oneblock.loot.modifier.AddLootTableModifier;

@Mod.EventBusSubscriber(bus = Mod.EventBusSubscriber.Bus.MOD)
public class ModContents {
    public static final DeferredRegister<Item> ITEM_DEFERRED_REGISTER = DeferredRegister.create(ForgeRegistries.ITEMS, OneBlock.MOD_ID);
    public static final DeferredRegister<Block> BLOCK_DEFERRED_REGISTER = DeferredRegister.create(ForgeRegistries.BLOCKS, OneBlock.MOD_ID);
    public static final DeferredRegister<BlockEntityType<?>> BLOCK_ENTITY_TYPE_DEFERRED_REGISTER = DeferredRegister.create(ForgeRegistries.BLOCK_ENTITY_TYPES, OneBlock.MOD_ID);

    public static final DeferredRegister<Codec<? extends IGlobalLootModifier>> LOOT_MODIFIERS = DeferredRegister.create(ForgeRegistries.Keys.GLOBAL_LOOT_MODIFIER_SERIALIZERS, OneBlock.MOD_ID);

    public static final RegistryObject<Block> one_stone = BLOCK_DEFERRED_REGISTER.register("one_stone", () -> new BlockOne(BlockBehaviour.Properties.of()
            .strength(-1.0F, 3600000.8F).noLootTable().noParticlesOnBreak().pushReaction(PushReaction.BLOCK)
            .sound(SoundType.AMETHYST).noOcclusion()));
    // public static final RegistryObject<Item> itemBlock = DREntityBlockItems.register("one", () -> new BlockItem(fluiddrawer.get(), new Item.Properties()));
    // public static final RegistryObject<BlockEntityType<BlockEntityOne>> tankTileEntityType = DRBlockEntities.register("one",
    //         () ->  BlockEntityType.Builder.of(BlockEntityOne::new, fluiddrawer.get()).build( null));
    public static final RegistryObject<Item> fantasy_bracelet = ITEM_DEFERRED_REGISTER.register("fantasy_bracelet",
            () -> new FantasyBraceletItem(new Item.Properties().durability(1)));

    public static final RegistryObject<Codec<? extends IGlobalLootModifier>> ADD_LOOT_TABLE = LOOT_MODIFIERS.register("add_loot_table", AddLootTableModifier.CODEC);

}
