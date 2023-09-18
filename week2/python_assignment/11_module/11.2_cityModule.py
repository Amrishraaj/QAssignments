# main_file

from city import *

city_name = "Chennai"
population = get_city_population(city_name)
is_capital = is_city_capital(city_name)
tourist_Attraction = tourist_spot(city_name)

print(f"City: {city_name}")
print(f"Population: {population} people")
print(f"Is Capital: {'Yes' if is_capital else 'No'}")
print(f"Famous Tourist spot: {tourist_Attraction}")
