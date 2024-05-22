from distutils.cmd import Command
from setuptools import setup


class TestCommand(Command):
    user_options = []

    def initialize_options(self):
        return super().initialize_options()

    def finalize_options(self):
        return super().finalize_options()

    def test(self):
        pass

    def run(self):
        raise SystemExit(self.test)


setup(
        name='linx',
        packages=['linx', 'linx/modules', 'linx/console'],
        version='1.0.0',
        description='漏洞检测工具',
        author='seaung',
        author_email='不告诉你',
        url='https://github.com/seaung/linx',
        download_url='https://github.com/seaung/linx/archive/1.0.0.tar.gz',
        keywords=['linx', 'pentest', 'python netowking tools'],
        scripts=['linx/linx.py'],
)

