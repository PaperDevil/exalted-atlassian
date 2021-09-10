import uvicorn
from app.internal.drivers.fast_api import FastAPIServer

app = FastAPIServer.get_app()


if __name__ == "__main__":
    uvicorn.run("manage:app", host="localhost", port=8080, log_level="info")
