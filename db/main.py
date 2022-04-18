import json
from fastapi import FastAPI

app = FastAPI()

@app.on_event("startup")
def load_data():
    global results
    f = open('db.json', encoding="utf8", errors='replace')
    data = json.load(f)
    results = data
    f.close()

@app.on_event("shutdown")
def shutdown_event():
    with open("log.txt", mode="a") as log:
        log.write("Application shutdown")

@app.get("/exercise/{item_idx}")
async def read_item(item_idx):
    res = None
    for sub in results:
        try:
            if int(sub['id']) == int(item_idx):
                res = sub
                break
        except:
            print(sub)
    if res is not None:
        return res
    else:
        return {}

@app.get("/")
def read_root():
    return {'message': 'This is the API for the database '}