# Create a dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Print the original dictionary
print("Original dictionary:", person)

# Access a value
print("Name:", person["name"])

# Add a new key-value pair
person["job"] = "Engineer"
print("After adding job:", person)

# Update an existing value
person["age"] = 26
print("After updating age:", person)

# Remove a key
del person["city"]
print("After removing city:", person)

# Check if a key exists
if "name" in person:
    print("Key 'name' exists!")

# Loop through dictionary
print("Key-Value pairs:")
for key, value in person.items():
    print(f"{key} → {value}")
