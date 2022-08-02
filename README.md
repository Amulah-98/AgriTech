<h1 align="center">USGS-LIDAR Point Cloud Data</h1>
<div>
<a href="https://github.com/Amulah-98/AgriTech/network/members"><img src="https://img.shields.io/github/forks/Amulah-98/AgriTech" alt="Forks Badge"/></a>
<a href="https://github.com/Amulah-98/AgriTech/pulls"><img src="https://img.shields.io/github/issues-pr/Amulah-98/AgriTech" alt="Pull Requests Badge"/></a>
<a href="https://github.com/Amulah-98/AgriTech/issues"><img src="https://img.shields.io/github/issues/Amulah-98/AgriTech" alt="Issues Badge"/></a>
<a href="https://github.com/Amulah-98/AgriTech/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/Amulah-98/AgriTech?color=2b9348"></a>
<a href="https://github.com/Amulah-98/AgriTech/blob/main/LICENSE"><img src="https://img.shields.io/github/license/Amulah-98/AgriTech?color=2b9348" alt="License Badge"/></a>
</div>

</br>

## Table of Contents

- [Introduction](##Introduction)
- [Project Structure](#project-structure)
  - [data](#data)
  - [notebooks](#notebooks)
  - [scripts](#scripts)
  - [tests](#tests)
  - [logs](#logs)
  - [root folder](#root-folder)
- [Installation guide](#installation-guide)

<hr>

## Introduction

<h3>Overview</h3>

USGS-LIDAR is a project for analyzing how water flows through a maize farm field.<br>

<h3>Business Need</h3>

Produce an easy to use, reliable and well designed python module that domain experts and data scientists
can use to fetch, visualize, and transform publicly available satellite and LIDAR data.
<hr>


## Project Structure

### [images](images):

- `images/` the folder where all snapshot for the project are stored.

### [logs](logs):

- `logs/` the folder where script logs are stored.

### [data](data):

- `data/` the folder where the dataset files are stored.

### [.github](.github):

- `.github/`: the folder where github actions and unit-tests are integrated.

### [.vscode](.vscode):

- `.vscode/`: the folder where local path are stored.

### [notebooks](notebooks):

- `notebooks`: a jupyter notebook for preprocessing the data.

### [scripts](scripts):

- `scripts/`: folder where modules are stored.

### [tests](tests):

- `tests/`: the folder containing unit tests for the scripts.

### root folder

- `requirements.txt`: a text file lsiting the projet's dependancies.
- `.travis.yml`: a configuration file for Travis CI for unit test.
- `setup.py`: a configuration file for installing the scripts as a package.
- `README.md`: Markdown text with a brief explanation of the project and the repository structure.

<hr>

# <a name='Installation guide'></a>Installation guide

### <a name='conda'></a>Conda Enviroment

```bash
conda create --name mlenv python==3.8.1
conda activate mlenv
conda install -c conda-forge pdal python-pdal gdal
conda install geopandas
```

then

```bash
git clone https://github.com/Amulah-98/AgriTech.git
cd AgriTech
sudo python3 setup.py install
```

<hr>

# <a name='license'></a>License

[MIT](https://github.com/Amulah-98/AgriTech/blob/main/LICENSE)
