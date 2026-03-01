# Written by: Christopher Gholmieh
# Imports:

# Enumerations:
from enumerations import Education, Race

# Numpy:
import numpy as np

# Enum:
from enum import Enum

# Secrets:
import secrets


# Constants:
BELOW_HIGH_SCHOOL_STANDARD_DEVIATION: float = 2_359.65
BELOW_HIGH_SCHOOL_MEAN: float = 40_357

HIGH_SCHOOL_STANDARD_DEVIATION: float = 1092.54
HIGH_SCHOOL_MEAN: float = 48316

COLLEGE_STANDARD_DEVIATION: float = 1_433.77
COLLEGE_MEAN: float = 89490.0

OTHER_STANDARD_DEVIATION: float = 826.62
OTHER_MEAN: float = 81711

BLACK_STANDARD_DEVIATION: float = 1852.33
BLACK_MEAN: float = 58100


# Functions:
def generate_distributed_expense(mean, standard_deviation, seed=None, quantity=1):
    if not seed:
        seed = secrets.randbits(64)

    # Variables (Assignment):
    # Generator:
    generator = np.random.default_rng(seed)

    # Outputs:
    outputs = generator.normal(loc=mean, scale=standard_deviation, size=quantity)

    # Outputs:
    return outputs


# Functions:
def generate_salary_expenses_information(salary: int) -> dict[str, float]:
    if salary < 15_000:
        return {
            # Deviation:
            "standard-deviation": 1180.54,

            # Mean:
            "mean": 32118.0
        }
    
    if 15_000 <= salary < 29_999:
        return {
            # Deviation:
            "standard-deviation": 1053.56,

            # Mean:
            "mean": 36368.0,
        }
    
    if 30_000 <= salary < 39_999:
        return {
            # Deviation:
            "standard-deviation": 1065.51,

            # Mean:
            "mean": 46246.0,
        }
    
    if 40_000 <= salary < 49_999:
        return {
            # Deviation:
            "standard-deviation": 1290.2,

            # Mean:
            "mean": 50375.0,
        }

    if 50_000 <= salary < 69_999:
        return {
            # Deviation:
            "standard-deviation": 1150.26,

            # Mean:
            "mean": 59378.0
        }

    if 70_000 <= salary < 99_999:
        return {
            # Deviation:
            "standard-deviation": 1241.25,

            # Mean:
            "mean": 71369.0,
        }
    
    if 100_000 <= salary < 149_999:
        return {
            # Deviation:
            "standard-deviation": 1449.19,

            # Mean:
            "mean": 89727.0
        }

    if 150_000 <= salary < 199_999:
        return {
            # Deviation:
            "standard-deviation": 2520.3,

            # Mean:
            "mean": 117378.0,
        }

    if salary >= 200_000:
        return {
            # Deviation:
            "standard-deviation": 2932.82,

            # Mean:
            "mean": 170722.0,
        }

    raise ValueError("[!] Salary is not fitting into any of the categories!")

def salary_level(salary: int) -> str:
    if salary < 15_000:
        return "lt_15000"
    
    if 15_000 <= salary <= 29_999:
        return "15k_lt_salary_lt_29k"
    
    if 30_000 <= salary <= 39_999:
        return "30k_lt_salary_lt_39k"
    
    if 40_000 <= salary <= 49_999:
        return "40k_salary_lt_49k"
    
    if 50_000 <= salary <= 69_999:
        return "50_lt_salary_69k"
    
    if 70_000 <= salary <= 99_999:
        return "70_lt_salary_lt_99k"
    
    if 100_000 <= salary <= 149_999:
        return "100k_salary_149k"
    
    if 150_000 <= salary <= 199_999:
        return "150k_lt_salary_lt_199k"
    
    if salary >= 200_000:
        return "salary_gt_200k"
    
    raise ValueError("[!] Salary is not fitting into any of the categories!")


def calculate_expenses(race: Race, education: Education, salary: int) -> str:
    # Variables (Assignment):
    # Expenses:
    expenses_map: dict[Enum, float] =  {
        # Education:
        Education.HIGH_SCHOOL: generate_distributed_expense(HIGH_SCHOOL_MEAN, HIGH_SCHOOL_STANDARD_DEVIATION, quantity=1).mean(),
        Education.BELOW_HIGH_SCHOOL: generate_distributed_expense(BELOW_HIGH_SCHOOL_MEAN, BELOW_HIGH_SCHOOL_STANDARD_DEVIATION, quantity=1).mean(),
        Education.COLLEGE: generate_distributed_expense(COLLEGE_MEAN, COLLEGE_STANDARD_DEVIATION, quantity=1).mean(),

        # Races:
        Race.BLACK: generate_distributed_expense(BLACK_MEAN, BLACK_STANDARD_DEVIATION, quantity=1).mean(),
        Race.OTHER: generate_distributed_expense(OTHER_MEAN, OTHER_STANDARD_DEVIATION, quantity=1).mean(),
    }

    # Information:
    salary_expenses_information: dict[str, float] = generate_salary_expenses_information(salary)

    # Expenses:
    salary_expenses: float = generate_distributed_expense(
        salary_expenses_information["mean"], salary_expenses_information["standard-deviation"],
        quantity=1
    ).mean()

    # Income:
    expenses: float =  (
        expenses_map[race] +
        expenses_map[education] +
        salary_expenses
    ) / 3

    # Level:
    level: str = salary_level(salary)

    # Income:
    return ",".join([
        ("1" if race == Race.BLACK else "0"),
        ("1" if education == Education.COLLEGE else "0"),
        ("1" if education == Education.HIGH_SCHOOL else "0"),

        ("1" if level == "lt_15000" else "0"),
        ("1" if level == "15k_lt_salary_lt_29k" else "0"),
        ("1" if level ==  "30k_lt_salary_lt_39k" else "0"),
        ("1" if level ==  "40k_salary_lt_49k" else "0"),
        ("1" if level == "50_lt_salary_69k" else "0"),
        ("1" if level == "70_lt_salary_lt_99k" else "0"),
        ("1" if level == "100k_salary_149k" else "0"),
        ("1" if level ==  "150k_lt_salary_lt_199k" else "0"),
        str(expenses)]) + "\n"



# Program:
with open("expenses_data.csv", "w") as file:
    file.write("race_is_black,is_college,is_hs,is_lt_15000,bt_15k_30k,bt_30k_39k,bt_40k_49k,bt_50k_69k,bt_70k_99k,bt_100k_149k,bt_150k_199k,expense\n")

    for race in [Race.BLACK, Race.OTHER]:
        for education in [Education.COLLEGE, Education.HIGH_SCHOOL, Education.BELOW_HIGH_SCHOOL]:
            for iteration in range(1000):
                file.write(calculate_expenses(race, education, 10_000))
                file.write(calculate_expenses(race, education, 20_000))
                file.write(calculate_expenses(race, education, 35_000))
                file.write(calculate_expenses(race, education, 45_000))
                file.write(calculate_expenses(race, education, 60_000))
                file.write(calculate_expenses(race, education, 75_000))
                file.write(calculate_expenses(race, education, 120_000))
                file.write(calculate_expenses(race, education, 180_000))
                file.write(calculate_expenses(race, education, 210_000))
