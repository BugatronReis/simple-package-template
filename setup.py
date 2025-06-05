# Meu Pacote Python


## Instalação
```bash
pip install package_name


### 3. setup.py (Configuração Essencial)
```python
from setuptools import setup, find_packages

setup(
    name="meu_pacote",
    version="0.1.0",
    author="Fernando Reis",
    description="Um pacote Python de exemplo",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        # Lista de dependências (mesmas do requirements.txt)
        # 'numpy>=1.24.3',
        # 'pandas>=2.0.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
)
