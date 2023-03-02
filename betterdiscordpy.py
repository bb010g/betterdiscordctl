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
args = parser.parse_args()

if args.version:
    print(pname + " " + version)
else:
    parser.print_help()