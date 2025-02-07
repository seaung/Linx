import sys
import os
import argparse
import logging
import requests
from console.console import ProcessConsole
from modules.helper import color
from modules.banner import print_banner


version = "1.0.0"
author = "seaung"


def setup_logging(log_level):
    """配置日志记录"""
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('linx.log'),
            logging.StreamHandler()
        ]
    )


def check_version():
    """检查版本更新"""
    try:
        response = requests.get('https://api.github.com/repos/seaung/linx/releases/latest')
        latest_version = response.json()['tag_name']
        if latest_version > version:
            color(f"\n[*] 发现新版本 {latest_version}，当前版本 {version}",'yellow')
            color("[*] 请访问 https://github.com/seaung/linx 获取最新版本\n",'yellow')
    except Exception as e:
        logging.warning(f"检查版本更新失败: {e}")


def parse_args():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(description='Linx - 渗透测试工具集')
    parser.add_argument('-v', '--version', action='version', version=f'Linx {version}')
    parser.add_argument('--debug', action='store_true', help='启用调试模式')
    parser.add_argument('--no-version-check', action='store_true', help='禁用版本检查')
    return parser.parse_args()


def main():
    """主函数"""
    args = parse_args()
    
    # 配置日志级别
    log_level = logging.DEBUG if args.debug else logging.INFO
    setup_logging(log_level)
    
    # 检查root权限
    if os.geteuid() != 0:
        sys.exit("[!] Only for roots kido!")
    
    try:
        # 显示banner
        print(print_banner())
        
        # 检查版本更新
        # if not args.no_version_check:
        #     check_version()
        
        # 初始化并启动控制台
        console = ProcessConsole()
        console.start()
    except KeyboardInterrupt:
        color('\n[*] 用户中断，程序退出', 'yellow')
        sys.exit(0)
    except Exception as e:
        logging.error(f"程序运行出错: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

