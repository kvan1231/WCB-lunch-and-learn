"""

Solve advent of code 2016/12/1 puzzle

"""

# Read in input

steps_input = "R5, L5, R5, R3"
print(steps_input)

# Split input into a sequence on instructions

steps_list = steps_input.split(",")
print(steps_list)

# Set starting position

position = (0, 0)

# Set starting orientation

orientation = (0, 1)
orientations = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# For each instruction, update orientation and position

for step in steps_list:
    # update orientation
    clean_step = step.strip()
    turn_direction = clean_step[0]
    current_orientation_index = orientations.index(orientation)
    if turn_direction == "R":
        updated_orientation_index = (current_orientation_index + 1) % len(
            orientations
        )
    elif turn_direction == "L":
        updated_orientation_index = current_orientation_index - 1
    orientation = orientations[updated_orientation_index]

    # update position
    num_blocks = int(clean_step[1:])
    position = (position[0] + (num_blocks * orientation[0]),
                position[1] + (num_blocks * orientation[1]))
# Return sum of absolute coordinates
print(abs(position[0]) + abs(position[1]))
