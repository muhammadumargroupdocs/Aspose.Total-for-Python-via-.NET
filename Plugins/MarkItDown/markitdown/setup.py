from setuptools import setup, find_packages

setup(
    name="markitdown",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "aspose-cells", "aspose-words", "pillow", "pytesseract"
    ]
)