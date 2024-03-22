from typing import Union

from fastapi import FastAPI
import datetime

app = FastAPI()

@app.get("/time")
def time():
    return {"now":"{}".format(datetime.datetime.now().strftime('%H:%M:%S'))}

@app.get("/date")
def date():
    return {"now":"{}".format(datetime.datetime.now().strftime('%Y:%m:%d'))}

