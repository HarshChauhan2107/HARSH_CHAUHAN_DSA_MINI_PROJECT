# API examples

Base URL: `http://127.0.0.1:5000`

## Create
```bash
curl -X POST http://127.0.0.1:5000/api/records \
  -H "Content-Type: application/json" \
  -d "{\"name\":\"Ada Lovelace\"}"
```

## List
```bash
curl http://127.0.0.1:5000/api/records
```

## Search
```bash
curl http://127.0.0.1:5000/api/records/1
```

## Update
```bash
curl -X PUT http://127.0.0.1:5000/api/records/1 \
  -H "Content-Type: application/json" \
  -d "{\"name\":\"Grace Hopper\"}"
```

## Delete
```bash
curl -X DELETE http://127.0.0.1:5000/api/records/1
```

## Analytics and health
```bash
curl http://127.0.0.1:5000/api/analytics
curl http://127.0.0.1:5000/api/health
```
