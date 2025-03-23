class Steve:
    def __init__(self, llm_integration):
        self.llm_integration = llm_integration
        self.product_data = self.load_product_data()
        self.marketing_data = self.load_marketing_descriptions()
        self.product_faqs = self.load_product_faqs()
        self.customer_reviews = self.load_customer_reviews()

    def load_product_data(self):
        from src.data.resources import load_product_data
        return load_product_data()

    def load_marketing_descriptions(self):
        from src.data.resources import load_marketing_descriptions
        return load_marketing_descriptions()
    
    def load_product_faqs(self):
        from src.data.resources import load_product_faqs
        return load_product_faqs()

    def load_customer_reviews(self):
        from src.data.resources import load_customer_reviews
        return load_customer_reviews()

    def recommend_product(self, user_query):
        # Logic to recommend a product based on user query
        product = None
        if "iPhone" in user_query:
            product = next((p for p in self.product_data if "iPhone" in p["name"]), None)
        elif "MacBook" in user_query:
            product = next((p for p in self.product_data if "MacBook" in p["name"]), None)
        elif "iPad" in user_query:
            product = next((p for p in self.product_data if "iPad" in p["name"]), None)
        elif "AirPods" in user_query:
            product = next((p for p in self.product_data if "AirPods" in p["name"]), None)
        elif "Mac Mini" in user_query or "MacMini" in user_query:
            product = next((p for p in self.product_data if "Mac Mini" in p["name"]), None)

        if product:
            marketing_desc = next((m for m in self.marketing_data if m["product_id"] == product["id"]), None)
            if marketing_desc:
                return marketing_desc["description"]
            else:
                return product["description"]
        else:
            return self.llm_integration.generate_response(user_query)

    def answer_question(self, question):
        # Logic to answer user questions
        product_id = None
        if "iPhone" in question:
            product_id = "iphone15"
        elif "MacBook" in question:
            product_id = "macbookair"
        elif "Apple Watch" in question:
            product_id = "applewatch9"
        elif "iPad" in question:
            product_id = "ipadpro"
        elif "AirPods" in question:
            product_id = "airpodsmax"
        elif "Mac Mini" in question or "MacMini" in question:
            product_id = "macmini"

        if product_id:
            faqs = next((f for f in self.product_faqs if product_id == f["product_id"]), None)
            if faqs and faqs["faqs"]:
                return faqs["faqs"][0]["answer"]
            else:
                return self.llm_integration.generate_response(question)
        else:
            return self.llm_integration.generate_response(question)

    def start_conversation(self):
        # Logic to initiate a conversation with the user
        greeting = "Hello! I'm Steve, your Apple product sales assistant. How can I help you today?"
        return greeting

    def handle_user_input(self, user_input, topic=None):
        # Logic to handle user input and provide appropriate responses
        prompt = f"User: {user_input}\nSteve:"
        response = self.llm_integration.generate_response(prompt)
        return response

    def interact_with_llm(self, user_input):
        prompt = f"User: {user_input}\nSteve:"
        response = self.llm_integration.generate_response(prompt)
        return response