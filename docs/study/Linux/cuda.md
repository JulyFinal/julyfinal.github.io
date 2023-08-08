


## driver 

`ubuntu-drivers devices` 查看驱动版本

`sudo ubuntu-drivers autoinstall` 或 `sudo apt install nvidia-driver-535` 自动安装驱动


## cuda

### install

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

### uninstall 

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


## python

### torch

cuda 12.2

```pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu121```
