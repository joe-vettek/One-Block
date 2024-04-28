package xueluoanping.oneblock.client;

import xueluoanping.oneblock.OneBlock;

public class OneBlockTranslator {

    public static String getCustomName(String target) {
        return "misc." + OneBlock.MOD_ID + ".custom_name." + target;
    }

    public static String getStageTip(String stage) {
        return "tip." + OneBlock.MOD_ID + ".new_stage." + stage;
    }
}
