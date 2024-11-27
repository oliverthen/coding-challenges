from setuptools import setup

setup(
    name="cccat",
    version="0.1.0",
    py_modules=["cccat"],
    install_requires=[
        "Click",
    ],
    entry_points={
        "console_scripts": [
            "cccat = cccat:cli",
        ],
    },
)