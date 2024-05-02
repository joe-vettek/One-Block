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

        var cond=new LootItemCondition[7];
        for (int i = 4; i < 11; i++) {
            cond[i-4]=LootTableIdCondition.builder(new ResourceLocation("ija-one-block", num(i) + variety)).build();
        }

        this.add("add_loot_from_04", new AddLootTableModifier(cond,
                new ResourceLocation("oneblock", "04")));

        cond=new LootItemCondition[2];
        for (int i = 9; i < 11; i++) {
            cond[i-9]=LootTableIdCondition.builder(new ResourceLocation("ija-one-block", num(i) + variety)).build();
        }
        this.add("add_loot_from_10", new AddLootTableModifier(cond,
                new ResourceLocation("oneblock", "10")));


        this.add("add_loot_from_12", new AddLootTableModifier(new LootItemCondition[]{
                LootTableIdCondition.builder(new ResourceLocation("ija-one-block", num(10) + variety)).build()
        }, new ResourceLocation("oneblock", "12")));


        cond=new LootItemCondition[7];
        for (int i = 4; i < 11; i++) {
            cond[i-4]=LootTableIdCondition.builder(new ResourceLocation("ija-one-block", num(i) + variety)).build();
        }
        this.add("add_loot_from_copper", new AddLootTableModifier(cond,
                new ResourceLocation("oneblock", "copper")));
    }


    public String num(int num) {
        return num > 9 ? num + "" : "0" + num;
    }
}
