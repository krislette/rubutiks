import time
import math

from config.settings import PIONEER_MODEL, WALL_MODEL, FLOOR_MODEL
from config.layout import FLOOR_POSITIONS, ALL_WALLS


def obj_name(base, i):
    # CoppeliaSim names the first instance without brackets, then [1], [2], etc.
    return base if i == 0 else f"{base}[{i}]"


def load_robot(sim):
    sim.loadModel(PIONEER_MODEL)
    time.sleep(0.3)
    robot = sim.getObject("/PioneerP3DX")
    sim.setObjectPosition(robot, [0.0, 0.0, 0.15])
    sim.setObjectOrientation(robot, [0, 0, 0])
    return robot


def load_floors(sim):
    for _ in FLOOR_POSITIONS:
        sim.loadModel(FLOOR_MODEL)
    time.sleep(1.0)

    for i, (fx, fy) in enumerate(FLOOR_POSITIONS):
        try:
            f = sim.getObject(obj_name("/Floor", i))
            sim.setObjectPosition(f, [fx, fy, 0.0])
        except Exception as e:
            print(f"[WARN] Floor {i}: {e}")


def load_walls(sim):
    for _ in ALL_WALLS:
        sim.loadModel(WALL_MODEL)
    time.sleep(1.0)

    for i, (x, y, rot) in enumerate(ALL_WALLS):
        try:
            w = sim.getObject(obj_name("/80cmHighWall100cm", i))
            sim.setObjectPosition(w, [x, y, 0.0])
            sim.setObjectOrientation(w, [0, 0, math.radians(rot)])
        except Exception as e:
            print(f"[WARN] Wall {i}: {e}")


def build_scene(sim):
    robot = load_robot(sim)
    load_floors(sim)
    load_walls(sim)
    print("Scene ready.")
    return robot
