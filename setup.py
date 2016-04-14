import setuptools

VERSION = "0.1.0"

setuptools.setup(
    name="emailer",
    packages=["emailer"],

    version=VERSION,
    download_url="https://github.com/cmeadows/emailer/archive/v%s.zip" % VERSION,
    url="https://github.com/cmeadows/emailer",

    author="Collin Meadows",
    author_email="cmeadows@eborkdev.com",

    description="Python email package to send emails based off of jinja templates",
    long_description=open('README.md').read(),
    license="MIT",
    keywords=["email", "emailer", "jinja", "jinja2"],
    classifiers=[
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",

        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
    ],

    install_requires=[
        "jinja2 >= 2.8"
    ],
)
