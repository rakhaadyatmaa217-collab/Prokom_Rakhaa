sandwich_orders = ["tuna", "pastrami", "chicken", "vegetarian"]
finished_sandwiches = []
while sandwich_orders:
    current = sandwich_orders.pop()
    print(f"I made your {current} sandwich.")
    finished_sandwiches.append(current)
print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
