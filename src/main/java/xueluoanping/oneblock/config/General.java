package xueluoanping.oneblock.config;

import net.minecraftforge.common.ForgeConfigSpec;
import xueluoanping.oneblock.OneBlock;
import xueluoanping.oneblock.client.OneBlockTranslator;
import xueluoanping.oneblock.util.Platform;

import java.io.IOException;
import java.nio.file.Files;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class General {
    public static ForgeConfigSpec COMMON_CONFIG;
    public static ForgeConfigSpec.BooleanValue debug;
    public static ForgeConfigSpec.BooleanValue collectItemNearby;

    public static ForgeConfigSpec.BooleanValue addMobName;
    public static ForgeConfigSpec.BooleanValue allowStructure;
    public static ForgeConfigSpec.BooleanValue allowSound;
    public static ForgeConfigSpec.BooleanValue allowFeature;
    public static ForgeConfigSpec.BooleanValue allowCommand;
    public static ForgeConfigSpec.BooleanValue allowHostileMobs;
    public static ForgeConfigSpec.ConfigValue<String> mobName;
    
    // public static ForgeConfigSpec.ConfigValue<String> order;
    public static Map<String, ForgeConfigSpec.BooleanValue> enableList = new HashMap<>();

    static {
        ForgeConfigSpec.Builder COMMON_BUILDER = new ForgeConfigSpec.Builder();
        COMMON_BUILDER.comment("Debug settings").push("Debug");
        debug = COMMON_BUILDER.comment("Set false to stop output dig log.").define("Log", false);
        COMMON_BUILDER.pop();

        COMMON_BUILDER.comment("Play settings").push("Play");
        collectItemNearby = COMMON_BUILDER.comment("Set true to collect item dropped nearby the oneblock but may cause some delay.")
                .define("CollectItem", true);
        addMobName = COMMON_BUILDER.comment("Set true to add a name for the mobs which spawn.")
                .define("AddMobName", true);
        mobName = COMMON_BUILDER.comment("Set the lang key for mob name.")
                .define("MobName", OneBlockTranslator.getCustomName("mob"), o -> o instanceof String);
        allowHostileMobs = COMMON_BUILDER.comment("Set true to summon unfriendly mobs.")
                .define("AllowUnfriendlyMobs", true);
        allowStructure = COMMON_BUILDER.comment("Set true to allow structure being placed.")
                .define("AllowGenerateStructure", true);
        allowFeature = COMMON_BUILDER.comment("Set true to allow feature being placed.")
                .define("AllowGenerateFeature", true);
        allowCommand = COMMON_BUILDER.comment("Set true to allow commands using.")
                .define("AllowCommand", true);
        allowSound = COMMON_BUILDER.comment("Set true to allow sounds being played.")
                .define("AllowPlaySound", true);
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
                                ForgeConfigSpec.BooleanValue enable =
                                        COMMON_BUILDER
                                                .comment(String.format("Enable compat package %s", packageName))
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
