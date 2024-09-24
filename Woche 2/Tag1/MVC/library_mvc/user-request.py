import controller

# Start eines Programms
if __name__ == "__main__":
    user_request = "I want a list of all book titles"

    # Controller muss diesen request aufnehmen
    controller.delegate_request(user_request)
