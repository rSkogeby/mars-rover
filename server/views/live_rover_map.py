from fastapi import FastAPI

app = FastAPI()

class Item(BaseModel):
    Input: str

@app.post('/api/input')
def hello(item: Item):
    print(item.Input)
    return(item.Input)
