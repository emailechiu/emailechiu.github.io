package tutorial.generic;
import net.minecraft.block.Block;
import net.minecraft.block.SoundType;
import net.minecraft.block.material.Material;
import net.minecraft.init.Blocks;
import net.minecraft.creativetab.CreativeTabs;
import net.minecraft.item.Item;
import net.minecraft.item.ItemSeeds;
import net.minecraft.item.ItemStack;
import net.minecraft.item.crafting.FurnaceRecipes;
import net.minecraftforge.common.MinecraftForge;
import net.minecraftforge.fml.common.Mod; 
import net.minecraftforge.fml.common.Mod.EventHandler; 
import net.minecraftforge.fml.common.Mod.Instance;
import net.minecraftforge.fml.common.SidedProxy;
import net.minecraftforge.fml.common.network.internal.NetworkModHolder;
import net.minecraftforge.fml.common.event.FMLInitializationEvent; 
import net.minecraftforge.fml.common.event.FMLPostInitializationEvent; 
import net.minecraftforge.fml.common.event.FMLPreInitializationEvent;
import net.minecraftforge.fml.common.registry.GameRegistry;


@Mod(modid=Generic.MODID, name=Generic.MODNAME, version=Generic.MODVER) //Tell forge "Oh hey, there's a new mod here to load." public class Generic //Start the class Declaration {
public class Generic {
//Set the ID of the mod (Should be lower case).
public static final String MODID = "generic";
//Set the "Name" of the mod.
public static final String MODNAME = "Generic Mod";
//Set the version of the mod.
public static final String MODVER = "0.0.0";
public final static Block genericDirt = new GenericBlock(Material.GROUND) .setHardness(0.5F) .setUnlocalizedName("stone") .setCreativeTab(CreativeTabs.BUILDING_BLOCKS);;

@Instance(value = Generic.MODID) //Tell Forge what instance to use.
public static Generic instance;


@EventHandler
public void preInit(FMLPreInitializationEvent event)
{
}
@EventHandler
public void load(FMLInitializationEvent event)
{
  //  proxy.registerRenderers();
    initBasicBlocks();
/*    initCraftingAndSmelting();
    initBasicItems();   
    initDamageValuesAndMetadata();
    initPacketHandling();
    initPlants();
    initWorldGen(); */
}

@EventHandler
public void postInit(FMLPostInitializationEvent event)
{
}
private void initBasicBlocks () {
    GameRegistry.registerBlock(genericDirt, "genericDirt");
}

} 


