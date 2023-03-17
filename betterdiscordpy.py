import argparse, os, subprocess

pname = "betterdiscordctl"
# Constants
version = "2.0.1"
verbosity = 0

# Options
verbosity = 0
d_flavors = ["canary", "ptb", "development"]
self_upgrade_url = 'https://github.com/bb010g/betterdiscordctl/raw/master/betterdiscordctl'

parser = argparse.ArgumentParser(description="Manage BetterDiscord installations on Linux")
parser.add_argument("-V", "--version", action='store_true', help="display version info and exit")
parser.add_argument("command", choices=["status", "install", "reinstall", "uninstall", "self-upgrade"])
parser.add_argument('-v', "--verbose", action='store_true', help="increase verbosity")
parser.add_argument('-q', "--quiet", action='store_true', help="decrease verbosity")
args = parser.parse_args()

def verbose(vmsg):
    global verbosity
    if verbosity > 0:
        return True
        if not vmsg == str:
            print("InvalidStringError: The input is not a valid string")
        elif vmsg == str:
            print(vmsg)
        
def xdg_discover_config():
    # finding config directory on linux
    #traditional dir
    if d_install == "traditional":
        xdg_config = "~/.config/"
    elif d_install == "snap":
        #snap dir
        xdg_config = subprocess.run(["snap", "run", "--shell", "discord"], stdout=subprocess.PIPE)
            

if args.version:
    print(pname + " " + version)
elif args.command:
    if args.command == "status":
        print("test")
    if args.command == "install":
        
    if args.command == "reinstall":
        print("test2")
    if args.command == "uninstall":
        print("test3")
    if args.command == "self-upgrade":
        print("test4")
elif args.verbose:
    verbosity =+ 1
elif args.quiet:
    verbosity = 0
else:
    parser.print_help()