# betterdiscordctl

A manager for BetterDiscord on Linux.

## Installation

### Packages

- Arch: https://aur.archlinux.org/packages/betterdiscordctl-git
- Ubuntu: https://launchpad.net/~chronobserver/+archive/ubuntu/betterdiscordctl
- Fedora: https://copr.fedorainfracloud.org/coprs/observeroftime/betterdiscordctl

### Manual

Requires `git`, `nodejs`, and `npm`. You can install `git` from your distro's
[package manager][git-packages]. If you don't have `nodejs` and `npm` in your
distro's [package manager][node-packages], you can
[download them][node-download].

[git-packages]:  https://git-scm.com/download/linux/
[node-packages]: https://nodejs.org/en/download/package-manager/
[node-download]: https://nodejs.org/en/download/

You can then install as follows (`#` means that a command needs root, which you
can get by prefixing it with `sudo`):

```
$ curl -O https://raw.githubusercontent.com/bb010g/betterdiscordctl/master/betterdiscordctl
$ chmod +x betterdiscordctl
# mv betterdiscordctl /usr/local/bin
```

You can then keep `betterdiscordctl` up to date with one command:

```
# betterdiscordctl upgrade
```

## Options

* `-V` / `--version`

  Displays the current version.

* `-h` / `--help`

  Displays usage information.

* `-v` / `--verbose`

  Increases the verbosity level, for progressively more debugging information.

* `-s` / `--scan` (default `/opt,/usr/share`)

  Changes the directories scanned for Discord installations. These are scanned
  in the order provided. Note that these do **not** end in `/discord`—if your
  Discord installation is at `/opt/discord`, then `/opt` should be scanned.

* `-f` / `--flavors` (default `,canary,ptb`)

  When scanning, looks for installations with the given suffixes (case
  insensitive, both hyphenated and unhyphenated). Stable is `''`, as it has no
  suffix. Note that **no** spaces follow commas. Your Discord flavor probably
  doesn't have a space in it, so don't use any in here.

* `-d` / `--discord` (requires `--modules`)

  Skip scanning and use the Discord installation directory specified. This
  **does** probably end in `/discord`.

* `-m` / `--modules`

  Disregards scanning results and uses the specified modules directory (found
  inside Discord's user-specific storage directory).

* `-r` / `--bd-repo` (default `https://github.com/rauenzi/BetterDiscordApp`)

  When installing BetterDiscord, use the specified Git repository. Does _not_
  affect updates. Defaults to Zerebos's BandagedBD fork.

* `--bd-repo-branch` (default `stable16`)

  When downloading from `--bd-repo`, use this branch.

* `-b` / `--betterdiscord`

  Instead of maintaining a local clone of BetterDiscord, use the specified
  directory.

* `-c` / `--copy-bd`

  Instead of using a symbolic link, copy the BetterDiscord directory into
  Discord's modules.

* `--global-asar`

  Instead of maintaining a local installation of `asar`, use the one in `PATH`.

* `--snap`

  Automatically detect the default Snap directories for Discord. The `-c` flag
  is set due to Snaps apps being [confined][snapcraft-docs].

* `--flatpak`

  Automatically detect the default Flatpak directories for Discord. The `-c`
  flag is set due to Flatpak apps being [sandboxed][flatpak-docs].

[snapcraft-docs]: https://docs.snapcraft.io/reference/confinement
[flatpak-docs]:   http://docs.flatpak.org/en/latest/working-with-the-sandbox.html

## Commands

### `status` (default)

Displays information about your current BetterDiscord setup.

### `install`

Installs BetterDiscord, managing what's necessary by default.

### `reinstall`

Reinstalls BetterDiscord, removing the old files.

### `update`

Updates BetterDiscord, updating your local repository if present
(`origin` branch). Also cleans up any old patch methods, if found.

(Advanced users should avoid using this if locally modifying their
linked repositories, and should instead manually fetch and update.)

### `uninstall`

Uninstalls BetterDiscord, removing the managed repository if used.

### `upgrade`

Updates `betterdiscordctl` to the latest version available on GitHub.

## Examples

* `betterdiscordctl`

  Works like `betterdiscordctl status`.

* `betterdiscordctl status -s /usr/share`

  Shows the status of the default Discord install in `/usr/share`, instead
  of `/opt`.

* `betterdiscordctl install -f ptb`

  Installs BetterDiscord to the PTB flavor, instead of the default.

* `betterdiscordctl reinstall -f canary`

  Reinstalls BetterDiscord to Discord Canary.

* `betterdiscordctl update --flatpak`

  Updates BetterDiscord for a Discord installed via Flatpak.

* `betterdiscordctl uninstall --snap`

  Uninstalls BetterDiscord for a Discord installed via Snap.

## Files

* `$XDG_DATA_HOME/betterdiscordctl` (fallback `~/.local/share/betterdiscordctl`)

  `betterdiscordctl`'s machine-specific data directory.

* `$XDG_DATA_HOME/betterdiscordctl/bd_map`

  A mapping of current Discord installations to BetterDiscord clones.

* `$XDG_DATA_HOME/betterdiscordctl/bd`

  A directory of BetterDiscord clones, indexed by `bd_map`.

* `$XDG_DATA_HOME/asar`

  A locally managed installation of `asar`.

* `$XDG_CONFIG_HOME/BetterDiscord` (fallback `~/.config/BetterDiscord`)

  `betterdiscord`'s normal data & configuration.

  * With `--snap`, this will fall back to `$SNAP_USER_DATA/.config`.

  * When `--flatpack` is used, this will fall back to
    `~/.var/app/com.discordapp.Discord/config/BetterDiscord`.
