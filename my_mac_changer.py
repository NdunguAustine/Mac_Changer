import subprocess
import optparse


def get_user_inputs():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--interface", dest="interface", help="interface to change")
    parse_object.add_option("-m", "--mac", dest="mac_address", help="new mac address")

    return parse_object.parse_args()


# subprocesses for commands
def change_mac_address(user_interface, user_mac_address):
    subprocess.call(["ifconfig", user_interface, "down"])
    subprocess.call(["ifconfig", user_interface, "hw", "ether", user_mac_address])
    subprocess.call(["ifconfig", user_interface, "up"])


def control_new_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig", interface])
    print(ifconfig)

print("My MacChanger Started!")
# Assigning arguments to function get_user_inputs
(user_input, arguments) = get_user_inputs()

# passing the arguments to fuction change_mac_address
change_mac_address(user_input.interface, user_input.mac_address)
control_new_mac(user_input.interface)