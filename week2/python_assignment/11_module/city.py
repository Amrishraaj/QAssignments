
def get_city_population(city_name):
    if city_name == "Chennai":
        return  11_933_000
    elif city_name == "Bangalore":
        return 13_608_000
    else:
        return None

def is_city_capital(city_name):
    # Check if the city is a capital city
    capitals = ["Chennai", "Bangalore", "Mumbai"]
    return city_name in capitals

def tourist_spot(city_name):
    city_info = {
        "Chennai": "Marina Beach is the longest natural urban beach in India.",
        "Bangalore": "Lalbagh Botanical Garden is a lush green paradise, spread over an area of 240 acres in Bengaluru."
    }
    return city_info.get(city_name, "City not found")
