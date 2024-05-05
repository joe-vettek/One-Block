package xueluoanping.oneblock.data.datapacks;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonElement;

public class ResourcePackInfo {
    private Pack pack=new Pack();

    public Pack getPack() {
        return pack;
    }

    public void setPack(Pack pack) {
        this.pack = pack;
    }
    public JsonElement toJson() {
        Gson gson = new GsonBuilder().create();
        return gson.toJsonTree(this);
    }

    public static class Pack {
        private String description="resources";
        private int pack_format=9;
        private String _comment="";

        public String getDescription() {
            return description;
        }

        public void setDescription(String description) {
            this.description = description;
        }

        public int getPack_format() {
            return pack_format;
        }

        public void setPack_format(int pack_format) {
            this.pack_format = pack_format;
        }

        public String get_comment() {
            return _comment;
        }

        public void set_comment(String _comment) {
            this._comment = _comment;
        }
    }
}

