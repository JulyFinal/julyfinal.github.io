# 



## install python

安装python3.11 与 3.11版本的pip

`nix-env -iA nixpkgs.python311`

`nix-env -iA nixpkgs.python311Packages.pip`


PS: 暂时还没有确定使用这种方法安装的python在编译 transformers 的时候是不是有什么问题风险（类似缺少编译工具、库等）

## 推荐使用的nix命令

nix develop , nix shell, nix run, nix build, nix store gc --debug, nix flakes

## uninstall nix

```bash
/nix/nix-installer uninstall

rm -rf /nix

# need delete nix user and group

rm -rf /etc/nix/nix.conf

rm -rf ~/.nix-profile

```
