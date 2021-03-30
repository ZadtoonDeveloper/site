from fastapi import FastAPI
import uvicorn
from backend.data import Data, Rectangle, Triangle_90
import datetime
app = FastAPI()

@app.get('/')
def root():
    return f"Hello there"
@app.get('/datetime')
def show_time():
    return f"{datetime.now()}"

@app.post('/personal', status_code = 200)
def personal_greetings(data: Data):
    json = data.dict()
    visitor_name = json["name"]
    return f"Hello {visitor_name}"


@app.post('/area-triangle-90', status_code = 200)
def area_triangle_90(data: Triangle_90):
    triangle_params = data.dict();
    return {"area":float(triangle_params['a'] * triangle_params['b'] / 2)}


@app.post('/area-rectangle', status_code = 200)
def area_rectangle(data: Rectangle):
    rectangle_params = data.dict();
    return {"area":float(rectangle_params['a'] * rectangle_params['b'])}


if __name__  == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)

