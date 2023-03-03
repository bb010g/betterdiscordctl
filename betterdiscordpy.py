import argparse

pname = "betterdiscordctl"
# Constants
version = "2.0.1"

# Options
verbosity = 0
d_flavors = ["canary", "ptb", "development"]
self_upgrade_url = 'https://github.com/bb010g/betterdiscordctl/raw/master/betterdiscordctl'

parser = argparse.ArgumentParser(description="Manage BetterDiscord installations on Linux")
parser.add_argument("-V", "--version", action='store_true', help="display version info and exit")
parser.add_argument("command", choices=["status", "install", "reinstall", "uninstall", "self-upgrade"])
args = parser.parse_args()

if args.version:
    print(pname + " " + version)
#elif args.command:
    if args.command == "status":
        print("test")
    if args.command == "install":
        print("test1")
    if args.command == "reinstall":
        print("test2")
    if args.command == "uninstall":
        print("test3")
    if args.command == "self-upgrade":
        print("test4")
else:
    parser.print_help()