
### Migrations
migrate
```shell
$ export $(grep -v "^#" .env | xargs)
$ alembic upgrade head
```

make migrations
```shell
$ alembic revision -m "<Some comment about yours migration>" --autogenerate
```