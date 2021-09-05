from pydantic import BaseModel, Field, EmailStr

class PostSchema(BaseModel):
    id: int = Field(default=None)
    title: str = Field(...)
    content: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "title": "Secured FastAPI app with JWT.",
                "content": "This app is secured by authentication using JWT. Uses PyJWT to sign, encode and decode JWT tokens."
            }
        }