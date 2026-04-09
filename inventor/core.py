class Item:
    def __init__(self, name:str,func,description:str="No description"):
        self.name = name
        self.func = func
        self.description = description
    def use(self):
        self.func(self)

class Inventory:
    def __init__(self):
        self.slots = {
            "items":[],
        }
        self.extra = {
            "items":{},
        }
        self.full_inv_message = "Your inventory is full"
    def add_item(self, item,slot:str="items"):
        if not self.extra[slot].get("capacity"):
            if self.slots.get(slot) is not None:
                self.slots[slot].append(item)
            else:
                print("No slot found")
        else:
            if self.extra[slot]["capacity"] < len(self.slots.get(slot)):
                if self.slots.get(slot) is not None:
                    self.slots[slot].append(item)
                else:
                    print("No slot found")
            else:
                print(self.full_inv_message)

    def remove_item(self, item,slot:str="items"):
        if self.slots.get(slot) is not None:
            self.slots[slot].remove(item)
        else:
            print("No slot found")
    def clear(self):
        for i in self.slots:
            self.slots[i] = []
    def create_slot(self,name:str):
        self.slots[name] = []
        self.extra[name] = {}
    def print_slot(self,slot:str="items",message:str="Your inventory"):
        print(message)
        for i in self.slots.get(slot):
            print(f"{i.name}: {i.description}")
    def set_capacity(self,capacity:int=10,slot:str="items",message:str="Your inventory is full"):
        self.extra[slot]["capacity"] = capacity
        self.full_inv_message = message

