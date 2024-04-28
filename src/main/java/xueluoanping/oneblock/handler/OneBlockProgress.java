package xueluoanping.oneblock.handler;

import net.minecraft.nbt.CompoundTag;
import net.minecraft.nbt.ListTag;

class OneBlockProgress {
    public OneBlockProgress(String name, int counter) {
        this(name, counter, 0, new ListTag(), new ListTag());
    }

    public OneBlockProgress(String name, int counter, int bedrockLastTime, ListTag remainCounter, ListTag quotaCounter) {
        this.name = name;
        this.counter = counter;
        this.bedrockLastTime = bedrockLastTime;
        this.remainCounter = remainCounter;
        this.quotaCounter = quotaCounter;
    }


    public OneBlockProgress() {
        this("", 0);
    }

    public String name;
    public int counter;
    public int bedrockLastTime;
    public ListTag remainCounter;
    public ListTag quotaCounter;
    private static final int TAG_REMAIN = 1;
    private static final int TAG_QUOTA = 2;

    public int getRemainAmount() {
        int amount = 0;
        for (int i = 0; i < this.remainCounter.size(); i++) {
            var tag = this.remainCounter.getCompound(i);
            amount += tag.getInt("count");
        }
        return amount;
    }

    public void addListTag(int tagType, String type, String id, int count) {
        var tag = new CompoundTag();
        tag.putString("type", type);
        tag.putString("id", id);
        tag.putInt("count", count);
        if (tagType == TAG_REMAIN)
            this.remainCounter.add(tag);
        else if (tagType == TAG_QUOTA) {
            this.quotaCounter.add(tag);
        }
    }

    public void addRemain(String type, String id, int count) {
        addListTag(TAG_REMAIN, type, id, count);
    }

    public void addQuota(String type, String id, int count) {
        addListTag(TAG_QUOTA, type, id, count);
    }

    public int updateListTag(int tagType, String type, String id) {
        var listTag = tagType == TAG_REMAIN ? this.remainCounter : this.quotaCounter;
        int removeIndex = -1;
        for (int i = 0; i < listTag.size(); i++) {
            var tag = listTag.getCompound(i);
            if (tag.getString("type").equals(type)
                    && tag.getString("id").equals(id)) {
                int count = tag.getInt("count") - 1;
                if (count > 0) {
                    tag.putInt("count", tag.getInt("count") - 1);
                } else {
                    removeIndex = i;
                }
                break;
            }
        }
        return removeIndex;
    }

    public void updateRemain(String type, String id) {
        int removeIndex = updateListTag(TAG_REMAIN, type, id);
        // it's not safe to delete anything in a cycle
        if (removeIndex >= 0) this.remainCounter.remove(removeIndex);
    }

    public void updateQuota(String type, String id) {
        int toZeroIndex = updateListTag(TAG_REMAIN, type, id);
        // just record the entry count 0
    }

    public int indexOfListTag(int tagType, String type, String id) {
        var listTag = tagType == TAG_REMAIN ? this.remainCounter : this.quotaCounter;
        int index = -1;
        for (int i = 0; i < listTag.size(); i++) {
            var tag = listTag.getCompound(i);
            if (tag.getString("type").equals(type)
                    && tag.getString("id").equals(id)) {
                index = i;
                break;
            }
        }
        return index;
    }

    public int indexOfRemain(String type, String id) {
        return indexOfListTag(TAG_REMAIN, type, id);
    }

    public int indexOfQuota(String type, String id) {
        return indexOfListTag(TAG_QUOTA, type, id);
    }

    public boolean checkQuota(String type, String id) {
        int index = indexOfQuota(type, id);
        boolean result = true;
        if (index >= 0) {
            result = this.quotaCounter.getCompound(index).getInt("count") > 0;
        }
        return result;
    }

    public void cleanRemain() {
        this.remainCounter.clear();
    }

    public void cleanQuota() {
        this.quotaCounter.clear();
    }

    public void updateBedrockLastTime() {
        this.bedrockLastTime--;
    }

    public void setBedrockLastTime(int tick) {
        this.bedrockLastTime = tick;
    }

    public void updateCounter() {
        this.counter++;
    }


}
