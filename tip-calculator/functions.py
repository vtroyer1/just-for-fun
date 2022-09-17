import sys
from turtle import speed


def get_user_food_quality_rating():
    food_quality_rating = round(float(input("Rate the quality of the food (1 out of 5 stars): ")), 2)
    return food_quality_rating

def get_user_service_rating():
    service_rating = round(float(input("Rate the customer service (1 out of 5 stars): ")), 2)
    return service_rating

def get_user_speed_rating():
    speed_rating = round(float(input("Rate how quickly your food was served (1 out of 5 stars): ")), 2)
    return speed_rating

def convert_ratings_to_tip_rate(ratings: list, tip_rate_min: float, tip_rate_max: float):
    num_ratings = len(ratings)
    
    rating = 0
    for x in ratings:
        rating += x

    max_rating = num_ratings * 5
    tip_rate = (rating/max_rating) * tip_rate_max

    if tip_rate <= (0.2 * tip_rate_max):
        tip_rate = 0
    elif tip_rate < tip_rate_min:
        tip_rate = tip_rate_min
    else:
        if tip_rate > tip_rate_max:
            tip_rate = tip_rate_max

    return tip_rate

def get_meal_cost():
    meal_cost = round(float(input("Type the subtotal cost of your meal here (do not include tax): ")), 2)
    return meal_cost