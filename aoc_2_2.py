import argparse
import pandas as pd
import copy

def intcode(opcode, noun, verb):

    # make a copy of the list so the original isn't changed
    code = copy.deepcopy(opcode) 

    # Restore gravity assist program to the "1202 program alarm" state
    code[1] = noun
    code[2] = verb

    for i in range(0, len(code), 4):

        # 1. add 
        if code[i] == 1:
            code[code[i+3]] = code[code[i+1]] + code[code[i+2]]

        # 2. multiply 
        elif code[i] == 2:
            code[code[i+3]] = code[code[i+1]] * code[code[i+2]]

        # 99. stop 
        elif code[i] == 99:
            # print(f"Value at position 0: {code[0]}")
            return code[0]

        else:
            # print(f"{code[i]} is not a valid code!")
            return None


if __name__ == "__main__":
    """
    "With terminology out of the way, we're ready to proceed. To complete the gravity assist, you need to determine what pair of inputs produces the output 19690720."

    The inputs should still be provided to the program by replacing the values at addresses 1 and 2, just like before. In this program, the value placed in address 1 is called the noun, and the value placed in address 2 is called the verb. Each of the two input values will be between 0 and 99, inclusive.

    Once the program has halted, its output is available at address 0, also just like before. Each time you try a pair of inputs, make sure you first reset the computer's memory to the values in the program (your puzzle input) - in other words, don't reuse memory from a previous attempt.

    Find the input noun and verb that cause the program to produce the output 19690720. What is 100 * noun + verb? (For example, if noun=12 and verb=2, the answer would be 1202.)    """

    parser = argparse.ArgumentParser()
    parser.add_argument('--file', '-f', type=str, help='file used for input for the problem')
    args = parser.parse_args()
    file_name = args.file

    with open(file_name) as f:
        opcode = open(file_name,'r').read().split(',')
        opcode = list(map(int, opcode))

    for noun in range(100):
        for verb in range(100):
            output = intcode(opcode, noun, verb)

            if output == 19690720:
                answer = 100 * noun + verb
                print(f"100 * {noun} + {verb} = {answer}")

                break



