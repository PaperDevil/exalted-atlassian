### Contributing
Step 1) Add OAuth Consumer and setup service URL (is important) in bitbucket.
Step 2) Get Consumer KEY and SECRET from bitbucket and put it in .env file.
Step 3) Create telegram bot from BotFather and setup bot-token to .env file.


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