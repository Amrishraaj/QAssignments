def list_mammals():
    return ["Dog", "Cow", "Tiger"]

def describe_mammal(mammal):
    if mammal == "Dog":
        return "dogs are good pets."
    elif mammal == "Cow":
        return "Cow is Herbivore"
    elif mammal == "Tiger":
        return "Tigers are carnivores"
    else:
        return "No such mammal found"
