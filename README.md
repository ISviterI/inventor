# inventor

[![Discord](https://img.shields.io/discord/1488880281376260186?color=7289da&label=discord&logo=discord&logoColor=white)](https://discord.gg/MXv3KTFmPE)

A simple library for creating inventory for games.

## Installation

```bash
pip install inventor
```

## Quick Start

```python
import inventor
inv = inventor.Inventory()
sword = inventor.Item("sword", lambda item: print("Attacked!"), description="Use it to attack")
inv.add_item(sword)
while True:
    action = input("What to do?: ")
    if action == "inventory":
        inv.print_slot(message="Here's ur inventory:")
    for i in inv.slots.get("items"):
        if action == i.name:
            i.use()
```