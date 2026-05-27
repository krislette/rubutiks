# Positions for the 3x3 grid of floor tiles (5m each = 15m x 15m total)
# Center tile is loaded first so Floor[0] sits in the middle
FLOOR_POSITIONS = [
    (0, 0),
    (-5, -5),
    (-5, 0),
    (-5, 5),
    (0, -5),
    (0, 5),
    (5, -5),
    (5, 0),
    (5, 5),
]

# Boundary walls enclose the full 15m x 15m arena.
# The wall model's length runs along Y by default, so:
#   North/South edges need 90° rotation to run along X
#   East/West edges stay at 0°
BOUNDARY_WALLS = (
    [(x, 7.5, 90) for x in range(-7, 8, 1)]  # North
    + [(x, -7.5, 90) for x in range(-7, 8, 1)]  # South
    + [(-7.5, y, 0) for y in range(-7, 8, 1)]  # West
    + [(7.5, y, 0) for y in range(-7, 8, 1)]  # East
)

INNER_WALLS = [
    # Diagonal cross at center
    (2.0, 2.0, 45),
    (-2.0, 2.0, -45),
    (2.0, -2.0, -45),
    (-2.0, -2.0, 45),
    # Cardinal straights
    (0.0, 4.0, 0),
    (0.0, -4.0, 0),
    (4.0, 0.0, 90),
    (-4.0, 0.0, 90),
    # Extra obstacles for more challenging navigation
    (1.0, 0.0, 0),
    (0.0, -1.0, 90),
    (3.0, 3.0, 0),
    (-3.0, 3.0, 90),
    (3.0, -3.0, 90),
    (-3.0, -3.0, 0),
    (5.0, 2.0, 45),
    (-5.0, 2.0, -45),
    (5.0, -2.0, -45),
    (-5.0, -2.0, 45),
    (1.0, 5.0, 90),
    (-1.0, 5.0, 90),
    (1.0, -5.0, 90),
    (-1.0, -5.0, 90),
    (5.0, 5.0, 0),
    (-5.0, 5.0, 0),
    (5.0, -5.0, 0),
    (-5.0, -5.0, 0),
    (3.0, 0.0, 45),
    (-3.0, 0.0, -45),
    (0.0, 3.0, 0),
    (0.0, -3.0, 0),
    (6.0, 4.0, 90),
    (-6.0, 4.0, 90),
    (6.0, -4.0, 0),
    (-6.0, -4.0, 0),
    (4.0, 6.0, 45),
    (-4.0, 6.0, -45),
    (4.0, -6.0, -45),
    (-4.0, -6.0, 45),
]

ALL_WALLS = BOUNDARY_WALLS + INNER_WALLS
