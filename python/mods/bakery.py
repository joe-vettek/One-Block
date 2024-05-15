# bakery
from core.api import RegisterEntry,Collections


class Block(Collections):
    # 草莓种子 Strawberry Seeds
    strawberry_seeds = RegisterEntry("bakery:strawberry_seeds")
    # 燕麦种子 Oat Seeds
    oat_seeds = RegisterEntry("bakery:oat_seeds")
    # 袋装草莓 Bag of Strawberries
    strawberry_crate = RegisterEntry("bakery:strawberry_crate")
    # 袋装燕麦 Bag of Oat
    oat_crate = RegisterEntry("bakery:oat_crate")
    # 燕麦捆 Oat Bale
    oat_block = RegisterEntry("bakery:oat_block")
    # 燕麦捆楼梯 Oat Bale Stairs
    oat_stairs = RegisterEntry("bakery:oat_stairs")
    # 燕麦捆半砖 Oat Bale Slab
    oat_slab = RegisterEntry("bakery:oat_slab")
    # 红砖水槽 Brick Sink
    kitchen_sink = RegisterEntry("bakery:kitchen_sink")
    # 红砖烤炉 Brick Oven
    brick_stove = RegisterEntry("bakery:brick_stove")
    # 烘焙台 Caking Station
    baker_station = RegisterEntry("bakery:baker_station")
    # 红砖柜台 Brick Counter
    brick_counter = RegisterEntry("bakery:brick_counter")
    # 抽屉 Drawer
    drawer = RegisterEntry("bakery:drawer")
    # 橱柜 Cabinet
    cabinet = RegisterEntry("bakery:cabinet")
    # 壁橱 Wall Cabinet
    wall_cabinet = RegisterEntry("bakery:wall_cabinet")
    # 铁桌 Iron Table
    iron_table = RegisterEntry("bakery:iron_table")
    # 铁椅 Iron Chair
    iron_chair = RegisterEntry("bakery:iron_chair")
    # 街边招牌 Street Sign
    street_sign = RegisterEntry("bakery:street_sign")
    # 蛋糕展示台 Cake Stand
    cake_stand = RegisterEntry("bakery:cake_stand")
    # 蛋糕展示柜 Cake Display
    cake_display = RegisterEntry("bakery:cake_display")
    # 纸杯蛋糕展示柜 Cupcake Display
    cupcake_display = RegisterEntry("bakery:cupcake_display")
    # 壁挂展示柜 Wall Display
    wall_display = RegisterEntry("bakery:wall_display")
    # 面包盒 Bread Box
    breadbox = RegisterEntry("bakery:breadbox")
    # 篮子 Tray
    tray = RegisterEntry("bakery:tray")
    # 面包篮 Basket of Bread
    bread_crate = RegisterEntry("bakery:bread_crate")
    # 巧克力礼盒 Chocolate Box
    chocolate_box = RegisterEntry("bakery:chocolate_box")
    # 小烹饪锅 Small Cooking Pot
    small_cooking_pot = RegisterEntry("bakery:small_cooking_pot")
    # 罐子 Jar
    jar = RegisterEntry("bakery:jar")
    # 料理碗 Crafting Bowl
    crafting_bowl = RegisterEntry("bakery:crafting_bowl")
    # Crusty Bread
    crusty_bread = RegisterEntry("bakery:crusty_bread")
    # 烘焙师面包 Bakers Bread
    bread = RegisterEntry("bakery:bread")
    # 法棍面包 Baguette
    baguette = RegisterEntry("bakery:baguette")
    # 吐司面包 Toast
    toast = RegisterEntry("bakery:toast")
    # 辫子面包 Braided Bread
    braided_bread = RegisterEntry("bakery:braided_bread")
    # 小圆面包 Bun
    bun = RegisterEntry("bakery:bun")
    # 草莓蛋糕 Strawberry Cake
    strawberry_cake = RegisterEntry("bakery:strawberry_cake")
    # 甜浆果蛋糕 Sweetberry Cake
    sweetberry_cake = RegisterEntry("bakery:sweetberry_cake")
    # 巧克力蛋糕 Chocolate Cake
    chocolate_cake = RegisterEntry("bakery:chocolate_cake")
    # 法式巧克力大蛋糕 Chocolate Gateau
    chocolate_gateau = RegisterEntry("bakery:chocolate_gateau")
    # 圆环蛋糕 Bundt Cake
    bundt_cake = RegisterEntry("bakery:bundt_cake")
    # 林茨蛋糕 Linzer Tart
    linzer_tart = RegisterEntry("bakery:linzer_tart")
    # 苹果派 Apple Pie
    apple_pie = RegisterEntry("bakery:apple_pie")
    # 发光浆果挞 Glowberry Tart
    glowberry_tart = RegisterEntry("bakery:glowberry_tart")
    # 巧克力挞 Chocolate Tart
    chocolate_tart = RegisterEntry("bakery:chocolate_tart")
    # 布丁 Pudding
    pudding = RegisterEntry("bakery:pudding")
    # 松饼 Waffle
    waffle = RegisterEntry("bakery:waffle")
    # 草莓果酱 Strawberry Jam
    strawberry_jam = RegisterEntry("bakery:strawberry_jam")
    # 甜浆果果酱 Sweetberry Jam
    sweetberry_jam = RegisterEntry("bakery:sweetberry_jam")
    # 发光浆果果酱 Glowberry Jam
    glowberry_jam = RegisterEntry("bakery:glowberry_jam")
    # 苹果酱 Apple Jam
    apple_jam = RegisterEntry("bakery:apple_jam")
    # 巧克力酱 Chocolate Spread
    chocolate_jam = RegisterEntry("bakery:chocolate_jam")
    # 石砖烤炉 Stone Bricks Stove
    stone_bricks_stove = RegisterEntry("bakery:stone_bricks_stove")
    # 圆石烤炉 Cobblestone Stove
    cobblestone_stove = RegisterEntry("bakery:cobblestone_stove")
    # 深板岩烤炉 Deepslate Stove
    deepslate_stove = RegisterEntry("bakery:deepslate_stove")
    # 花岗岩烤炉 Granite Stove
    granite_stove = RegisterEntry("bakery:granite_stove")
    # 泥砖烤炉 Mud Stove
    mud_stove = RegisterEntry("bakery:mud_stove")
    # 砂岩烤炉 Sandstone Stove
    sandstone_stove = RegisterEntry("bakery:sandstone_stove")
    # 末地石砖烤炉 Endbrick Stove
    end_stove = RegisterEntry("bakery:end_stove")
    # 红色下界砖烤炉 Red Nether Bricks Stove
    red_nether_bricks_stove = RegisterEntry("bakery:red_nether_bricks_stove")
    # 石英烤炉 Quartz Stove
    quartz_stove = RegisterEntry("bakery:quartz_stove")
    # 全物品收集者旗帜：§c馥郁烘焙 Completionist Banner: §cBakery
    bakery_standard = RegisterEntry("bakery:bakery_standard")

class Item(Collections):
    # 草莓 Strawberry
    strawberry = RegisterEntry("bakery:strawberry")
    # 燕麦 Oat
    oat = RegisterEntry("bakery:oat")
    # 擀面杖 Rolling Pin
    rolling_pin = RegisterEntry("bakery:rolling_pin")
    # 面包刀 Bread Knife
    bread_knife = RegisterEntry("bakery:bread_knife")
    # 蛋糕面团 Cake Dough
    cake_dough = RegisterEntry("bakery:cake_dough")
    # 甜面团 Sweet Dough
    sweet_dough = RegisterEntry("bakery:sweet_dough")
    # 面团 Dough
    dough = RegisterEntry("bakery:dough")
    # 酵母 Yeast
    yeast = RegisterEntry("bakery:yeast")
    # 牛角面包 Croissant
    croissant = RegisterEntry("bakery:croissant")
    # 蔬菜三明治 Vegetable Sandwich
    vegetable_sandwich = RegisterEntry("bakery:vegetable_sandwich")
    # 三明治 Sandwich
    sandwich = RegisterEntry("bakery:sandwich")
    # 草莓蛋糕切片 Slice of Strawberry Cake
    strawberry_cake_slice = RegisterEntry("bakery:strawberry_cake_slice")
    # 草莓蛋糕切片 Slice of Sweetberry Cake
    sweetberry_cake_slice = RegisterEntry("bakery:sweetberry_cake_slice")
    # 巧克力蛋糕切片 Slice of Chocolate Cake
    chocolate_cake_slice = RegisterEntry("bakery:chocolate_cake_slice")
    # 法式巧克力大蛋糕切片 Slice of Chocolate Gateau
    chocolate_gateau_slice = RegisterEntry("bakery:chocolate_gateau_slice")
    # 圆环蛋糕切片 Slice of Bundt Cake
    bundt_cake_slice = RegisterEntry("bakery:bundt_cake_slice")
    # 林茨蛋糕切片 Slice of Linzer Tart
    linzer_tart_slice = RegisterEntry("bakery:linzer_tart_slice")
    # 苹果派切片 Slice of Apple Pie
    apple_pie_slice = RegisterEntry("bakery:apple_pie_slice")
    # 发光浆果挞切片 Slice of Glowberry Tart
    glowberry_pie_slice = RegisterEntry("bakery:glowberry_pie_slice")
    # 巧克力挞切片 Slice of Chocolate Tart
    chocolate_tart_slice = RegisterEntry("bakery:chocolate_tart_slice")
    # 布丁切片 Slice of Pudding
    pudding_slice = RegisterEntry("bakery:pudding_slice")
    # 草莓曲奇 Strawberry Glazed Cookie
    strawberry_glazed_cookie = RegisterEntry("bakery:strawberry_glazed_cookie")
    # 草莓釉面饼干 Sweetberry Glazed Cookie
    sweetberry_glazed_cookie = RegisterEntry("bakery:sweetberry_glazed_cookie")
    # 巧克力曲奇 Chocolate Glazed Cookie
    chocolate_glazed_cookie = RegisterEntry("bakery:chocolate_glazed_cookie")
    # 草莓纸杯蛋糕 Strawberry Cupcake
    strawberry_cupcake = RegisterEntry("bakery:strawberry_cupcake")
    # 草莓纸杯蛋糕 Sweetberry Cupcake
    sweetberry_cupcake = RegisterEntry("bakery:sweetberry_cupcake")
    # 苹果纸杯蛋糕 Apple Cupcake
    apple_cupcake = RegisterEntry("bakery:apple_cupcake")
    # 果酱卷 Jam Roll
    jam_roll = RegisterEntry("bakery:jam_roll")
    # 填馅号角蛋糕 Stuffed Cornet
    cornet = RegisterEntry("bakery:cornet")
    # MissLilitu饼干 MissLilitu Biscuit
    misslilitu_biscuit = RegisterEntry("bakery:misslilitu_biscuit")
    # 松露巧克力 Chocolate Truffle
    chocolate_truffle = RegisterEntry("bakery:chocolate_truffle")
    # 流浪烘焙师刷怪蛋 Wandering Baker Spawn Egg
    wandering_baker_spawn_egg = RegisterEntry("bakery:wandering_baker_spawn_egg")

class Entity(Collections):
    # 流浪烘焙师 Wandering Baker
    wandering_baker = RegisterEntry("bakery:wandering_baker")


blocks = Block()
items = Item()
entities = Entity()