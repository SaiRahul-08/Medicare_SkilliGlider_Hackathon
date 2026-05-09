def validate_input(data):

    for value in data.values():

        if value == "":
            return False

    return True