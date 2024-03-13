from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="nebula_realtime_autopilot",
    version="0.0.1-beta",
    packages=find_packages(),
    install_requires=[],
    python_requires=">=3.8",
    author="Subodh Jena",
    author_email="jenasubodh@gmail.com",
    description="Symbl.ai Realtime Autopilot for Nebula",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/subodhjena/nebula_realtime_autopilot",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
    ],
    project_urls={
        "Bug Tracker": "https://github.com/subodhjena/nebula_realtime_autopilot/issues",
    },
)
