"""
Example 3: Cooperative Task Solving
=====================================
Multiple agents cooperate to solve a task — cleaning a grid world.
Each agent is assigned a region and they collectively clean the entire grid.

Run: python examples/03_cooperative_task.py
"""

import random


class GridWorld:
    """A 2D grid world with dirty cells that need cleaning."""

    def __init__(self, width: int, height: int, dirt_ratio: float = 0.4):
        self.width = width
        self.height = height
        self.grid = [
            [random.random() < dirt_ratio for _ in range(width)]
            for _ in range(height)
        ]

    def is_dirty(self, x: int, y: int) -> bool:
        return self.grid[y][x]

    def clean(self, x: int, y: int):
        self.grid[y][x] = False

    def count_dirty(self) -> int:
        return sum(cell for row in self.grid for cell in row)

    def display(self):
        for row in self.grid:
            print(" ".join("X" if cell else "." for cell in row))
        print()


class CleanerAgent:
    """An agent that cleans dirty cells in its assigned region."""

    def __init__(self, name: str, region: list):
        self.name = name
        self.region = region  # List of (x, y) tuples
        self.cells_cleaned = 0

    def clean_region(self, world: GridWorld):
        for x, y in self.region:
            if world.is_dirty(x, y):
                world.clean(x, y)
                self.cells_cleaned += 1
        print(f"  [{self.name}] Cleaned {self.cells_cleaned} cells in assigned region")


def divide_grid(width: int, height: int, num_agents: int) -> list:
    """Divide grid cells among agents as evenly as possible."""
    all_cells = [(x, y) for y in range(height) for x in range(width)]
    random.shuffle(all_cells)
    regions = [[] for _ in range(num_agents)]
    for i, cell in enumerate(all_cells):
        regions[i % num_agents].append(cell)
    return regions


if __name__ == "__main__":
    print("=== Cooperative Grid Cleaning ===\n")

    world = GridWorld(8, 8, dirt_ratio=0.5)
    print("Initial grid (X=dirty, .=clean):")
    world.display()

    dirty_before = world.count_dirty()
    print(f"Dirty cells before: {dirty_before}\n")

    # Create 3 agents with divided regions
    num_agents = 3
    regions = divide_grid(world.width, world.height, num_agents)
    agents = [CleanerAgent(f"Cleaner-{i+1}", regions[i]) for i in range(num_agents)]

    # Each agent cleans its assigned region
    for agent in agents:
        agent.clean_region(world)

    dirty_after = world.count_dirty()
    print(f"\nDirty cells after: {dirty_after}")
    print(f"Total cleaned: {dirty_before - dirty_after}")

    print("\nFinal grid:")
    world.display()
