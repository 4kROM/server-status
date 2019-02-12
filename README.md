# Check Server Status

[![](https://img.shields.io/badge/Python-3.7.x-orange.svg?style=flat-square&logo=python&logoColor=white)](https://www.python.org)

## Intorduction

Endpoints to check server status.

## How to set-up

- clone this repo

- create virtual environment

  - using `conda`
    ```bash
    conda env create -f environment.yml -p .venv
    source activate ./.venv
    ```

  - using `venv`
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install --upgrade --upgrade-strategy=only-if-needed -r requirements.txt
    ```

- run gunicorn
  ```bash
  gunicorn -c gunicorn_config.py app:api
  ```

- hit the endpoints
  ```bash
  curl -X GET localhost:8000/ping
  curl -X GET localhost:8000/_status
  ```

## Maintainer

Akrom Khasani | `akrom (at) volantis (dot) io`

[![](https://img.shields.io/badge/Made%20with%20&hearts;-@VolantisIO-orange.svg?style=flat-square)](https://volantis.io)
