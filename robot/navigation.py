import time
import math
import random

from config.settings import FORWARD_SPEED, TURN_SPEED


def get_pos(sim, robot):
    p = sim.getObjectPosition(robot, -1)
    return p[0], p[1]


def navigate(sim, robot):
    lm = sim.getObject("/PioneerP3DX/leftMotor")
    rm = sim.getObject("/PioneerP3DX/rightMotor")

    prev_pos = get_pos(sim, robot)
    turning = 0

    print("Autonomous navigation started...")

    try:
        while True:
            cur_pos = get_pos(sim, robot)
            moved = math.dist(cur_pos, prev_pos)
            prev_pos = cur_pos

            if turning > 0:
                turning -= 1

            elif moved < 0.001:
                # Obstacle detected: back up then turn in a random direction
                sim.setJointTargetVelocity(lm, -FORWARD_SPEED)
                sim.setJointTargetVelocity(rm, -FORWARD_SPEED)
                sim.setJointTargetForce(lm, 100)  # increase motor torque too
                sim.setJointTargetForce(rm, 100)
                time.sleep(0.8)

                turning = random.randint(30, 50)
                direction = 1 if random.random() > 0.5 else -1
                sim.setJointTargetVelocity(lm, direction * TURN_SPEED)
                sim.setJointTargetVelocity(rm, -direction * TURN_SPEED)
                print(
                    f"Obstacle detected — backing up then turning {'right' if direction > 0 else 'left'}"
                )

            else:
                sim.setJointTargetVelocity(lm, FORWARD_SPEED)
                sim.setJointTargetVelocity(rm, FORWARD_SPEED)

            time.sleep(0.05)

    except KeyboardInterrupt:
        sim.setJointTargetVelocity(lm, 0)
        sim.setJointTargetVelocity(rm, 0)
        sim.stopSimulation()
        print("Simulation stopped.")
