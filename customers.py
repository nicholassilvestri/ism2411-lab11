# ISM2411 Lab/Week 11- Customer Dictionary & Lookup
# Name: Nicholas Silvestri

# Reflection Questions
#
# 1. I would use .get() when a dictionary key may not exist, and I want to avoid a KeyError. It allows me to provide a default value if the key is not found. I would use bracket notation when I am certain that the key exists in the dictionary and I want to access its value directly. I typically use .get() for optional information and brackets for required information.
#
#2. Exercise 8 reminds me of Excel PivotTables and SUMIF because it groups data by category and calculates totals. Python is more useful for larger datasets because it can automate calculations, process many records, and repeat the same operations efficiently.


#---Exercise 1: One Customer---
print("\nExercise 1-One Customer")
customer={
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1250
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

print(customer)

#---Exercise 2: Update and Add---

customer["phone"]="813-555-1234"
print(customer)

customer["tier"]="platinum"
print(customer)

del customer["email"]
print(customer)

#---Exercise 3: Safe Lookup---
print("\nExercise 3-Safe Lookup")

email=customer.get("email", "no email on file")
print("Email:", email)

try:
    print(customer["email"])
except KeyError:
    print("KeyError: The email key does not exist.")

#---Exercise 4: Iterate---
print("\nExercise 4-Iterate")
for key, value in customer.items():
    print(f"{key}: {value}")

for key in customer:
    print("Key only",key)

#---Exercise 5: Lookup Table---

tier_discounts={
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}
tier=customer["tier"]
discount=tier_discounts.get(tier, 0)

purchase_price=200
final_price=purchase_price*(1-discount)

print("Tier:", tier)
print("Discount rate:", f"{discount:.0%}")
print("Final price:", f"${final_price:.2f}")

#---Exercise 6: List of Dictionaries---
print("\nExercise 6-List of Dictionaries")

customers=[
    {"name": "Alice", "tier": "platinum"},
    {"name": "Bob", "tier": "silver"},
    {"name": "Charlie", "tier": "bronze"}
]

for person in customers:
    tier=person["tier"]
    discount_rate=tier_discounts.get(tier,0)
    discount_amount=300*discount_rate

    print(
        f"{person['name']} | " 
        f"Tier: {tier} | "
        f"Discount: ${discount_amount:.2f}"
    )

#---Exercise 7: Nested Catalog---
print("\nExercise 7-Nested Catalog")

catalog={
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
    
}

for product, details in catalog.items():
    if details["stock"]<20:
        print(
            f"LOW STOCK: {product} "
            f"(Stock: {details['stock']})"
        )

#---Exercise 8: Sales by Region---
print("\nExercise 8-Sales by Region")

transactions=[
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
    
]

sales_summary={}

for transaction in transactions:
    region=transaction["region"]
    amount=transaction["amount"]

    sales_summary[region]=sales_summary.get(region,0)+amount

for region in sorted(sales_summary):
    print(f"{region}: ${sales_summary[region]:.2f}")