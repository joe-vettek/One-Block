package xueluoanping.oneblock.api;

import java.util.LinkedHashMap;
import java.util.List;

public class OneBlockConfig {
    private List<String> order;
    private LinkedHashMap<String, String> stageLink;


    public void setOrder(List<String> order) {
        this.order = order;
    }

    public List<String> getOrder() {
        return order;
    }

    public LinkedHashMap<String, String> getStageLink() {
        return stageLink;
    }

    public void setStageLink(LinkedHashMap<String, String> stageLink) {
        this.stageLink = stageLink;
    }

    public boolean matchSubWithAddition(String maySub, String additionTarget) {
        if (getStageLink().containsKey(maySub)) {
            return getStageLink().get(maySub).equals(additionTarget);
        }
        return false;
    }
}
