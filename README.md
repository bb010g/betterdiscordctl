# betterdiscordctl

A manager for BetterDiscord on Linux.

## Installation

### Packages

- Arch: https://aur.archlinux.org/packages/betterdiscordctl-git
- Ubuntu: https://launchpad.net/~chronobserver/+archive/ubuntu/betterdiscordctl
- Fedora: https://copr.fedorainfracloud.org/coprs/observeroftime/betterdiscordctl
- NixOS: https://search.nixos.org/packages?channel=unstable&query=betterdiscordctl&show=betterdiscordctl

### Manual

Requires `curl` which you can install from your distro's [package manager][curl-packages].

[curl-packages]: https://curl.se/download.html#Linux

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

* `-f` / `--flavors` (default `:canary:ptb`)

  When scanning, looks for installations with the given suffixes (case
  insensitive, both hyphenated and unhyphenated). Stable is `''`, as it has no
  suffix. Note that **no** spaces follow colons. Your Discord flavor probably
  doesn't have a space in it, so don't use any in here.

* `-m` / `--modules`

  Disregards scanning results and uses the specified modules directory (found
  inside Discord's user-specific storage directory).

* `-r` / `--bd-repo` (default `https://github.com/rauenzi/BetterDiscordApp`)

  When installing BetterDiscord, use the specified Git repository.

* `--bd-repo-release` (default `latest`)

  When downloading from `--bd-repo`, use this release.

* `-b` / `--betterdiscord`

  Instead of downloading a copy of `betterdiscord.asar`, use the specified file.

* `--snap`

  Automatically detect the default Snap directory for Discord.

* `--snap-bin` (default `snap`)

  Calls this `snap` executable.

* `--flatpak`

  Automatically detect the default Flatpak directory for Discord.

* `--flatpak-bin` (default `flatpak`)

  Calls this `flatpak` executable.

* `--upgrade-url` (default `https://git.io/bdctl`)

  Use the specified URL for upgrading betterdiscordctl.

## Commands

### `status` (default)

Displays information about your current BetterDiscord setup.

### `install`

Installs BetterDiscord, managing what's necessary by default.

### `reinstall`

Reinstalls BetterDiscord, removing the old files.

### `uninstall`

Uninstalls BetterDiscord, removing the managed repository if used.

### `upgrade`

Updates `betterdiscordctl` to the latest version available on GitHub.

## Examples

* `betterdiscordctl`

  Works like `betterdiscordctl status`.

* `betterdiscordctl install -f ptb`

  Installs BetterDiscord to the PTB flavor, instead of the default.

* `betterdiscordctl reinstall -f canary`

  Reinstalls BetterDiscord to Discord Canary.

* `betterdiscordctl status --flatpak`

  Shows the BetterDiscord status for a Discord installed via Flatpak.

* `betterdiscordctl uninstall --snap`

  Uninstalls BetterDiscord for a Discord installed via Snap.

## Files

* `$XDG_DATA_HOME/betterdiscordctl` (fallback `~/.local/share/betterdiscordctl`)

  **No longer used and may be deleted in a later release.**

* `$XDG_CONFIG_HOME/BetterDiscord` (fallback `~/.config/BetterDiscord`)

  `betterdiscord`'s normal data & configuration.

  * With `--snap`, this will fall back to `$SNAP_USER_DATA/.config`.

  * With `--flatpak`, this will fall back to
    `~/.var/app/com.discordapp.Discord/config/BetterDiscord`.
