import controller

# Start eines Programms
if __name__ == "__main__":
    user_request = "I want a banana"

    # Controller muss diesen request aufnehmen
    controller.delegate_request(user_request)
