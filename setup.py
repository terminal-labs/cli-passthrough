import ast
import io
import re

from setuptools import setup, find_packages

with io.open("README.md", "rt", encoding="utf8") as f:
    readme = f.read()

setup(
    author="Terminal Labs",
    author_email="solutions@terminallabs.com",
    description="Importable CLI-passthrough with bells and whistles.",
    include_package_data=True,
    keywords="cli utilities logging pty subprocess terminal",
    license="BSD-3-Clause",
    long_description=readme,
    long_description_content_type="text/markdown",
    name="CLI-passthrough",
    packages=find_packages(),
    url="https://github.com/terminal-labs/cli-passthrough",
    version="0.1.2",
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Topic :: Utilities",
    ],
    entry_points="""
        [console_scripts]
        cli-passthrough=cli_passthrough.cli:main
     """,
    install_requires=["click"],
)
