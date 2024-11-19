package xueluoanping.oneblock.data.blockstate;


import net.minecraft.core.Direction;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.data.PackOutput;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.Blocks;
import net.minecraft.world.level.block.state.properties.BlockStateProperties;
import net.neoforged.neoforge.client.model.generators.BlockStateProvider;
import net.neoforged.neoforge.client.model.generators.ConfiguredModel;
import net.neoforged.neoforge.client.model.generators.ModelFile;
import net.neoforged.neoforge.common.data.ExistingFileHelper;
import net.neoforged.neoforge.registries.DeferredHolder;
import xueluoanping.oneblock.ModContents;
import xueluoanping.oneblock.OneBlock;

import java.util.List;

public class BlockStatesDataProvider extends BlockStateProvider {


    private final ExistingFileHelper existingFileHelper;

    public BlockStatesDataProvider(PackOutput output, ExistingFileHelper existingFileHelper) {
        super(output, OneBlock.MOD_ID, existingFileHelper);
        this.existingFileHelper = existingFileHelper;
    }

    @Override
    protected void registerStatesAndModels() {
        simpleBlock(ModContents.one_stone.value(),
                new ModelFile.ExistingModelFile(ResourceLocation.withDefaultNamespace("block/air"),existingFileHelper));
    }


}
