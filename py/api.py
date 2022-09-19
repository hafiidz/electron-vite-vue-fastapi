from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import uvicorn
import sys
import os

# TODO, to make this flexible when Vite change their port#, i.e. auto track port allowed list
origins = [
    "http://localhost",
    "https://localhost",
    "http://localhost:4242",
    "http://localhost:5173",
    "http://127.0.0.1",
    "https://127.0.0.1",
    "http://127.0.0.1:4242",
    "http://127.0.0.1:5173",
    "http://127.0.0.1:80",
    "http://127.0.0.1:8080",
]

with open('pid.txt', 'w') as f:
    f.write(str(os.getpid()))

def setPort():
    p = 4242
    try:
        p = sys.argv[1] 
    except:
        print("error with sys.argv, assigned default port: 4242")   
    return p

app = FastAPI()
port = setPort()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/pid")
def read_root():
    return {"pid": str(os.getpid())}

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=port)