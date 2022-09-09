# Linux 问题常规收集

## Git 问题

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

