package xueluoanping.oneblock.api;

import java.util.List;

public class OneBlockSubConfig {
    private List<Sub> list;

    public List<Sub> getList() {
        return list;
    }

    public void setList(List<Sub> list) {
        this.list = list;
    }

    public static class Sub {
        private String id;
        private int priority;
        private String target;

        public String getId() {
            return id;
        }

        public void setId(String id) {
            this.id = id;
        }


        public int getPriority() {
            return priority;
        }

        public void setPriority(int priority) {
            this.priority = priority;
        }

        public String getTarget() {
            return target;
        }

        public void setTarget(String target) {
            this.target = target;
        }
    }

}
