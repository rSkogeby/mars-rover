from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from models.rover import run_rover_mission, verify_input

app = FastAPI()


origins = [
    "http://localhost",
    "http://0.0.0.0:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )

class Item(BaseModel):
    Input: str

@app.post('/api/input')
def hello(item: Item):
    if verify_input(item.Input) == 1:
        rover_list = run_rover_mission(item.Input)
        return {'response': '\n'.join(rover_list)}
    else:
        return {'response': 'Input needs to be more specific!'}
