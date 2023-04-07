from setuptools import setup

setup(
    name="Flask Boilerplate Creator",
    version="0.0.1",
    description="Create boilerplate structure of flask web application",
    author="Harkishan Khuva",
    author_email="hakitechy@gmail.com",
    license="MIT",
    keywords=["fbc", "flask-boilerplate-creator", "flask boilerplate creator"],
    packages=["fbc"],
    package_dir={
        "fbc": "flask-boilerplate-creator"
    },
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/hakiKhuva/flask-boilerplate-creator",
    python_requires=">=3.8"
)