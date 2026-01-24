from sklearn.datasets import fetch_california_housing
import matplotlib.pyplot as plt

# Load California Housing dataset
housing = fetch_california_housing(as_frame=True)
df = housing.frame

# Create boxplot for Median House Value
plt.figure(figsize=(6, 4))
df["MedHouseVal"].plot(kind="box")
plt.title("California Housing: Median House Value")

# Save the figure
plt.savefig("figs/boxplot.png")
plt.close()
