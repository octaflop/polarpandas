---
marp: true
theme: default
paginate: true
---

# Pandas vs Polars: Data Analysis Showdown 🐼🆚🐻‍❄️
## Exploring Dataframes in Python

![w:300 h:300](../polarpandas_github_repo_qr.png)

---

# Welcome to the Data Jungle! 🌴📊

- Hands-on workshop with real-world datasets
- Explore personal data (social media, finance, etc.) Whatever you BYOD
- Master dataframe operations
- Discover the speed of Polars

![bg right:40% 80%](./imgs/duelbear.png)

---

# What's a Dataframe? 🤔

- 2D labeled data structure
- Columns of potentially different types
- Like a spreadsheet or SQL table

```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Paris', 'Tokyo']
})
print(df)
```

---

# Pandas: The Versatile Dataframe 🐼

![w:300 h:200](https://api.placeholder.com/300x200?text=Pandas+Logo)

- Python's popular library for data manipulation
- Great for exploration and data preprocessing
- Intuitive API with powerful features

```python
# From our code: Basic Pandas operations
console.print(df.head().to_string())
df.info()
console.print(df.describe().to_string())
```

---

# Real-world Example: Customer Analysis 🛍️

Imagine you're analyzing customer data for an e-commerce platform:

```python
# Similar to our generate_sample_data function
customer_data = pd.DataFrame({
    'Customer_ID': range(1, 10001),
    'Age': np.random.randint(18, 80, 10000),
    'City': np.random.choice(['New York', 'London', 'Tokyo', 'Paris', 'Sydney'], 10000),
    'Total_Spent': np.random.randint(50, 1000, 10000)
})

# Analyze average spending by city
city_spending = customer_data.groupby('City')['Total_Spent'].mean().sort_values(ascending=False)
print(city_spending)
```

---

# Data Wrangling: Pandas in Action 🥋

Let's explore some Pandas operations from our code:

```python
# Filtering
young_ny = df[(df['Age'] < 30) & (df['City'] == 'New York')]
console.print(young_ny.head().to_string())

# Grouping and aggregating
city_salary = df.groupby('City')['Salary'].mean().sort_values(ascending=False)
console.print(city_salary.to_string())
```

---

# Pandas Performance: The Reality Check ⏱️

As datasets grow, Pandas can slow down:

```python
# Performance test from our code
start_time = time()
for _ in range(5):
    result_pandas = df.groupby('City').agg({
        'Age': 'mean',
        'Salary': ['min', 'max', 'mean']
    })
pandas_time = (time() - start_time) / 5
print(f"Pandas groupby operation time: {pandas_time:.4f} seconds")
```

---

# Enter Polars: The Speed Demon 🐻‍❄️💨

![w:300 h:200](https://api.placeholder.com/300x200?text=Polars+Logo)

- Rust-powered DataFrame library for Python
- Designed for performance and memory efficiency
- Similar API to Pandas, but with some key differences

---

# Polars in Action: Lightning-Fast Operations ⚡

Let's look at some Polars operations from our code:

```python
import polars as pl

# Convert Pandas DataFrame to Polars
df_polars = pl.from_pandas(df)

# Basic operations
console.print(df_polars.head())
console.print(df_polars.schema)
console.print(df_polars.describe())

# Data wrangling
city_salary_polars = df_polars.group_by('City').agg(pl.col('Salary').mean().alias('Avg_Salary')).sort('Avg_Salary', descending=True)
console.print(city_salary_polars)
```

---

# Real-world Example: Time Series Analysis 📈

Imagine you're analyzing stock market data:

```python
import polars as pl
import numpy as np

# Generate sample stock data
dates = pl.date_range(start=pl.date(2020, 1, 1), end=pl.date(2023, 12, 31), interval="1d")
stock_data = pl.DataFrame({
    'Date': dates,
    'Price': np.random.randint(100, 200, len(dates)) + np.random.random(len(dates))
})

# Calculate 30-day moving average
stock_data = stock_data.with_columns(
    pl.col('Price').rolling_mean(window_size=30).alias('MA30')
)

print(stock_data.tail())
```

---

# Performance Showdown: Pandas vs Polars 🏁

Let's compare the performance using our code:

```python
# Pandas performance
pandas_time = run_pandas_demo(df)

# Polars performance
polars_time = run_polars_demo(df)

# Display results
console.print(f"Pandas groupby operation time: {pandas_time:.4f} seconds")
console.print(f"Polars groupby operation time: {polars_time:.4f} seconds")

speedup = pandas_time / polars_time
console.print(f"Polars is {speedup:.2f}x faster than Pandas for this operation")
```

---

# Visualizing the Performance Difference 📊

Our code uses plotext for command-line visualization:

```python
import plotext as plt

plt.clear_figure()
plt.bar(["Pandas", "Polars"], [pandas_time, polars_time], orientation="horizontal")
plt.title("Groupby Operation Performance")
plt.xlabel("Time (seconds)")
plt.show()
```

![bg right:40% 80%](https://api.placeholder.com/400x300?text=Performance+Chart)

---

# When to Use What? 🤔

- Pandas:
  - Smaller to medium-sized datasets
  - Data exploration and preprocessing
  - When you need a wide range of built-in functions

- Polars:
  - Large datasets (millions of rows)
  - Performance-critical operations
  - When memory efficiency is crucial

---

# Best Practices for Data Analysis 🌟

1. Start with data exploration using Pandas
2. Profile your code to identify bottlenecks
3. Use Polars for performance-critical operations
4. Leverage both libraries in your data pipeline

```python
# Example: Using both libraries in a workflow
import pandas as pd
import polars as pl

# Initial data loading and exploration with Pandas
df_pandas = pd.read_csv('large_dataset.csv')
print(df_pandas.describe())

# Convert to Polars for heavy computations
df_polars = pl.from_pandas(df_pandas)
result = df_polars.group_by('category').agg([
    pl.col('value').sum().alias('total_value'),
    pl.col('quantity').mean().alias('avg_quantity')
])

# Convert back to Pandas for visualization or reporting
result_pandas = result.to_pandas()
```

---

# Wrap-up: Embrace the Power of Both! 🐼🐻‍❄️

- Master Pandas for its versatility and ecosystem
- Leverage Polars for high-performance operations
- Stay curious and keep exploring new data tools

![bg right:40% 80%](https://api.placeholder.com/400x300?text=Pandas+and+Polars)

---

# Thank You! 🙏

Questions?
Time to crunch some numbers! 💻📊

![w:300 h:300](https://api.placeholder.com/300x300?text=Thank+You)