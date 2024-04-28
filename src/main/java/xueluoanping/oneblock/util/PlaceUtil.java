package xueluoanping.oneblock.util;

import com.mojang.brigadier.exceptions.CommandSyntaxException;
import net.minecraft.ResourceLocationException;
import net.minecraft.commands.CommandSourceStack;
import net.minecraft.core.BlockPos;
import net.minecraft.core.Holder;
import net.minecraft.core.SectionPos;
import net.minecraft.core.registries.Registries;
import net.minecraft.network.chat.Component;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.server.MinecraftServer;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.level.ChunkPos;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.Mirror;
import net.minecraft.world.level.block.Rotation;
import net.minecraft.world.level.block.entity.StructureBlockEntity;
import net.minecraft.world.level.chunk.ChunkGenerator;
import net.minecraft.world.level.levelgen.feature.ConfiguredFeature;
import net.minecraft.world.level.levelgen.structure.BoundingBox;
import net.minecraft.world.level.levelgen.structure.Structure;
import net.minecraft.world.level.levelgen.structure.StructureStart;
import net.minecraft.world.level.levelgen.structure.templatesystem.BlockRotProcessor;
import net.minecraft.world.level.levelgen.structure.templatesystem.StructurePlaceSettings;
import net.minecraft.world.level.levelgen.structure.templatesystem.StructureTemplate;
import net.minecraft.world.level.levelgen.structure.templatesystem.StructureTemplateManager;
import xueluoanping.oneblock.OneBlock;

import java.util.Optional;

public class PlaceUtil {

    private static boolean checkLoaded(ServerLevel serverLevel, ChunkPos chunkPos2, ChunkPos chunkPos1) {
        // throw BlockPosArgument.ERROR_NOT_LOADED.create();
        return ChunkPos.rangeClosed(chunkPos2, chunkPos1).allMatch((chunkPos) -> serverLevel.isLoaded(chunkPos.getWorldPosition()));
    }

    public static void placeStructure(ServerLevel level, BlockPos base, ResourceLocation resourceLocation) {
        Structure structure = DatapackRegisterFinderUtil.getStructure(level, resourceLocation.toString());
        ChunkGenerator chunkgenerator = level.getChunkSource().getGenerator();
        if (structure == null) OneBlock.error("Failed found " +resourceLocation);
        StructureStart structurestart = structure.generate(level.structureManager().registryAccess(), chunkgenerator, chunkgenerator.getBiomeSource(), level.getChunkSource().randomState(), level.getStructureManager(), level.getSeed(), new ChunkPos(base), 0, level, (biomeHolder) -> true);
        if (!structurestart.isValid()) {
            OneBlock.error("Failed place" + "");
        } else {
            BoundingBox boundingbox = structurestart.getBoundingBox();
            ChunkPos chunkpos = new ChunkPos(SectionPos.blockToSectionCoord(boundingbox.minX()), SectionPos.blockToSectionCoord(boundingbox.minZ()));
            ChunkPos chunkpos1 = new ChunkPos(SectionPos.blockToSectionCoord(boundingbox.maxX()), SectionPos.blockToSectionCoord(boundingbox.maxZ()));
            if (checkLoaded(level, chunkpos, chunkpos1))
                ChunkPos.rangeClosed(chunkpos, chunkpos1).forEach((chunkPos) -> {
                    structurestart.placeInChunk(level, level.structureManager(), chunkgenerator, level.getRandom(), new BoundingBox(chunkPos.getMinBlockX(), level.getMinBuildHeight(), chunkPos.getMinBlockZ(), chunkPos.getMaxBlockX(), level.getMaxBuildHeight(), chunkPos.getMaxBlockZ()), chunkPos);
                });
        }
    }

    public static void placeTemplate(ServerLevel level, BlockPos base, ResourceLocation resourceLocation) {
        placeTemplate(level, base, resourceLocation, Rotation.NONE, Mirror.NONE, 1f);
    }

    public static void placeTemplate(ServerLevel level, BlockPos base, ResourceLocation resourceLocation, Rotation rotation, Mirror mirror, float integrity) {

        StructureTemplateManager structuretemplatemanager = level.getStructureManager();
        Optional<StructureTemplate> optional;
        try {
            optional = structuretemplatemanager.get(resourceLocation);
        } catch (ResourceLocationException resourcelocationexception) {
            OneBlock.error("Failed get" + resourceLocation.toString());
            return;
        }

        if (optional.isEmpty()) {
            OneBlock.error("Failed place" + resourceLocation.toString());
        } else {
            StructureTemplate structuretemplate = optional.get();
            var size = structuretemplate.getSize();
            // base=base.offset(size.);
            checkLoaded(level, new ChunkPos(base), new ChunkPos(base.offset(structuretemplate.getSize())));
            StructurePlaceSettings structureplacesettings = (new StructurePlaceSettings()).setMirror(mirror).setRotation(rotation);
            // degree of intactness
            if (integrity < 1.0F) {
                structureplacesettings.clearProcessors().addProcessor(new BlockRotProcessor(integrity)).setRandom(level.getRandom());
            }
            // above to start
            base = base.above();
            boolean flag = structuretemplate.placeInWorld(level, base, base, structureplacesettings, level.getRandom(), Block.UPDATE_CLIENTS);
            OneBlock.error("Place " + flag + resourceLocation.toString());
        }
    }

    public static void placeFeature(ServerLevel level, BlockPos pos, ResourceLocation resourceLocation) {
        ConfiguredFeature<?, ?> configuredfeature = DatapackRegisterFinderUtil.getConfiguredFeature(level, resourceLocation.toString());

        if (configuredfeature != null) {
            ChunkPos chunkpos = new ChunkPos(pos);
            if (checkLoaded(level, new ChunkPos(chunkpos.x - 1, chunkpos.z - 1), new ChunkPos(chunkpos.x + 1, chunkpos.z + 1)))
                // above to start
                if (!configuredfeature.place(level, level.getChunkSource().getGenerator(), level.getRandom(), pos.above())) {
                    OneBlock.error("Failed place" + resourceLocation.toString());
                }
        }
    }


}
