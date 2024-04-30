package xueluoanping.oneblock.data.loot;

import net.minecraft.data.PackOutput;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.world.level.storage.loot.predicates.LootItemCondition;
import net.minecraftforge.common.data.GlobalLootModifierProvider;
import net.minecraftforge.common.loot.LootTableIdCondition;
import xueluoanping.oneblock.loot.modifier.AddLootTableModifier;

import java.util.List;

public class GLMProvider extends GlobalLootModifierProvider {
    public GLMProvider(PackOutput gen, String modid) {
        super(gen, modid);
    }

    @Override
    protected void start() {

        String variety = "-variety";
        for (int i = 4; i < 11; i++) {
            this.add("add_loot_" + num(i) + variety+"_from_03-1", new AddLootTableModifier(new LootItemCondition[]{
                    LootTableIdCondition.builder(new ResourceLocation("ija-one-block", num(i) + variety)).build()
            }, new ResourceLocation("oneblock", "03-1")));
        }

        for (int i = 9; i < 11; i++) {
            this.add("add_loot_" + num(i) + variety+"_from_08-1", new AddLootTableModifier(new LootItemCondition[]{
                    LootTableIdCondition.builder(new ResourceLocation("ija-one-block", num(i) + variety)).build()
            }, new ResourceLocation("oneblock", "08-1")));
        }
        for (int i = 10; i < 11; i++) {
            this.add("add_loot_" + num(i) + variety+"_from_09-1", new AddLootTableModifier(new LootItemCondition[]{
                    LootTableIdCondition.builder(new ResourceLocation("ija-one-block", num(i) + variety)).build()
            }, new ResourceLocation("oneblock", "09-1")));
        }
        for (int i = 3; i < 11; i++) {
            this.add("add_loot_" + num(i) + variety+"_from_copper", new AddLootTableModifier(new LootItemCondition[]{
                    LootTableIdCondition.builder(new ResourceLocation("ija-one-block", num(i) + variety)).build()
            }, new ResourceLocation("oneblock", "copper")));
        }
    }


    public String num(int num) {
        return num > 9 ? num + "" : "0" + num;
    }
}
