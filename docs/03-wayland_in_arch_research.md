# Wayland 在 Arch 中的研究

目前依然存在的问题有截图。

```
sudo pacman -S wlroots sway alacritty waybar wofi xorg-xwayland xorg-xlsclients qt5-wayland glfw-wayland bemenu-wayland otf-font-awesome

sudo pacman -S vulkan-validation-layers

# 亮度 音量
sudo pacman -S acpilight（用于Intel核显）
sudo pacman -S alsa-utils alsa-plugins

# 环境变量配置
/etc/environment
WLR_RENDERER=vulkan
# WLR_RENDERER=gles2
MOZ_ENABLE_WAYLAND=1 # firefox开启wayland

# 简单的脚本 登陆自动启动Sway
vim ~/.bash_profile ：
[[ -f ~/.bashrc ]] && . ~/.bashrc
[ "$(tty)" = "/dev/tty1" ] && exec sway
```

## PS：
### Arch Linux 上的完整 Wayland 设置

https://a-wing.top/linux/2022/01/03/translate_wayland.html

### 探索linux桌面全面wayland化（基于swaywm）

https://zhuanlan.zhihu.com/p/462322143

## 内核
https://liquorix.net/
https://hyprland.org/
