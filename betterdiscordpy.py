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
parser.add_argument('-i', "--d-install", choices=["traditional", "flatpak", "snap"])
args = parser.parse_args()

def verbose(vmsg):
    global verbosity
    if verbosity > 0:
        return True
        if not vmsg == str:
            print("Verbose Error: InvalidStringError: The input is not a valid string")
            exit()
        elif not vmsg:
            print("Verbose Error: EmptyStringError: The input can't be an empty string")
        elif vmsg == str:
            print(vmsg)
        
def xdg_discover_config():
    global d_install, xdg_config
    # finding config directory in linux
    if d_install == "traditional":
        #traditional dir
        xdg_config = "~/.config/"
    elif d_install == "snap":
        #snap dir
        snap_user_data = os.environ['SNAP_USER_DATA']
        xdg_config = os.path.join(snap_user_data, 'discord', '.config')
    elif d_install == "flatpak":
        # flatpak dir
        flatpak_bin = '/usr/bin/flatpak'

        # Path to the Discord app in the flatpak repository
        discord_app = 'com.discordapp.Discord'

        # Try to obtain the configuration directory using the XDG_CONFIG_HOME environment variable
        cmd = f"printf -- '%s\n' \"$XDG_CONFIG_HOME\""
        xdg_config = subprocess.run([flatpak_bin, 'run', '--command=sh', discord_app, '-c', cmd], stdout=subprocess.PIPE, text=True, env=os.environ).stdout.strip()

        if not xdg_config:
            xdg_config = f"~/.var/app/{discord_app}/config"

            

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