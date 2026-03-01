# Written by: Christopher Gholmieh
# Imports:

# Pandas:
import pandas as pd

# Matplotlib:
import matplotlib.pyplot as plt

# Seaborn:
import seaborn as sns

# Variables (Assignment):
# Dataframe:
dataframe = pd.read_csv("expenses_data.csv")

# > Salary:
dataframe["salary"] = dataframe["expense"] + dataframe["disposable_income"]

# Style:
sns.set_theme(style="whitegrid")

# Figure:
plt.figure(figsize=(10, 6))

# Scatter:
sns.scatterplot(
    # Data:
    data=dataframe,

    # X:
    x="salary",

    # Y:
    y="expense",

    # Alpha:
    alpha=0.4
)

sns.regplot(
    data=dataframe,
    x="salary",
    y="expense",
    scatter=False,
    color="red"
)

# X:
plt.xlabel("Salary", fontsize=12)

# Y:
plt.ylabel("Expense", fontsize=12)

# Title:
plt.title("Salary vs Expense", fontsize=14)

# Layout:
plt.tight_layout()

# Show:
plt.show()

########################################################### (Salary vs Disposable Income)
plt.figure(figsize=(10,6))

# Plot:
sns.scatterplot(
    # Data:
    data=dataframe,

    # X:
    x="salary",

    # Y:
    y="disposable_income",

    # Alpha:
    alpha=0.4
)

# Regression:
sns.regplot(
    # Data:
    data=dataframe,

    # X:
    x="salary",

    # Y:
    y="disposable_income",

    # Scatter:
    scatter=False,
    # Color:
    color="red"
)

# X:
plt.xlabel("Salary")

# Y:
plt.ylabel("Disposable Income")

# Title:
plt.title("Salary vs Disposable Income")

# Layout:
plt.tight_layout()

# Show:
plt.show()