#https://packaging.python.org/en/latest/tutorials/packaging-projects/
mkdir building-python-packages
building-python-packages
~/anaconda3/bin/activate
python -m pip install --upgrade pip
touch build.sh
vim build.sh
mkdir packaging_tutorial
cd packaging_tutorial
mkdir src
mkdir example_package_musab
mv example_package_musab src
cd src
ls
cd example_package_musab
ls
touch __init__.py
touch example.py
ls
code ~/building-python-packages/packaging_tutorial
code ~/building-python-packages/
ls
cd ../..
ls
pwd
touch LICENSE pyproject.toml README.md
mkdir tests
ls
python -m pip install --upgrade build
python -m build
ls
ls dist
python -m pip install --upgrade twine
touch ~/.pypirc
vim ~/.pypirc
python -m twine upload --repository testpypi dist/*
ls
cd ..
ls
cd ..
mkdir testing-python-packages
cd testing-python-packages
python -m venv venv
source venv/bin/activate
pip install -i https://test.pypi.org/simple/ example-package-musab==0.0.1
python
ls
