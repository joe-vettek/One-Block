package xueluoanping.oneblock.util;

import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.core.registries.Registries;
import net.minecraft.resources.ResourceKey;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.sounds.SoundEvent;
import net.minecraft.world.entity.EntityType;
import net.minecraft.world.item.Item;
import net.minecraft.world.level.Level;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.levelgen.feature.ConfiguredFeature;
import net.minecraft.world.level.levelgen.structure.Structure;
import net.minecraft.world.level.levelgen.structure.templatesystem.StructureTemplateManager;
import net.minecraft.world.level.storage.loot.LootTable;

public class RegisterFinderUtil {

    public static EntityType<?> getEntity(String s) {
        return getEntity(ResourceLocation.parse(s));
    }

    public static EntityType<?> getEntity(ResourceLocation rs) {
        return BuiltInRegistries.ENTITY_TYPE.get(rs);
    }

    public static Block getBlock(String s) {
        return getBlock(ResourceLocation.parse(s));
    }

    // BuiltInRegistries
    public static Block getBlock(ResourceLocation rs) {
        return BuiltInRegistries.BLOCK.get(rs);
    }

    public static Item getItem(String s) {
        return getItem(ResourceLocation.parse(s));
    }

    public static Item getItem(ResourceLocation rs) {
        return BuiltInRegistries.ITEM.get(rs);
    }

    public static Item getItem(String s, String s2) {
        return getItem(ResourceLocation.fromNamespaceAndPath(s, s2));
    }


    public static ResourceLocation getItemKey(Item s) {
        return BuiltInRegistries.ITEM.getKey(s);
    }

    public static ResourceLocation getBlockKey(Block s) {
        return BuiltInRegistries.BLOCK.getKey(s);
    }

    public static ResourceLocation getEntityKey(EntityType<?> entity) {
        return BuiltInRegistries.ENTITY_TYPE.getKey(entity);
    }

    public static SoundEvent getSound(String id) {
        return BuiltInRegistries.SOUND_EVENT.get(ResourceLocation.parse(id));
    }

    public static ResourceLocation getSoundKey(SoundEvent soundEvent) {
        return BuiltInRegistries.SOUND_EVENT.getKey(soundEvent);
    }

    public static ResourceLocation getStructureKey(ResourceLocation rs) {
        var structureType = BuiltInRegistries.STRUCTURE_TYPE.get(rs);
        return structureType == null ? null : BuiltInRegistries.STRUCTURE_TYPE.getKey(structureType);
    }

    public static Structure getStructure(ServerLevel serverLevel, String s) {
        var res = getStructureKey(ResourceLocation.parse(s));
        return res == null ? null : serverLevel.structureManager().registryAccess()
                .registryOrThrow(Registries.STRUCTURE)
                .get(res);
    }


    // Feature is a type of terrain feature.
    // ConfiguredFeature is a specific terrain feature.
    // PlacedFeature is a terrain feature with specific placement conditions set.
    public static ConfiguredFeature<?, ?> getConfiguredFeature(ServerLevel serverLevel, String s) {
        var res = serverLevel.registryAccess().registryOrThrow(Registries.CONFIGURED_FEATURE).get(ResourceLocation.parse(s));
        return res != null ? res : serverLevel.registryAccess().registryOrThrow(Registries.CONFIGURED_FEATURE).get(ResourceLocation.fromNamespaceAndPath("minecraft", "oak_bees_005"));
    }

    // public static Feature<?> getFeature(String s) {
    //     return BuiltInRegistries.FEATURE.get(ResourceLocation.parse(s));
    // }

    public static boolean checkTemplateKey(ServerLevel serverLevel, String s) {
        StructureTemplateManager structuretemplatemanager = serverLevel.getStructureManager();
        return structuretemplatemanager.listTemplates().anyMatch(ss -> ss.toString().equals(s));
    }


    public static ResourceKey<LootTable> getLootTable(ResourceLocation resourceLocation) {
        return ResourceKey.create(Registries.LOOT_TABLE, resourceLocation);
    }

    public static ResourceKey<LootTable> getLootTable(String s, String s2) {
        return ResourceKey.create(Registries.LOOT_TABLE, ResourceLocation.fromNamespaceAndPath(s, s2));
    }

    public static ResourceKey<LootTable> getLootTable(String s) {
        return ResourceKey.create(Registries.LOOT_TABLE, ResourceLocation.parse(s));
    }
}
