import argparse
import pandas as pd
import re

if __name__ == "__main__":
    """
	The gravity assist was successful, and you're well on your way to the Venus refuelling station. During the rush back on Earth, the fuel management system wasn't completely installed, so that's next on the priority list.

	Opening the front panel reveals a jumble of wires. Specifically, two wires are connected to a central port and extend outward on a grid. You trace the path each wire takes as it leaves the central port, one wire per line of text (your puzzle input).

	The wires twist and turn, but the two wires occasionally cross paths. To fix the circuit, you need to find the intersection point closest to the central port. Because the wires are on a grid, use the Manhattan distance for this measurement. While the wires do technically cross right at the central port where they both start, this point does not count, nor does a wire count as crossing with itself.
    """

    def find_axes_range(paths):
        """
        returns the largest X and Y value
        """
        x_max, y_max = 0, 0
        for path in paths:
            digits = re.split('(\d+)', path)

            if (digits[0] == 'L') or (digits[0] == 'R'):
                if int(digits[1]) > x_max:
                    x_max = int(digits[1])
            elif (digits[0] == 'U') or (digits[0] == 'D'):
                if int(digits[1]) > y_max:
                    y_max = int(digits[1])

        return x_max, y_max


    def build_circuit(x_max, y_max):
        circuit = [['.' for x in range(x_max)] for y in range(y_max)]

        return circuit

    def print_circuit(circuit):
        for row in circuit:
            print(' '.join([str(elem) for elem in row]))

    parser = argparse.ArgumentParser()
    parser.add_argument('--file', '-f', type=str, help='file used for input for the problem')
    args = parser.parse_args()
    file_name = args.file

    with open(file_name) as f:
        paths = open(file_name,'r').read().split('\n')
        wire_1 = paths[0].split(',')
        wire_2 = paths[1].split(',')

        print(wire_1)
        print()
        print(wire_2)
        paths = list(map(str, paths))

    x_range, y_range = find_axes_range(paths)

    print(f"x_range = {x_range}, y_range = {y_range}")

    circuit = build_circuit(x_range, y_range)
    # print_circuit(circuit)
