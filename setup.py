from setuptools import setup, find_packages

setup(
    name="vendas-cli",
    version="0.1",
    packages=find_packages(where="."),
    install_requires=[
        "charset-normalizer==3.3.2",
    ],
    entry_points={
        "console_scripts": [
            "vendas-cli=src.main:main",
        ],
    },
    python_requires=">=3.10",
    author="Raphael Amorminio",
    description= "CLI para processamento de arquivos CSV: Lê um CSV e gera um relatório de faturamento.",
)