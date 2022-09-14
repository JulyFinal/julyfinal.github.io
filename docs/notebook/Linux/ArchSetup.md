# Arch 安装指南
## 安装时
### 系统
```bash
# 检查
systemctl stop reflector.service # 禁止自动选择源
ls /sys/firmware/efi/efivars # 检查是否进入UEFI模式

# 无线网络
iwctl #执行iwctl命令，进入交互式命令行 
device list #列出设备名，比如无线网卡看到叫 wlan0 
station wlan0 scan #扫描网络 
station wlan0 get-networks #列出网络 比如想连接YOUR-WIRELESS-NAME这个无线 
station wlan0 connect YOUR-WIRELESS-NAME #进行连接 输入密码即可 
exit #成功后exit退出

# set time
timedatectl set-ntp true

# 分区
fdisk -l # cfdisk fdisk的可视化
fdisk /dev/nvme0n1

# 分区大小
# GPT分区
# 挂载点 空间
# /mnt/boot 300MiB
# /mnt 剩余空间

mkfs.fat -F 32 nvme0n1p1
mkfs.btrfs nvme0n1p2

# mount
mount -t btrfs -o ssd /dev/nvme0n1p2 /mnt
mount /dev/nvme0n1p1 /mnt/boot

# 设置镜像地址
/etc/pacman.d/mirrorlist

Server = https://mirrors.ustc.edu.cn/archlinux/$repo/os/$arch
Server = https://mirrors.tuna.tsinghua.edu.cn/archlinux/$repo/os/$arch
Server = https://mirror.archlinux.tw/ArchLinux/$repo/os/$arch
Server = https://mirror.aktkn.sg/archlinux/$repo/os/$arch
Server = https://mirrors.cat.net/archlinux/$repo/os/$arch

# 预放入包程序
pacstrap /mnt base base-devel linux linux-headers linux-firmware
pacstrap /mnt sudo zsh neovim vi dhcpcd wpa_supplicant networkmanager # 网络无线
pacstrap /mnt bluez bluez-utils # 蓝牙

# 可选

# 写入卷标
genfstab -U /mnt >> /mnt/etc/fstab

# 进入系统
arch-chroot /mnt

# 设置时区
ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
hwclock --systohc


# locale
/etc/locale.gen
# 取消en_US.UTF-8 和 zh_CN.UTF-8 注释
locale-gen
echo 'LANG=en_US.UTF-8' > /etc/locale.conf


# hostname
/etc/hostname
# 设置主机名 finalserver
vim /etc/hosts
127.0.0.1 localhost 
::1 localhost 
127.0.1.1 finalserver

## 可选 设置root密码
passwd root

# edit sudo
visudo
# 开启%wheel ALL=(ALL) ALL
useradd -m -G wheel -s /bin/zsh final
# set passwd
passwd final

# 安装微码
pacman -S intel-ucode

# 设置grub
pacman -S grub efibootmgr
grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB
# 接下来编辑/etc/default/grub 文件，去掉`GRUB_CMDLINE_LINUX_DEFAULT`一行中最后的 quiet 参数，同时把 log level 的数值从 3 改成 5。这样是为了后续如果出现系统错误，方便排错。同时在同一行加入 nowatchdog 参数，这可以显著提高开关机速度。
grub-mkconfig -o /boot/grub/grub.cfg

mkinitcpio -P

# 设置服务
systemctl enable dhcpcd
systemctl enable wpa_supplicant
systemctl enable NetworkManager
systemctl enable bluetooth
systemctl enable --now bluetooth

## 优化SSD
systemctl enable fstrim.timer

#exit
# 退出
umount -R /mnt

```


## 安装后

### 可选
  
  ```bash
  sudo pacman -S sof-firmware alsa-firmware alsa-ucm-conf #一些可能需要的声音固件 
  sudo pacman -S ntfs-3g #识别NTFS格式的硬盘 
  sudo pacman -S adobe-source-han-serif-cn-fonts wqy-zenhei #安装几个开源中文字体 一般装上文泉驿就能解决大多wine应用中文方块的问题 
  sudo pacman -S noto-fonts-cjk noto-fonts-emoji noto-fonts-extra #安装谷歌开源字体及表情 
  sudo pacman -S firefox #安装火狐浏览器
  sudo pacman -S ark #与dolphin同用右键解压
  sudo pacman -S p7zip unrar unarchiver lzop lrzip #安装ark可选依赖 
  sudo pacman -S packagekit-qt5 packagekit appstream-qt appstream #确保Discover(软件中心）可用 需重启 
  sudo pacman -S gwenview #图片查看器 
  sudo pacman -S xf86-video-intel plasma-meta firefox
  sudo pacman -S dolphin konsole yakuake # 文件管理器 命令行 下拉式命令行
  sudo pacman -S git wget kate bind #一些工具
  ```
  
  ```bash
  sudo pacman -S sddm
  systemctl enable sddm
  ````

  ```bash
  /etc/resolv.conf
  
  nameserver 8.8.8.8 
  nameserver 2001:4860:4860::8888 
  nameserver 8.8.4.4 
  nameserver 2001:4860:4860::8844
  
  加入不可配置符号，避免路由器设置写入
  sudo chattr +i /etc/resolv.conf
  ```
  
  ```bash
  # 核心显卡
  sudo pacman -S mesa lib32-mesa vulkan-intel lib32-vulkan-intel
  ```

### YAY
```
# yay 配置
git clone https://aur.archlinux.org/yay
cd yay
makepkg -si

# go换源
go env -w GO111MODULE=on
go env -w GOPROXY=https://goproxy.cn,direct
# 临时生效
export GO111MODULE=on
export GOPROXY=https://goproxy.cn
# 永久生效
echo "export GO111MODULE=on" >> ~/.profile
echo "export GOPROXY=https://goproxy.cn" >> ~/.profile
source ~/.profile

# 替换yay 为yay-bin
yay -S yay-bin
# 问及移除 yay 时选是
yay
rm -rf yay
```
### Proxy

```shell
sudo pacman -S proxychains-ng
```
### GIT UI
```bash
sudo pacman -S lazygit
```

```bash
git config --global user.name julyfinal
git config --global user.email julyfinal@outlook.com
# git config --global http.proxy socks5://127.0.0.1:7890
# git config --global https.proxy socks5://127.0.0.1:7890
```
### 输入法

```shell
sudo pacman -S fcitx5-im 
sudo pacman -S fcitx5-chinese-addons  # fcitx5-rime fcitx-configtool可选 
# 可选
yay -S fcitx5-pinyin-moegirl
sudo pacman -S fcitx5-pinyin-zhwiki #中文维基百科词库 
sudo pacman -S fcitx5-material-color #主题

# /etc/environment
GTK_IM_MODULE=fcitx
QT_IM_MODULE=fcitx
XMODIFIERS=@im=fcitx
SDL_IM_MODULE=fcitx

# i3w etc.
# fcitx5
exec_always --no-startup-id fcitx5

fcitx5 &
```

### GFW
```shell
yay -S clash-for-windows-bin
```

### 虚拟机
需要提前了解linux的核心版本
```shell
uname -r
# 5.15.38-1-MANJARO
```
则下方的linux为linux515
```shell
sudo pacman -S virtualbox linux515-virtualbox-host-modules # virtualbox-host-dkms

# 查看 Virtualbox 版本
$ vboxmanage --version
6.1.30r148432
​
# 安装拓展包，选择跟 Virtualbox 版本号一致的
$ yay virtualbox-ext-oracle

sudo gpasswd -a $USER vboxusers
```

### 编程环境

### WPS
```text
yay -S wps-office wps-office-mui-zh-cn ttf-wps-fonts
```

### UniVPN
```shell
sudo -i

# seco client 依赖 ubuntu 的 arch 命令， 模拟 arch 命令返回 x86_64
echo "echo x86_64" > /usr/bin/arch
chmod u+x /usr/bin/arch

# install seco client
sh ./univpn-linux-64-10781.2.550.0329.run

# 启动后台服务
cd /usr/local/UniVPN/promote
./UniVPNPromoteService -d

# 界面就可以启动UniVPN了
```