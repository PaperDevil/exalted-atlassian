### Environment (.env)
```shell
DEBUG=bool
TITLE_API="Some Title for swagger API"
VERSION_API=0.1

TELEGRAM_TOKEN="<Token from BotFather>"
CHANNEL_ID="ID's notifications channel" # properly removed
HTTPS_HOST_ADDRESS="host address of bot api"
TELEGRAM_BOT_ADDRESS=https://t.me/exalted_atlassian_bot

DB_NAME=<DB_NAME>
DB_USER=<DB_USER>
DB_PASSWORD=<DB_PASSWORD>
DB_HOST=<DB_HOST>
DB_PORT=5432

OAUTH_CONSUMER_KEY="consumer key from bitbucket"
OAUTH_CONSUMER_SECRET="consumer secret from bitbucket"
```

### Contributing
Step 1) Add OAuth Consumer and setup service URL (is important) in bitbucket. <br>
Step 2) Get Consumer KEY and SECRET from bitbucket and put it in .env file. <br>
Step 3) Create telegram bot from BotFather and setup bot-token to .env file. <br>


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