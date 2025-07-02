# OPTIMADE Client

An OPTIMADE Client as a Materials Cloud tool.

It runs a Jupyter notebook in Voilà with the [Materials Cloud Voilà template](https://github.com/materialscloud-org/voila-materialscloud-template).

## Run locally

```bash
pip install -e .
voila --Voila.config_file_paths=./ OPTIMADE-Client.ipynb
```

For development:

```bash
pip install -e .[dev]
pre-commit install
```

## Deploy to Materials Cloud

To build and publish latest Docker images:

- update version in `setup.py`, commit and push;
- create and push a new tag:

```
git tag YYYY.MM.DD
git push --tags
```

this will start a Github actions workflow that builds and pushes the latest Docker image to

```
ghcr.io/materialscloud-org/tools-optimade-client:YYYY.MM.DD
ghcr.io/materialscloud-org/tools-optimade-client:latest
```

The Materials Cloud server will deploy these images to

- https://optimadeclient.dev.materialscloud.io/
- https://optimadeclient.materialscloud.io/

(A manual deploy might need to be triggered.)

## Contacts

Casper Welzel Andersen, casper.andersen@epfl.ch  
Jusong Yu, jusong.yu@epfl.ch  
Kristjan Eimre, kristjan.eimre@epfl.ch
