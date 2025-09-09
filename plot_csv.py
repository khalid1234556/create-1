import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file (fix path with raw string or double backslashes)
df = pd.read_csv(r'C:\Users\khbra\Downloads\project\khalid\diabetes.csv')

# Check the column names to plot correctly
print(df.columns)  # Helps you see what actual column names are

# Example: if the CSV has columns like 'Glucose' and 'Insulin'
# Replace 'x' and 'y' with real column names from your CSV
plt.plot(df['Glucose'], df['Insulin'], marker='o')

plt.title('Line Chart from CSV')
plt.xlabel('Glucose')
plt.ylabel('Insulin')
plt.grid(True)
plt.show()



