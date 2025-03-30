import random
import pandas as pd
from faker import Faker
import os

# Initialize Faker instance
fake = Faker()

# Configuration for dataset size
num_customers = 50000  # Number of customers
num_stores = 60  # Number of stores
num_products = 400  # Number of products
num_transactions = 500000  # Number of transactions
num_reviews = 100000  # Number of reviews

# -----------------------------------------
# Create output directory if it doesn't exist
output_dir = "data_output/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# -----------------------------------------
# Generate Customer Data
# -----------------------------------------
customers = []
for _ in range(num_customers):
    customers.append({
        "cust_id": fake.uuid4(),
        "cust_name": fake.name(),
        "cust_email": fake.email(),
        "signup_date": fake.date_this_decade(),
        "cust_location": fake.city(),
        "cust_gender": random.choice(["M", "F"]),
        "cust_age": random.randint(18, 65)
    })

customer_df = pd.DataFrame(customers)

# -----------------------------------------
# Generate Store Data
# -----------------------------------------
stores = []
for _ in range(num_stores):
    stores.append({
        "store_id": fake.uuid4(),
        "store_name": fake.company(),
        "store_location": fake.city()
    })

store_df = pd.DataFrame(stores)

# -----------------------------------------
# Generate Product Data
# -----------------------------------------
products = []
for _ in range(num_products):
    products.append({
        "prod_id": fake.uuid4(),
        "prod_name": fake.word(),
        "prod_category": random.choice(["Electronics", "Clothing", "Grocery", "Furniture"]),
        "prod_price": round(random.uniform(10, 1000), 2)
    })

product_df = pd.DataFrame(products)

# -----------------------------------------
# Generate Transaction Data
# -----------------------------------------
transactions = []
for _ in range(num_transactions):
    transactions.append({
        "trans_id": fake.uuid4(),
        "cust_id": random.choice(customer_df['cust_id']),
        "trans_date": fake.date_this_year(),
        "trans_amt": round(random.uniform(20, 5000), 2),
        "store_id": random.choice(store_df['store_id']),
        "prod_id": random.choice(product_df['prod_id'])
    })

transaction_df = pd.DataFrame(transactions)

# -----------------------------------------
# Generate Review Data
# -----------------------------------------
reviews = []
for _ in range(num_reviews):
    reviews.append({
        "review_id": fake.uuid4(),
        "cust_id": random.choice(customer_df['cust_id']),
        "prod_id": random.choice(product_df['prod_id']),
        "review_rating": random.randint(1, 5),
        "review_text": fake.sentence(),
        "trans_id": random.choice(transaction_df['trans_id'])
    })

review_df = pd.DataFrame(reviews)

# -----------------------------------------
# Generate Store Stock Data
# -----------------------------------------
store_stock = []
for _ in range(num_products * num_stores):
    store_stock.append({
        "prod_id": random.choice(product_df['prod_id']),
        "store_id": random.choice(store_df['store_id']),
        "stock_quantity": random.randint(0, 100)
    })

store_stock_df = pd.DataFrame(store_stock)

# -----------------------------------------
# Save data to CSV files in data_output/
# -----------------------------------------
customer_df.to_csv(f"{output_dir}customers.csv", index=False)
store_df.to_csv(f"{output_dir}stores.csv", index=False)
product_df.to_csv(f"{output_dir}products.csv", index=False)
transaction_df.to_csv(f"{output_dir}transactions.csv", index=False)
review_df.to_csv(f"{output_dir}reviews.csv", index=False)
store_stock_df.to_csv(f"{output_dir}store_stock.csv", index=False)

print("✅ Datasets generated successfully and saved in 'data_output/' folder! 🎉")
