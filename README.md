# inventor

[![Discord](https://img.shields.io/discord/1488880281376260186?color=7289da&label=discord&logo=discord&logoColor=white)](https://discord.gg/MXv3KTFmPE)

A simple library for creating inventory for games.

## Installation

```bash
pip install inventor
```

## Quick Start

```python
import chronolight

# Timeline
tl = chronolight.Timeline()
tl.wait(1)
tl.call(lambda: print("1 second passed"))
tl.wait(0.5)
tl.call(lambda: print("Another 0.5 seconds passed"))
tl.run()

# Delayed call
chronolight.delay(2, lambda: print("After 2 seconds"))
```