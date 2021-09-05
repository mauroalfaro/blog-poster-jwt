# blog-poster-jwt
Basic CRUD api made with Python and FastAPI. And with JWT authentication.

## Description
Basic CRUD api for blog posts made with Python and FastAPI. Secured with authentication using JSON Web Tokens (JWTs). Uses PyJWT to sign, encode, and decode JWT tokens.

## Design
Basic Python/FastAPI application with CRUD endpoints for blog posts and User creation and authentication (login and sign up).
Includes:
- Python/FastAPI
- Uvicorn Server
- Pydantic Schemas
- Pydantic validators (for Email field)
- FastAPI UI to test the app
- Authentication and security for adding posts
- JSON Web Tokens to authenticate Users
- JWT Bearer tokens

## Using the app
If you want to test and deploy the app locally, you should clone this repository, create a virtual environment with venv and install the requirements:
```bash
pip install -r requirements.txt
```

Then, after sourcing your venv environment, you can run the app by executing:
```bash
python app/main.py
```
The application will start on port 8081. You can access to the FastAPI UI on the URL http://localhost:8081/docs#/

This app contains a JWT token handler and a class to handle bearer tokens.

To test the flow correctly, you should test the authentication by trying to visit a protected route without passing in a token, and you will get a 'Not authenticated' error message.

To authenticate yourself with a JWT token, create a new user and copy the generated access token, then click on the authorize button in the top right corner and paste the token. You should now be able to use the protected route.

Users and blog posts created are saved on memory, so everytime you test the app you will have to sign up and authenticate a new user


## Notes
- You can swap out virtualenv and Pip for Poetry or Pipenv.
- If you dont know how to create and source your virtual environment with venv, the commands are the following:
```bash
python3.9 -m venv venv
source venv/bin/activate
```
