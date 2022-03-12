import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="Archibald",
    version="0.2",
    description="A command line tool for inspecting archimate files",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/MrRubberneck/archibald",
    author="",
    author_email="info@realpython.com",
    license="Apache 2.0",
    classifiers=[],
    packages=["archibald"],
    include_package_data=True,
    install_requires=["click, console-menu, lxml"],
    entry_points={},
)
