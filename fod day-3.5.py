import numpy as np
product_sales = {
    'ProductA': 150,
    'ProductB': 200,
    'ProductC': 120,
    'ProductD': 180,
    'ProductE': 250,
    'ProductF': 200,
}

# Calculate frequency distribution
frequency_distribution = {}
for product, sales_count in product_sales.items():
    frequency_distribution[product] = sales_count

# Find the most popular product
most_popular_product = max(frequency_distribution, key=frequency_distribution.get)

# Print the frequency distribution
print("Product Frequency Distribution:")
for product, sales_count in frequency_distribution.items():
    print(f"{product}: {sales_count} times")

# Print the most popular product
print(f"\nThe most popular product is: {most_popular_product} with {frequency_distribution[most_popular_product]} sales.")
