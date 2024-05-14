package xueluoanping.oneblock.handler;

import net.minecraft.commands.CommandSourceStack;
import net.minecraft.commands.Commands;
import net.minecraft.commands.arguments.ResourceLocationArgument;
import net.minecraft.commands.arguments.coordinates.BlockPosArgument;
import net.minecraft.core.BlockPos;
import net.minecraft.network.chat.ClickEvent;
import net.minecraft.network.chat.Component;
import net.minecraft.network.chat.HoverEvent;
import net.minecraft.network.chat.TextColor;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.server.packs.PackType;
import net.minecraft.server.packs.repository.Pack;
import net.minecraft.server.packs.repository.PackSource;
import net.minecraftforge.event.AddPackFindersEvent;
import net.minecraftforge.event.AddReloadListenerEvent;
import net.minecraftforge.event.RegisterCommandsEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.forgespi.locating.IModFile;
import xueluoanping.oneblock.OneBlock;
import xueluoanping.oneblock.api.ModFilePackResources;
import xueluoanping.oneblock.api.StageData;
import xueluoanping.oneblock.config.General;
import xueluoanping.oneblock.util.ClientUtils;
import xueluoanping.oneblock.util.Platform;

import java.util.List;

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


    public static void onAddPackFindersEvent(AddPackFindersEvent event) {

        if (event.getPackType() == PackType.SERVER_DATA) {
            IModFile modFile = Platform.getModFile(OneBlock.MOD_ID);

            // General.enableList.forEach(
            //         (pack, booleanValue) -> {
            //             if (booleanValue.get()) {
            //                 String packID = "oneblock-extra-" + pack;
            //                 event.addRepositorySource(consumer -> consumer.accept(
            //                         Pack.readMetaAndCreate(packID, Component.translatable(pack), true,
            //                                 id -> new ModFilePackResources(packID, modFile, "datapacks/" + packID), PackType.SERVER_DATA,
            //                                 Pack.Position.BOTTOM, PackSource.BUILT_IN)));
            //             }
            //         }
            // );

            for (String packID : List.of("ija-one-block", "oneblock")) {
                event.addRepositorySource(consumer -> consumer.accept(
                        Pack.readMetaAndCreate(packID, Component.translatable(packID), true,
                                id -> new ModFilePackResources(packID, modFile, "datapacks/" + packID), PackType.SERVER_DATA,
                                Pack.Position.BOTTOM, PackSource.BUILT_IN)));
            }

        }
    }

    @SubscribeEvent
    public void onAddReloadListener(AddReloadListenerEvent event) {
        // event.addListener(network.instance);
        event.addListener(StageManager.instance2);

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
                                                pre = context.getArgument("stage", ResourceLocation.class).getPath();
                                            } catch (IllegalArgumentException e) {
                                                // e.printStackTrace();
                                            }
                                            String finalPre = pre;
                                            StageManager.STAGE_DATA_LIST
                                                    .stream()
                                                    .map(stageData -> stageData.getResourceLocation() + "")
                                                    .filter(s -> s.contains(finalPre)).forEach(builder::suggest);
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
        dispatcher.register(
                Commands.literal(OneBlock.MOD_ID)
                        .requires((sourceStack) -> sourceStack.hasPermission(2))
                        .then(Commands.literal("list_stage_info")
                                .executes((stackCommandContext) ->
                                        list_stage(stackCommandContext.getSource()))));
        // dispatcher.register(
        //         Commands.literal(OneBlock.MOD_ID)
        //                 .requires((sourceStack) -> sourceStack.hasPermission(2))
        //                 .then(Commands.literal("list")
        //                         .then(Commands.literal("block").executes(context -> 1))
        //                         .then(Commands.literal("item").executes(context -> 1))
        //                         .then(Commands.literal("mob").executes(context -> 1))
        //                         .then(Commands.literal("template").executes(context -> 1))
        //                         .then(Commands.literal("structure").executes(context -> 1))
        //                         .then(Commands.literal("feature").executes(context -> 1))
        //                         .then(Commands.literal("sound").executes(context -> 1))
        //                 )
        //
        // );
    }

    private int list_stage(CommandSourceStack source) {
        for (StageData stageData : StageManager.STAGE_DATA_LIST) {
            var stringBuilder = Component.empty().append("Click to Copy " + stageData.getResourceLocation())
                    .withStyle((style) -> style
                            .withColor(TextColor.parseColor("#7FFF00"))
                            .withHoverEvent(new HoverEvent(HoverEvent.Action.SHOW_TEXT, Component.empty().append("Click it to copy")))
                            .withClickEvent(new ClickEvent(ClickEvent.Action.COPY_TO_CLIPBOARD, stageData.toString())));
            ClientUtils.informPlayer(source.getServer(), stringBuilder);
        }
        return 1;
    }

    private int skip_to_stage(CommandSourceStack source, ResourceLocation id, BlockPos pos) {
        int startPos = StageManager.getStageStartPos(id);
        OneBlock.logger(id, pos, startPos, source.getLevel());
        var save = Levelhandler.getSaveData(source.getLevel());
        var progress = save.get(pos);
        if (progress != null) {
            progress.counter = startPos;
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
