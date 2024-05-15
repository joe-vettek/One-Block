# herbalbrews
from core.api import RegisterEntry,Collections


class Block(Collections):
    # 炉灶 Stove
    stove = RegisterEntry("herbalbrews:stove")
    # 袋装茶叶 Bag of Tea Leafs
    tea_leaf_crate = RegisterEntry("herbalbrews:tea_leaf_crate")
    # 绿茶叶块 Green Tea Leaf Block
    green_tea_leaf_block = RegisterEntry("herbalbrews:green_tea_leaf_block")
    # 晒干的绿茶叶块 Dried Green Tea Leaf Block
    dried_green_tea_leaf_block = RegisterEntry("herbalbrews:dried_green_tea_leaf_block")
    # 红茶叶块 Black Tea Leaf Block
    black_tea_leaf_block = RegisterEntry("herbalbrews:black_tea_leaf_block")
    # 混茶叶块 Mixed Tea Leaf Block
    mixed_tea_leaf_block = RegisterEntry("herbalbrews:mixed_tea_leaf_block")
    # 乌龙茶叶块 Oolong Tea Leaf Block
    oolong_tea_leaf_block = RegisterEntry("herbalbrews:oolong_tea_leaf_block")
    # 野生咖啡树 Wild Coffee
    wild_coffee_plant = RegisterEntry("herbalbrews:wild_coffee_plant")
    # 野生马黛树 Wild Yerba Mate
    wild_yerba_mate_plant = RegisterEntry("herbalbrews:wild_yerba_mate_plant")
    # 野生红灌木茶树 Wild Rooibos
    wild_rooibos_plant = RegisterEntry("herbalbrews:wild_rooibos_plant")
    # 木槿 Hibiscus
    hibiscus = RegisterEntry("herbalbrews:hibiscus")
    # 薰衣草 Lavender
    lavender = RegisterEntry("herbalbrews:lavender")
    # 茶树花 Tea Blossom
    tea_blossom = RegisterEntry("herbalbrews:tea_blossom")
    # 马黛茶叶 Yerba Mate Leaf
    yerba_mate_leaf = RegisterEntry("herbalbrews:yerba_mate_leaf")
    # 红灌木茶叶 Rooibos Leaf
    rooibos_leaf = RegisterEntry("herbalbrews:rooibos_leaf")
    # 咖啡豆 Coffee Beans
    coffee_beans = RegisterEntry("herbalbrews:coffee_beans")
    # 茶壶 Tea Kettle
    tea_kettle = RegisterEntry("herbalbrews:tea_kettle")
    # 铜茶壶 Copper Tea Kettle
    copper_tea_kettle = RegisterEntry("herbalbrews:copper_tea_kettle")
    # 酿煮锅 Brewing Cauldron
    cauldron = RegisterEntry("herbalbrews:cauldron")
    # 扎壶 Jug
    jug = RegisterEntry("herbalbrews:jug")
    # Hibiscus Tea
    hibiscus_tea = RegisterEntry("herbalbrews:hibiscus_tea")
    # Milk Coffee
    milk_coffee = RegisterEntry("herbalbrews:milk_coffee")
    # 全物品收集者旗帜：§a煨茶酝露 Completionist Banner: §aHerbal Brews
    herbalbrews_standard = RegisterEntry("herbalbrews:herbalbrews_standard")

class Item(Collections):
    # 女巫帽 Witch Hat
    witch_hat = RegisterEntry("herbalbrews:witch_hat")
    # 高顶礼帽 Top Hat
    top_hat = RegisterEntry("herbalbrews:top_hat")
    # 绿茶叶 Green Tea Leaf
    green_tea_leaf = RegisterEntry("herbalbrews:green_tea_leaf")
    # 晒干的绿茶叶 Dried Green Tea
    dried_green_tea = RegisterEntry("herbalbrews:dried_green_tea")
    # 晒干的红茶叶 Dried Black Tea
    dried_black_tea = RegisterEntry("herbalbrews:dried_black_tea")
    # 晒干的乌龙茶叶 Dried Oolong Tea
    dried_oolong_tea = RegisterEntry("herbalbrews:dried_oolong_tea")
    # 薰衣草花簇 Lavender Blossom
    lavender_blossom = RegisterEntry("herbalbrews:lavender_blossom")
    # 绿茶 Green Tea
    green_tea = RegisterEntry("herbalbrews:green_tea")
    # 红茶 Black Tea
    black_tea = RegisterEntry("herbalbrews:black_tea")
    # 薰衣草茶 Lavender Tea
    lavender_tea = RegisterEntry("herbalbrews:lavender_tea")
    # 马黛茶 Yerba Mate Tea
    yerba_mate_tea = RegisterEntry("herbalbrews:yerba_mate_tea")
    # 红灌木茶 Rooibos Tea
    rooibos_tea = RegisterEntry("herbalbrews:rooibos_tea")
    # 乌龙茶 Oolong Tea
    oolong_tea = RegisterEntry("herbalbrews:oolong_tea")
    # 咖啡 Coffee
    coffee = RegisterEntry("herbalbrews:coffee")
    # 盔甲药水 Armor Flask
    armor_flask = RegisterEntry("herbalbrews:armor_flask")
    # 大瓶盔甲药水 Big Armor Flask
    armor_flask_big = RegisterEntry("herbalbrews:armor_flask_big")
    # 增伤药水 Damage Flask
    damage_flask = RegisterEntry("herbalbrews:damage_flask")
    # 大瓶增伤药水 Big Damage Flask
    damage_flask_big = RegisterEntry("herbalbrews:damage_flask_big")
    # 野性药水 Feral Flask
    feral_flask = RegisterEntry("herbalbrews:feral_flask")
    # 大瓶野性药水 Big Feral Flask
    feral_flask_big = RegisterEntry("herbalbrews:feral_flask_big")


blocks = Block()
items = Item()