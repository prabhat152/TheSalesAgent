class Conversation:
    def __init__(self, steve):
        self.steve = steve
        self.state = "waiting"
        self.history = []
        self.topic = None

    def add_to_history(self, user_input, response):
        self.history.append({"user": user_input, "steve": response})

    def get_history(self):
        return self.history

    def set_topic(self, topic):
        self.topic = topic

    def get_topic(self):
        return self.topic

    def handle_user_input(self, user_input):
        response = self.steve.handle_user_input(user_input, self.topic)  # Pass topic
        self.history.append(f"User: {user_input}")
        self.history.append(f"Steve: {response}")
        self.state = "responding"

        if user_input.lower() in ["thank you, that's all.", "that's all", "goodbye", "bye", "exit", "quit"]:
            self.end_conversation()
        
        return response

    def start_conversation(self):
        return self.steve.start_conversation()

    def end_conversation(self):
        self.state = "ended"