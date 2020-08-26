package me.Orangatan.spdrun;

import java.util.Arrays;

import org.bukkit.Bukkit;
import org.bukkit.Location;
import org.bukkit.Material;
import org.bukkit.command.Command;
import org.bukkit.command.CommandSender;
import org.bukkit.entity.Player;
import org.bukkit.event.EventHandler;
import org.bukkit.event.EventPriority;
import org.bukkit.event.Listener;
import org.bukkit.event.player.PlayerInteractEvent;
import org.bukkit.inventory.ItemStack;
import org.bukkit.plugin.java.JavaPlugin;

public class Main extends JavaPlugin implements Listener{
	
	String hunters[] = {"", "", "", "", "", "", "", "", "", ""};
	String speedrunners[] = {"", "", "", "", "", "", "", "", "", ""};
	ItemStack compasses[] = new ItemStack[10];
	int huntnum = 0;
	int speednum = 0;
	
	@Override
	public void onEnable() {
		// when server startup, reloads, etc: everything here will run
		getServer().getPluginManager().registerEvents(this, this);

	}
	
	public void onDisable() {
		
		//when server is disabled, everything here will run
	}
	
	public boolean onCommand(CommandSender sender, Command cmd, String label, String[] args) {
		if (label.equalsIgnoreCase("speedrun")) {
			if (args.length == 0) {
				Player player = (Player) sender;
				player.sendMessage("Incorrect command format. Please indicate whether you are a hunter or speedrunner after your command.");
				return false;
			}
			else if (args.length > 1) {
				Player player = (Player) sender;
				player.sendMessage("Unexpected additional args.");
				return false;
			}
			else if (args[0].equals("hunter")) {
				Player player = (Player) sender;
				String name = player.getName();
				for (int i = 0; i < speedrunners.length; i++) {
					if (speedrunners[i].equals(name)) {
						for (int j = i; j < speedrunners.length-1; j++) {
							speedrunners[j] = speedrunners[j+1];
						}
						speednum--;
						break;
					}
				}
				for (int i = 0; i < hunters.length; i++) {
					if (hunters[i].equals(name)) {
						player.sendMessage("You are already a hunter");
						return false;
					}
				}
				player.sendMessage("You are now a hunter!");
				hunters[huntnum] = player.getName();
				huntnum++;
				player.getInventory().addItem(new ItemStack(Material.COMPASS));
				return true;
			}
			else if (args[0].equals("speedrunner")) {
				Player player = (Player) sender;
				String name = player.getName();
				for (int i = 0; i < hunters.length; i++) {
					if (hunters[i].equals(name)) {
						for (int j = i; j < hunters.length-1; j++) {
							hunters[j] = hunters[j+1];
						}
						huntnum--;
						break;
					}
				}
				for (int i = 0; i < speedrunners.length; i++) {
					if (speedrunners[i].equals(name)) {
						player.sendMessage("You are already a speedrunner");
						return false;
					}
				}
				player.sendMessage("You are now a speedrunner!");
				speedrunners[speednum] = player.getName();
				speednum++;
				return true;
			}
			else {
				Player player = (Player) sender;
				player.sendMessage("Incorrect syntax. Type 'hunter' or 'speedrunner' after the command.");
				return true;
			}
		}
		return false;
	}
	
	
	@SuppressWarnings("deprecation")
	@EventHandler(priority = EventPriority.HIGH)
	public void onPlayerUse(PlayerInteractEvent event) {
		Player player = event.getPlayer();
		if (event.hasItem()) {
			if (event.getItem().getType() == Material.COMPASS) {
				Location nearplayer[] = new Location[speedrunners.length];
				for (int i = 0; i < speedrunners.length; i++) {
					nearplayer[i] = Bukkit.getPlayer(speedrunners[i]).getLocation();
				}
				double biggest = 0;
				int p = 0;
				Location point = new Location(null, 0,0,0);
				Location playerloc = player.getLocation();
				for (int i = 0; i < speedrunners.length; i++) {
					Location loc = nearplayer[i];
					double x = loc.getBlockX() - playerloc.getBlockX();
					double z = loc.getBlockZ() - playerloc.getBlockZ();
					double val = Math.sqrt(Math.pow(x, 2) + Math.pow(z,2));
					if (val < biggest) {
						point = loc;
						biggest = val;
						p = i;
					}
				}
				if (biggest != 0) {
					String message = "Now pointing to " + speedrunners[p] + "!"; 
					player.sendMessage(message);
					player.setCompassTarget(point);
				}
				else {
					player.sendMessage("No speedrunners in game");
				}
			}
		}
	}
	
}
