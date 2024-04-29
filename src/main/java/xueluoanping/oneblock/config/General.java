package xueluoanping.oneblock.config;

import net.minecraftforge.common.ForgeConfigSpec;

import java.util.ArrayList;
import java.util.List;

public class General {
    public static ForgeConfigSpec COMMON_CONFIG;
    public static ForgeConfigSpec.BooleanValue debug;
    public static ForgeConfigSpec.BooleanValue collectItemNearby;
    public static ForgeConfigSpec.ConfigValue<ArrayList<String>> order;

    static {
        ForgeConfigSpec.Builder COMMON_BUILDER = new ForgeConfigSpec.Builder();
        COMMON_BUILDER.comment("Debug settings").push("DebugMode");
        debug = COMMON_BUILDER.comment("Set false to stop output dig log.").define("debugMode", false);
        COMMON_BUILDER.pop();

        COMMON_BUILDER.comment("Play settings").push("Collect Item");
        collectItemNearby = COMMON_BUILDER.comment("Set true to collect item dropped nearby the oneblock but may cause some delay.").define("Collect Item", true);
        COMMON_BUILDER.pop();

        COMMON_BUILDER.push("Order");
        order = COMMON_BUILDER.comment("Set stage order.").define("order", new ArrayList<>(List.of(
                "oneblock:phases/end_portal",
                "oneblock:phases/00",
                "oneblock:phases/01",
                "oneblock:phases/02",
                "oneblock:phases/03",
                "oneblock:phases/03-1",
                "oneblock:phases/04",
                "oneblock:phases/05",
                "oneblock:phases/06",
                "oneblock:phases/07",
                "oneblock:phases/08",
                "oneblock:phases/08-1",
                "oneblock:phases/09",
                "oneblock:phases/09-1",
                "oneblock:phases/end_portal",
                "oneblock:phases/10",
                "oneblock:phases/all")),o -> true);
        COMMON_BUILDER.pop();
        COMMON_CONFIG = COMMON_BUILDER.build();
    }
}
