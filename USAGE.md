# How to use betterdiscordctl

## Requirements

#### Git

Install using your [package manager](https://git-scm.com/download/linux)

#### Node with npm

Install using your [package manager](https://nodejs.org/en/download/package-manager/)

Or download a [binary package](https://nodejs.org/en/download/)

## Installation

#### Download the script

```
$ curl -O https://raw.githubusercontent.com/ObserverOfTime/betterdiscordctl/master/betterdiscordctl
```

#### Make it executable

```
$ chmod +x betterdiscordctl
```

#### Move it to a directory in your PATH for later use

```
$ sudo mv betterdiscordctl /usr/local/bin
```

#### Run the script

Replace `[COMMAND]` with `install` to install BD for the first time, `update` to update an existing installation, or `uninstall` to uninstall an existing installation.

Replace `[PATH]` with the path to Discord's parent directory. For example, if Discord is installed in `/usr/share/discord`, `[PATH]` should be `/usr/share`.

If you installed Discord via snap you will also need to pass the `--snap` flag.

- For Stable

```
$ betterdiscordctl [COMMAND] -s [PATH]
````

- For PTB

```
$ betterdiscordctl [COMMAND] -s [PATH] -f PTB
````

- For Canary

```
$ betterdiscordctl [COMMAND] -s [PATH] -f Canary
````

> After installation, your plugins and themes will be located in `$XDG_CONFIG_HOME/BetterDiscord` (or `$HOME/.config/BetterDiscord`).
Or, `$HOME/snap/discord/current/.config/BetterDiscord`, if you installed Discord via snap.

