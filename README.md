# betterdiscordctl

A utility for managing BetterDiscord on Linux.

To completely remove `betterdiscordctl`'s local data, delete
`$XDG_DATA_HOME/betterdiscordctl` (or ` $HOME/.local/share/betterdiscordctl`).

## Usage

Some simple instructions can be found [here](./USAGE.md).

## Dependencies

Requires `nodejs`, `npm`, and `git`. If you don't have `nodejs` and `npm` in
your distro's [package manager][node-packages], you can
[download it][node-download].

[node-packages]: https://nodejs.org/en/download/package-manager/
[node-download]: https://nodejs.org/en/download/

## Commands

### `status` (default)

Displays information about your current BetterDiscord setup.

### `install`

Installs BetterDiscord, managing what's necessary by default.

### `update`

Updates BetterDiscord, updating your local repository if present (`origin`
branch). Also cleans up any old patch methods, if found.

(Advanced users should avoid using this if locally modifying their linked
repositories, and should instead manually fetch and update.)

### `uninstall`

Uninstalls BetterDiscord, removing the managed repository if used.

## Options

### `-h` / `--help`

Displays usage information.

### `-v` / `--verbose`

Increases the verbosity level, for progressively more debugging information.

### `-s` / `--scan` (default `/opt`)

Changes the directory scanned for Discord installations.

### `-f` / `--flavors` (default `,Canary,PTB`)

When scanning, looks for installations with the given suffixes (both hyphenated
and unhyphenated). Stable is `''`, as it has no suffix.

### `-d` / `--discord` (requires `--modules`)

Skip scanning and use the Discord installation directory specified.

### `-m` / `--modules`

Disregards scanning results and uses the specified modules directory (found
inside Discord's user-specific storage directory).

### `-r` / `--bd-repo` (default `https://github.com/rauenzi/BetterDiscordApp`)

When initially installing BetterDiscord, use the specified Git repository. Does
_not_ affect updates. Defaults to Zerebos's BandagedBD fork.

### `--bd-repo-branch` (default `stable16`)

When downloading from `--bd-repo`, use this branch.

### `-b` / `--betterdiscord`

Instead of maintaining a local clone of BetterDiscord, use the specified
directory.

### `-c` / `--copy-bd`

Instead of using a symbolic link, copy the BetterDiscord directory into
Discord's modules.

### `--global-asar`

Instead of maintaining a local installation of `asar`, use the one in `PATH`.

### `--snap`

Needed for `betterdiscordctl` to find the modules directory if you installed Discord
via snap. Furthermore, it automatically sets `-c` because symlinks don't work.


### `-V` / `--version`

Displays the current version.
