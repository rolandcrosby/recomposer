from setuptools import setup

setup(
    name="recomposer",
    version="1.0.0",
    description="use obscure ligatures to shorten strings",
    author="Roland Crosby",
    author_email="roland@rolandcrosby.com",
    url="https://github.com/rolandcrosby/recomposer",
    entry_points={
        "console_scripts": [
            "recomposer = recomposer:main"
        ]
    },
    packages=["recomposer"]
)
