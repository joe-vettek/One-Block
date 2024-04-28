package xueluoanping.oneblock.util;

import net.minecraft.core.BlockPos;
import net.minecraft.server.MinecraftServer;

public class CommandUtils {
    public static void performCommand(MinecraftServer server, BlockPos pos, String command) {
        var commandManager = server.getCommands();
        var source = server.createCommandSourceStack();
        command = String.format(command, pos.getX(), pos.getY(), pos.getZ());
        commandManager.performPrefixedCommand(source, command);
    }
}
