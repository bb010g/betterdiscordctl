# betterdiscordctl

A utility for managing BetterDiscord on Linux.

## Table of Contents

- [Dependencies](#dependencies)
- [Options](#options)
- [Commands](#commands)
- [Installation](#installation)
- [Examples](#examples)
- [Locations](#locations)

## Dependencies

### Git

Install using your [package manager][git-packages]

[git-packages]: https://git-scm.com/download/linux

### Node & npm

Install using your [package manager][node-packages]

Or download a [binary package][node-download]

[node-packages]: https://nodejs.org/en/download/package-manager

[node-download]: https://nodejs.org/en/download

## Options

### `-V` / `--version`

Displays the current version.

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

Needed for `betterdiscordctl` to find the modules directory if Discord was installed via snap. Furthermore, it automatically sets `-c` because symlinks don't work.

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

### `upgrade`

Updates `betterdiscordctl` to the latest version available on GitHub.

## Installation

### Arch

You can install `betterdiscordctl` from [AUR][AUR-package].

[AUR-package]: https://aur.archlinux.org/packages/betterdiscordctl-git

### Other distributions

```
$ curl -O https://raw.githubusercontent.com/bb010g/betterdiscordctl/master/betterdiscordctl
$ chmod +x betterdiscordctl
$ sudo mv betterdiscordctl /usr/local/bin
```
> /usr/local/bin must be in your `PATH` for this to work.

You can then keep `betterdiscordctl` up to date with this command:

```
$ betterdiscordctl upgrade
```

## Examples

### Status (Discord in `/usr/share/discord`)

```
$ betterdiscordctl status -s /usr/share
````

### Install (Discord PTB in `/opt/discord-ptb`)

```
$ betterdiscordctl install -s /opt -f PTB
````

### Update (Discord Canary in `/opt/discord-canary`)

```
$ betterdiscordctl update -s /opt -f Canary
```

### Uninstall (Snap Discord in `/snap/discord/current/usr/share/discord`)

```
$ betterdiscordctl uninstall -s /snap/discord/current/usr/share --snap
```

## Locations

### `betterdiscordctl`'s local data

`$XDG_DATA_HOME/betterdiscordctl` (or ` $HOME/.local/share/betterdiscordctl`)

### BetterDiscord plugins & themes

#### Stable/PTB/Canary

`$XDG_CONFIG_HOME/BetterDiscord` (or `$HOME/.config/BetterDiscord`)

#### Snap

`$HOME/snap/discord/current/.config/BetterDiscord`
