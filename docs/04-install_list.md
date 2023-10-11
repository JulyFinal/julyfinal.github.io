# Linux 问题常规收集


# node npm nvm 

使用nvm安装管理node


## nvm

从 `https://github.com/nvm-sh/nvm#installing-and-updating` 找到安装命令

`curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.5/install.sh | bash`

## node

使用 `nvm ls` 可以列出可以安装的各种node版本

`nvm install {node version}`  like `nvm install 18.14.1`


# astro build my blog

[原文教程](https://docs.astro.build/zh-cn/tutorial/0-introduction/)

1. 安装node npm
2. `npm create astro@latest`
3. `npm run dev`


# Git 问题

```bash
# 当前env中的代理
env|grep -i proxy

# 查看git设置
git config --global -l

# 设置Git代理
git config --global http.proxy http://127.0.0.1:7890
git config --global https.proxy http://127.0.0.1:7890

# 取消设置Git代理
git config --global --unset http.proxy 
git config --global --unset https.proxy 

# 关闭ssl认证
git config --global http.sslVerify false

# 关闭Https 每次的密码认证
git config --global credential.helper store
```

## DNS 问题

```
# 设置 /etc/resolv.conf  无效后
sudo vim /etc/systemd/resolved.conf 

DNS=114.114.114.114
DNS=8.8.8.8

systemctl restart systemd-resolved.service
systemd-resolve --status
```

## driver 

`ubuntu-drivers devices` 查看驱动版本

`sudo ubuntu-drivers autoinstall` 或 `sudo apt install nvidia-driver-535` 自动安装驱动

## fix driver

1. sudo apt-get install dkms
2. sudo dkms install -m nvidia -v 535.xxx.xx（NVIDIA版本号）



# cuda

## install

查看GCC版本

https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html 


选择cuda版本

https://developer.nvidia.com/cuda-toolkit-archive


导入环境变量

```bash
export PATH="/usr/local/cuda-12.2/bin:$PATH"
export LD_LIBRARY_PATH="/usr/local/cuda-12.2/lib64:$LD_LIBRARY_PATH"  
```
检查是否成功

`nvcc -V`

## uninstall 

```
cd /usr/local/cuda-xx.x/bin/
sudo ./cuda-uninstaller
sudo rm -rf /usr/local/cuda-xx.x
```

## cuDNN

### install

https://developer.nvidia.com/rdp/cudnn-download


拷贝文件

```
cp cuda/lib64/* /usr/local/cuda-12.2/lib64/
cp cuda/include/* /usr/local/cuda-12.2/include/
```

查看cudann version

```
cat /usr/local/cuda/include/cudnn.h | grep CUDNN_MAJOR -A 2

```

### uninstall

```
sudo rm -rf /usr/local/cuda/include/cudnn*.h
sudo rm -rf /usr/local/cuda/lib64/libcudnn*
sudo rm -rf /usr/include/cudnn*.h
sudo rm -rf /usr/lib/x86_64-linux-gnu/libcudnn*
```


# python

## torch

cuda 12.2

```pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu121```
