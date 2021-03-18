from fastapi import FastAPI
import uvicorn
from data import Data
app = FastAPI()

@app.get('/')
def root():
    return f"Hello there"
@app.post('/personal')
def personal_greetings(data: Data):
    json = data.dict()
    visitor_name = json["name"]
    return f"Hello {visitor_name}"

if __name__  == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)

