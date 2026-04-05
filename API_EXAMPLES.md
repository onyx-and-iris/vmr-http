# API Usage

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

## Strip Gate Router

### */strip/{index}/gate*

> Get single parameter

```console
curl -X 'GET' \
  'http://127.0.0.1:8000/strip/0/gate/knob' \
  -H 'accept: application/json'
```

> Set multiple parameters

```console
curl -X 'PATCH' \
  'http://127.0.0.1:8000/strip/0/gate' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "threshold": -28.7,
  "damping": -60,
  "attack": 2
}'
```

---

## Bus Router

### */bus/{index}*

> Get single parameter

```console
curl -X 'GET' \
  'http://127.0.0.1:8000/bus/0/mono' \
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

## Bus EQ Channel Cell Router

### */bus/{index}/eq/channel/{channel_index}/cell/{cell_index}*

> Get single parameter

```console
curl -X 'GET' \
  'http://127.0.0.1:8000/bus/0/eq/channel/0/cell/0/type' \
  -H 'accept: application/json'
```

> Set single

```console
curl -X 'PATCH' \
  'http://127.0.0.1:8000/bus/0/eq/channel/0/cell/0' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "q": 9.5
}'
```

> Set multiple parameters

```console
curl -X 'PATCH' \
  'http://127.0.0.1:8000/bus/0/eq/channel/0/cell/0' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "on": true,
  "type": 4,
  "f": 538.2,
  "gain": -0.6,
  "q": 9.5
}'
```

---

## More

For a full list of endpoints and schemas, see the [Swagger UI](http://localhost:8000/docs) or [ReDoc](http://localhost:8000/redoc).
