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
        var itemStack=ModContents.fantasy_bracelet.get().getDefaultInstance();
        itemStack.setDamageValue(1);
        add(itemStack,"破碎的手环");

        add(ModContents.one_stone.get(), "一块普通的石头");
        addCustomName("mob", "天赐之物");
    }


}
