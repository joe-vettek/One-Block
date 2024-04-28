package xueluoanping.oneblock.config;

import net.minecraftforge.common.ForgeConfigSpec;

public class General {
    public static ForgeConfigSpec COMMON_CONFIG;
    public static ForgeConfigSpec.BooleanValue debug;
    public static ForgeConfigSpec.BooleanValue collectItemNearby;
    static {
        ForgeConfigSpec.Builder COMMON_BUILDER = new ForgeConfigSpec.Builder();
        COMMON_BUILDER.comment("Debug settings").push("DebugMode");
        debug = COMMON_BUILDER.comment("Set false to stop output dig log.").define("debugMode",false);
        COMMON_BUILDER.pop();

        COMMON_BUILDER.comment("Play settings").push("Collect Item");
        collectItemNearby = COMMON_BUILDER.comment("Set true to collect item dropped nearby the oneblock but may cause some delay.").define("Collect Item",true);
        COMMON_BUILDER.pop();
        COMMON_CONFIG = COMMON_BUILDER.build();
    }
}
