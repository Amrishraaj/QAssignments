def list_birds():
    return ["Eagle", "Rooster", "Penguin"]

def describe_bird(bird):
    if bird == "Eagle":
        return "Eagles fly high."
    elif bird == "Rooster":
        return "Roosters wake up early."
    elif bird == "Penguin":
        return "Penguins have good parenting skills."
    else:
        return " bird not found"
