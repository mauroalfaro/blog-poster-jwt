from fastapi import FastAPI
from app.model import PostSchema

posts = [
    {
        "id": 1,
        "title": "Blog post number 1",
        "content": "Lorem Ipsum ..."
    }
]

users = []

app = FastAPI()

@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Blog poster root endpoint."}


@app.get("/posts", tags=["posts"])
async def get_posts() -> dict:
    return { "data": posts }


@app.get("/posts/{id}", tags=["posts"])
async def lookup_post(id: int) -> dict:
    if id > len(posts):
        return {
            "error": "No existent post with that Id"
        }

    for post in posts:
        if post["id"] == id:
            return {
                "data": post
            }


@app.post("/posts", tags=["posts"])
async def add_post(post: PostSchema) -> dict:
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {
        "data": "Post added successfully."
    }