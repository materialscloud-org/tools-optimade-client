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

After a tag/release is created, Github Actions will build and publish the docker image at

```
ghcr.io/materialscloud-org/tools-optimade-client:<tag>
ghcr.io/materialscloud-org/tools-optimade-client:latest
```

The Materials Cloud server will deploy these images to

- https://optimadeclient.dev.materialscloud.io/
- https://optimadeclient.materialscloud.io/

Note, a manual deploy might need to be triggered.

## Contacts

Casper Welzel Andersen, casper.andersen@epfl.ch  
Jusong Yu, jusong.yu@epfl.ch  
Kristjan Eimre, kristjan.eimre@epfl.ch
