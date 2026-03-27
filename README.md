# Multi-Agent System Basics

> **A comprehensive introduction to Multi-Agent Systems (MAS) for AI practitioners and learners.**

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://python.org)
[![Level](https://img.shields.io/badge/Level-Beginner-2E8B57)](#)
[![Track](https://img.shields.io/badge/Track-Agent%20Systems-0A7EA4)](#)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

## What is a Multi-Agent System?

A **Multi-Agent System (MAS)** is a system composed of multiple interacting intelligent agents. Each agent is an autonomous entity that observes and acts upon an environment, directing its activity towards achieving goals.

```
┌──────────────────────────────────────────────┐
│              ENVIRONMENT                      │
│                                               │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐      │
│  │ Agent A  │◄►│ Agent B  │◄►│ Agent C  │     │
│  │ (Sensor) │  │(Planner) │  │(Executor)│     │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘    │
│       │              │              │          │
│       ▼              ▼              ▼          │
│   ┌──────────────────────────────────────┐    │
│   │         Shared Knowledge Base         │    │
│   └──────────────────────────────────────┘    │
└──────────────────────────────────────────────┘
```

## What You Will Learn

By the end of this repository, you should be able to:

- explain what an agent is and what makes a system multi-agent
- recognize the core interaction patterns between agents and environments
- understand the difference between communication, coordination, cooperation, and competition
- use this repository as the first step into the broader agent systems track

## Prerequisites

This repository is designed as the beginner entry point for the agent track.

Helpful background:

- basic Python familiarity
- comfort running small example scripts
- curiosity about how multiple agents interact to solve problems

## Where This Fits In The Learning Path

Use this repository first, then continue with:

- [agent-communication-protocols](https://github.com/dhirajkrsingh/agent-communication-protocols) for agent messaging patterns
- [agent-architecture-patterns](https://github.com/dhirajkrsingh/agent-architecture-patterns) for reactive, BDI, and utility-driven designs
- [distributed-agent-coordination](https://github.com/dhirajkrsingh/distributed-agent-coordination) once you want more advanced coordination mechanisms

## Table of Contents

- [Key Concepts](#key-concepts)
- [Examples](#examples)
- [Best Practices](#best-practices)
- [Getting Started](#getting-started)
- [References & Top Repos](#references--top-repos)

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Agent** | An autonomous entity that perceives its environment and takes actions |
| **Environment** | The world in which agents operate and interact |
| **Communication** | How agents exchange information (messages, signals, shared memory) |
| **Coordination** | How agents organize their actions to achieve common goals |
| **Cooperation** | Agents working together towards a shared objective |
| **Competition** | Agents pursuing conflicting goals |
| **Emergent Behavior** | Complex system-level behavior arising from simple agent interactions |

## Examples

### 1. Simple Reactive Agent
See [`examples/01_simple_agent.py`](examples/01_simple_agent.py) — A basic agent that reacts to environmental stimuli.

### 2. Multi-Agent Communication
See [`examples/02_message_passing.py`](examples/02_message_passing.py) — Two agents communicating via message passing.

### 3. Cooperative Task Solving
See [`examples/03_cooperative_task.py`](examples/03_cooperative_task.py) — Multiple agents collaborating to solve a task.

### 4. Agent with Memory
See [`examples/04_agent_with_memory.py`](examples/04_agent_with_memory.py) — An agent that learns from past interactions.

## Best Practices

1. **Single Responsibility** — Each agent should have one clear purpose
2. **Loose Coupling** — Agents should communicate through well-defined interfaces
3. **Fault Tolerance** — Design agents to handle failures of other agents gracefully
4. **Scalability** — System should work whether there are 2 or 200 agents
5. **Observability** — Log agent decisions and communications for debugging
6. **Idempotent Messages** — Messages should be safe to process more than once

## Getting Started

```bash
git clone https://github.com/dhirajkrsingh/multi-agent-system-basics.git
cd multi-agent-system-basics
pip install -r requirements.txt
python examples/01_simple_agent.py
```

## References & Top Repos

| Resource | Description |
|----------|-------------|
| [microsoft/autogen](https://github.com/microsoft/autogen) | Multi-agent conversation framework by Microsoft |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | Build stateful multi-agent applications |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | Framework for orchestrating role-playing agents |
| [camel-ai/camel](https://github.com/camel-ai/camel) | Communicative Agents for Mind Exploration |
| [Wooldridge - Intro to MAS](https://www.cs.ox.ac.uk/people/michael.wooldridge/pubs/imas/IMAS2e.html) | Classic textbook on Multi-Agent Systems |

## Author

Dhiraj Singh

## Usage Notice

This repository is shared publicly for learning and reference.
It is made available for everyone through [VAIU Research Lab](https://vaiu.ai/Research_Lab).
For reuse, redistribution, adaptation, or collaboration, contact Dhiraj Singh / [VAIU Research Lab](https://vaiu.ai/Research_Lab).
