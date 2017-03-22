# How to set up up your Raspberry Pi to have a static IP address

Usually when you connect a Raspberry Pi to a Local Area Network (LAN) it is automatically assigned an IP address. Typically, this address will change each time you connect.

Sometimes, however, you might want your Pi to boot up with the same IP address each time. This can be useful if you are making a small self contained network, or building a standalone project such as a robot. Here's how to do it.

## Setup

Edit the file `/etc/dhcpcd.conf` as follows:

1. Type `sudo nano /etc/dhcpcd.conf` at the command prompt.

1. Scroll to the bottom of the script, and add the following lines:

	``` bash
	interface eth0

	static ip_address=192.168.0.2/24
	static routers=192.168.0.1
	static domain_name_servers=192.168.0.1

	interface wlan0

	static ip_address=192.168.0.2/24
	static routers=192.168.0.1
	static domain_name_servers=192.168.0.1
	```

1. Save the file with `ctrl + o` and then exit nano with `ctrl + x`.

Your Raspberry Pi will now boot up with the IP address `192.168.0.2` every time; we didn't use `192.168.0.1` as this is reserved for the router. You can of course use any address you like, but in the configuration above the range must be between `192.168.0.2` and `192.168.0.255`.

## Testing

1. Reboot with `sudo reboot`.

1. Log in and type `ip a`.

1. You should see the IP address you set in the `eth0:` or `wlan0` entry.

## Troubleshooting

If your Pi is not networked then the IP address may not show. To fix this, connect your Pi to an active network socket, which can be on another running Raspberry Pi; you can also manually bring up (activate) the network interface by typing `sudo ifup eth0` followed by `ip a`.

If you still cannot see your IP address, or it is different to the one you set, then open the `dhcpcd.conf` file, as described in step 1 of the setup instructions, and check that your edits are correct.

## Clean up - reverting the changes

Normally you don't want your computer set to use a static IP address. You can change the network configuration back by editing the `dhcpcd.conf` file as follows:

1. Type `sudo nano /etc/dhcpcd.conf` at the command prompt.

1. Look for the lines you added.

	``` bash
	interface eth0

	static ip_address=192.168.0.2/24
	static routers=192.168.0.1
	static domain_name_servers=192.168.0.1

	interface wlan0

	static ip_address=192.168.0.2/24
	static routers=192.168.0.1
	static domain_name_servers=192.168.0.1
	```

1. Remove these lines and then save the file `ctrl + o` and exit `ctrl + x`
1. Reboot the Raspberry Pi.
