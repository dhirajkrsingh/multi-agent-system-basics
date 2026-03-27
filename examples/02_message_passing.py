"""
Example 2: Message Passing Between Agents
==========================================
Two agents communicate through an asynchronous message queue.
Demonstrates the Producer-Consumer pattern common in MAS.

Run: python examples/02_message_passing.py
"""

import queue
import threading
import time
import random


class Message:
    """A structured message exchanged between agents."""

    def __init__(self, sender: str, receiver: str, performative: str, content: str):
        self.sender = sender
        self.receiver = receiver
        self.performative = performative  # e.g., REQUEST, INFORM, CONFIRM
        self.content = content

    def __repr__(self):
        return f"[{self.performative}] {self.sender} -> {self.receiver}: {self.content}"


class MessageBus:
    """A central message bus for agent communication."""

    def __init__(self):
        self.queues = {}

    def register(self, agent_name: str):
        self.queues[agent_name] = queue.Queue()

    def send(self, message: Message):
        if message.receiver in self.queues:
            self.queues[message.receiver].put(message)
            print(f"  [BUS] Delivered: {message}")

    def receive(self, agent_name: str, timeout: float = 1.0):
        try:
            return self.queues[agent_name].get(timeout=timeout)
        except queue.Empty:
            return None


class SensorAgent:
    """An agent that senses the environment and sends data to the processor."""

    def __init__(self, name: str, bus: MessageBus):
        self.name = name
        self.bus = bus
        self.bus.register(name)

    def run(self, num_readings: int = 5):
        for i in range(num_readings):
            temperature = round(random.uniform(18.0, 35.0), 1)
            msg = Message(
                sender=self.name,
                receiver="Processor",
                performative="INFORM",
                content=f"temperature={temperature}",
            )
            self.bus.send(msg)
            time.sleep(0.5)


class ProcessorAgent:
    """An agent that receives sensor data and processes it."""

    def __init__(self, name: str, bus: MessageBus):
        self.name = name
        self.bus = bus
        self.bus.register(name)
        self.readings = []

    def run(self, expected_messages: int = 5):
        received = 0
        while received < expected_messages:
            msg = self.bus.receive(self.name, timeout=2.0)
            if msg:
                value = float(msg.content.split("=")[1])
                self.readings.append(value)
                received += 1
                status = "HIGH" if value > 30 else "NORMAL"
                print(f"  [{self.name}] Processed: {value}C -> Status: {status}")

        avg = sum(self.readings) / len(self.readings)
        print(f"\n  [{self.name}] Average temperature: {avg:.1f}C over {len(self.readings)} readings")


if __name__ == "__main__":
    bus = MessageBus()

    sensor = SensorAgent("Sensor-1", bus)
    processor = ProcessorAgent("Processor", bus)

    print("=== Multi-Agent Message Passing Demo ===\n")

    # Run agents in separate threads
    sensor_thread = threading.Thread(target=sensor.run, args=(5,))
    processor_thread = threading.Thread(target=processor.run, args=(5,))

    sensor_thread.start()
    processor_thread.start()

    sensor_thread.join()
    processor_thread.join()

    print("\n=== Done ===")
