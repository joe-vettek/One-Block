package xueluoanping.oneblock.data.blockstate;

import net.minecraft.data.PackOutput;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.world.item.Item;
import net.minecraftforge.common.data.ExistingFileHelper;
import xueluoanping.oneblock.ModContents;
import xueluoanping.oneblock.OneBlock;
import xueluoanping.oneblock.util.RegisterFinderUtil;

public class ItemModelProvider extends net.minecraftforge.client.model.generators.ItemModelProvider {


	public static final String GENERATED = "item/generated";
	public static final String HANDHELD = "item/handheld";

	public ItemModelProvider(PackOutput generator, ExistingFileHelper existingFileHelper) {
		super(generator, OneBlock.MOD_ID, existingFileHelper);
	}


	@Override
	protected void registerModels() {
		basicItem(ModContents.fantasy_bracelet.get());
	}


	private String itemName(Item item) {
		return RegisterFinderUtil.getItemKey(item).getPath();
	}

	public ResourceLocation resourceItem(String path) {
		return new ResourceLocation(OneBlock.MOD_ID, "item/" + path);
	}



}
