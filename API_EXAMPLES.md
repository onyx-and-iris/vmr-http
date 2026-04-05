# API Usage Examples

## Prerequisites

- The FastAPI server must be running (default: http://localhost:8000)

---

## App Router

### */health*

```console
curl -X 'GET' \
  'http://127.0.0.1:8000/health' \
  -H 'accept: application/json'
```

---

## Strip Router

### */strip/{index}*

> Get single parameter

```console
curl -X 'GET' \
  'http://127.0.0.1:8000/strip/0/gain' \
  -H 'accept: application/json'
```

> Set single parameter

```console
curl -X 'PATCH' \
  'http://127.0.0.1:8000/strip/0' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "mute": true,
}'
```

> Set multiple parameters

```console
curl -X 'PATCH' \
  'http://127.0.0.1:8000/strip/0' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "gain": -36.8,
  "mute": true,
  "mono": false,
  "solo": true,
  "A1": true,
  "A2": false,
  "A3": true,
  "B1": false,
  "B2": true,
}'
```

---

## Bus Router

### */bus/{index}*

> Get single parameter

```console
curl -X 'GET' \
  'http://127.0.0.1:8000/bus/1/mono' \
  -H 'accept: application/json'
```

> Set single parameter

```console
curl -X 'PATCH' \
  'http://127.0.0.1:8000/bus/0' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "gain": -32.8,
}'
```

> Set multiple parameters

```console
curl -X 'PATCH' \
  'http://127.0.0.1:8000/bus/0' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "gain": -18.7,
  "mute": false,
  "mono": 1
}'
```

---

## More

For a full list of endpoints and schemas, see the [Swagger UI](http://localhost:8000/docs) or [ReDoc](http://localhost:8000/redoc).
