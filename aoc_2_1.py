import argparse
import pandas as pd

if __name__ == "__main__":
    """
    An Intcode program is a list of integers separated by commas (like 1,0,0,3,99). To run one, start by looking at the first integer (called position 0). Here, you will find an opcode - either 1, 2, or 99. The opcode indicates what to do; for example, 99 means that the program is finished and should immediately halt. Encountering an unknown opcode means something went wrong.

    Opcode 1 adds together numbers read from two positions and stores the result in a third position. The three integers immediately after the opcode tell you these three positions - the first two indicate the positions from which you should read the input values, and the third indicates the position at which the output should be stored.

    For example, if your Intcode computer encounters 1,10,20,30, it should read the values at positions 10 and 20, add those values, and then overwrite the value at position 30 with their sum.

    Opcode 2 works exactly like opcode 1, except it multiplies the two inputs instead of adding them. Again, the three integers after the opcode indicate where the inputs and outputs are, not their values.

    Once you're done processing an opcode, move to the next one by stepping forward 4 positions.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('--file', '-f', type=str, help='file used for input for the problem')
    args = parser.parse_args()
    file_name = args.file

    with open(file_name) as f:
        opcode = open(file_name,'r').read().split(',')
        opcode = list(map(int, opcode))


    # Restore gravity assist program to the "1202 program alarm" state
    opcode[1] = 12
    opcode[2] = 2

    for i in range(0, len(opcode), 4):
        # print(opcode)

        # 1. add 
        if opcode[i] == 1:
            opcode[opcode[i+3]] = opcode[opcode[i+1]] + opcode[opcode[i+2]]

        # 2. multiply 
        elif opcode[i] == 2:
            opcode[opcode[i+3]] = opcode[opcode[i+1]] * opcode[opcode[i+2]]

        # 99. stop 
        elif opcode[i] == 99:
            print(f"Value at position 0: {opcode[0]}")

            break

        else:
            print(f"{opcode[i]} is not a valid opcode!")



