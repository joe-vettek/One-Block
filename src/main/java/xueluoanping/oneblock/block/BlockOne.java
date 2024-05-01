package xueluoanping.oneblock.block;


import net.minecraft.core.BlockPos;
import net.minecraft.core.Direction;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.util.RandomSource;
import net.minecraft.world.entity.Entity;
import net.minecraft.world.entity.LivingEntity;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.item.*;
import net.minecraft.world.level.BlockGetter;
import net.minecraft.world.level.Level;
import net.minecraft.world.level.LevelAccessor;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.RenderShape;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.world.level.block.state.StateDefinition;
import net.minecraft.world.phys.shapes.CollisionContext;
import net.minecraft.world.phys.shapes.VoxelShape;
import org.jetbrains.annotations.Nullable;
import xueluoanping.oneblock.OneBlock;
import xueluoanping.oneblock.handler.Levelhandler;
import xueluoanping.oneblock.util.ClientUtils;


// Todo: make a start block
public class BlockOne extends Block {


    public BlockOne(Properties properties) {
        super(properties);

    }


    // Add all the properties here, or may cause a null point exception.
    @Override
    protected void createBlockStateDefinition(StateDefinition.Builder<Block, BlockState> p_49915_) {
        super.createBlockStateDefinition(p_49915_);
    }


    @Override
    public VoxelShape getShape(BlockState state, BlockGetter worldIn, BlockPos pos, CollisionContext context) {
        return super.getShape(state, worldIn, pos, context);
    }

    @Override
    public BlockState updateShape(BlockState blockState, Direction direction, BlockState state, LevelAccessor accessor, BlockPos pos, BlockPos pos1) {
        if (accessor instanceof ServerLevel serverLevel) {
            serverLevel.scheduleTick(pos, this, 1);
        }
        return super.updateShape(blockState, direction, state, accessor, pos, pos1);
    }

    @Override
    public RenderShape getRenderShape(BlockState p_149645_1_) {
        return RenderShape.INVISIBLE;
    }


    // @Override
    // public BlockEntity newBlockEntity(BlockPos pos, BlockState state) {
    //     return new BlockEntityOne( pos, state);
    // }

    @Override
    public void setPlacedBy(Level p_49847_, BlockPos p_49848_, BlockState p_49849_, @Nullable LivingEntity p_49850_, ItemStack p_49851_) {
        super.setPlacedBy(p_49847_, p_49848_, p_49849_, p_49850_, p_49851_);
    }

    // trigger whenever on place
    @Override
    public void onPlace(BlockState state, Level level, BlockPos pos, BlockState state1, boolean p_60570_) {
        super.onPlace(state, level, pos, state1, p_60570_);
        if (level instanceof ServerLevel serverLevel) {
            serverLevel.scheduleTick(pos, this, 1);
        }
    }

    // do work
    @Override
    public void tick(BlockState state, ServerLevel level, BlockPos pos, RandomSource randomSource) {
        super.tick(state, level, pos, randomSource);
        // if (level instanceof ServerLevel serverLevel)
        {
            OneBlock.logger(pos, "Loading a stage");
            var save = Levelhandler.oneBlockSaveHolder.get(level);
            save.remove(pos);
            save.update(pos, save.getOrDefault(pos));
            level.removeBlock(pos, false);
            ClientUtils.playFireWorkParticles(level, pos);
        }
    }

    @Override
    public boolean isRandomlyTicking(BlockState p_49921_) {
        return true;
    }

    // set trigger
    @Override
    public void randomTick(BlockState p_222954_, ServerLevel p_222955_, BlockPos p_222956_, RandomSource p_222957_) {
        super.randomTick(p_222954_, p_222955_, p_222956_, p_222957_);
    }

    @Override
    public void fallOn(Level level, BlockState state, BlockPos pos, Entity entity, float v) {
        super.fallOn(level, state, pos, entity, v);
        if (level instanceof ServerLevel serverLevel)
            this.tick(state, serverLevel, pos, level.getRandom());
    }
}
