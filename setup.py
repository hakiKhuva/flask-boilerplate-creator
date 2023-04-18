from setuptools import setup

setup(
    name="Flask Boilerplate Creator",
    version="0.0.4",
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
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/hakiKhuva/flask-boilerplate-creator",
    python_requires=">=3.8",
    long_description=open("README.md","r").read(),
    long_description_content_type="text/markdown"
)