import time
from coppeliasim_zmqremoteapi_client import RemoteAPIClient

from robot.scene import build_scene
from robot.navigation import navigate


def main():
    client = RemoteAPIClient()
    sim = client.require("sim")

    # Stop any running simulation before building the scene
    sim.stopSimulation()
    while sim.getSimulationState() != sim.simulation_stopped:
        time.sleep(0.1)

    robot = build_scene(sim)

    sim.startSimulation()
    navigate(sim, robot)


if __name__ == "__main__":
    main()
