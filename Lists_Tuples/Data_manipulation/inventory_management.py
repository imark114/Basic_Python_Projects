# Inventory Management: Build a simple inventory system using lists. Store items and their quantities in a list of tuples. Implement functions to add, remove, and search for items.

def add_item(inventory, iteam, quantity):
    found = False
    for i, (name, qty) in enumerate(inventory):
        if name == iteam:
            inventory[i] = (name, qty + quantity)
            found = True
            break
    if not found:
        inventory.append((iteam, quantity))

def remove_item(inventory, item, quantity=None):

    for i, (name, qty) in enumerate(inventory):
        if name == item:
            if quantity is None or quantity >= qty:
                inventory.pop(i)
            else:
                inventory[i] = (name, qty - quantity)

def search_item(inventory, item):
    for name, qty in inventory:
        if name == item:
            return qty
    return None

inventory = [
  ("apple", 10),
  ("banana", 5),
  ("orange", 8)
]

add_item(inventory, 'apple', 3)
add_item(inventory, 'grape', 8)
remove_item(inventory, 'banana')
print(search_item(inventory, 'banana'))