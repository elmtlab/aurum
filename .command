#build dist
python3 setup.py sdist bdist_wheel 

#upload dist
python3 -m twine upload dist/*     