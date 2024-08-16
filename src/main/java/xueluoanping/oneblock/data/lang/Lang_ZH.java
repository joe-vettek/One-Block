package xueluoanping.oneblock.data.lang;


import net.minecraft.data.PackOutput;
import net.neoforged.neoforge.common.data.ExistingFileHelper;
import xueluoanping.oneblock.ModContents;
import xueluoanping.oneblock.OneBlock;
import xueluoanping.oneblock.config.General;

public class Lang_ZH extends LangHelper {
    public Lang_ZH(PackOutput gen, ExistingFileHelper helper) {
        super(gen, helper, OneBlock.MOD_ID, "zh_cn");
    }


    @Override
    protected void addTranslations() {
        add(OneBlock.MOD_ID, "单方块");
        
        addNewStageTip("00", "§6\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n 阶段 0:导引§7\n 一切皆有开始。\n§a\n 新方块：§f箱子、草块、沙砾、橡木原木§a\n 新物品：§f苹果、鸡蛋、橡树树苗、小麦种子、水桶§a\n 新生物：§f猪\n\n ");
        addNewStageTip("01", "§6\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n 阶段 1: 平原§7\n 这里生长着足够多的花草树木，可供您终生享用。\n§a\n 新方块：§f桦木原木、粘土、甜瓜、灰化土、南瓜§a\n 新物品：§f桦树苗、胡萝卜、皮革、瓜子、土豆、南瓜子、甜浆果§a\n 新生物：§f鸡、牛、羊\n\n ");
        addNewStageTip("02", "§6\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n 阶段 2: 地下§7\n 许多怪物在黑暗的洞穴中徘徊。\n§a\n 新方块：§f安山岩、煤矿石、闪长岩、泥土、花岗岩、铁矿石、石头§a\n 新物品：§f棕蘑菇、煤、羽毛、红蘑菇、云杉树苗、绳子§a\n 新生物：§f爬行者、蘑菇、兔子、蜘蛛、僵尸\n\n ");
        addNewStageTip("03", "§6\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n 阶段 3: 冰冻苔原§7\n 冬天用它冰冷的手覆盖着大地。\n§a\n 新方块：§f深色橡木原木、金矿石、浮冰、雪块、云杉原木、细雪§a\n 新物品：§f蓝冰、骨头、骨粉、深色橡木树苗、金锭、冰、铁锭、兔脚、兔皮、雪球§a\n 新生物：§f狐狸, 北极熊, 流浪者, 狼\n\n ");
        addNewStageTip("04", "§6\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n 阶段 4: 溪流§7\n 河流在薄雾笼罩下。\n§a\n 新方块：§f红树林原木、泥土§a\n 新物品：§ff红树苗、鱼§a\n 新生物：§f青蛙\n\n ");
        addNewStageTip("05", "§6\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n 阶段 5: 海洋§7\n 奇怪的生物潜伏在无尽的深水中。\n§a\n 新方块：§f脑珊瑚块、气泡珊瑚块、暗海晶石、钻石矿石、火珊瑚块、角珊瑚块、海晶石、海晶石砖、沙子、海灯、海绵、管状珊瑚块§a\n 新物品：§f脑珊瑚、脑珊瑚扇、气泡珊瑚、气泡珊瑚扇、干海带、火珊瑚、火珊瑚扇、海洋之心、角珊瑚、角珊瑚扇、墨囊、海带、睡莲、鹦鹉螺壳、海晶石晶体、海晶石碎片、鳞甲、海泡菜、海草、三叉戟、管状珊瑚、管状珊瑚扇、海龟蛋§a\n 新生物：§f鳕鱼、海豚、溺尸、远古守卫者、守卫者、河豚、鲑鱼、鱿鱼、热带鱼、海龟\n\n ");
        addNewStageTip("06", "§6\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n 阶段 6: 丛林地牢§7\n 古树掩映、藤蔓缠绕，隐藏着一座地牢。\n§a\n 新方块：§f圆石、丛林原木、苔石、红石矿石§a\n 新物品：§f竹子、可可豆、钻石、丛林树苗、青金石、铅、纸、糖、甘蔗、藤蔓§a\n 新生物：§f马、豹猫、熊猫、鹦鹉、恼人鬼、女巫\n\n ");
        addNewStageTip("07", "§6\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n 阶段 7: 红色沙漠§7\n 您漫步在一个充满炎热、尘土和死亡的恶劣地方。\n§a\n 新方块：§f金合欢原木、棕色陶瓦、绿宝石矿石、青金石矿石、浅灰色陶瓦、橙色陶瓦、红沙子、红砂岩、红色陶瓦、砂岩、陶瓦、白色陶瓦、黄色陶瓦§a\n 新物品：§f金合欢树苗、仙人掌、枯萎的灌木、绿宝石、经验瓶、红石、粘液球§a\n 新生物：§f驴、尸壳、羊驼、劫掠者、村民、卫道士、流浪商人\n\n ");
        addNewStageTip("08", "§6\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n 阶段 8: 下界§7\n 地狱般的维度入侵，混乱蔓延。\n§a\n 新方块：§f远古残骸、玄武岩、黑石、深红菌丝、哭泣的黑曜石、镀金黑石、荧石、岩浆块、下界砖块、下界金矿石、下界石英矿石、下界疣块、地狱岩、黑曜石、红色下界砖块、菌光体、灵魂沙、灵魂土、诡异菌丝、诡异疣块§a\n 新物品：§f烈焰粉、烈焰魔杖、恶魂之泪、熔岩桶、熔岩膏、地狱芽苗、地狱疣、地狱合金碎片、石英、缠绕藤蔓、垂泪藤蔓、凋灵骷髅头颅§a\n 新生物：§f烈焰人、恶魂、疣猪兽、熔岩怪、猪灵、炽足兽、凋灵骷髅\n\n ");
        addNewStageTip("09", "§6\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n 阶段 9: 闲暇时光§7\n 宁静的微风吹过大地。\n§a\n 新方块：§f蜂巢、蜂巢、蜂蜜块、蜂巢块、石英块、粘液块§a\n 新物品：§f甜菜种子、甜菜汤、蛋糕、火焰炸弹、闪闪发光的瓜片、金胡萝卜、蜂蜜瓶、蜂窝、铁马铠、皮革马铠、名牌、马鞍§a\n 新生物：§f蜜蜂、猫、骡、幻影、骷髅马、史莱姆、僵尸马\n\n ");
        addNewStageTip("10", "§6\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n 阶段 10: 越过山丘§7\n 漫步在无人踏足之处。\n§a\n 新方块：§f樱桃木、可疑的沙子、可疑的砾石§a\n 新物品：§f樱桃树苗，粉色花瓣，刷子§a\n 新生物：§f骆驼、山羊、轻灵\n\n ");
        addNewStageTip("11", "§6\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n 阶段 11: 孤离之地§7\n 您面前的是一片荒芜的土地。\n§a\n 新方块：§f骨块、錾制石砖、裂纹石砖、南瓜灯、浅灰色混凝土粉末、苔藓石砖、菌丝体、石砖§a\n 新物品：§f蛛网、发酵蛛眼、火药、幻影膜、毒土豆、腐肉§a\n 新生物：§f洞穴蜘蛛、唤魔者、蠹虫、骷髅\n\n ");
        addNewStageTip("12", "§6\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n 阶段 12: 深岩之下§7\n 在深邃的地下，隐藏着一个被神秘低语所笼罩的境界。\n§a\n 新方块：§f深层板岩、紫水晶、方解石、石块、粘液块§a\n 新物品：§f发光浆果、孢子花、悬垂根须、发光地衣、尖头滴石、回音碎片§a\n 新生物：§f发光鱿鱼、美西螈、监守者\n\n ");
        addNewStageTip("13", "§6\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n 阶段 13: 末地§7\n 当黑暗虚空与你的世界相撞时，古老的力量便崛起了。\n§a\n 新方块：§f末地石、末地石砖、紫珀块、紫珀柱§a\n 新物品：§f紫颂果、龙息、末影魔杖、末影之眼、末影珍珠、幽灵箭§a\n 新生物：§f末影人、末影螨、潜影贝\n\n ");
        addNewStageTip("all", "§6\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n 您达到了最终阶段！\n 但无限方块仍然散发着奇异的能量。");

        add(ModContents.fantasy_bracelet.get(),"奇异手环");
        var itemStack=ModContents.fantasy_bracelet.get().getDefaultInstance();
        itemStack.setDamageValue(1);
        add(itemStack,"破碎的手环");

        add(ModContents.one_stone.get(), "一块普通的石头");
        addCustomName("mob", "天赐之物");

    }


}
