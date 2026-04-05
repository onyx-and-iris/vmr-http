# Voicemeeter HTTP

[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

---

## Install

```console
pip install vmr-http
```

## Run

```console
uvicorn vmr_http:app
```

## Use

*Set multiple Strip 0 parameters at once*

```bash
curl -X 'PATCH' \
  'http://127.0.0.1:8000/strip/0' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "gain": -38.7,
  "mute": true,
  "mono": true,
  "A1": true,
  "A2": false,
  "A5": true,
  "B1": true,
  "B3": true
}'
```

*Set Strip 1 mute*

```bash
curl -X 'PATCH' \
  'http://127.0.0.1:8000/strip/1' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "mute": true,
}'
```

*Get Bus 3 gain*

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/bus/3/gain' \
  -H 'accept: application/json'
```

*Get Bus 4 Mode*

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/bus/4/mode' \
  -H 'accept: application/json'
```

*Set Bus 2 Mode*

```bash
curl -X 'PATCH' \
  'http://127.0.0.1:8000/bus/2/mode' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "mode": "Composite"
}'
```

*Healthcheck*

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/health' \
  -H 'accept: application/json'
```

## Documentation

FastAPI [generates automatic docs][auto-docs], visit the link in the startup message when you launch the server.

[auto-docs]: https://fastapi.tiangolo.com/features/#automatic-docs
