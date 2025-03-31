from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing",
    version="0.0.1",
    author="Karina Kato",
    project_challenge_by="Thiago Alencar",
    description="Image Processing Package using Skimage",
    long_description="https://github.com/thiagoalcr/Projeto_Criando_um_Pacote_de_Processamento_de_Imagens_com_Python/tree/main",
    long_description_content_type="text/markdown",
    url="https://github.com/thiagoalcr/simple-package-template.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
