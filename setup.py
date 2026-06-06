"""Setup script for the Synthetic Medical Imaging Dataset Generator."""

from setuptools import setup, find_packages

setup(
    name="synthetic-med-imaging",
    version="2.0.0",
    description="Multi-modal synthetic medical imaging dataset generator",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Synthetic Med Imaging Team",
    license="Apache-2.0",
    python_requires=">=3.10",
    packages=find_packages(where="."),
    package_dir={"": "."},
    package_data={
        "src": ["conditioning/assets/*.json"],
    },
    entry_points={
        "console_scripts": [
            "synth-med=src.interface.cli:app",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
