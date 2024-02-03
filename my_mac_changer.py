import subprocess
import optparse

parse_object = optparse.OptionParser()
parse_object.add_option("-i", "--interface", dest="interface", help="interface to change")

print("My MacChanger Started!")

interface = "eth0"
mac_address = "00:22:33:44:66:88"
subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", mac_address])
subprocess.call(["ifconfig", interface, "up"])
