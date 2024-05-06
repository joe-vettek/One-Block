package xueluoanping.oneblock.data.lang;

import net.minecraft.data.PackOutput;
import net.minecraftforge.common.data.ExistingFileHelper;
import xueluoanping.oneblock.ModContents;
import xueluoanping.oneblock.OneBlock;

public class Lang_EN extends LangHelper {
    public Lang_EN(PackOutput gen, ExistingFileHelper helper) {
        super(gen, helper, OneBlock.MOD_ID, "en_us");
    }


    @Override
    protected void addTranslations() {
        add(modid, "One Block");
        // helper.exists(OneBlock.rl("textures"), PackType.CLIENT_RESOURCES)
        // helper.getResource(OneBlock.rl("textures"), PackType.CLIENT_RESOURCES)
        addNewStageTip("00", "§6\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n Phase 0: Tutorial§7\n Everything has a beginning.\n§a\n New Blocks: §fChest, Grass Block, Gravel, Oak Log§a\n New Items: §fApple, Egg, Oak Sapling, Wheat Seeds, Water Bucket§a\n New Mobs: §fPig\n\n ");
        addNewStageTip("01", "§6\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n Phase 1: The Plains§7\n Enough flowers and trees grow here to last a lifetime.\n§a\n New Blocks: §fBirch Log, Clay, Melon, Podzol, Pumpkin§a\n New Items: §fBirch Sapling, Carrot, Leather, Melon Seeds, Potato, Pumpkin Seeds, Sweet Berries§a\n New Mobs: §fChicken, Cow, Sheep\n\n ");
        addNewStageTip("02", "§6\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n Phase 2: The Underground§7\n Many a monster roam through dark hollows.\n§a\n New Blocks: §fAndesite, Coal Ore, Diorite, Dirt, Granite, Iron Ore, Stone§a\n New Items: §fBrown Mushroom, Coal, Feather, Red Mushroom, Spruce Sapling, String§a\n New Mobs: §fCreeper, Mooshroom, Rabbit, Spider, Zombie\n\n ");
        addNewStageTip("03", "§6\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n Phase 3: Icy Tundra§7\n Winter covers the land with its icy hands.\n§a\n New Blocks: §fDark Oak Log, Gold Ore, Packed Ice, Snow Block, Spruce Log, Powder Snow§a\n New Items: §fBlue Ice, Bone, Bone Meal, Dark Oak Sapling, Gold Ingot, Ice, Iron Ingot, Rabbit Foot, Rabbit Hide, Snowball§a\n New Mobs: §fFox, Polar Bear, Stray, Wolf\n\n ");
        addNewStageTip("04", "§6\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n Phase 4: Steaminess§7\n Rivers veil in misty embrace.\n§a\n New Blocks: §fMangrove Log, Mud§a\n New Items: §ffMangrove Saplings, Fish§a\n New Mobs: §fFrog\n\n ");
        addNewStageTip("05", "§6\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n Phase 5: Ocean§7\n Strange creatures lurk in the endless, deep water.\n§a\n New Blocks: §fBrain Coral Block, Bubble Coral Block, Dark Prismarine, Diamond Ore, Fire Coral Block, Horn Coral Block, Prismarine, Prismarine Bricks, Sand, Sea Lantern, Sponge, Tube Coral Block§a\n New Items: §fBrain Coral, Brain Coral Fan, Bubble Coral, Bubble Coral Fan, Dried Kelp, Fire Coral, Fire Coral Fan, Heart Of The Sea, Horn Coral, Horn Coral Fan, Ink Sac, Kelp, Lily Pad, Nautilus Shell, Prismarine Crystals, Prismarine Shard, Scute, Sea Pickle, Seagrass, Trident, Tube Coral, Tube Coral Fan, Turtle Egg§a\n New Mobs: §fCod, Dolphin, Drowned, Elder Guardian, Guardian, Pufferfish, Salmon, Squid, Tropical Fish, Turtle\n\n ");
        addNewStageTip("06", "§6\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n Phase 6: Jungle Dungeon§7\n Hidden by ancient trees and covered in vines lies a dungeon.\n§a\n New Blocks: §fCobblestone, Jungle Log, Mossy Cobblestone, Redstone Ore§a\n New Items: §fBamboo, Cocoa Beans, Diamond, Jungle Sapling, Lapis Lazuli, Lead, Paper, Sugar, Sugar Cane, Vine§a\n New Mobs: §fHorse, Ocelot, Panda, Parrot, Vex, Witch\n\n ");
        addNewStageTip("07", "§6\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n Phase 7: Red Desert§7\n You roam a hostile place of heat, dust and death.\n§a\n New Blocks: §fAcacia Log, Brown Terracotta, Emerald Ore, Lapis Ore, Light Gray Terracotta, Orange Terracotta, Red Sand, Red Sandstone, Red Terracotta, Sandstone, Terracotta, White Terracotta, Yellow Terracotta§a\n New Items: §fAcacia Sapling, Cactus, Dead Bush, Emerald, Experience Bottle, Redstone, Slime Ball§a\n New Mobs: §fDonkey, Husk, Llama, Pillager, Villager, Vindicator, Wandering Trader\n\n ");
        addNewStageTip("08", "§6\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n Phase 8: The Nether§7\n A hell-like dimension invades and spreads chaos.\n§a\n New Blocks: §fAncient Debris, Basalt, Blackstone, Crimson Nylium, Crying Obsidian, Gilded Blackstone, Glowstone, Magma Block, Nether Bricks, Nether Gold Ore, Nether Quartz Ore, Nether Wart Block, Netherrack, Obsidian, Red Nether Bricks, Shroomlight, Soul Sand, Soul Soil, Warped Nylium, Warped Wart Block§a\n New Items: §fBlaze Powder, Blaze Rod, Ghast Tear, Lava Bucket, Magma Cream, Nether Sprouts, Nether Wart, Netherite Scrap, Quartz, Twisting Vines, Weeping Vines, Wither Skeleton Skull§a\n New Mobs: §fBlaze, Ghast, Hoglin, Magma Cube, Piglin, Strider, Wither Skeleton\n\n ");
        addNewStageTip("09", "§6\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n Phase 9: Idyll§7\n A breeze of peace blows across the land.\n§a\n New Blocks: §fBee Nest, Beehive, Honey Block, Honeycomb Block, Quartz Block, Slime Block§a\n New Items: §fBeetroot Seeds, Beetroot Soup, Cake, Fire Charge, Glistering Melon Slice, Golden Carrot, Honey Bottle, Honeycomb, Iron Horse Armor, Leather Horse Armor, Name Tag, Saddle§a\n New Mobs: §fBee, Cat, Mule, Phantom, Skeleton Horse, Slime, Zombie Horse\n\n ");
        addNewStageTip("10", "§6\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n Phase 10: Over Hills§7\n Wander where no footsteps tread.\n§a\n New Blocks: §fCherry Log, Suspicious sand, Suspicious Gravel§a\n New Items: §fCherry Sapling, Pink Petals, Brush§a\n New Mobs: §fCamel, Goat, Allay\n\n ");
        addNewStageTip("11", "§6\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n Phase 11: Desolate Land§7\n A barren land lies before you.\n§a\n New Blocks: §fBone Block, Chiseled Stone Bricks, Cracked Stone Bricks, Jack O Lantern, Light Gray Concrete Powder, Mossy Stone Bricks, Mycelium, Stone Bricks§a\n New Items: §fCobweb, Fermented Spider Eye, Gunpowder, Phantom Membrane, Poisonous Potato, Rotten Flesh§a\n New Mobs: §fCave Spider, Evoker, Silverfish, Skeleton\n\n ");
        addNewStageTip("12", "§6\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n Phase 12: Subterranean Depths§7\n Below the profound depths lies a realm veiled in mysterious whispers.0\n§a\n New Blocks: §fDeepslate, Amethyst, Calcite, Sculk, Slime Block§a\n New Items: §fGlow Berries, Spore Blossom, Hanging Roots, Glow Lichen, Pointed Dripstone, Echo Shard§a\n New Mobs: §fGlow Squid, Axolotl, Warden\n\n ");
        addNewStageTip("13", "§6\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n Phase 13: The End§7\n Ancient powers rise as the dark void collides with your world.\n§a\n New Blocks: §fEnd Stone, End Stone Bricks, Purpur Block, Purpur Pillar§a\n New Items: §fChorus Fruit, Dragon Breath, End Rod, Ender Eye, Ender Pearl, Spectral Arrow§a\n New Mobs: §fEnderman, Endermite, Shulker\n\n ");
        addNewStageTip("all", "§6\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n You reached the Afterphases!\n The infinite block pulsates with strange energy.");

        add(ModContents.one_stone.get(), "One Stone");
        add(ModContents.fantasy_bracelet.get(), "Fantasy Bracelet");
        var itemStack=ModContents.fantasy_bracelet.get().getDefaultInstance();
        itemStack.setDamageValue(1);
        add(itemStack,"Shattered Bracelet");
        addCustomName("mob", "Gift from the Up");
    }


}
