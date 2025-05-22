from setuptools import setup, find_packages

setup(
    name="gerador_docs",
    version="0.1.6",
    description="Programa auxiliar para gerar documentos para a emissão de CAF e Declarações de Agricultor",
    author="Erik Marques",
    author_email="lucro.alternativo@outlook.com",
    packages=find_packages(),
    install_requires=[
        # Adicione aqui as dependências do seu projeto, por exemplo:
        # "pandas>=1.0.0",
        # "openpyxl",
    ],
    python_requires=">=3.8",
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)