package xueluoanping.oneblock.handler;

import net.minecraft.resources.ResourceLocation;
import net.minecraft.util.RandomSource;
import xueluoanping.oneblock.OneBlock;

import java.util.List;
import java.util.stream.Collectors;

public class StageData {

    private String name;
    private int count;
    private List<BlockEntry> list;
    private String end_gift;
    private ResourceLocation resourceLocation;
    private String sub_target;

    public String getResName() {
        return String.format("%s.%s", resourceLocation.getNamespace(), resourceLocation.getPath().replace("/", "."));
    }

    public String getSub_target() {
        return sub_target;
    }

    public void setSub_target(String sub_target) {
        this.sub_target = sub_target;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getCount() {
        return count;
    }

    public void setCount(int count) {
        this.count = count;
    }

    public List<BlockEntry> getList() {
        return list;
    }

    public void setList(List<BlockEntry> list) {
        this.list = list;
    }

    public String getEnd_gift() {
        return end_gift;
    }

    public void setEnd_gift(String end_gift) {
        this.end_gift = end_gift;
    }

    public ResourceLocation getResourceLocation() {
        return resourceLocation;
    }

    public void setResourceLocation(ResourceLocation resourceLocation) {
        this.resourceLocation = resourceLocation;
    }

    public BlockEntry selectRandomByWeight(RandomSource random, OneBlockProgress nowProgress, boolean reachRemain) {
        var blockEntryStream = this.list;
        if (reachRemain)
            blockEntryStream = blockEntryStream.stream()
                    .filter(blockEntry -> nowProgress.indexOfRemain(blockEntry.getType(), blockEntry.getGlobalId()) >= 0).collect(Collectors.toList());

        int totalWeight = blockEntryStream
                .stream()
                .filter(blockEntry -> nowProgress.checkQuota(blockEntry.getType(), blockEntry.getGlobalId()))
                .mapToInt(BlockEntry::getWeight).sum();

        int randomNumber = random.nextInt(totalWeight) + 1;

        int cumulativeWeight = 0;
        for (BlockEntry entry : blockEntryStream) {
            cumulativeWeight += entry.getWeight();
            if (randomNumber <= cumulativeWeight) {
                return entry;
            }
        }
        OneBlock.error("Found error in", this.getResName(), totalWeight, nowProgress == null ? null : nowProgress.remainCounter.toString());
        return new BlockEntry("block", "minecraft:barrier");
    }

    public static class BlockEntry {
        private String type;
        private String id;
        private int weight;
        private String loot_table;
        private String blockstates;
        private String nbt;
        private int count;
        private int min_times;
        private int max_times;

        private List<BlockEntry> preprocessing;
        private int offset_x;
        private int offset_y;
        private int offset_z;


        public String getGlobalId() {
            String gid = this.id;
            if (this.getBlockstates() != null) {
                gid += ";Blockstates:" + this.getBlockstates();
            }
            if (this.getNbt() != null) {
                gid += ";Nbt:" + this.getNbt();
            }
            if (this.getLoot_table() != null) {
                gid += ";Loot_table:" + this.getLoot_table();
            }
            return gid;
        }

        public BlockEntry(String type, String id) {
            this.type = type;
            this.id = id;
            this.weight = 0;
            this.count = 0;
            // Gson default set 0 so we could ignore it if it less than 1
            this.min_times = 0;
            this.max_times = 0;
            // not offset
            this.offset_x = 0;
            this.offset_y = 0;
            this.offset_z = 0;
        }

        public String getLoot_table() {
            return loot_table;
        }

        public void setLoot_table(String loot_table) {
            this.loot_table = loot_table;
        }

        public int getMax_times() {
            return max_times;
        }

        public void setMax_times(int max_times) {
            this.max_times = max_times;
        }

        public int getMin_times() {
            return min_times;
        }

        public void setMin_times(int min_times) {
            this.min_times = min_times;
        }

        public int getCount() {
            return count;
        }

        public void setCount(int count) {
            this.count = count;
        }


        public String getType() {
            return type;
        }

        public void setType(String type) {
            this.type = type;
        }

        public String getId() {
            return id;
        }

        public void setId(String id) {
            this.id = id;
        }

        public int getWeight() {
            return weight;
        }

        public void setWeight(int weight) {
            this.weight = weight;
        }

        public String getBlockstates() {
            return blockstates;
        }

        public void setBlockstates(String blockstates) {
            this.blockstates = blockstates;
        }

        public String getNbt() {
            return nbt;
        }

        public void setNbt(String nbt) {
            this.nbt = nbt;
        }

        public int getOffset_x() {
            return offset_x;
        }

        public void setOffset_x(int offset_x) {
            this.offset_x = offset_x;
        }

        public int getOffset_y() {
            return offset_y;
        }

        public void setOffset_y(int offset_y) {
            this.offset_y = offset_y;
        }

        public int getOffset_z() {
            return offset_z;
        }

        public void setOffset_z(int offset_z) {
            this.offset_z = offset_z;
        }

        public List<BlockEntry> getPreprocessing() {
            return preprocessing;
        }

        public void setPreprocessing(List<BlockEntry> preprocessing) {
            this.preprocessing = preprocessing;
        }
    }
}
