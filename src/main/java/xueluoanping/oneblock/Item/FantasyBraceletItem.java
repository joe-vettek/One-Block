package xueluoanping.oneblock.Item;

import net.minecraft.core.BlockPos;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.InteractionHand;
import net.minecraft.world.InteractionResultHolder;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.level.ClipContext;
import net.minecraft.world.level.Level;
import net.minecraft.world.phys.BlockHitResult;
import net.minecraft.world.phys.HitResult;
import xueluoanping.oneblock.ModContents;
import xueluoanping.oneblock.handler.Levelhandler;

public class FantasyBraceletItem extends Item {
    public FantasyBraceletItem(Properties properties) {
        super(properties);
    }

    @Override
    public InteractionResultHolder<ItemStack> use(Level level, Player player, InteractionHand hand) {
        if (level instanceof ServerLevel serverLevel) {
            ItemStack itemstack = player.getItemInHand(hand);

            BlockHitResult hitresult = getPlayerPOVHitResult(serverLevel, player, ClipContext.Fluid.NONE);
            if (hitresult.getType() == HitResult.Type.MISS) {
                return InteractionResultHolder.pass(itemstack);
            } else {
                if (hitresult.getType() == HitResult.Type.BLOCK) {
                    BlockPos pos = hitresult.getBlockPos();
                    var save = Levelhandler.oneBlockSaveHolder.get(serverLevel);
                    if (itemstack.getDamageValue() != 0) {
                        var oldPos = save.remove(pos);
                        if (oldPos != null)
                            itemstack.setDamageValue(0);
                    } else {
                        itemstack.setDamageValue(1);
                        // save.remove(pos);
                        // save.update(pos, save.getOrDefault(pos));
                        // level.removeBlock(pos, false);
                        level.setBlockAndUpdate(pos,ModContents.one_stone.get().defaultBlockState());
                    }

                    // if (!player.isCreative())
                    //     player.setItemInHand(hand, itemstack);
                    return InteractionResultHolder.success(itemstack);
                } else {
                    return InteractionResultHolder.pass(itemstack);
                }
            }

        }
        return super.use(level, player, hand);
    }


}
