# Linx

Linx 是一个用 Python3 编写的交互式渗透测试工具集，提供了多种安全测试和网络工具功能。

## 功能特点

- 网站爬虫 - 自动化网站内容抓取和分析
- 端口扫描 - 快速探测目标主机开放端口
- 暴力破解 - 支持数据库和SSH服务的密码破解
- 网络嗅探 - 捕获和分析网络数据包
- 无线网络 - WiFi网络扫描和破解
- 远程调用 - 提供RPC功能进行远程操作

## 环境要求

- Python >= 3.6
- Linux/macOS 系统 (需要root权限)

## 安装

```bash
# 从 GitHub 克隆项目
git clone https://github.com/seaung/linx.git

# 安装依赖
pip3 install -r requirements.txt

# 安装 Linx
python3 setup.py install
```

## 使用说明

### 基本命令

```bash
# 启动 Linx
sudo python3 linx.py

# 查看帮助
help

# 退出程序
exit 或 quit
```

### 设置命令

- `set interface` - 设置网络接口
- `set domain` - 设置目标域名
- `set port` - 设置目标端口
- `set target` - 设置目标URL

### 信息显示

- `show interface` - 显示当前网络接口
- `show target` - 显示当前目标
- `show domain` - 显示当前域名
- `show port` - 显示当前端口

### 功能模块使用

每个模块都支持 `show` 命令查看具体帮助信息：

```bash
# 查看模块帮助
<模块名> show

# 示例：查看端口扫描模块帮助
scan show
```

## 许可证

MIT License

## 作者

作者：seaung
项目地址：https://github.com/seaung/linx
