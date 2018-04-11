from setuptools import setup, find_packages

setup(
    name='CLI-passthrough',
    version=0.1,
    url='https://github.com/terminal-labs/cli-passthrough',
    author='Terminal Labs',
    author_email='solutions@terminallabs.com',
    license='BSD-3-Clause',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires= [
        'click',
    ],
    entry_points='''
        [console_scripts]
        cli-passthrough=cli_passthrough.cli:main
     '''
)
