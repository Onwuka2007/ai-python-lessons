from datetime import datetime
from random import randrange
from typing import Optional
from fastapi import APIRouter, HTTPException, Response, status
from pydantic import BaseModel

router = APIRouter(
    prefix="/posts",
    tags=["Posts"],  # Groups these endpoints nicely in the Swagger UI docs
)


class Post(BaseModel):
    title: str
    content: str
    isPublished: bool = True
    rating: Optional[int | float] = None


my_posts = [
    {
        "title": "About niggas",
        "content": "Some offensive BS",
        "isPublished": False,
        "rating": 2,
        "id": 1,
    },
    {
        "title": "Some other shii",
        "content": "Sometimes in montenegro",
        "rating": 4.3,
        "id": 2,
    },
]

@router.get("/")
def get_posts(limit: int = 10):
    # Slice the list to return only the requested number of posts
    return {
        "message": "Your Posts are somewhere!",
        "total": len(my_posts),
        "data": my_posts[:limit]
    }

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_posts(post: Post):
    post_dict = post.model_dump()
    post_dict["created_at"] = datetime.now()
    post_dict["id"] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"message": "Successfully created!", "data": post_dict}


@router.get("/{id}")
def get_post(id: int):
    post_index = next(
        (index for index, p in enumerate(my_posts) if p["id"] == id), None
    )
    if post_index is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found"
        )
    return {"data": my_posts[post_index]}


@router.put("/{id}")
def update_post(id: int, post: Post):
    post_index = next(
        (index for index, p in enumerate(my_posts) if p["id"] == id), None
    )
    if post_index is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found"
        )

    post_dict = post.model_dump()
    post_dict["id"] = id
    my_posts[post_index] = post_dict
    return {"message": "Successfully updated!", "data": post_dict}


@router.delete("/{id}")
def delete_post(id: int):
    post_index = next(
        (index for index, p in enumerate(my_posts) if p["id"] == id), None
    )
    if post_index is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found"
        )

    my_posts.pop(post_index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
