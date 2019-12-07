import argparse
import pandas as pd

def calculate_fuel(mass, fuel_total=0):
    fuel = int(mass//3 - 2)
    # print(f"fuel = {fuel}")
    # print(f"total = {fuel_total}")
    # print()
    if fuel <= 0:
        return fuel_total
    else:
        fuel_total += fuel
        return calculate_fuel(fuel, fuel_total)


if __name__ == "__main__":
    """
    Fuel itself requires fuel just like a module - take its mass, divide by three, round down, and subtract 2. However, that fuel also requires fuel, and that fuel requires fuel, and so on. Any mass that would require negative fuel should instead be treated as if it requires zero fuel; the remaining mass, if any, is instead handled by wishing really hard, which has no mass and is outside the scope of this calculation.

    So, for each module mass, calculate its fuel and add it to the total. Then, treat the fuel amount you just calculated as the input mass and repeat the process, continuing until a fuel requirement is zero or negative.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('--file', '-f', type=str, help='file used for input for the problem')
    args = parser.parse_args()
    file_name = args.file

    with open(file_name) as f:
        mass = open(file_name,'r').read().split('\n')
        mass = list(map(int, mass))

    df = pd.DataFrame({'mass': mass})
    print(df['mass'])

    df['fuel'] = df['mass'].apply(calculate_fuel)
    print(df)

    fuel_required = df['fuel'].sum()

    print(fuel_required)