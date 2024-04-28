package xueluoanping.oneblock.data.lang;

import net.minecraft.data.PackOutput;
import net.minecraftforge.common.data.ExistingFileHelper;
import net.minecraftforge.common.data.LanguageProvider;
import xueluoanping.oneblock.OneBlock;
import xueluoanping.oneblock.client.OneBlockTranslator;

public abstract class LangHelper extends LanguageProvider {
    protected final ExistingFileHelper helper;
    protected final PackOutput output;


    public LangHelper(PackOutput output, ExistingFileHelper helper, String modid, String locale) {
        super(output, modid, locale);
        this.output = output;
        this.helper = helper;
        this.modid = modid;
        this.locale = locale;
    }

    public void addDebugKey(String key, String value) {
        // add(ModConstant.DebugKey.getRealKey(key), value);
    }

    public void addNewStageTip(String stageName, String hint) {
        add(OneBlockTranslator.getStageTip(modid+".phases."+stageName), hint);
    }

    public void addCustomName(String target, String hint) {
        add(OneBlockTranslator.getCustomName(target), hint);
    }

    // There is a lot of code here that is redundant, but indispensable. In order to make corrections
    protected abstract void addTranslations();

    private final String locale;
    public final String modid;

}
