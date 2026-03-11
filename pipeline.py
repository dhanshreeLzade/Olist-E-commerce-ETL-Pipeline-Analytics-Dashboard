from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.load import load_data

orders, customers, items, products, category = extract_data()

df = transform_data(orders, customers, items, products, category)

load_data(df)