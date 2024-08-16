package xueluoanping.oneblock.config;

import net.neoforged.neoforge.common.ModConfigSpec;
import xueluoanping.oneblock.OneBlock;
import xueluoanping.oneblock.util.Platform;

import java.io.IOException;
import java.nio.file.Files;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class General {
    public static ModConfigSpec COMMON_CONFIG;
    public static ModConfigSpec.BooleanValue debug;
    public static ModConfigSpec.BooleanValue collectItemNearby;
    // public static ModConfigSpec.ConfigValue<String> order;
    public static Map<String, ModConfigSpec.BooleanValue> enableList = new HashMap<>();

    static {
        ModConfigSpec.Builder COMMON_BUILDER = new ModConfigSpec.Builder();
        COMMON_BUILDER.comment("Debug settings").push("Debug");
        debug = COMMON_BUILDER.comment("Set false to stop output dig log.").define("Log", false);
        COMMON_BUILDER.pop();

        COMMON_BUILDER.comment("Play settings").push("Play");
        collectItemNearby = COMMON_BUILDER.comment("Set true to collect item dropped nearby the oneblock but may cause some delay.")
                .define("CollectItem", true);
        COMMON_BUILDER.pop();

        // order = COMMON_BUILDER.comment("Set stage order.").
        // .define("Stage Order", "oneblock:phases/00;oneblock:phases/01;oneblock:phases/02;oneblock:phases/03;oneblock:phases/04;oneblock:phases/05;oneblock:phases/06;oneblock:phases/07;oneblock:phases/08;oneblock:phases/09;oneblock:phases/10;oneblock:phases/11;oneblock:phases/12;oneblock:phases/13;oneblock:phases/all");
        COMMON_BUILDER.comment("Compat settings").push("Compat");
        var basePath = Platform.getModFile(OneBlock.MOD_ID).findResource("datapacks");
        try (var fileList = Files.list(basePath)) {
            fileList.forEach(
                    path -> {
                        var s = path.toString().split("oneblock-extra-");
                        if (s.length > 1) {
                            var packageName = s[1];
                            if (Platform.isModLoaded(packageName)) {
                                ModConfigSpec.BooleanValue enable =
                                        COMMON_BUILDER
                                                .comment(String.format("Enable compat package %s", packageName))
                                                .translation(packageName)
                                                .define(packageName, true);
                                enableList.put(packageName, enable);
                            }
                        }
                    }
            );
        } catch (IOException e) {
            e.printStackTrace();
        }
        COMMON_BUILDER.pop();

        COMMON_CONFIG = COMMON_BUILDER.build();


    }

    // public static ArrayList<String> getOrder() {
    //     return new ArrayList<>(List.of("oneblock:phases/00;oneblock:phases/01;oneblock:phases/02;oneblock:phases/03;oneblock:phases/04;oneblock:phases/05;oneblock:phases/06;oneblock:phases/07;oneblock:phases/08;oneblock:phases/09;oneblock:phases/10;oneblock:phases/11;oneblock:phases/12;oneblock:phases/13;oneblock:phases/all".split(";")));
    // }
}
