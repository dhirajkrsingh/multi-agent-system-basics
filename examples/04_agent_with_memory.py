"""
Example 4: Agent with Memory
==============================
An agent that remembers past observations and adapts its behavior over time.
This bridges reactive agents and more sophisticated learning agents.

Run: python examples/04_agent_with_memory.py
"""

from collections import deque


class MemoryAgent:
    """An agent that maintains a history of observations and uses them for better decisions."""

    def __init__(self, name: str, memory_size: int = 10):
        self.name = name
        self.memory = deque(maxlen=memory_size)
        self.action_count = {}

    def observe(self, observation: dict):
        self.memory.append(observation)

    def get_trend(self, key: str) -> str:
        values = [obs[key] for obs in self.memory if key in obs]
        if len(values) < 2:
            return "insufficient_data"
        recent_avg = sum(values[-3:]) / min(3, len(values[-3:]))
        older_avg = sum(values[:-3]) / max(1, len(values[:-3])) if len(values) > 3 else recent_avg
        if recent_avg > older_avg * 1.1:
            return "increasing"
        elif recent_avg < older_avg * 0.9:
            return "decreasing"
        return "stable"

    def decide(self) -> str:
        if not self.memory:
            return "explore"

        latest = self.memory[-1]
        temp_trend = self.get_trend("temperature")

        # Decision logic based on current state + trends
        if latest.get("temperature", 20) > 30 and temp_trend == "increasing":
            action = "activate_cooling"
        elif latest.get("temperature", 20) < 15 and temp_trend == "decreasing":
            action = "activate_heating"
        elif latest.get("humidity", 50) > 80:
            action = "activate_dehumidifier"
        else:
            action = "monitor"

        self.action_count[action] = self.action_count.get(action, 0) + 1
        return action

    def report(self):
        print(f"\n  [{self.name}] Memory size: {len(self.memory)}")
        print(f"  [{self.name}] Action history: {dict(self.action_count)}")
        if self.memory:
            print(f"  [{self.name}] Temperature trend: {self.get_trend('temperature')}")
            print(f"  [{self.name}] Last observation: {self.memory[-1]}")


if __name__ == "__main__":
    print("=== Agent with Memory Demo ===\n")

    agent = MemoryAgent("SmartThermostat", memory_size=10)

    # Simulate a sequence of environmental readings
    readings = [
        {"temperature": 22, "humidity": 45},
        {"temperature": 24, "humidity": 50},
        {"temperature": 26, "humidity": 55},
        {"temperature": 28, "humidity": 60},
        {"temperature": 31, "humidity": 65},
        {"temperature": 33, "humidity": 70},
        {"temperature": 34, "humidity": 75},
        {"temperature": 32, "humidity": 82},  # High humidity!
        {"temperature": 29, "humidity": 78},
        {"temperature": 26, "humidity": 70},
        {"temperature": 23, "humidity": 60},
        {"temperature": 20, "humidity": 50},
        {"temperature": 17, "humidity": 45},
        {"temperature": 14, "humidity": 40},
        {"temperature": 12, "humidity": 38},
    ]

    for i, reading in enumerate(readings):
        agent.observe(reading)
        action = agent.decide()
        print(f"  Step {i+1}: Temp={reading['temperature']}C, Humidity={reading['humidity']}% -> Action: {action}")

    agent.report()
