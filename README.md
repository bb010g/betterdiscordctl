# betterdiscordctl

A manager for BetterDiscord on Linux.

## Installation

### Packages

- Arch: https://aur.archlinux.org/packages/betterdiscordctl-git
- Ubuntu: https://launchpad.net/~chronobserver/+archive/ubuntu/betterdiscordctl
- Fedora: https://copr.fedorainfracloud.org/coprs/observeroftime/betterdiscordctl
- NixOS: https://search.nixos.org/packages?channel=unstable&query=betterdiscordctl&show=betterdiscordctl

### Manual

Requires `curl`, which you can install from your distro's
[package manager][curl-packages], if it's not already installed.

[curl-packages]: https://curl.se/download.html#Linux

You can then install as follows (`#` means that a command needs root, which
you can get by prefixing it with `sudo`):

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

betterdiscordctl (mostly) follows the Fuchsia
[command-line tools rubric's execution section][fuchsia-cli-execution] and
[CLI tool help requirements][fuchsia-cli_help].

[fuchsia-cli-execution]: https://fuchsia.dev/fuchsia-src/concepts/api/cli#execution
[fuchsia-cli_help]: https://fuchsia.dev/fuchsia-src/concepts/api/cli_help

TODO: Update this options section (based on `--help`?)

* `-V`, `--version`

  Displays the current version.

* `-h`, `--help`

  Displays usage information.

* `-v`, `--verbose`

  Increases the verbosity level, for progressively more debugging information.

* `-q`, `--quiet`

  Decreases the verbosity level, for progressively less debugging information.

* `-f`, `--d-flavors` `<d_flavors>` (default `:canary:ptb`)

  When scanning, looks for installations with the given suffixes (case
  insensitive, both hyphenated and unhyphenated). Stable is `''`, as it has no
  suffix. Note that **no** spaces follow colons. Your Discord flavor probably
  doesn't have a space in it, so don't use any in here.

* `-m`, `--d-modules` `<d_modules>`

  Disregards scanning results and uses the specified modules directory (found
  inside Discord's user-specific storage directory).

* `-D`, `--bd-remote-dir` `<bd_r_dir>`

* `-U`, `--bd-remote-url` `<bd_r_url>`

* `-H`, `--bd-remote-github` `<bd_r_github>` (default `~rauenzi/BetterDiscordApp#latest`)

  When installing BetterDiscord, use the specified GitHub repository.
  Defaults to upstream BetterDiscord.

  When downloading from `--bd-remote-github`, use this release.

* `--bd-remote-asar` `<bd_r_asar>`

  Instead of downloading `betterdiscord.asar` from a release, use the
  specified BetterDiscord asar file name. This flag is mostly meant for quirky
  tests of custom BetterDiscord builds.

* `-i`, `--d-install` …

  + `traditional` (default)

  + `flatpak`

  Automatically detect the default Flatpak directory for Discord.

  + `snap`

  Automatically detect the default Snap directory for Discord.

* `--flatpak-bin` `<flatpak>` (default `flatpak`)

  Calls this `flatpak` executable.

* `--snap-bin` `<snap>` (default `snap`)

  Calls this `snap` executable.

* `--upgrade-url` `<upgrade_url>` (default `https://github.com/bb010g/betterdiscordctl/raw/master/betterdiscordctl`)

  Use the specified URL for upgrading betterdiscordctl.

## Commands

### `status`

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

* `betterdiscordctl --help`

  Lists options & commands.

* `betterdiscordctl -f ptb status`

  Shows the BetterDiscord for the PTB flavor.

* `betterdiscordctl -f canary install`

  Installs BetterDiscord to the Canary flavor.

* `betterdiscordctl -i flatpak reinstall`

  Reinstalls BetterDiscord to a Discord installed via Flatpak.

* `betterdiscordctl -i snap uninstall`

  Uninstalls BetterDiscord from a Discord installed via Snap.

## Files

* `$XDG_DATA_HOME/betterdiscordctl` (fallback `~/.local/share/betterdiscordctl`)

  `betterdiscordctl`'s machine-specific data directory. Currently unused and
  not created on new installs.

* `$XDG_CONFIG_HOME/BetterDiscord` (fallback `~/.config/BetterDiscord`)

  `betterdiscord`'s normal data & configuration.

  * With `--flatpak`, this will fall back to
    `~/.var/app/com.discordapp.Discord/config/BetterDiscord`.

  * With `--snap`, this will fall back to `$SNAP_USER_DATA/.config`.
