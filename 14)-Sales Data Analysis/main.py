# sales Data analysis --

#  Demo Data
products = ['Mobile', 'Earbuds', 'Charger', 'Power Bank', 'Headphones']
units_sold = [120, 200, 150, 90, 160]
price = [10000, 1500, 800, 1200, 2000]

# Step 1:
total_sales = []
for i in range(len(products)):
    sale = units_sold[i] * price[i]
    total_sales.append(sale)

# Step 2: Total revenue
total_revenue = sum(total_sales)

# Step 3: Average revenue
average_revenue = total_revenue / len(products)

# Step 4: High selling product
max_sale = max(total_sales)
max_index = total_sales.index(max_sale)
best_product = products[max_index]

# Step 5: Output
print("Product-wise Total Sales:")
for i in range(len(products)):
    print(f"{products[i]}: ₹{total_sales[i]}")

print("\nTotal Revenue:", total_revenue)
print("Average Revenue:", round(average_revenue, 2))
print("Highest Selling Product:", best_product, "with sales $",max_sale)
