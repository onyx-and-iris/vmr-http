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

## Documentation

For a few examples see [API_EXAMPLES](./API_EXAMPLES.md).

For an exhaustive list of the endpoints FastAPI generates [automatic docs][auto-docs], simply launch the server and then visit:

*Swagger UI*
- http://localhost:8000/docs

*ReDoc*
- http://localhost:8000/redoc

---

## License

`vmr-http` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.

[auto-docs]: https://fastapi.tiangolo.com/features/#automatic-docs
