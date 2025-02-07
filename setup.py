from distutils.cmd import Command
from setuptools import setup, find_packages


class TestCommand(Command):
    description = '运行单元测试'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import unittest
        test_suite = unittest.TestLoader().discover('linx/tests')
        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(test_suite)
        raise SystemExit(not result.wasSuccessful())


with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='linx',
    packages=find_packages(),
    version='1.0.0',
    description='漏洞检测工具',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='seaung',
    author_email='不告诉你',
    url='https://github.com/seaung/linx',
    download_url='https://github.com/seaung/linx/archive/1.0.0.tar.gz',
    keywords=['linx', 'pentest', 'python networking tools', 'security'],
    scripts=['linx/linx.py'],
    install_requires=[
        'psutil',
        'termcolor',
        'requests',
    ],
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Security',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    cmdclass={
        'test': TestCommand,
    },
)

