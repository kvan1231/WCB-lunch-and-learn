class Santa:
    def __init__(self) -> None:
        self.position = (0, 0)
        self.orientation = (0, 1)

    def turn(self, direction):
        orientations = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        current_orientation_index = orientations.index(self.orientation)
        if direction == "R":
            updated_orientation_index = (current_orientation_index + 1) % len(
                orientations
            )
        elif direction == "L":
            updated_orientation_index = current_orientation_index - 1
        self.orientation = orientations[updated_orientation_index]

    def walk(self, num_blocks):
        self.position = (self.position[0] + (num_blocks * self.orientation[0]),
                         self.position[1] + (num_blocks * self.orientation[1]))

    def follow_instruction(self, instruction):
        instruction = instruction.strip()
        direction = instruction[0]
        num_blocks = int(instruction[1:])

        self.turn(direction)
        self.walk(num_blocks)

    def follow_instructions(self, instructions):
        instruction_list = instructions.split(",")
        for instruction in instruction_list:
            self.follow_instruction(instruction)

    def get_distance_travelled(self):
        return abs(self.position[0]) + abs(self.position[1])


santa = Santa()
santa.follow_instructions("R5, L5, R5, R3")
print(santa.get_distance_travelled())
