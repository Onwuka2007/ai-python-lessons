from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World Nigga!"}

@app.get('/posts')
def get_posts():
    return {'data': 'Your Posts are somewhere!'}