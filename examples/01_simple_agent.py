"""
Example 1: Simple Reactive Agent
=================================
A basic agent that perceives its environment and reacts with predefined rules.
This is the simplest form of an agent — no memory, no planning, just stimulus-response.

Run: python examples/01_simple_agent.py
"""


class SimpleReactiveAgent:
    """A reactive agent that responds to environmental stimuli using condition-action rules."""

    def __init__(self, name: str):
        self.name = name
        self.rules = {}

    def add_rule(self, condition: str, action: str):
        self.rules[condition] = action

    def perceive_and_act(self, environment_state: dict) -> str:
        for condition, action in self.rules.items():
            if condition in environment_state and environment_state[condition]:
                print(f"[{self.name}] Perceived '{condition}' -> Action: '{action}'")
                return action
        print(f"[{self.name}] No matching rule for current state.")
        return "idle"


class Environment:
    """A simple grid environment that agents can observe."""

    def __init__(self):
        self.state = {
            "obstacle_ahead": False,
            "target_visible": False,
            "low_battery": False,
        }

    def update(self, **kwargs):
        self.state.update(kwargs)

    def get_state(self) -> dict:
        return self.state.copy()


if __name__ == "__main__":
    # Create environment
    env = Environment()

    # Create a reactive agent
    robot = SimpleReactiveAgent("Robot-1")
    robot.add_rule("obstacle_ahead", "turn_right")
    robot.add_rule("target_visible", "move_forward")
    robot.add_rule("low_battery", "return_to_base")

    # Scenario 1: Clear path, target visible
    print("=== Scenario 1: Target visible ===")
    env.update(target_visible=True)
    robot.perceive_and_act(env.get_state())

    # Scenario 2: Obstacle ahead
    print("\n=== Scenario 2: Obstacle ahead ===")
    env.update(obstacle_ahead=True, target_visible=False)
    robot.perceive_and_act(env.get_state())

    # Scenario 3: Low battery
    print("\n=== Scenario 3: Low battery ===")
    env.update(obstacle_ahead=False, low_battery=True)
    robot.perceive_and_act(env.get_state())

    # Scenario 4: Nothing happening
    print("\n=== Scenario 4: Idle ===")
    env.update(obstacle_ahead=False, target_visible=False, low_battery=False)
    robot.perceive_and_act(env.get_state())
