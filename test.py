import inventor
inv = inventor.Inventory()
sword = inventor.Item("sword", lambda item: print("Attacked!"), description="Use it to attack")
inv.add_item(sword)
while True:
    action = input("What to do?: ")
    if action == "inventory":
        inv.print_slot()
    for i in inv.slots.get("items"):
        if action == i.name:
            i.use()