package xueluoanping.oneblock.util;

import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.core.registries.Registries;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.entity.EntityType;
import net.minecraft.world.item.Item;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.levelgen.feature.ConfiguredFeature;
import net.minecraft.world.level.levelgen.structure.Structure;

public class DatapackRegisterFinderUtil {


    public static ResourceLocation getStructureKey(ResourceLocation rs) {
        var structureType = BuiltInRegistries.STRUCTURE_TYPE.get(rs);
        return structureType == null ? null : BuiltInRegistries.STRUCTURE_TYPE.getKey(structureType);
    }

    public static Structure getStructure(ServerLevel serverLevel, String s) {
        var res = getStructureKey(new ResourceLocation(s));
        return res == null ? null : serverLevel.structureManager().registryAccess()
                .registryOrThrow(Registries.STRUCTURE)
                .get(res);
    }

    // Feature is a type of terrain feature.
    // ConfiguredFeature is a specific terrain feature.
    // PlacedFeature is a terrain feature with specific placement conditions set.
    public static ConfiguredFeature<?, ?> getConfiguredFeature(ServerLevel serverLevel, String s) {
        var res = serverLevel.registryAccess().registryOrThrow(Registries.CONFIGURED_FEATURE).get(new ResourceLocation(s));
        return res != null ? res : serverLevel.registryAccess().registryOrThrow(Registries.CONFIGURED_FEATURE).get(new ResourceLocation("minecraft","oak_bees_005"));
    }
}
