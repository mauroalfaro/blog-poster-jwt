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

class UserSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Mauro Alfaro",
                "email": "mauro@alfaro.io",
                "password": "weakpassword"
            }
        }

class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "mauro@alfaro.io",
                "password": "weakpassword"
            }
        }