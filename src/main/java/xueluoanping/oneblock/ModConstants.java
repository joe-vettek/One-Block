package xueluoanping.oneblock;

import net.minecraft.world.item.Item;
import net.minecraft.world.level.block.Block;
import xueluoanping.oneblock.util.LazyGet;
import xueluoanping.oneblock.util.RegisterFinderUtil;


public class ModConstants {


    public static final String TYPE_BLOCK = "block";
    public static final String TYPE_GIFT = "gift";
    public static final String TYPE_MOB = "mob";
    public static final String TYPE_ARCHAEOLOGY = "archaeology";
    public static final String TYPE_STRUCTURE = "structure";
    public static final String TYPE_TEMPLATE = "template";
    public static final String TYPE_CONFIGURED_FEATURE = "configured_feature";
    public static final String TYPE_COMMAND = "command";
    public static final String TYPE_SOUND = "sound";
    // var b=BuiltInRegistries.BLOCK.stream()
    //         .filter(block -> block.defaultBlockState()
    //                 .is(BlockTags.LOGS))
    //         .collect(Collectors.toList());
    // var bi=b.get(level.random.nextInt(b.size()));
    // .stream().findFirst().get();
}
