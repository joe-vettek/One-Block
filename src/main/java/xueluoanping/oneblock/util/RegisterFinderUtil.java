package xueluoanping.oneblock.util;

import net.minecraft.core.Registry;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.core.registries.Registries;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.entity.EntityType;
import net.minecraft.world.item.Item;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.levelgen.feature.ConfiguredFeature;
import net.minecraft.world.level.levelgen.feature.Feature;
import net.minecraft.world.level.levelgen.structure.Structure;

public class RegisterFinderUtil {

    public static EntityType<?> getEntity(String s) {
        return getEntity(new ResourceLocation(s));
    }

    public static EntityType<?> getEntity(ResourceLocation rs) {
        return BuiltInRegistries.ENTITY_TYPE.get(rs);
    }

    public static Block getBlock(String s) {
        return getBlock(new ResourceLocation(s));
    }

    // BuiltInRegistries
    public static Block getBlock(ResourceLocation rs) {
        return BuiltInRegistries.BLOCK.get(rs);
    }

    public static Item getItem(String s) {
        return getItem(new ResourceLocation(s));
    }

    public static Item getItem(ResourceLocation rs) {
        return BuiltInRegistries.ITEM.get(rs);
    }

    public static Item getItem(String s, String s2) {
        return getItem(new ResourceLocation(s, s2));
    }


    public static ResourceLocation getItemKey(Item s) {
        return BuiltInRegistries.ITEM.getKey(s);
    }

    public static ResourceLocation getBlockKey(Block s) {
        return BuiltInRegistries.BLOCK.getKey(s);
    }


    // public static Feature<?> getFeature(String s) {
    //     return BuiltInRegistries.FEATURE.get(new ResourceLocation(s));
    // }
}
