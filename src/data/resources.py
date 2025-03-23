def load_product_data():
    # Function to load product data from a specified file
    import json
    file_path = "src/data/products.json"
    with open(file_path, 'r') as file:
        return json.load(file)

def load_marketing_descriptions():
    # Function to load marketing descriptions from a specified file
    import json
    file_path = "src/data/marketing_descriptions.json"
    with open(file_path, 'r') as file:
        return json.load(file)

def load_product_faqs():
    # Function to load product FAQs from a specified file
    import json
    file_path = "src/data/product_faqs.json"
    with open(file_path, 'r') as file:
        return json.load(file)

def load_customer_reviews():
    # Function to load customer reviews from a specified file
    import json
    file_path = "src/data/customer_reviews.json"
    with open(file_path, 'r') as file:
        return json.load(file)

def get_product_info(product_id, product_data):
    # Function to retrieve product information by product ID
    return next((product for product in product_data if product['id'] == product_id), None)

def get_all_products(product_data):
    # Function to retrieve all products
    return product_data

def get_marketing_description(product_id, marketing_data):
    # Function to retrieve marketing description by product ID
    return next((desc for desc in marketing_data if desc['product_id'] == product_id), None)