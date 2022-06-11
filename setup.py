import re
from setuptools import setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

with open("pcbheart/__init__.py") as f:
    searched = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE
    )
    version = searched.group(1) if searched is not None else ""
    if not version:
        raise RuntimeError(
            "project version is not set, could not find '__version__' variable in top-level package."
        )

with open("README.md") as f:
    readme = f.read()

packages = [
    "pcbheart",
]

setup(
    name="pcbheart",
    author="pygame-community",
    url="https://github.com/pygame-community/pcbheart",
    project_urls={
        "Issue tracker": "https://github.com/pygame-community/pcbheart/issues",
    },
    version=version,
    packages=packages,
    license="MIT",
    description=(
        "Another heart of PygameBot, the bot powering the Pygame Community Discord server."
    ),
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=requirements,
    python_requires=">=3.9.0",
    platforms=["any"],
    classifiers=[
        "Topic :: Software Development",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Internet",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
)
