<a id="readme-top"></a>

<div align="center">
  <h1>Rogue Navigator</h1>
  <p align="center">
    A reactive autonomous robot navigation system in a simulated obstacle environment
  </p>
</div>

## About The Project

Rogue Navigator implements a behavior-based obstacle avoidance system for a Pioneer P3DX differential-drive robot inside a fully enclosed arena. Built with Python and the CoppeliaSim ZMQ Remote API, the robot navigates a 15m × 15m environment with 32 boundary walls and 38 inner obstacles using a reactive control loop, no map, no sensors, no memory.

The project is inspired by how early game AI works: an agent with no knowledge of its world still needs to keep moving and react to whatever it runs into. The robot detects collisions by monitoring displacement, backs up, picks a random direction, and keeps going.

## Table of Contents

1. [About The Project](#about-the-project)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Simulation Snapshots](#simulation-snapshots)
5. [Setup](#setup)
6. [Project Structure](#project-structure)

## Features

- **Reactive Navigation**: Detects obstacles by tracking displacement per control cycle, no proximity sensors required
- **Randomized Avoidance**: Turn direction and duration are randomized on every obstacle hit to prevent the robot from looping
- **Full Arena Enclosure**: 32 boundary wall sections cover all four edges with no gaps
- **Dense Obstacle Layout**: 38 inner walls placed at varied angles create a challenging navigation environment
- **Modular Codebase**: Scene setup, navigation logic, layout data, and settings are all separated into their own files
- **Programmatic Scene Building**: The entire arena is constructed through the Python API with no manual scene editing in CoppeliaSim

## Technologies Used

| Technology | Purpose |
| --- | --- |
| [Python 3](https://www.python.org/) | Control script language |
| [CoppeliaSim EDU](https://www.coppeliarobotics.com/) | Robot simulation environment |
| [ZMQ Remote API](https://www.coppeliarobotics.com/helpFiles/en/zmqRemoteApiOverview.htm) | Python-to-simulator communication |
| [Pioneer P3DX](https://www.mobile-robots.net/wiki/Pioneer_P3-DX) | Differential-drive robot model |

## Simulation Snapshots

### Arena Overview
<img width="548" height="357" alt="image" src="https://github.com/user-attachments/assets/542d1287-4063-449b-90a8-e278c33ff9a4" />

### Robot Mid-Maneuver
<img width="633" height="406" alt="image" src="https://github.com/user-attachments/assets/b7cfc9fe-6f9d-4367-83d9-a85ca3e32acc" />

## Setup

### Prerequisites

- Python 3.8 or higher
- CoppeliaSim EDU installed on your machine
- ZMQ Remote API client library

### Installation

```bash
git clone https://github.com/krislette/rubutiks.git
cd rubutiks
pip install coppeliasim-zmqremoteapi-client
```

### Run

```bash
# Make sure CoppeliaSim is open before running
python main.py
```

The script will stop any existing simulation, build the scene, and start autonomous navigation. Press `Ctrl+C` to stop.

> **Note**: Model paths in `robot_sim/config/settings.py` point to the default CoppeliaSim EDU installation directory on Windows. Update them if your installation path is different.

## Project Structure

```
rubutiks/
├── robot_sim/
│   ├── scene.py            # Loads and positions the robot, floors, and walls
│   └── navigation.py       # Reactive control loop and obstacle avoidance logic
├── config/
│    ├── settings.py        # Model file paths and speed constants
│    └── layout.py          # Floor tile positions and wall layout data
├── main.py                 # Entry point
├── README.md               # This one this one this one youre reading it rn
└── requirements.txt        # Project requirement package(s) [though just 1 in this case]
```

<p align="right"><a href="#readme-top">Back to top</a></p>
