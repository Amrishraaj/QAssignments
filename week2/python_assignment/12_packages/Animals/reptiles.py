def list_reptiles():
    return ["Lizard", "Crocodile", "Chameleon"]

def describe_reptile(reptile):
    if reptile == "Lizard":
        return "Lizards catch mosquitoes."
    elif reptile == "Crocodile":
        return "Crocodiles are lazy reptiles."
    elif reptile == "Chameleon":
        return "Chameleons change color."
    else:
        return "Unknown reptile"
