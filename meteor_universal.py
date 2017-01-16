# Based on the Meteor project and TomFruedenburg's meteor universal (thx a lot).
print("Meteor Installer for ARMv(6,7,8) and 32-bit devices!")

# Importing modules and building functions
import platform
import os, sys

# Checking admin rights
if os.getuid() != 0:
    print("Kindly run as sudo (superuser) aka root.")
    sys.exit(1)

# Requires confirmation
print("This installer requires a working internet connection.")
inp = input("Do you wish to continue? [y/n]: ")
if inp == "n" or inp == "no":
    print("Stopping installation.")
    sys.exit(0)

# Starting install functions
print("Starting Meteor installation.")
os.chdir("/usr/local/lib/")
os.mkdir("/usr/local/lib/meteor")
os.system("sudo chmod 777 meteor")
os.system("git clone https://github.com/4commerce-technologies-AG/meteor.git")
os.system("ln -s /usr/local/lib/meteor/meteor /usr/local/bin/meteor")
os.system("meteor --version")
print('''Installation is successful.
Meteor is now accessible from the 'meteor' command.''')
