from fastapi import FastAPI
from routers import posts

app = FastAPI()

# Register the router
app.include_router(posts.router)


@app.get("/")
def read_root():
    return {"message": "Hello World!"}
