# Tip Calculator App
import functions as f

meal_cost = f.get_meal_cost()

rating_food_quality = f.get_user_food_quality_rating()
rating_customer_service = f.get_user_service_rating()
rating_speed = f.get_user_speed_rating()

rating_list = []
rating_list.append(rating_food_quality)
rating_list.append(rating_customer_service)
rating_list.append(rating_speed)

min_tip_rate = 0.07
max_tip_rate = 0.2

final_tip_rate = f.convert_ratings_to_tip_rate(rating_list, min_tip_rate, max_tip_rate)
final_tip_dollar = int(round((final_tip_rate * meal_cost), 2))

print("\n" + ("-" * 80))
print(f'With a meal total of ${meal_cost}, I recommend you tip ${final_tip_dollar}. This is about a {final_tip_rate * 100}% tip.\n')
print(("-" * 80) + "\n")