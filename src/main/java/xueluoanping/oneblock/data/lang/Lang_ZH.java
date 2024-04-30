package xueluoanping.oneblock.data.lang;


import net.minecraft.data.PackOutput;
import net.minecraftforge.common.data.ExistingFileHelper;
import xueluoanping.oneblock.ModContents;
import xueluoanping.oneblock.OneBlock;

public class Lang_ZH extends LangHelper {
    public Lang_ZH(PackOutput gen, ExistingFileHelper helper) {
        super(gen, helper, OneBlock.MOD_ID, "zh_cn");
    }


    @Override
    protected void addTranslations() {
        add(OneBlock.MOD_ID, "单方块");

        add(ModContents.fantasy_bracelet.get(),"奇异手环");
        // addWailaHint( "§o<..按住shift以查看更多..>");
        // addSlot("§7%s号格子: 装有%s的%s");
    }


}
