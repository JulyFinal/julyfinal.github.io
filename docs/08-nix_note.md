# NIX

## install python

安装python3.11 与 3.11版本的pip

`nix-env -iA nixpkgs.python311`

`nix-env -iA nixpkgs.python311Packages.pip`


## 推荐使用的nix命令

```
nix develop 

nix shell

nix run

nix build

nix store gc --debug # 回收空间

nix flake

```
## uninstall nix

```bash

/nix/nix-installer uninstall

rm -rf /nix

# need delete nix user and group

rm -rf /etc/nix/nix.conf

rm -rf ~/.nix-profile

```
