package xueluoanping.oneblock.block;


import net.minecraft.core.BlockPos;
import net.minecraft.core.Direction;
import net.minecraft.nbt.CompoundTag;
import net.minecraft.nbt.ListTag;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.entity.BlockEntity;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.world.level.chunk.UpgradeData;
import net.minecraft.world.level.material.Fluids;
import net.minecraftforge.common.capabilities.Capability;

import net.minecraftforge.common.capabilities.ForgeCapabilities;
import net.minecraftforge.common.util.INBTSerializable;
import net.minecraftforge.common.util.LazyOptional;
import net.minecraftforge.fluids.FluidStack;
// import net.minecraftforge.fluids.capability.CapabilityFluidHandler;
import net.minecraftforge.fluids.FluidType;
import net.minecraftforge.fluids.capability.templates.FluidTank;
import net.minecraftforge.network.PacketDistributor;
import org.jetbrains.annotations.NotNull;
import xueluoanping.oneblock.ModContents;


import javax.annotation.Nonnull;
import javax.annotation.Nullable;
import java.util.EnumSet;

public class BlockEntityOne extends BlockEntity {


    public BlockEntityOne(BlockPos pos, BlockState state) {
        super(null,pos,state);

    }

}
