# create
from core.api import RegisterEntry,Collections


class Item(Collections):
    # 铜背罐 Copper Backtank
    copper_backtank = RegisterEntry("create:copper_backtank")
    # 下界合金背罐 Netherite Backtank
    netherite_backtank = RegisterEntry("create:netherite_backtank")
    # 扳手 Wrench
    wrench = RegisterEntry("create:wrench")
    # 无线红石遥控器 Linked Controller
    linked_controller = RegisterEntry("create:linked_controller")
    # 土豆加农炮 Potato Cannon
    potato_cannon = RegisterEntry("create:potato_cannon")
    # 伸缩机械手 Extendo Grip
    extendo_grip = RegisterEntry("create:extendo_grip")
    # 对称之杖 Wand Of Symmetry
    wand_of_symmetry = RegisterEntry("create:wand_of_symmetry")
    # 手持式环境塑形器 Creative Worldshaper
    handheld_worldshaper = RegisterEntry("create:handheld_worldshaper")
    # 列车时刻表 Train Schedule
    schedule = RegisterEntry("create:schedule")
    # 小麦粉 Wheat Flour
    wheat_flour = RegisterEntry("create:wheat_flour")
    # 面团 Dough
    dough = RegisterEntry("create:dough")
    # 余烬面粉 Cinder Flour
    cinder_flour = RegisterEntry("create:cinder_flour")
    # 玫瑰石英 Rose Quartz
    rose_quartz = RegisterEntry("create:rose_quartz")
    # 磨制玫瑰石英 Polished Rose Quartz
    polished_rose_quartz = RegisterEntry("create:polished_rose_quartz")
    # 黑曜石粉末 Powdered Obsidian
    powdered_obsidian = RegisterEntry("create:powdered_obsidian")
    # 坚固板 Sturdy Sheet
    sturdy_sheet = RegisterEntry("create:sturdy_sheet")
    # 扇叶 Propeller
    propeller = RegisterEntry("create:propeller")
    # 搅拌器 Whisk
    whisk = RegisterEntry("create:whisk")
    # 黄铜手部零件 Brass Hand
    brass_hand = RegisterEntry("create:brass_hand")
    # 合成槽盖板 Crafter Slot Cover
    crafter_slot_cover = RegisterEntry("create:crafter_slot_cover")
    # 电子管 Electron Tube
    electron_tube = RegisterEntry("create:electron_tube")
    # 精密构件 Precision Mechanism
    precision_mechanism = RegisterEntry("create:precision_mechanism")
    # 烈焰蛋糕 Blaze Cake
    blaze_cake = RegisterEntry("create:blaze_cake")
    # 创造烈焰蛋糕 Creative Blaze Cake
    creative_blaze_cake = RegisterEntry("create:creative_blaze_cake")
    # 巧克力棒 Bar of Chocolate
    bar_of_chocolate = RegisterEntry("create:bar_of_chocolate")
    # 甜甜卷 Sweet Roll
    sweet_roll = RegisterEntry("create:sweet_roll")
    # 巧克力包层浆果 Chocolate Glazed Berries
    chocolate_glazed_berries = RegisterEntry("create:chocolate_glazed_berries")
    # 蜜渍苹果 Honeyed Apple
    honeyed_apple = RegisterEntry("create:honeyed_apple")
    # 建造工茶饮 Builder's Tea
    builders_tea = RegisterEntry("create:builders_tea")
    # 粗锌 Raw Zinc
    raw_zinc = RegisterEntry("create:raw_zinc")
    # 安山合金 Andesite Alloy
    andesite_alloy = RegisterEntry("create:andesite_alloy")
    # 锌锭 Zinc Ingot
    zinc_ingot = RegisterEntry("create:zinc_ingot")
    # 黄铜锭 Brass Ingot
    brass_ingot = RegisterEntry("create:brass_ingot")
    # 铜粒 Copper Nugget
    copper_nugget = RegisterEntry("create:copper_nugget")
    # 锌粒 Zinc Nugget
    zinc_nugget = RegisterEntry("create:zinc_nugget")
    # 黄铜粒 Brass Nugget
    brass_nugget = RegisterEntry("create:brass_nugget")
    # 经验颗粒 Nugget of Experience
    experience_nugget = RegisterEntry("create:experience_nugget")
    # 铜板 Copper Sheet
    copper_sheet = RegisterEntry("create:copper_sheet")
    # 黄铜板 Brass Sheet
    brass_sheet = RegisterEntry("create:brass_sheet")
    # 铁板 Iron Sheet
    iron_sheet = RegisterEntry("create:iron_sheet")
    # 金板 Golden Sheet
    golden_sheet = RegisterEntry("create:golden_sheet")
    # 粉碎铁矿石 Crushed Raw Iron
    crushed_raw_iron = RegisterEntry("create:crushed_raw_iron")
    # 粉碎金矿石 Crushed Raw Gold
    crushed_raw_gold = RegisterEntry("create:crushed_raw_gold")
    # 粉碎铜矿石 Crushed Raw Copper
    crushed_raw_copper = RegisterEntry("create:crushed_raw_copper")
    # 粉碎锌矿石 Crushed Raw Zinc
    crushed_raw_zinc = RegisterEntry("create:crushed_raw_zinc")
    # 工程师护目镜 Engineer's Goggles
    goggles = RegisterEntry("create:goggles")
    # 强力胶 Super Glue
    super_glue = RegisterEntry("create:super_glue")
    # 矿车连轴器 Minecart Coupling
    minecart_coupling = RegisterEntry("create:minecart_coupling")
    # 合成蓝图 Crafting Blueprint
    crafting_blueprint = RegisterEntry("create:crafting_blueprint")
    # 铜潜水头盔 Copper Diving Helmet
    copper_diving_helmet = RegisterEntry("create:copper_diving_helmet")
    # 下界合金潜水头盔 Netherite Diving Helmet
    netherite_diving_helmet = RegisterEntry("create:netherite_diving_helmet")
    # 铜潜水靴 Copper Diving Boots
    copper_diving_boots = RegisterEntry("create:copper_diving_boots")
    # 下界合金潜水靴 Netherite Diving Boots
    netherite_diving_boots = RegisterEntry("create:netherite_diving_boots")
    # 砂纸 Sand Paper
    sand_paper = RegisterEntry("create:sand_paper")
    # 红沙砂纸 Red Sand Paper
    red_sand_paper = RegisterEntry("create:red_sand_paper")
    # 树木肥料 Tree Fertilizer
    tree_fertilizer = RegisterEntry("create:tree_fertilizer")
    # 列表过滤器 List Filter
    filter = RegisterEntry("create:filter")
    # 属性过滤器 Attribute Filter
    attribute_filter = RegisterEntry("create:attribute_filter")
    # 空白蓝图 Empty Schematic
    empty_schematic = RegisterEntry("create:empty_schematic")
    # 蓝图与笔 Schematic And Quill
    schematic_and_quill = RegisterEntry("create:schematic_and_quill")

class Block(Collections):
    # 蓝图加农炮 Schematicannon
    schematicannon = RegisterEntry("create:schematicannon")
    # 蓝图桌 Schematic Table
    schematic_table = RegisterEntry("create:schematic_table")
    # 传动杆 Shaft
    shaft = RegisterEntry("create:shaft")
    # 齿轮 Cogwheel
    cogwheel = RegisterEntry("create:cogwheel")
    # 大齿轮 Large Cogwheel
    large_cogwheel = RegisterEntry("create:large_cogwheel")
    # 十字齿轮箱 Gearbox
    gearbox = RegisterEntry("create:gearbox")
    # 竖直十字齿轮箱 Vertical Gearbox
    vertical_gearbox = RegisterEntry("create:vertical_gearbox")
    # 离合器 Clutch
    clutch = RegisterEntry("create:clutch")
    # 反转齿轮箱 Gearshift
    gearshift = RegisterEntry("create:gearshift")
    # 链式传动箱 Encased Chain Drive
    encased_chain_drive = RegisterEntry("create:encased_chain_drive")
    # 可调节链式传动箱 Adjustable Chain Gearshift
    adjustable_chain_gearshift = RegisterEntry("create:adjustable_chain_gearshift")
    # 传送带 Mechanical Belt
    belt_connector = RegisterEntry("create:belt_connector")
    # 创造马达 Creative Motor
    creative_motor = RegisterEntry("create:creative_motor")
    # 水车 Water Wheel
    water_wheel = RegisterEntry("create:water_wheel")
    # 大型水车 Large Water Wheel
    large_water_wheel = RegisterEntry("create:large_water_wheel")
    # 鼓风机 Encased Fan
    encased_fan = RegisterEntry("create:encased_fan")
    # 分散网 Nozzle
    nozzle = RegisterEntry("create:nozzle")
    # 转盘 Turntable
    turntable = RegisterEntry("create:turntable")
    # 手摇曲柄 Hand Crank
    hand_crank = RegisterEntry("create:hand_crank")
    # 布谷鸟闹钟 Cuckoo Clock
    cuckoo_clock = RegisterEntry("create:cuckoo_clock")
    # 石磨 Millstone
    millstone = RegisterEntry("create:millstone")
    # 粉碎轮 Crushing Wheel
    crushing_wheel = RegisterEntry("create:crushing_wheel")
    # 动力辊压机 Mechanical Press
    mechanical_press = RegisterEntry("create:mechanical_press")
    # 动力搅拌器 Mechanical Mixer
    mechanical_mixer = RegisterEntry("create:mechanical_mixer")
    # 工作盆 Basin
    basin = RegisterEntry("create:basin")
    # 空的烈焰人燃烧室 Empty Blaze Burner
    empty_blaze_burner = RegisterEntry("create:empty_blaze_burner")
    # 烈焰人燃烧室 Blaze Burner
    blaze_burner = RegisterEntry("create:blaze_burner")
    # 置物台 Depot
    depot = RegisterEntry("create:depot")
    # 弹射置物台 Weighted Ejector
    weighted_ejector = RegisterEntry("create:weighted_ejector")
    # 溜槽 Chute
    chute = RegisterEntry("create:chute")
    # 智能溜槽 Smart Chute
    smart_chute = RegisterEntry("create:smart_chute")
    # 速度表 Speedometer
    speedometer = RegisterEntry("create:speedometer")
    # 应力表 Stressometer
    stressometer = RegisterEntry("create:stressometer")
    # 木质支架 Wooden Bracket
    wooden_bracket = RegisterEntry("create:wooden_bracket")
    # 金属支架 Metal Bracket
    metal_bracket = RegisterEntry("create:metal_bracket")
    # 流体管道 Fluid Pipe
    fluid_pipe = RegisterEntry("create:fluid_pipe")
    # 动力泵 Mechanical Pump
    mechanical_pump = RegisterEntry("create:mechanical_pump")
    # 智能流体管道 Smart Fluid Pipe
    smart_fluid_pipe = RegisterEntry("create:smart_fluid_pipe")
    # 流体阀门 Fluid Valve
    fluid_valve = RegisterEntry("create:fluid_valve")
    # 铜阀门手轮 Copper Valve Handle
    copper_valve_handle = RegisterEntry("create:copper_valve_handle")
    # 流体储罐 Fluid Tank
    fluid_tank = RegisterEntry("create:fluid_tank")
    # 创造流体储罐 Creative Fluid Tank
    creative_fluid_tank = RegisterEntry("create:creative_fluid_tank")
    # 软管滑轮 Hose Pulley
    hose_pulley = RegisterEntry("create:hose_pulley")
    # 分液池 Item Drain
    item_drain = RegisterEntry("create:item_drain")
    # 注液器 Spout
    spout = RegisterEntry("create:spout")
    # 移动式流体接口 Portable Fluid Interface
    portable_fluid_interface = RegisterEntry("create:portable_fluid_interface")
    # 蒸汽引擎 Steam Engine
    steam_engine = RegisterEntry("create:steam_engine")
    # 蒸汽笛 Steam Whistle
    steam_whistle = RegisterEntry("create:steam_whistle")
    # 动力活塞 Mechanical Piston
    mechanical_piston = RegisterEntry("create:mechanical_piston")
    # 黏性动力活塞 Sticky Mechanical Piston
    sticky_mechanical_piston = RegisterEntry("create:sticky_mechanical_piston")
    # 活塞杆 Piston Extension Pole
    piston_extension_pole = RegisterEntry("create:piston_extension_pole")
    # 起重机取物器 Gantry Carriage
    gantry_carriage = RegisterEntry("create:gantry_carriage")
    # 起重机杆 Gantry Shaft
    gantry_shaft = RegisterEntry("create:gantry_shaft")
    # 风车轴承 Windmill Bearing
    windmill_bearing = RegisterEntry("create:windmill_bearing")
    # 动力轴承 Mechanical Bearing
    mechanical_bearing = RegisterEntry("create:mechanical_bearing")
    # 发条轴承 Clockwork Bearing
    clockwork_bearing = RegisterEntry("create:clockwork_bearing")
    # 绳索滑轮 Rope Pulley
    rope_pulley = RegisterEntry("create:rope_pulley")
    # 升降机滑轮 Elevator Pulley
    elevator_pulley = RegisterEntry("create:elevator_pulley")
    # 矿车装配站 Cart Assembler
    cart_assembler = RegisterEntry("create:cart_assembler")
    # 控制铁轨 Controller Rail
    controller_rail = RegisterEntry("create:controller_rail")
    # 轴向底盘 Linear Chassis
    linear_chassis = RegisterEntry("create:linear_chassis")
    # 轴向底盘二号 Secondary Linear Chassis
    secondary_linear_chassis = RegisterEntry("create:secondary_linear_chassis")
    # 径向底盘 Radial Chassis
    radial_chassis = RegisterEntry("create:radial_chassis")
    # 黏着器 Sticker
    sticker = RegisterEntry("create:sticker")
    # 动态结构控制器 Contraption Controls
    contraption_controls = RegisterEntry("create:contraption_controls")
    # 动力钻头 Mechanical Drill
    mechanical_drill = RegisterEntry("create:mechanical_drill")
    # 动力锯 Mechanical Saw
    mechanical_saw = RegisterEntry("create:mechanical_saw")
    # 机械手 Deployer
    deployer = RegisterEntry("create:deployer")
    # 移动式存储接口 Portable Storage Interface
    portable_storage_interface = RegisterEntry("create:portable_storage_interface")
    # 接触式红石信号发生器 Redstone Contact
    redstone_contact = RegisterEntry("create:redstone_contact")
    # 动力收割机 Mechanical Harvester
    mechanical_harvester = RegisterEntry("create:mechanical_harvester")
    # 动力犁 Mechanical Plough
    mechanical_plough = RegisterEntry("create:mechanical_plough")
    # 动力压路机 Mechanical Roller
    mechanical_roller = RegisterEntry("create:mechanical_roller")
    # 风帆框架 Windmill Sail Frame
    sail_frame = RegisterEntry("create:sail_frame")
    # 风帆 Windmill Sail
    white_sail = RegisterEntry("create:white_sail")
    # 安山机壳 Andesite Casing
    andesite_casing = RegisterEntry("create:andesite_casing")
    # 黄铜机壳 Brass Casing
    brass_casing = RegisterEntry("create:brass_casing")
    # 铜机壳 Copper Casing
    copper_casing = RegisterEntry("create:copper_casing")
    # 动力合成器 Mechanical Crafter
    mechanical_crafter = RegisterEntry("create:mechanical_crafter")
    # 可编程齿轮箱 Sequenced Gearshift
    sequenced_gearshift = RegisterEntry("create:sequenced_gearshift")
    # 飞轮 Flywheel
    flywheel = RegisterEntry("create:flywheel")
    # 转速控制器 Rotation Speed Controller
    rotation_speed_controller = RegisterEntry("create:rotation_speed_controller")
    # 动力臂 Mechanical Arm
    mechanical_arm = RegisterEntry("create:mechanical_arm")
    # 列车轨道 Train Track
    track = RegisterEntry("create:track")
    # 列车机壳 Train Casing
    railway_casing = RegisterEntry("create:railway_casing")
    # 列车站 Train Station
    track_station = RegisterEntry("create:track_station")
    # 列车信号机 Train Signal
    track_signal = RegisterEntry("create:track_signal")
    # 列车侦测器 Train Observer
    track_observer = RegisterEntry("create:track_observer")
    # 列车驾驶台 Train Controls
    controls = RegisterEntry("create:controls")
    # 物品保险库 Item Vault
    item_vault = RegisterEntry("create:item_vault")
    # 安山漏斗 Andesite Funnel
    andesite_funnel = RegisterEntry("create:andesite_funnel")
    # 黄铜漏斗 Brass Funnel
    brass_funnel = RegisterEntry("create:brass_funnel")
    # 安山隧道 Andesite Tunnel
    andesite_tunnel = RegisterEntry("create:andesite_tunnel")
    # 黄铜隧道 Brass Tunnel
    brass_tunnel = RegisterEntry("create:brass_tunnel")
    # 智能侦测器 Smart Observer
    content_observer = RegisterEntry("create:content_observer")
    # 存量转信器 Threshold Switch
    stockpile_switch = RegisterEntry("create:stockpile_switch")
    # 创造板条箱 Creative Crate
    creative_crate = RegisterEntry("create:creative_crate")
    # 显示链接器 Display Link
    display_link = RegisterEntry("create:display_link")
    # 翻牌显示器 Display Board
    display_board = RegisterEntry("create:display_board")
    # 辉光管 Nixie Tube
    nixie_tube = RegisterEntry("create:nixie_tube")
    # 玫瑰石英灯 Rose Quartz Lamp
    rose_quartz_lamp = RegisterEntry("create:rose_quartz_lamp")
    # 无线红石信号终端 Redstone Link
    redstone_link = RegisterEntry("create:redstone_link")
    # 模拟拉杆 Analog Lever
    analog_lever = RegisterEntry("create:analog_lever")
    # 置物板 Placard
    placard = RegisterEntry("create:placard")
    # 脉冲中继器 Pulse Repeater
    pulse_repeater = RegisterEntry("create:pulse_repeater")
    # 脉冲延长器 Pulse Extender
    pulse_extender = RegisterEntry("create:pulse_extender")
    # 锁存器 Powered Latch
    powered_latch = RegisterEntry("create:powered_latch")
    # 转换锁存器 Powered Toggle Latch
    powered_toggle_latch = RegisterEntry("create:powered_toggle_latch")
    # 奇异钟 Peculiar Bell
    peculiar_bell = RegisterEntry("create:peculiar_bell")
    # 缠魂钟 Haunted Bell
    haunted_bell = RegisterEntry("create:haunted_bell")
    # 棕色工具箱 Brown Toolbox
    brown_toolbox = RegisterEntry("create:brown_toolbox")
    # 剪贴板 Clipboard
    clipboard = RegisterEntry("create:clipboard")
    # 安山梯子 Andesite Ladder
    andesite_ladder = RegisterEntry("create:andesite_ladder")
    # 黄铜梯子 Brass Ladder
    brass_ladder = RegisterEntry("create:brass_ladder")
    # 铜梯子 Copper Ladder
    copper_ladder = RegisterEntry("create:copper_ladder")
    # 安山栏杆 Andesite Bars
    andesite_bars = RegisterEntry("create:andesite_bars")
    # 黄铜栏杆 Brass Bars
    brass_bars = RegisterEntry("create:brass_bars")
    # 铜栏杆 Copper Bars
    copper_bars = RegisterEntry("create:copper_bars")
    # 安山脚手架 Andesite Scaffolding
    andesite_scaffolding = RegisterEntry("create:andesite_scaffolding")
    # 黄铜脚手架 Brass Scaffolding
    brass_scaffolding = RegisterEntry("create:brass_scaffolding")
    # 铜脚手架 Copper Scaffolding
    copper_scaffolding = RegisterEntry("create:copper_scaffolding")
    # 金属梁 Metal Girder
    metal_girder = RegisterEntry("create:metal_girder")
    # 伪装半阶 Copycat Step
    copycat_step = RegisterEntry("create:copycat_step")
    # 伪装板 Copycat Panel
    copycat_panel = RegisterEntry("create:copycat_panel")
    # 红色坐垫 Red Seat
    red_seat = RegisterEntry("create:red_seat")
    # 安山门 Andesite Door
    andesite_door = RegisterEntry("create:andesite_door")
    # 黄铜门 Brass Door
    brass_door = RegisterEntry("create:brass_door")
    # 铜门 Copper Door
    copper_door = RegisterEntry("create:copper_door")
    # 列车门 Train Door
    train_door = RegisterEntry("create:train_door")
    # 列车活板门 Train Trapdoor
    train_trapdoor = RegisterEntry("create:train_trapdoor")
    # 边框玻璃门 Framed Glass Door
    framed_glass_door = RegisterEntry("create:framed_glass_door")
    # 边框玻璃活板门 Framed Glass Trapdoor
    framed_glass_trapdoor = RegisterEntry("create:framed_glass_trapdoor")
    # 锌矿石 Zinc Ore
    zinc_ore = RegisterEntry("create:zinc_ore")
    # 深层锌矿石 Deepslate Zinc Ore
    deepslate_zinc_ore = RegisterEntry("create:deepslate_zinc_ore")
    # 粗锌块 Block of Raw Zinc
    raw_zinc_block = RegisterEntry("create:raw_zinc_block")
    # 锌块 Block of Zinc
    zinc_block = RegisterEntry("create:zinc_block")
    # 安山合金块 Block of Andesite Alloy
    andesite_alloy_block = RegisterEntry("create:andesite_alloy_block")
    # 工业铁块 Block of Industrial Iron
    industrial_iron_block = RegisterEntry("create:industrial_iron_block")
    # 黄铜块 Block of Brass
    brass_block = RegisterEntry("create:brass_block")
    # 经验块 Block of Experience
    experience_block = RegisterEntry("create:experience_block")
    # 玫瑰石英块 Block of Rose Quartz
    rose_quartz_block = RegisterEntry("create:rose_quartz_block")
    # 玫瑰石英砖块 Rose Quartz Tiles
    rose_quartz_tiles = RegisterEntry("create:rose_quartz_tiles")
    # 玫瑰石英小砖块 Small Rose Quartz Tiles
    small_rose_quartz_tiles = RegisterEntry("create:small_rose_quartz_tiles")
    # 铜砖瓦 Copper Shingles
    copper_shingles = RegisterEntry("create:copper_shingles")
    # 斑驳的铜砖瓦 Exposed Copper Shingles
    exposed_copper_shingles = RegisterEntry("create:exposed_copper_shingles")
    # 锈蚀的铜砖瓦 Weathered Copper Shingles
    weathered_copper_shingles = RegisterEntry("create:weathered_copper_shingles")
    # 氧化的铜砖瓦 Oxidized Copper Shingles
    oxidized_copper_shingles = RegisterEntry("create:oxidized_copper_shingles")
    # 铜砖瓦台阶 Copper Shingle Slab
    copper_shingle_slab = RegisterEntry("create:copper_shingle_slab")
    # 斑驳的铜砖瓦台阶 Exposed Copper Shingle Slab
    exposed_copper_shingle_slab = RegisterEntry("create:exposed_copper_shingle_slab")
    # 锈蚀的铜砖瓦台阶 Weathered Copper Shingle Slab
    weathered_copper_shingle_slab = RegisterEntry("create:weathered_copper_shingle_slab")
    # 氧化的铜砖瓦台阶 Oxidized Copper Shingle Slab
    oxidized_copper_shingle_slab = RegisterEntry("create:oxidized_copper_shingle_slab")
    # 铜砖瓦楼梯 Copper Shingle Stairs
    copper_shingle_stairs = RegisterEntry("create:copper_shingle_stairs")
    # 斑驳的铜砖瓦楼梯 Exposed Copper Shingle Stairs
    exposed_copper_shingle_stairs = RegisterEntry("create:exposed_copper_shingle_stairs")
    # 锈蚀的铜砖瓦楼梯 Weathered Copper Shingle Stairs
    weathered_copper_shingle_stairs = RegisterEntry("create:weathered_copper_shingle_stairs")
    # 氧化的铜砖瓦楼梯 Oxidized Copper Shingle Stairs
    oxidized_copper_shingle_stairs = RegisterEntry("create:oxidized_copper_shingle_stairs")
    # 涂蜡铜砖瓦 Waxed Copper Shingles
    waxed_copper_shingles = RegisterEntry("create:waxed_copper_shingles")
    # 斑驳的涂蜡铜砖瓦 Waxed Exposed Copper Shingles
    waxed_exposed_copper_shingles = RegisterEntry("create:waxed_exposed_copper_shingles")
    # 锈蚀的涂蜡铜砖瓦 Waxed Weathered Copper Shingles
    waxed_weathered_copper_shingles = RegisterEntry("create:waxed_weathered_copper_shingles")
    # 氧化的涂蜡铜砖瓦 Waxed Oxidized Copper Shingles
    waxed_oxidized_copper_shingles = RegisterEntry("create:waxed_oxidized_copper_shingles")
    # 涂蜡铜砖瓦台阶 Waxed Copper Shingle Slab
    waxed_copper_shingle_slab = RegisterEntry("create:waxed_copper_shingle_slab")
    # 斑驳的涂蜡铜砖瓦台阶 Waxed Exposed Copper Shingle Slab
    waxed_exposed_copper_shingle_slab = RegisterEntry("create:waxed_exposed_copper_shingle_slab")
    # 锈蚀的涂蜡铜砖瓦台阶 Waxed Weathered Copper Shingle Slab
    waxed_weathered_copper_shingle_slab = RegisterEntry("create:waxed_weathered_copper_shingle_slab")
    # 氧化的涂蜡铜砖瓦台阶 Waxed Oxidized Copper Shingle Slab
    waxed_oxidized_copper_shingle_slab = RegisterEntry("create:waxed_oxidized_copper_shingle_slab")
    # 涂蜡铜砖瓦楼梯 Waxed Copper Shingle Stairs
    waxed_copper_shingle_stairs = RegisterEntry("create:waxed_copper_shingle_stairs")
    # 斑驳的涂蜡铜砖瓦楼梯 Waxed Exposed Copper Shingle Stairs
    waxed_exposed_copper_shingle_stairs = RegisterEntry("create:waxed_exposed_copper_shingle_stairs")
    # 锈蚀的涂蜡铜砖瓦楼梯 Waxed Weathered Copper Shingle Stairs
    waxed_weathered_copper_shingle_stairs = RegisterEntry("create:waxed_weathered_copper_shingle_stairs")
    # 氧化的涂蜡铜砖瓦楼梯 Waxed Oxidized Copper Shingle Stairs
    waxed_oxidized_copper_shingle_stairs = RegisterEntry("create:waxed_oxidized_copper_shingle_stairs")
    # 铜瓦 Copper Tiles
    copper_tiles = RegisterEntry("create:copper_tiles")
    # 斑驳的铜瓦 Exposed Copper Tiles
    exposed_copper_tiles = RegisterEntry("create:exposed_copper_tiles")
    # 锈蚀的铜瓦 Weathered Copper Tiles
    weathered_copper_tiles = RegisterEntry("create:weathered_copper_tiles")
    # 氧化的铜瓦 Oxidized Copper Tiles
    oxidized_copper_tiles = RegisterEntry("create:oxidized_copper_tiles")
    # 铜瓦台阶 Copper Tile Slab
    copper_tile_slab = RegisterEntry("create:copper_tile_slab")
    # 斑驳的铜瓦台阶 Exposed Copper Tile Slab
    exposed_copper_tile_slab = RegisterEntry("create:exposed_copper_tile_slab")
    # 锈蚀的铜瓦台阶 Weathered Copper Tile Slab
    weathered_copper_tile_slab = RegisterEntry("create:weathered_copper_tile_slab")
    # 氧化的铜瓦台阶 Oxidized Copper Tile Slab
    oxidized_copper_tile_slab = RegisterEntry("create:oxidized_copper_tile_slab")
    # 铜瓦楼梯 Copper Tile Stairs
    copper_tile_stairs = RegisterEntry("create:copper_tile_stairs")
    # 斑驳的铜瓦楼梯 Exposed Copper Tile Stairs
    exposed_copper_tile_stairs = RegisterEntry("create:exposed_copper_tile_stairs")
    # 锈蚀的铜瓦楼梯 Weathered Copper Tile Stairs
    weathered_copper_tile_stairs = RegisterEntry("create:weathered_copper_tile_stairs")
    # 氧化的铜瓦楼梯 Oxidized Copper Tile Stairs
    oxidized_copper_tile_stairs = RegisterEntry("create:oxidized_copper_tile_stairs")
    # 涂蜡铜瓦 Waxed Copper Tiles
    waxed_copper_tiles = RegisterEntry("create:waxed_copper_tiles")
    # 斑驳的涂蜡铜瓦 Waxed Exposed Copper Tiles
    waxed_exposed_copper_tiles = RegisterEntry("create:waxed_exposed_copper_tiles")
    # 锈蚀的涂蜡铜瓦 Waxed Weathered Copper Tiles
    waxed_weathered_copper_tiles = RegisterEntry("create:waxed_weathered_copper_tiles")
    # 氧化的涂蜡铜瓦 Waxed Oxidized Copper Tiles
    waxed_oxidized_copper_tiles = RegisterEntry("create:waxed_oxidized_copper_tiles")
    # 涂蜡铜瓦台阶 Waxed Copper Tile Slab
    waxed_copper_tile_slab = RegisterEntry("create:waxed_copper_tile_slab")
    # 斑驳的涂蜡铜瓦台阶 Waxed Exposed Copper Tile Slab
    waxed_exposed_copper_tile_slab = RegisterEntry("create:waxed_exposed_copper_tile_slab")
    # 锈蚀的涂蜡铜瓦台阶 Waxed Weathered Copper Tile Slab
    waxed_weathered_copper_tile_slab = RegisterEntry("create:waxed_weathered_copper_tile_slab")
    # 氧化的涂蜡铜瓦台阶 Waxed Oxidized Copper Tile Slab
    waxed_oxidized_copper_tile_slab = RegisterEntry("create:waxed_oxidized_copper_tile_slab")
    # 涂蜡铜瓦楼梯 Waxed Copper Tile Stairs
    waxed_copper_tile_stairs = RegisterEntry("create:waxed_copper_tile_stairs")
    # 斑驳的涂蜡铜瓦楼梯 Waxed Exposed Copper Tile Stairs
    waxed_exposed_copper_tile_stairs = RegisterEntry("create:waxed_exposed_copper_tile_stairs")
    # 锈蚀的涂蜡铜瓦楼梯 Waxed Weathered Copper Tile Stairs
    waxed_weathered_copper_tile_stairs = RegisterEntry("create:waxed_weathered_copper_tile_stairs")
    # 氧化的涂蜡铜瓦楼梯 Waxed Oxidized Copper Tile Stairs
    waxed_oxidized_copper_tile_stairs = RegisterEntry("create:waxed_oxidized_copper_tile_stairs")
    # 十字玻璃窗 Tiled Glass
    tiled_glass = RegisterEntry("create:tiled_glass")
    # 边框玻璃 Framed Glass
    framed_glass = RegisterEntry("create:framed_glass")
    # 水平边框玻璃 Horizontal Framed Glass
    horizontal_framed_glass = RegisterEntry("create:horizontal_framed_glass")
    # 竖直边框玻璃 Vertical Framed Glass
    vertical_framed_glass = RegisterEntry("create:vertical_framed_glass")
    # 十字玻璃窗户板 Tiled Glass Pane
    tiled_glass_pane = RegisterEntry("create:tiled_glass_pane")
    # 边框玻璃板 Framed Glass Pane
    framed_glass_pane = RegisterEntry("create:framed_glass_pane")
    # 水平边框玻璃板 Horizontal Framed Glass Pane
    horizontal_framed_glass_pane = RegisterEntry("create:horizontal_framed_glass_pane")
    # 竖直边框玻璃板 Vertical Framed Glass Pane
    vertical_framed_glass_pane = RegisterEntry("create:vertical_framed_glass_pane")
    # 橡木窗户 Oak Window
    oak_window = RegisterEntry("create:oak_window")
    # 云杉木窗户 Spruce Window
    spruce_window = RegisterEntry("create:spruce_window")
    # 白桦木窗户 Birch Window
    birch_window = RegisterEntry("create:birch_window")
    # 丛林木窗户 Jungle Window
    jungle_window = RegisterEntry("create:jungle_window")
    # 金合欢木窗户 Acacia Window
    acacia_window = RegisterEntry("create:acacia_window")
    # 深色橡木窗户 Dark Oak Window
    dark_oak_window = RegisterEntry("create:dark_oak_window")
    # 红树木窗户 Mangrove Window
    mangrove_window = RegisterEntry("create:mangrove_window")
    # 绯红木窗户 Crimson Window
    crimson_window = RegisterEntry("create:crimson_window")
    # 诡异木窗户 Warped Window
    warped_window = RegisterEntry("create:warped_window")
    # 华丽铁窗户 Ornate Iron Window
    ornate_iron_window = RegisterEntry("create:ornate_iron_window")
    # 橡木窗户板 Oak Window Pane
    oak_window_pane = RegisterEntry("create:oak_window_pane")
    # 云杉木窗户板 Spruce Window Pane
    spruce_window_pane = RegisterEntry("create:spruce_window_pane")
    # 白桦木窗户板 Birch Window Pane
    birch_window_pane = RegisterEntry("create:birch_window_pane")
    # 丛林木窗户板 Jungle Window Pane
    jungle_window_pane = RegisterEntry("create:jungle_window_pane")
    # 金合欢木窗户板 Acacia Window Pane
    acacia_window_pane = RegisterEntry("create:acacia_window_pane")
    # 深色橡木窗户板 Dark Oak Window Pane
    dark_oak_window_pane = RegisterEntry("create:dark_oak_window_pane")
    # 红树木窗户板 Mangrove Window Pane
    mangrove_window_pane = RegisterEntry("create:mangrove_window_pane")
    # 绯红木窗户板 Crimson Window Pane
    crimson_window_pane = RegisterEntry("create:crimson_window_pane")
    # 诡异木窗户板 Warped Window Pane
    warped_window_pane = RegisterEntry("create:warped_window_pane")
    # 华丽铁窗户板 Ornate Iron Window Pane
    ornate_iron_window_pane = RegisterEntry("create:ornate_iron_window_pane")
    # 切制花岗岩 Cut Granite
    cut_granite = RegisterEntry("create:cut_granite")
    # 切制花岗岩楼梯 Cut Granite Stairs
    cut_granite_stairs = RegisterEntry("create:cut_granite_stairs")
    # 切制花岗岩台阶 Cut Granite Slab
    cut_granite_slab = RegisterEntry("create:cut_granite_slab")
    # 切制花岗岩墙 Cut Granite Wall
    cut_granite_wall = RegisterEntry("create:cut_granite_wall")
    # 磨制切制花岗岩 Polished Cut Granite
    polished_cut_granite = RegisterEntry("create:polished_cut_granite")
    # 磨制切制花岗岩楼梯 Polished Cut Granite Stairs
    polished_cut_granite_stairs = RegisterEntry("create:polished_cut_granite_stairs")
    # 磨制切制花岗岩台阶 Polished Cut Granite Slab
    polished_cut_granite_slab = RegisterEntry("create:polished_cut_granite_slab")
    # 磨制切制花岗岩墙 Polished Cut Granite Wall
    polished_cut_granite_wall = RegisterEntry("create:polished_cut_granite_wall")
    # 切制花岗岩砖块 Cut Granite Bricks
    cut_granite_bricks = RegisterEntry("create:cut_granite_bricks")
    # 切制花岗岩砖块楼梯 Cut Granite Brick Stairs
    cut_granite_brick_stairs = RegisterEntry("create:cut_granite_brick_stairs")
    # 切制花岗岩砖块台阶 Cut Granite Brick Slab
    cut_granite_brick_slab = RegisterEntry("create:cut_granite_brick_slab")
    # 切制花岗岩砖块墙 Cut Granite Brick Wall
    cut_granite_brick_wall = RegisterEntry("create:cut_granite_brick_wall")
    # 花岗岩小砖块 Small Granite Bricks
    small_granite_bricks = RegisterEntry("create:small_granite_bricks")
    # 花岗岩小砖块楼梯 Small Granite Brick Stairs
    small_granite_brick_stairs = RegisterEntry("create:small_granite_brick_stairs")
    # 花岗岩小砖块台阶 Small Granite Brick Slab
    small_granite_brick_slab = RegisterEntry("create:small_granite_brick_slab")
    # 花岗岩小砖块墙 Small Granite Brick Wall
    small_granite_brick_wall = RegisterEntry("create:small_granite_brick_wall")
    # 层叠花岗岩 Layered Granite
    layered_granite = RegisterEntry("create:layered_granite")
    # 花岗岩柱 Granite Pillar
    granite_pillar = RegisterEntry("create:granite_pillar")
    # 切制闪长岩 Cut Diorite
    cut_diorite = RegisterEntry("create:cut_diorite")
    # 切制闪长岩楼梯 Cut Diorite Stairs
    cut_diorite_stairs = RegisterEntry("create:cut_diorite_stairs")
    # 切制闪长岩台阶 Cut Diorite Slab
    cut_diorite_slab = RegisterEntry("create:cut_diorite_slab")
    # 切制闪长岩墙 Cut Diorite Wall
    cut_diorite_wall = RegisterEntry("create:cut_diorite_wall")
    # 磨制切制闪长岩 Polished Cut Diorite
    polished_cut_diorite = RegisterEntry("create:polished_cut_diorite")
    # 磨制切制闪长岩楼梯 Polished Cut Diorite Stairs
    polished_cut_diorite_stairs = RegisterEntry("create:polished_cut_diorite_stairs")
    # 磨制切制闪长岩台阶 Polished Cut Diorite Slab
    polished_cut_diorite_slab = RegisterEntry("create:polished_cut_diorite_slab")
    # 磨制切制闪长岩墙 Polished Cut Diorite Wall
    polished_cut_diorite_wall = RegisterEntry("create:polished_cut_diorite_wall")
    # 切制闪长岩砖块 Cut Diorite Bricks
    cut_diorite_bricks = RegisterEntry("create:cut_diorite_bricks")
    # 切制闪长岩砖块楼梯 Cut Diorite Brick Stairs
    cut_diorite_brick_stairs = RegisterEntry("create:cut_diorite_brick_stairs")
    # 切制闪长岩砖块台阶 Cut Diorite Brick Slab
    cut_diorite_brick_slab = RegisterEntry("create:cut_diorite_brick_slab")
    # 切制闪长岩砖块墙 Cut Diorite Brick Wall
    cut_diorite_brick_wall = RegisterEntry("create:cut_diorite_brick_wall")
    # 闪长岩小砖块 Small Diorite Bricks
    small_diorite_bricks = RegisterEntry("create:small_diorite_bricks")
    # 闪长岩小砖块楼梯 Small Diorite Brick Stairs
    small_diorite_brick_stairs = RegisterEntry("create:small_diorite_brick_stairs")
    # 闪长岩小砖块台阶 Small Diorite Brick Slab
    small_diorite_brick_slab = RegisterEntry("create:small_diorite_brick_slab")
    # 闪长岩小砖块墙 Small Diorite Brick Wall
    small_diorite_brick_wall = RegisterEntry("create:small_diorite_brick_wall")
    # 层叠闪长岩 Layered Diorite
    layered_diorite = RegisterEntry("create:layered_diorite")
    # 闪长岩柱 Diorite Pillar
    diorite_pillar = RegisterEntry("create:diorite_pillar")
    # 切制安山岩 Cut Andesite
    cut_andesite = RegisterEntry("create:cut_andesite")
    # 切制安山岩楼梯 Cut Andesite Stairs
    cut_andesite_stairs = RegisterEntry("create:cut_andesite_stairs")
    # 切制安山岩台阶 Cut Andesite Slab
    cut_andesite_slab = RegisterEntry("create:cut_andesite_slab")
    # 切制安山岩墙 Cut Andesite Wall
    cut_andesite_wall = RegisterEntry("create:cut_andesite_wall")
    # 磨制切制安山岩 Polished Cut Andesite
    polished_cut_andesite = RegisterEntry("create:polished_cut_andesite")
    # 磨制切制安山岩楼梯 Polished Cut Andesite Stairs
    polished_cut_andesite_stairs = RegisterEntry("create:polished_cut_andesite_stairs")
    # 磨制切制安山岩台阶 Polished Cut Andesite Slab
    polished_cut_andesite_slab = RegisterEntry("create:polished_cut_andesite_slab")
    # 磨制切制安山岩墙 Polished Cut Andesite Wall
    polished_cut_andesite_wall = RegisterEntry("create:polished_cut_andesite_wall")
    # 切制安山岩砖块 Cut Andesite Bricks
    cut_andesite_bricks = RegisterEntry("create:cut_andesite_bricks")
    # 切制安山岩砖块楼梯 Cut Andesite Brick Stairs
    cut_andesite_brick_stairs = RegisterEntry("create:cut_andesite_brick_stairs")
    # 切制安山岩砖块台阶 Cut Andesite Brick Slab
    cut_andesite_brick_slab = RegisterEntry("create:cut_andesite_brick_slab")
    # 切制安山岩砖块墙 Cut Andesite Brick Wall
    cut_andesite_brick_wall = RegisterEntry("create:cut_andesite_brick_wall")
    # 安山岩小砖块 Small Andesite Bricks
    small_andesite_bricks = RegisterEntry("create:small_andesite_bricks")
    # 安山岩小砖块楼梯 Small Andesite Brick Stairs
    small_andesite_brick_stairs = RegisterEntry("create:small_andesite_brick_stairs")
    # 安山岩小砖块台阶 Small Andesite Brick Slab
    small_andesite_brick_slab = RegisterEntry("create:small_andesite_brick_slab")
    # 安山岩小砖块墙 Small Andesite Brick Wall
    small_andesite_brick_wall = RegisterEntry("create:small_andesite_brick_wall")
    # 层叠安山岩 Layered Andesite
    layered_andesite = RegisterEntry("create:layered_andesite")
    # 竖纹安山岩 Andesite Pillar
    andesite_pillar = RegisterEntry("create:andesite_pillar")
    # 切制方解石 Cut Calcite
    cut_calcite = RegisterEntry("create:cut_calcite")
    # 切制方解石楼梯 Cut Calcite Stairs
    cut_calcite_stairs = RegisterEntry("create:cut_calcite_stairs")
    # 切制方解石台阶 Cut Calcite Slab
    cut_calcite_slab = RegisterEntry("create:cut_calcite_slab")
    # 切制方解石墙 Cut Calcite Wall
    cut_calcite_wall = RegisterEntry("create:cut_calcite_wall")
    # 磨制切制方解石 Polished Cut Calcite
    polished_cut_calcite = RegisterEntry("create:polished_cut_calcite")
    # 磨制切制方解石楼梯 Polished Cut Calcite Stairs
    polished_cut_calcite_stairs = RegisterEntry("create:polished_cut_calcite_stairs")
    # 磨制切制方解石台阶 Polished Cut Calcite Slab
    polished_cut_calcite_slab = RegisterEntry("create:polished_cut_calcite_slab")
    # 磨制切制方解石墙 Polished Cut Calcite Wall
    polished_cut_calcite_wall = RegisterEntry("create:polished_cut_calcite_wall")
    # 切制方解石砖块 Cut Calcite Bricks
    cut_calcite_bricks = RegisterEntry("create:cut_calcite_bricks")
    # 切制方解石砖块楼梯 Cut Calcite Brick Stairs
    cut_calcite_brick_stairs = RegisterEntry("create:cut_calcite_brick_stairs")
    # 切制方解石砖块台阶 Cut Calcite Brick Slab
    cut_calcite_brick_slab = RegisterEntry("create:cut_calcite_brick_slab")
    # 切制方解石砖块墙 Cut Calcite Brick Wall
    cut_calcite_brick_wall = RegisterEntry("create:cut_calcite_brick_wall")
    # 方解石小砖块 Small Calcite Bricks
    small_calcite_bricks = RegisterEntry("create:small_calcite_bricks")
    # 方解石小砖块楼梯 Small Calcite Brick Stairs
    small_calcite_brick_stairs = RegisterEntry("create:small_calcite_brick_stairs")
    # 方解石小砖块台阶 Small Calcite Brick Slab
    small_calcite_brick_slab = RegisterEntry("create:small_calcite_brick_slab")
    # 方解石小砖块墙 Small Calcite Brick Wall
    small_calcite_brick_wall = RegisterEntry("create:small_calcite_brick_wall")
    # 层叠方解石 Layered Calcite
    layered_calcite = RegisterEntry("create:layered_calcite")
    # 竖纹方解石 Calcite Pillar
    calcite_pillar = RegisterEntry("create:calcite_pillar")
    # 切制滴水石块 Cut Dripstone
    cut_dripstone = RegisterEntry("create:cut_dripstone")
    # 切制滴水石楼梯 Cut Dripstone Stairs
    cut_dripstone_stairs = RegisterEntry("create:cut_dripstone_stairs")
    # 切制滴水石台阶 Cut Dripstone Slab
    cut_dripstone_slab = RegisterEntry("create:cut_dripstone_slab")
    # 切制滴水石墙 Cut Dripstone Wall
    cut_dripstone_wall = RegisterEntry("create:cut_dripstone_wall")
    # 磨制切制滴水石块 Polished Cut Dripstone
    polished_cut_dripstone = RegisterEntry("create:polished_cut_dripstone")
    # 磨制切制滴水石楼梯 Polished Cut Dripstone Stairs
    polished_cut_dripstone_stairs = RegisterEntry("create:polished_cut_dripstone_stairs")
    # 磨制切制滴水石台阶 Polished Cut Dripstone Slab
    polished_cut_dripstone_slab = RegisterEntry("create:polished_cut_dripstone_slab")
    # 磨制切制滴水石墙 Polished Cut Dripstone Wall
    polished_cut_dripstone_wall = RegisterEntry("create:polished_cut_dripstone_wall")
    # 切制滴水石砖块 Cut Dripstone Bricks
    cut_dripstone_bricks = RegisterEntry("create:cut_dripstone_bricks")
    # 切制滴水石砖块楼梯 Cut Dripstone Brick Stairs
    cut_dripstone_brick_stairs = RegisterEntry("create:cut_dripstone_brick_stairs")
    # 切制滴水石砖块台阶 Cut Dripstone Brick Slab
    cut_dripstone_brick_slab = RegisterEntry("create:cut_dripstone_brick_slab")
    # 切制滴水石砖块墙 Cut Dripstone Brick Wall
    cut_dripstone_brick_wall = RegisterEntry("create:cut_dripstone_brick_wall")
    # 滴水石小砖块 Small Dripstone Bricks
    small_dripstone_bricks = RegisterEntry("create:small_dripstone_bricks")
    # 滴水石小砖块楼梯 Small Dripstone Brick Stairs
    small_dripstone_brick_stairs = RegisterEntry("create:small_dripstone_brick_stairs")
    # 滴水石小砖块台阶 Small Dripstone Brick Slab
    small_dripstone_brick_slab = RegisterEntry("create:small_dripstone_brick_slab")
    # 滴水石小砖块墙 Small Dripstone Brick Wall
    small_dripstone_brick_wall = RegisterEntry("create:small_dripstone_brick_wall")
    # 层叠滴水石 Layered Dripstone
    layered_dripstone = RegisterEntry("create:layered_dripstone")
    # 滴水石柱 Dripstone Pillar
    dripstone_pillar = RegisterEntry("create:dripstone_pillar")
    # 切制深板岩 Cut Deepslate
    cut_deepslate = RegisterEntry("create:cut_deepslate")
    # 切制深板岩楼梯 Cut Deepslate Stairs
    cut_deepslate_stairs = RegisterEntry("create:cut_deepslate_stairs")
    # 切制深板岩台阶 Cut Deepslate Slab
    cut_deepslate_slab = RegisterEntry("create:cut_deepslate_slab")
    # 切制深板岩墙 Cut Deepslate Wall
    cut_deepslate_wall = RegisterEntry("create:cut_deepslate_wall")
    # 磨制切制深板岩 Polished Cut Deepslate
    polished_cut_deepslate = RegisterEntry("create:polished_cut_deepslate")
    # 磨制切制深板岩楼梯 Polished Cut Deepslate Stairs
    polished_cut_deepslate_stairs = RegisterEntry("create:polished_cut_deepslate_stairs")
    # 磨制切制深板岩台阶 Polished Cut Deepslate Slab
    polished_cut_deepslate_slab = RegisterEntry("create:polished_cut_deepslate_slab")
    # 磨制切制深板岩墙 Polished Cut Deepslate Wall
    polished_cut_deepslate_wall = RegisterEntry("create:polished_cut_deepslate_wall")
    # 切制深板岩砖块 Cut Deepslate Bricks
    cut_deepslate_bricks = RegisterEntry("create:cut_deepslate_bricks")
    # 切制深板岩砖块楼梯 Cut Deepslate Brick Stairs
    cut_deepslate_brick_stairs = RegisterEntry("create:cut_deepslate_brick_stairs")
    # 切制深板岩砖块台阶 Cut Deepslate Brick Slab
    cut_deepslate_brick_slab = RegisterEntry("create:cut_deepslate_brick_slab")
    # 切制深板岩砖块墙 Cut Deepslate Brick Wall
    cut_deepslate_brick_wall = RegisterEntry("create:cut_deepslate_brick_wall")
    # 深板岩小砖块 Small Deepslate Bricks
    small_deepslate_bricks = RegisterEntry("create:small_deepslate_bricks")
    # 深板岩小砖块楼梯 Small Deepslate Brick Stairs
    small_deepslate_brick_stairs = RegisterEntry("create:small_deepslate_brick_stairs")
    # 深板岩小砖块台阶 Small Deepslate Brick Slab
    small_deepslate_brick_slab = RegisterEntry("create:small_deepslate_brick_slab")
    # 深板岩小砖块墙 Small Deepslate Brick Wall
    small_deepslate_brick_wall = RegisterEntry("create:small_deepslate_brick_wall")
    # 层叠深板岩 Layered Deepslate
    layered_deepslate = RegisterEntry("create:layered_deepslate")
    # 深板岩柱 Deepslate Pillar
    deepslate_pillar = RegisterEntry("create:deepslate_pillar")
    # 切制凝灰岩 Cut Tuff
    cut_tuff = RegisterEntry("create:cut_tuff")
    # 切制凝灰岩楼梯 Cut Tuff Stairs
    cut_tuff_stairs = RegisterEntry("create:cut_tuff_stairs")
    # 切制凝灰岩台阶 Cut Tuff Slab
    cut_tuff_slab = RegisterEntry("create:cut_tuff_slab")
    # 切制凝灰岩墙 Cut Tuff Wall
    cut_tuff_wall = RegisterEntry("create:cut_tuff_wall")
    # 磨制切制凝灰岩 Polished Cut Tuff
    polished_cut_tuff = RegisterEntry("create:polished_cut_tuff")
    # 磨制切制凝灰岩楼梯 Polished Cut Tuff Stairs
    polished_cut_tuff_stairs = RegisterEntry("create:polished_cut_tuff_stairs")
    # 磨制切制凝灰岩台阶 Polished Cut Tuff Slab
    polished_cut_tuff_slab = RegisterEntry("create:polished_cut_tuff_slab")
    # 磨制切制凝灰岩墙 Polished Cut Tuff Wall
    polished_cut_tuff_wall = RegisterEntry("create:polished_cut_tuff_wall")
    # 切制凝灰岩砖块 Cut Tuff Bricks
    cut_tuff_bricks = RegisterEntry("create:cut_tuff_bricks")
    # 切制凝灰岩砖块楼梯 Cut Tuff Brick Stairs
    cut_tuff_brick_stairs = RegisterEntry("create:cut_tuff_brick_stairs")
    # 切制凝灰岩砖块台阶 Cut Tuff Brick Slab
    cut_tuff_brick_slab = RegisterEntry("create:cut_tuff_brick_slab")
    # 切制凝灰岩砖块墙 Cut Tuff Brick Wall
    cut_tuff_brick_wall = RegisterEntry("create:cut_tuff_brick_wall")
    # 凝灰岩小砖块 Small Tuff Bricks
    small_tuff_bricks = RegisterEntry("create:small_tuff_bricks")
    # 凝灰岩小砖块楼梯 Small Tuff Brick Stairs
    small_tuff_brick_stairs = RegisterEntry("create:small_tuff_brick_stairs")
    # 凝灰岩小砖块台阶 Small Tuff Brick Slab
    small_tuff_brick_slab = RegisterEntry("create:small_tuff_brick_slab")
    # 凝灰岩小砖块墙 Small Tuff Brick Wall
    small_tuff_brick_wall = RegisterEntry("create:small_tuff_brick_wall")
    # 层叠凝灰岩 Layered Tuff
    layered_tuff = RegisterEntry("create:layered_tuff")
    # 凝灰岩柱 Tuff Pillar
    tuff_pillar = RegisterEntry("create:tuff_pillar")
    # 皓蓝石 Asurine
    asurine = RegisterEntry("create:asurine")
    # 切制皓蓝石 Cut Asurine
    cut_asurine = RegisterEntry("create:cut_asurine")
    # 切制皓蓝石楼梯 Cut Asurine Stairs
    cut_asurine_stairs = RegisterEntry("create:cut_asurine_stairs")
    # 切制皓蓝石台阶 Cut Asurine Slab
    cut_asurine_slab = RegisterEntry("create:cut_asurine_slab")
    # 切制皓蓝石墙 Cut Asurine Wall
    cut_asurine_wall = RegisterEntry("create:cut_asurine_wall")
    # 磨制切制皓蓝石 Polished Cut Asurine
    polished_cut_asurine = RegisterEntry("create:polished_cut_asurine")
    # 磨制切制皓蓝石楼梯 Polished Cut Asurine Stairs
    polished_cut_asurine_stairs = RegisterEntry("create:polished_cut_asurine_stairs")
    # 磨制切制皓蓝石台阶 Polished Cut Asurine Slab
    polished_cut_asurine_slab = RegisterEntry("create:polished_cut_asurine_slab")
    # 磨制切制皓蓝石墙 Polished Cut Asurine Wall
    polished_cut_asurine_wall = RegisterEntry("create:polished_cut_asurine_wall")
    # 切制皓蓝石砖块 Cut Asurine Bricks
    cut_asurine_bricks = RegisterEntry("create:cut_asurine_bricks")
    # 切制皓蓝石砖块楼梯 Cut Asurine Brick Stairs
    cut_asurine_brick_stairs = RegisterEntry("create:cut_asurine_brick_stairs")
    # 切制皓蓝石砖块台阶 Cut Asurine Brick Slab
    cut_asurine_brick_slab = RegisterEntry("create:cut_asurine_brick_slab")
    # 切制皓蓝石砖块墙 Cut Asurine Brick Wall
    cut_asurine_brick_wall = RegisterEntry("create:cut_asurine_brick_wall")
    # 皓蓝石小砖块 Small Asurine Bricks
    small_asurine_bricks = RegisterEntry("create:small_asurine_bricks")
    # 皓蓝石小砖块楼梯 Small Asurine Brick Stairs
    small_asurine_brick_stairs = RegisterEntry("create:small_asurine_brick_stairs")
    # 皓蓝石小砖块台阶 Small Asurine Brick Slab
    small_asurine_brick_slab = RegisterEntry("create:small_asurine_brick_slab")
    # 皓蓝石小砖块墙 Small Asurine Brick Wall
    small_asurine_brick_wall = RegisterEntry("create:small_asurine_brick_wall")
    # 层叠皓蓝石 Layered Asurine
    layered_asurine = RegisterEntry("create:layered_asurine")
    # 竖纹皓蓝石 Asurine Pillar
    asurine_pillar = RegisterEntry("create:asurine_pillar")
    # 绯红岩 Crimsite
    crimsite = RegisterEntry("create:crimsite")
    # 切制绯红岩 Cut Crimsite
    cut_crimsite = RegisterEntry("create:cut_crimsite")
    # 切制绯红岩楼梯 Cut Crimsite Stairs
    cut_crimsite_stairs = RegisterEntry("create:cut_crimsite_stairs")
    # 切制绯红岩台阶 Cut Crimsite Slab
    cut_crimsite_slab = RegisterEntry("create:cut_crimsite_slab")
    # 切制绯红岩墙 Cut Crimsite Wall
    cut_crimsite_wall = RegisterEntry("create:cut_crimsite_wall")
    # 磨制切制绯红岩 Polished Cut Crimsite
    polished_cut_crimsite = RegisterEntry("create:polished_cut_crimsite")
    # 磨制切制绯红岩楼梯 Polished Cut Crimsite Stairs
    polished_cut_crimsite_stairs = RegisterEntry("create:polished_cut_crimsite_stairs")
    # 磨制切制绯红岩台阶 Polished Cut Crimsite Slab
    polished_cut_crimsite_slab = RegisterEntry("create:polished_cut_crimsite_slab")
    # 磨制切制绯红岩墙 Polished Cut Crimsite Wall
    polished_cut_crimsite_wall = RegisterEntry("create:polished_cut_crimsite_wall")
    # 切制绯红岩砖块 Cut Crimsite Bricks
    cut_crimsite_bricks = RegisterEntry("create:cut_crimsite_bricks")
    # 切制绯红岩砖块楼梯 Cut Crimsite Brick Stairs
    cut_crimsite_brick_stairs = RegisterEntry("create:cut_crimsite_brick_stairs")
    # 切制绯红岩砖块台阶 Cut Crimsite Brick Slab
    cut_crimsite_brick_slab = RegisterEntry("create:cut_crimsite_brick_slab")
    # 切制绯红岩砖块墙 Cut Crimsite Brick Wall
    cut_crimsite_brick_wall = RegisterEntry("create:cut_crimsite_brick_wall")
    # 绯红岩小砖块 Small Crimsite Bricks
    small_crimsite_bricks = RegisterEntry("create:small_crimsite_bricks")
    # 绯红岩小砖块楼梯 Small Crimsite Brick Stairs
    small_crimsite_brick_stairs = RegisterEntry("create:small_crimsite_brick_stairs")
    # 绯红岩小砖块台阶 Small Crimsite Brick Slab
    small_crimsite_brick_slab = RegisterEntry("create:small_crimsite_brick_slab")
    # 绯红岩小砖块墙 Small Crimsite Brick Wall
    small_crimsite_brick_wall = RegisterEntry("create:small_crimsite_brick_wall")
    # 层叠绯红岩 Layered Crimsite
    layered_crimsite = RegisterEntry("create:layered_crimsite")
    # 竖纹绯红岩 Crimsite Pillar
    crimsite_pillar = RegisterEntry("create:crimsite_pillar")
    # 石灰岩 Limestone
    limestone = RegisterEntry("create:limestone")
    # 切制石灰岩 Cut Limestone
    cut_limestone = RegisterEntry("create:cut_limestone")
    # 切制石灰岩楼梯 Cut Limestone Stairs
    cut_limestone_stairs = RegisterEntry("create:cut_limestone_stairs")
    # 切制石灰岩台阶 Cut Limestone Slab
    cut_limestone_slab = RegisterEntry("create:cut_limestone_slab")
    # 切制石灰岩墙 Cut Limestone Wall
    cut_limestone_wall = RegisterEntry("create:cut_limestone_wall")
    # 磨制切制石灰岩 Polished Cut Limestone
    polished_cut_limestone = RegisterEntry("create:polished_cut_limestone")
    # 磨制切制石灰岩楼梯 Polished Cut Limestone Stairs
    polished_cut_limestone_stairs = RegisterEntry("create:polished_cut_limestone_stairs")
    # 磨制切制石灰岩台阶 Polished Cut Limestone Slab
    polished_cut_limestone_slab = RegisterEntry("create:polished_cut_limestone_slab")
    # 磨制切制石灰岩墙 Polished Cut Limestone Wall
    polished_cut_limestone_wall = RegisterEntry("create:polished_cut_limestone_wall")
    # 切制石灰岩砖块 Cut Limestone Bricks
    cut_limestone_bricks = RegisterEntry("create:cut_limestone_bricks")
    # 切制石灰岩砖块楼梯 Cut Limestone Brick Stairs
    cut_limestone_brick_stairs = RegisterEntry("create:cut_limestone_brick_stairs")
    # 切制石灰岩砖块台阶 Cut Limestone Brick Slab
    cut_limestone_brick_slab = RegisterEntry("create:cut_limestone_brick_slab")
    # 切制石灰岩砖块墙 Cut Limestone Brick Wall
    cut_limestone_brick_wall = RegisterEntry("create:cut_limestone_brick_wall")
    # 石灰岩小砖块 Small Limestone Bricks
    small_limestone_bricks = RegisterEntry("create:small_limestone_bricks")
    # 石灰岩小砖块楼梯 Small Limestone Brick Stairs
    small_limestone_brick_stairs = RegisterEntry("create:small_limestone_brick_stairs")
    # 石灰岩小砖块台阶 Small Limestone Brick Slab
    small_limestone_brick_slab = RegisterEntry("create:small_limestone_brick_slab")
    # 石灰岩小砖块墙 Small Limestone Brick Wall
    small_limestone_brick_wall = RegisterEntry("create:small_limestone_brick_wall")
    # 层叠石灰岩 Layered Limestone
    layered_limestone = RegisterEntry("create:layered_limestone")
    # 石灰岩柱 Limestone Pillar
    limestone_pillar = RegisterEntry("create:limestone_pillar")
    # 赭金砂 Ochrum
    ochrum = RegisterEntry("create:ochrum")
    # 切制赭金砂 Cut Ochrum
    cut_ochrum = RegisterEntry("create:cut_ochrum")
    # 切制赭金砂楼梯 Cut Ochrum Stairs
    cut_ochrum_stairs = RegisterEntry("create:cut_ochrum_stairs")
    # 切制赭金砂台阶 Cut Ochrum Slab
    cut_ochrum_slab = RegisterEntry("create:cut_ochrum_slab")
    # 切制赭金砂墙 Cut Ochrum Wall
    cut_ochrum_wall = RegisterEntry("create:cut_ochrum_wall")
    # 磨制切制赭金砂 Polished Cut Ochrum
    polished_cut_ochrum = RegisterEntry("create:polished_cut_ochrum")
    # 磨制切制赭金砂楼梯 Polished Cut Ochrum Stairs
    polished_cut_ochrum_stairs = RegisterEntry("create:polished_cut_ochrum_stairs")
    # 磨制切制赭金砂台阶 Polished Cut Ochrum Slab
    polished_cut_ochrum_slab = RegisterEntry("create:polished_cut_ochrum_slab")
    # 磨制切制赭金砂墙 Polished Cut Ochrum Wall
    polished_cut_ochrum_wall = RegisterEntry("create:polished_cut_ochrum_wall")
    # 切制赭金砂砖块 Cut Ochrum Bricks
    cut_ochrum_bricks = RegisterEntry("create:cut_ochrum_bricks")
    # 切制赭金砂砖块楼梯 Cut Ochrum Brick Stairs
    cut_ochrum_brick_stairs = RegisterEntry("create:cut_ochrum_brick_stairs")
    # 切制赭金砂砖块台阶 Cut Ochrum Brick Slab
    cut_ochrum_brick_slab = RegisterEntry("create:cut_ochrum_brick_slab")
    # 切制赭金砂砖块墙 Cut Ochrum Brick Wall
    cut_ochrum_brick_wall = RegisterEntry("create:cut_ochrum_brick_wall")
    # 赭金砂小砖块 Small Ochrum Bricks
    small_ochrum_bricks = RegisterEntry("create:small_ochrum_bricks")
    # 赭金砂小砖块楼梯 Small Ochrum Brick Stairs
    small_ochrum_brick_stairs = RegisterEntry("create:small_ochrum_brick_stairs")
    # 赭金砂小砖块台阶 Small Ochrum Brick Slab
    small_ochrum_brick_slab = RegisterEntry("create:small_ochrum_brick_slab")
    # 赭金砂小砖块墙 Small Ochrum Brick Wall
    small_ochrum_brick_wall = RegisterEntry("create:small_ochrum_brick_wall")
    # 层叠赭金砂 Layered Ochrum
    layered_ochrum = RegisterEntry("create:layered_ochrum")
    # 赭金砂柱 Ochrum Pillar
    ochrum_pillar = RegisterEntry("create:ochrum_pillar")
    # 熔渣 Scoria
    scoria = RegisterEntry("create:scoria")
    # 切制熔渣 Cut Scoria
    cut_scoria = RegisterEntry("create:cut_scoria")
    # 切制熔渣楼梯 Cut Scoria Stairs
    cut_scoria_stairs = RegisterEntry("create:cut_scoria_stairs")
    # 切制熔渣台阶 Cut Scoria Slab
    cut_scoria_slab = RegisterEntry("create:cut_scoria_slab")
    # 切制熔渣墙 Cut Scoria Wall
    cut_scoria_wall = RegisterEntry("create:cut_scoria_wall")
    # 磨制切制熔渣 Polished Cut Scoria
    polished_cut_scoria = RegisterEntry("create:polished_cut_scoria")
    # 磨制切制熔渣楼梯 Polished Cut Scoria Stairs
    polished_cut_scoria_stairs = RegisterEntry("create:polished_cut_scoria_stairs")
    # 磨制切制熔渣台阶 Polished Cut Scoria Slab
    polished_cut_scoria_slab = RegisterEntry("create:polished_cut_scoria_slab")
    # 磨制切制熔渣墙 Polished Cut Scoria Wall
    polished_cut_scoria_wall = RegisterEntry("create:polished_cut_scoria_wall")
    # 切制熔渣砖块 Cut Scoria Bricks
    cut_scoria_bricks = RegisterEntry("create:cut_scoria_bricks")
    # 切制熔渣砖块楼梯 Cut Scoria Brick Stairs
    cut_scoria_brick_stairs = RegisterEntry("create:cut_scoria_brick_stairs")
    # 切制熔渣砖块台阶 Cut Scoria Brick Slab
    cut_scoria_brick_slab = RegisterEntry("create:cut_scoria_brick_slab")
    # 切制熔渣砖块墙 Cut Scoria Brick Wall
    cut_scoria_brick_wall = RegisterEntry("create:cut_scoria_brick_wall")
    # 熔渣小砖块 Small Scoria Bricks
    small_scoria_bricks = RegisterEntry("create:small_scoria_bricks")
    # 熔渣小砖块楼梯 Small Scoria Brick Stairs
    small_scoria_brick_stairs = RegisterEntry("create:small_scoria_brick_stairs")
    # 熔渣小砖块台阶 Small Scoria Brick Slab
    small_scoria_brick_slab = RegisterEntry("create:small_scoria_brick_slab")
    # 熔渣小砖块墙 Small Scoria Brick Wall
    small_scoria_brick_wall = RegisterEntry("create:small_scoria_brick_wall")
    # 层叠熔渣 Layered Scoria
    layered_scoria = RegisterEntry("create:layered_scoria")
    # 熔渣柱 Scoria Pillar
    scoria_pillar = RegisterEntry("create:scoria_pillar")
    # 焦黑熔渣 Scorchia
    scorchia = RegisterEntry("create:scorchia")
    # 切制焦黑熔渣 Cut Scorchia
    cut_scorchia = RegisterEntry("create:cut_scorchia")
    # 切制焦黑熔渣楼梯 Cut Scorchia Stairs
    cut_scorchia_stairs = RegisterEntry("create:cut_scorchia_stairs")
    # 切制焦黑熔渣台阶 Cut Scorchia Slab
    cut_scorchia_slab = RegisterEntry("create:cut_scorchia_slab")
    # 切制焦黑熔渣墙 Cut Scorchia Wall
    cut_scorchia_wall = RegisterEntry("create:cut_scorchia_wall")
    # 磨制切制焦黑熔渣 Polished Cut Scorchia
    polished_cut_scorchia = RegisterEntry("create:polished_cut_scorchia")
    # 磨制切制焦黑熔渣楼梯 Polished Cut Scorchia Stairs
    polished_cut_scorchia_stairs = RegisterEntry("create:polished_cut_scorchia_stairs")
    # 磨制切制焦黑熔渣台阶 Polished Cut Scorchia Slab
    polished_cut_scorchia_slab = RegisterEntry("create:polished_cut_scorchia_slab")
    # 磨制切制焦黑熔渣墙 Polished Cut Scorchia Wall
    polished_cut_scorchia_wall = RegisterEntry("create:polished_cut_scorchia_wall")
    # 切制焦黑熔渣砖块 Cut Scorchia Bricks
    cut_scorchia_bricks = RegisterEntry("create:cut_scorchia_bricks")
    # 切制焦黑熔渣砖块楼梯 Cut Scorchia Brick Stairs
    cut_scorchia_brick_stairs = RegisterEntry("create:cut_scorchia_brick_stairs")
    # 切制焦黑熔渣砖块台阶 Cut Scorchia Brick Slab
    cut_scorchia_brick_slab = RegisterEntry("create:cut_scorchia_brick_slab")
    # 切制焦黑熔渣砖块墙 Cut Scorchia Brick Wall
    cut_scorchia_brick_wall = RegisterEntry("create:cut_scorchia_brick_wall")
    # 焦黑熔渣小砖块 Small Scorchia Bricks
    small_scorchia_bricks = RegisterEntry("create:small_scorchia_bricks")
    # 焦黑熔渣小砖块楼梯 Small Scorchia Brick Stairs
    small_scorchia_brick_stairs = RegisterEntry("create:small_scorchia_brick_stairs")
    # 焦黑熔渣小砖块台阶 Small Scorchia Brick Slab
    small_scorchia_brick_slab = RegisterEntry("create:small_scorchia_brick_slab")
    # 焦黑熔渣小砖块墙 Small Scorchia Brick Wall
    small_scorchia_brick_wall = RegisterEntry("create:small_scorchia_brick_wall")
    # 层叠焦黑熔渣 Layered Scorchia
    layered_scorchia = RegisterEntry("create:layered_scorchia")
    # 焦黑熔渣柱 Scorchia Pillar
    scorchia_pillar = RegisterEntry("create:scorchia_pillar")
    # 辉绿岩 Veridium
    veridium = RegisterEntry("create:veridium")
    # 切制辉绿岩 Cut Veridium
    cut_veridium = RegisterEntry("create:cut_veridium")
    # 切制辉绿岩楼梯 Cut Veridium Stairs
    cut_veridium_stairs = RegisterEntry("create:cut_veridium_stairs")
    # 切制辉绿岩台阶 Cut Veridium Slab
    cut_veridium_slab = RegisterEntry("create:cut_veridium_slab")
    # 切制辉绿岩墙 Cut Veridium Wall
    cut_veridium_wall = RegisterEntry("create:cut_veridium_wall")
    # 磨制切制辉绿岩 Polished Cut Veridium
    polished_cut_veridium = RegisterEntry("create:polished_cut_veridium")
    # 磨制切制辉绿岩楼梯 Polished Cut Veridium Stairs
    polished_cut_veridium_stairs = RegisterEntry("create:polished_cut_veridium_stairs")
    # 磨制切制辉绿岩台阶 Polished Cut Veridium Slab
    polished_cut_veridium_slab = RegisterEntry("create:polished_cut_veridium_slab")
    # 磨制切制辉绿岩墙 Polished Cut Veridium Wall
    polished_cut_veridium_wall = RegisterEntry("create:polished_cut_veridium_wall")
    # 切制辉绿岩砖块 Cut Veridium Bricks
    cut_veridium_bricks = RegisterEntry("create:cut_veridium_bricks")
    # 切制辉绿岩砖块楼梯 Cut Veridium Brick Stairs
    cut_veridium_brick_stairs = RegisterEntry("create:cut_veridium_brick_stairs")
    # 切制辉绿岩砖块台阶 Cut Veridium Brick Slab
    cut_veridium_brick_slab = RegisterEntry("create:cut_veridium_brick_slab")
    # 切制辉绿岩砖块墙 Cut Veridium Brick Wall
    cut_veridium_brick_wall = RegisterEntry("create:cut_veridium_brick_wall")
    # 辉绿岩小砖块 Small Veridium Bricks
    small_veridium_bricks = RegisterEntry("create:small_veridium_bricks")
    # 辉绿岩小砖块楼梯 Small Veridium Brick Stairs
    small_veridium_brick_stairs = RegisterEntry("create:small_veridium_brick_stairs")
    # 辉绿岩小砖块台阶 Small Veridium Brick Slab
    small_veridium_brick_slab = RegisterEntry("create:small_veridium_brick_slab")
    # 辉绿岩小砖块墙 Small Veridium Brick Wall
    small_veridium_brick_wall = RegisterEntry("create:small_veridium_brick_wall")
    # 层叠辉绿岩 Layered Veridium
    layered_veridium = RegisterEntry("create:layered_veridium")
    # 辉绿岩柱 Veridium Pillar
    veridium_pillar = RegisterEntry("create:veridium_pillar")


items = Item()
blocks = Block()