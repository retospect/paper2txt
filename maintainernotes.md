# Maintainer's build notes

```
git commit 
git clean -fdx --dry-run
tox
bumpver update --patch
poetry publish --build --username $PYPI_USERNAME --password $PYPI_PASSWORD
```

gpg sign soon!

## test:
```
pip uninstall -y paper2txt
python -m pip cache purge

pip install paper2txt

pip install --force-reinstall dist/*.whl
```

poetry run paper2txt
