# betterdiscordctl

A utility for managing BetterDiscord on Linux. Requires NodeJS and Git to be installed.

To completely remove `betterdiscordctl`'s local data, delete
`$XDG_DATA_HOME/betterdiscordctl`.

## Commands

### `status` (default)

Displays information about your current BetterDiscord setup.

### `install`

Installs BetterDiscord, managing what's necessary by default.

### `update`

Updates BetterDiscord, updating your local repository if present (`origin`
branch).

(Advanced users should avoid using this if locally modifying their linked
repositories, and should instead manually fetch and update.)

### `uninstall`

Uninstalls BetterDiscord, removing the managed repository if used.

## Flags

### `-h` / `--help`

Displays usage information.

### `-v` / `--verbose`

Increases the verbosity level, for progressively more debugging information.

### `-s` / `--scan` (default `/opt`)

Changes the directory scanned for Discord installations.

### `-f` / `--flavors` (default `,Canary,PTB`)

When scanning, looks for installations with the given suffixes (both hyphenated
and unhyphenated).

### `-d` / `--discord` (requires `--modules`)

Skip scanning and use the Discord installation directory specified.

### `-m` / `--modules`

Disregards scanning results and uses the specified modules directory (found
inside Discord's user-specific storage directory).

### `-r` / `--bd-repo` (default `https://github.com/rauenzi/BetterDiscordApp`)

When initially installing BetterDiscord, use the specified Git repository. Does
_not_ affect updates. Defaults to Zerebos's BandagedBD fork.

### `-b` / `--betterdiscord`

Instead of maintaining a local clone of BetterDiscord, use the specified
directory.

### `-c` / `--copy-bd`

Instead of using a symbolic link, copy the BetterDiscord directory into
Discord's modules.

### `--global-asar`

Instead of maintaining a local installation of `asar`, use the one in `PATH`.
