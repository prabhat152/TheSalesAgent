def format_response(response):
    return response.strip()

def validate_input(user_input):
    if not user_input:
        raise ValueError("Input cannot be empty.")
    return user_input.strip()

def log_interaction(user_input, response):
    with open("interaction_log.txt", "a") as log_file:
        log_file.write(f"User: {user_input}\nSteve: {response}\n\n")