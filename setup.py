import io

from setuptools import find_packages
from setuptools import setup

with io.open("README.md", "rt", encoding="utf8") as f:
    readme = f.read()

install_requires = ["click"]
dev_requires = ["ipdb", "pre-commit"]

setup(
    author="Terminal Labs",
    author_email="solutions@terminallabs.com",
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Topic :: Utilities",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    description="Importable CLI-passthrough with bells and whistles.",
    entry_points="""
        [console_scripts]
        cli-passthrough=cli_passthrough.cli:main
     """,
    extras_require={"dev": dev_requires},
    include_package_data=True,
    install_requires=install_requires,
    keywords="cli utilities logging pty subprocess terminal",
    license="BSD-3-Clause",
    long_description=readme,
    long_description_content_type="text/markdown",
    name="CLI-passthrough",
    packages=find_packages(),
    url="https://github.com/terminal-labs/cli-passthrough",
    version="0.1.3",
)
