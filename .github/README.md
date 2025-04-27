# AppleTree

An attempt to recreate a similar experience to
[flaport/home](https://github.com/flaport/home) on MacOS.

a.k.a _my [dotfiles](#list-of-configs) + [bootstrapping scripts](#todo) for MacOS._

a.k.a _highly opinionated configurations for anything I ever used on MacOS._

> This is a work in progress. Will push changes when I make them.

## Installation
**This repository is meant to be your home folder!** Indeed, the .gitignore ignores all
files in this folder by default so this makes it safe to use as a git repository.
However, this means that to start tracking a file you must force add it with
`git add -f <file>`.

To configure your current home folder as a git repository, run the following commands:

```bash
git init --initial-branch=master
git remote add origin https://github.com/flaport/appletree # or your fork
git branch --set-upstream-to=origin/master master
git pull origin master
```

That's it! You can now start using this repository as your home folder.

## List of configs
- [Flameshot](https://github.com/flameshot-org/flameshot): great screenshot tool.
- [Ghostty](https://github.com/ghostty-org/ghostty) as a terminal. I like this one on MacOS better than Alacrity.
- [Karabiner](https://github.com/pqrs-org/Karabiner-Elements): I use this to swap ctrl and fn, because ctrl needs to be the most left key on the keyboard.
- [Neovim](https://github.com/neovim/neovim): I try to keep this config the same as the one in [home](https://github.com/flaport/home).
- [Simple Bar](https://github.com/Jean-Tinland/simple-bar): a status bar for Yabai so i can see my workspaces.
- [Skhd](https://github.com/koekeishiya/skhd): hotkey daemon. Works great with Yabai.
- [Yabai](https://github.com/koekeishiya/yabai): the best window manager for MacOS (I do miss my dear [DWM](https://github.com/flaport/dwm) fork though 😢)
- [Zsh](https://github.com/zsh-users/zsh): The only decent bash replacement.
- ... probably more to come.

You can install all of these using [Homebrew](https://brew.sh/). However, I did install
yabai using the curl script:

```bash
curl -L https://raw.githubusercontent.com/koekeishiya/yabai/master/scripts/install.sh | sudo sh /dev/stdin
```

I highly recommend going through the [documentation of
yabai](https://github.com/koekeishiya/yabai/wiki). There are a few custom
configuration steps you need to go through for it to work well.

## Todo

- [ ] Bootstrapping scripts.
