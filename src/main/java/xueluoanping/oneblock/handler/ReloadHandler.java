package xueluoanping.oneblock.handler;

import com.mojang.brigadier.arguments.ArgumentType;
import com.mojang.brigadier.arguments.StringArgumentType;
import com.sun.jdi.connect.Connector;
import net.minecraft.commands.CommandSourceStack;
import net.minecraft.commands.Commands;
import net.minecraft.commands.arguments.ResourceLocationArgument;
import net.minecraft.commands.arguments.coordinates.BlockPosArgument;
import net.minecraft.core.BlockPos;
import net.minecraft.resources.ResourceLocation;
import net.minecraftforge.event.AddReloadListenerEvent;
import net.minecraftforge.event.RegisterCommandsEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import xueluoanping.oneblock.ModContents;
import xueluoanping.oneblock.OneBlock;
import xueluoanping.oneblock.config.General;

// @Mod.EventBusSubscriber(bus = Mod.EventBusSubscriber.Bus.FORGE, value = Dist.DEDICATED_SERVER)
public class ReloadHandler {
    public static ReloadHandler instance = new ReloadHandler();

    // @SubscribeEvent
    // public void onLevelLoad(LevelEvent.Load event) {
    // }
    //
    // @SubscribeEvent
    // public void onLevelSave(LevelEvent.Save event) {
    //
    // }

    @SubscribeEvent
    public void onAddReloadListener(AddReloadListenerEvent event) {
        // event.addListener(network.instance);
        event.addListener(network.instance2);

    }

    @SubscribeEvent
    public void onRegisterCommands(RegisterCommandsEvent event) {
        var dispatcher = event.getDispatcher();

        dispatcher.register(
                Commands.literal(OneBlock.MOD_ID)
                        .requires((sourceStack) -> sourceStack.hasPermission(2))
                        .then(Commands.literal("skip_to")
                                .then(Commands.argument("stage", ResourceLocationArgument.id())
                                        .suggests((context, builder) -> {
                                            String pre = "";
                                            try {
                                                pre= context.getArgument("stage", ResourceLocation.class).getPath();
                                            } catch (IllegalArgumentException e) {
                                                // e.printStackTrace();
                                            }
                                            String finalPre = pre;
                                            General.getOrder().stream().filter(s -> s.contains(finalPre)).forEach(builder::suggest);
                                            return builder.buildFuture();
                                        })
                                        .then(Commands.argument("pos", BlockPosArgument.blockPos())
                                                .suggests((context, builder) -> {
                                                    var save = Levelhandler.getSaveData(context.getSource().getLevel());
                                                    save.getBlockPos().stream().map(pos -> String.format("%s %s %s", pos.getX(), pos.getY(), pos.getZ())).forEach(builder::suggest);
                                                    return builder.buildFuture();
                                                })
                                                .executes((stackCommandContext) ->
                                                        skip_to_stage(stackCommandContext.getSource(), ResourceLocationArgument.getId(stackCommandContext, "stage"), BlockPosArgument.getLoadedBlockPos(stackCommandContext, "pos"))))))
        );
        dispatcher.register(
                Commands.literal(OneBlock.MOD_ID)
                        .requires((sourceStack) -> sourceStack.hasPermission(2))
                        .then(Commands.literal("set")
                                .then(Commands.argument("pos", BlockPosArgument.blockPos()).executes((stackCommandContext) ->
                                        set_stage(stackCommandContext.getSource(), BlockPosArgument.getLoadedBlockPos(stackCommandContext, "pos")))))
        );
        dispatcher.register(
                Commands.literal(OneBlock.MOD_ID)
                        .requires((sourceStack) -> sourceStack.hasPermission(2))
                        .then(Commands.literal("remove")
                                .then(Commands.argument("pos", BlockPosArgument.blockPos())
                                        .suggests((context, builder) -> {
                                            var save = Levelhandler.getSaveData(context.getSource().getLevel());
                                            save.getBlockPos().stream().map(pos -> String.format("%s %s %s", pos.getX(), pos.getY(), pos.getZ())).forEach(builder::suggest);
                                            return builder.buildFuture();
                                        })
                                        .executes((stackCommandContext) ->
                                                remove_stage(stackCommandContext.getSource(), BlockPosArgument.getLoadedBlockPos(stackCommandContext, "pos")))))
        );
    }

    private int skip_to_stage(CommandSourceStack source, ResourceLocation id, BlockPos pos) {
        OneBlock.logger(id, pos, network.getStageStartPos(id), source.getLevel());
        var save = Levelhandler.getSaveData(source.getLevel());
        var progress = save.get(pos);
        if (progress != null) {
            progress.counter = network.getStageStartPos(id);
            save.update(pos, progress);
            source.getLevel().removeBlock(pos, false);
        } else {
            return 0;
        }
        return 1;
    }

    private int set_stage(CommandSourceStack source, BlockPos pos) {
        OneBlock.logger("Set", pos, source.getLevel());
        var save = Levelhandler.getSaveData(source.getLevel());
        var progress = save.get(pos);
        if (progress == null) {
            save.update(pos, save.getOrDefault(pos));
            source.getLevel().removeBlock(pos, false);
        } else {
            return 0;
        }
        return 1;
    }

    private int remove_stage(CommandSourceStack source, BlockPos pos) {
        OneBlock.logger("Remove", pos, source.getLevel());
        var save = Levelhandler.getSaveData(source.getLevel());
        var progress = save.get(pos);
        if (progress != null) {
            save.remove(pos);
        } else {
            return 0;
        }
        return 1;
    }
}
