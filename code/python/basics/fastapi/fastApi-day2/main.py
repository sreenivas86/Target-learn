from fastapi import FastAPI
app = FastAPI()

@app.get('/')
def helloWorld():
    return {"message":"welcome to FastAPI"}

@app.get('/about')
def about():
    return {
        "framework": "fastapi",
        "language":"python"
    }

@app.get('/hello/{name}')
def hello(name:str):
    return {
        "message":f"hello {name}"
    }

@app.get("/course")
def get_course():
    return {
        "course":"FastApi",
        "duration":"7 days",
        "price": "5000"
    }
