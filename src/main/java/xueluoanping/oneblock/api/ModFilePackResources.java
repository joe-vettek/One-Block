package xueluoanping.oneblock.api;

import net.minecraft.network.chat.Component;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.server.packs.*;
import net.minecraft.server.packs.repository.Pack;
import net.minecraft.server.packs.repository.PackSource;
import net.minecraft.server.packs.resources.IoSupplier;
import net.neoforged.neoforgespi.locating.IModFile;
import org.jetbrains.annotations.Nullable;

import java.io.InputStream;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
import java.util.Set;


/*
 * Thanks Create MIT License
 * */
public class ModFilePackResources extends PathPackResources implements PackResources, PackSource {
    protected final IModFile modFile;
    protected final String sourcePath;

    public ModFilePackResources(PackLocationInfo pLocation, IModFile modFile, String sourcePath) {
        super(pLocation, modFile.findResource(sourcePath));
        this.modFile = modFile;
        this.sourcePath = sourcePath;
    }

    @Override
    public Component decorate(Component pName) {
        return pName;
    }

    @Override
    public boolean shouldAddAutomatically() {
        return true;
    }


    // @Override
    // protected Path resolve(String... paths) {
    // 	String[] allPaths = new String[paths.length + 1];
    // 	allPaths[0] = sourcePath;
    // 	System.arraycopy(paths, 0, allPaths, 1, paths.length);
    // 	return modFile.findResource(allPaths);
    // }


    @Override
    public Set<String> getNamespaces(PackType pType) {
        return super.getNamespaces(pType);
    }

    @Override
    public @Nullable IoSupplier<InputStream> getRootResource(String... pElements) {
        return super.getRootResource(pElements);
    }

    @Override
    public @Nullable IoSupplier<InputStream> getResource(PackType pPackType, ResourceLocation pLocation) {
        return super.getResource(pPackType, pLocation);
    }

    public static class PathResourcesSupplier implements Pack.ResourcesSupplier {
        private final Path content;
        protected final IModFile modFile;

        public PathResourcesSupplier(IModFile modFile, Path pContent) {
            this.content = pContent;
            this.modFile = modFile;
        }

        @Override
        public ModFilePackResources openPrimary(PackLocationInfo pLocation) {
            return new ModFilePackResources(pLocation,this.modFile, this.content.toString());
        }

        @Override
        public ModFilePackResources openFull(PackLocationInfo pLocation, Pack.Metadata pMetadata) {
            ModFilePackResources packresources = this.openPrimary(pLocation);
            List<String> list = pMetadata.overlays();
            if (list.isEmpty()) {
                return packresources;
            } else {
                List<PackResources> list1 = new ArrayList<>(list.size());

                for (String s : list) {
                    Path path = this.content.resolve(s);
                    list1.add(new PathPackResources(pLocation, path));
                }

                // return new CompositePackResources(packresources, list1);
                return null;
            }
        }
    }
}
