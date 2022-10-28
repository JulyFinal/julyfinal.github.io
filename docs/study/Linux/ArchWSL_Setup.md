# Arch子系统

首先从[ArchWSL](https://github.com/yuk7/ArchWSL)下载appx和cer。

	1. 从 [GH/镜像] 下载发布的 .appx 和 .cer 文件。
	2. 安装 .cer 文件到 “本地计算机” 的 “受信任的根证书颁发机构”。 
	3. 双击安装 appx 文件。
	
修改默认`wsl --set-default-version 2`
设置ArchWSL为2 `wsl --set-version Arch 2`
	
```
echo "%wheel ALL=(ALL) ALL" > /etc/sudoers.d/wheel
useradd -m -G wheel -s /bin/bash {username}
passwd {username}

# 切换用户
sudo pacman-key --init
sudo pacman-key --populate
sudo pacman -Syy archlinux-keyring
# 修改mirrorlist为中国

Arch.exe config --default-user {username}
```

PS:

网络问题

```
# wsl2 ping不通windows主机
New-NetFirewallRule -DisplayName "WSL" -Direction Inbound  -InterfaceAlias "vEthernet (WSL)"  -Action Allow
```

# 自动获取主机IP

```bash
chmod 777 /etc/hosts

cat >> ~/.profile <<EOF
windows_ip=`grep -oP '(?<=nameserver ).+' /etc/resolv.conf`
if [ "`grep windows /etc/hosts`" ]; then
        sed -i "s/.*windows/$windows_ip windows/" /etc/hosts
else
        echo $windows_ip windows >> /etc/hosts
fi
EOF

```
