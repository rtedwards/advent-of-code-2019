import argparse
import pandas as pd

def calculate_fuel(mass):
    return int(mass//3 - 2)


if __name__ == "__main__":
    """
    The Elves quickly load you into a spacecraft and prepare to launch.

    At the first Go / No Go poll, every Elf is Go until the Fuel Counter-Upper. They haven't determined the amount of fuel required yet.

    Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('--file', '-f', type=str, help='file used for input for the problem')
    args = parser.parse_args()
    file_name = args.file

    with open(file_name) as f:
        mass = open(file_name,'r').read().split('\n')
        mass = list(map(int, mass))

    df = pd.DataFrame({'mass': mass})

    df['fuel'] = df['mass'].apply(calculate_fuel)

    fuel_required = df['fuel'].sum()

    print(fuel_required)
