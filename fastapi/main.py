from fastapi import FastAPI, HTTPException, Query
from typing import List
from pydantic import BaseModel
import random
import restaurant
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request payload for password generation (Default setting using security best practices)
class Password(BaseModel):
    length: int = 12
    allow_upper: bool = True
    allow_number: bool = True
    allow_special: bool = True

# Response examples
password_responses = {
    200: {
        "description": "Success",
        "content": {
            "application/json": {
                "example": {"password": "U1%cp(C(-J-4", "length": 12},
            }
        },
    },
    422 : {
        "description": "Unprocessable Content",
        "content": {
            "application/json": {
                "examples": {
                    "Password too long": {"value": {"detail": "Password length too long!"}},
                    "Password too short": {"value": {"detail": "Password must contain at least 8 characters!"}},
                    "Input type error": {"value": {"detail": [{"type": "int_parsing","loc": ["body", "length" ], "msg": "Input should be a valid integer, unable to parse string as an integer", 
                                                               "input": "string", "url": "https://errors.pydantic.dev/2.6/v/int_parsing"}]}}
                }
            }
        },
    }
}

# API End Point for password generator
@app.post("/generate-password", responses=password_responses)
def generate_password(password: Password):
    # Error handling for invalid inputs.
    if (password.length < 8):
        raise HTTPException(status_code=422, detail="Password must contain at least 8 characters!")
    if (password.length > 30):
        raise HTTPException(status_code=422, detail="Password length too long!")

    # Characters used in the password
    lower_case = "abcdefghijklmnopqrstuvxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
    numbers = "0123456789"
    special_char = "~`!@#$%^&*()-_+={}[]|;:<>,./?"

    # Always include lower case characters in the password
    pwd = ""
    categories = [lower_case]

    # Optional selection of characters in the password
    if password.allow_upper: categories.append(upper_case)
    if password.allow_number: categories.append(numbers)
    if password.allow_special: categories.append(special_char)
    
    # Generate password based on the character categories, 
    # and ensure each categories appears at least once
    random.shuffle(categories)
    for i in range(len(categories)):
        c = random.choice(categories[i])
        pwd += c

    while len(pwd) < password.length: 
        category = random.choice(categories)
        c = random.choice(category)
        pwd += c

    return {"password": pwd, "length": password.length}


# Custom API endpoint (Recommend restaurants within travel distance from given location)
@app.get("/recommend-restaurant", responses=restaurant.restaurant_responses)
def recommend_restaurant(location: str, mode: restaurant.TravelMode, 
                              time_range: int = Query(default=15, description="minutes"), 
                              categories: List[restaurant.CateringType] = 
                              Query(default="catering.restaurant", 
                                    description="Restaurant categories (multiple selections)")):
    return restaurant.recommend_restaurant(location, mode, time_range, categories)



# TODO: checkbox value / switch between restaurant and password view