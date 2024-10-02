import io

import pandas as pd
import polars as pl
import numpy as np
# import matplotlib.pyplot as plt
from time import time
from rich.console import Console
from rich.table import Table
from rich.progress import track
import plotext as plt

console = Console()

def generate_sample_data(size=100000):
    np.random.seed(42)
    data = {
        'Name': [f'Person_{i}' for i in range(1, size + 1)],
        'Age': np.random.randint(18, 80, size),
        'City': np.random.choice(['New York', 'Paris', 'Tokyo', 'London', 'Sydney'], size),
        'Salary': np.random.randint(30000, 150000, size)
    }
    return pd.DataFrame(data)

def run_pandas_demo(df):
    console.rule("[bold blue]Pandas Demo")

    with console.status("[bold green]Performing Pandas operations...") as status:
        # Basic operations
        console.print("\n[yellow]First 5 rows:")
        console.print(df.head().to_string())

        console.print("\n[yellow]Dataframe info:")
        buffer = io.StringIO()
        df.info(buf=buffer)
        console.print(buffer.getvalue())

        console.print("\n[yellow]Summary statistics:")
        console.print(df.describe().to_string())

        # Data wrangling
        console.print("\n[yellow]Average salary by city:")
        city_salary = df.groupby('City')['Salary'].mean().sort_values(ascending=False)
        console.print(city_salary.to_string())

        # Filtering
        console.print("\n[yellow]People under 30 in New York:")
        young_ny = df[(df['Age'] < 30) & (df['City'] == 'New York')]
        console.print(young_ny.head().to_string())

    # Performance test
    start_time = time()
    for _ in track(range(5), description="Running Pandas groupby..."):
        result_pandas = df.groupby('City').agg({
            'Age': 'mean',
            'Salary': ['min', 'max', 'mean']
        })
    pandas_time = (time() - start_time) / 5
    console.print(f"\n[bold green]Pandas groupby operation time: {pandas_time:.4f} seconds")

    return pandas_time

def run_polars_demo(df):
    console.rule("[bold red]Polars Demo")

    with console.status("[bold green]Performing Polars operations...") as status:
        # Convert Pandas DataFrame to Polars DataFrame
        df_polars = pl.from_pandas(df)

        # Basic operations
        console.print("\n[yellow]First 5 rows:")
        console.print(df_polars.head())

        console.print("\n[yellow]Dataframe schema:")
        console.print(df_polars.schema)

        console.print("\n[yellow]Summary statistics:")
        console.print(df_polars.describe())

        # Data wrangling
        console.print("\n[yellow]Average salary by city:")
        city_salary_polars = df_polars.group_by('City').agg(pl.col('Salary').mean().alias('Avg_Salary')).sort('Avg_Salary', descending=True)
        console.print(city_salary_polars)

        # Filtering
        console.print("\n[yellow]People under 30 in New York:")
        young_ny_polars = df_polars.filter((pl.col('Age') < 30) & (pl.col('City') == 'New York'))
        console.print(young_ny_polars.head())

    # Performance test
    start_time = time()
    for _ in track(range(5), description="Running Polars groupby..."):
        result_polars = df_polars.group_by('City').agg([
            pl.col('Age').mean().alias('Age_Mean'),
            pl.col('Salary').min().alias('Salary_Min'),
            pl.col('Salary').max().alias('Salary_Max'),
            pl.col('Salary').mean().alias('Salary_Mean')
        ])
    polars_time = (time() - start_time) / 5
    console.print(f"\n[bold green]Polars groupby operation time: {polars_time:.4f} seconds")

    return polars_time

def display_performance_comparison(pandas_time, polars_time):
    console.rule("[bold magenta]Performance Comparison")

    table = Table(title="Groupby Operation Performance")
    table.add_column("Library", style="cyan")
    table.add_column("Time (seconds)", style="magenta")
    table.add_row("Pandas", f"{pandas_time:.4f}")
    table.add_row("Polars", f"{polars_time:.4f}")
    console.print(table)

    speedup = pandas_time / polars_time
    console.print(f"\n[bold green]Polars is {speedup:.2f}x faster than Pandas for this operation")

    # Command-line bar chart
    plt.clear_figure()
    plt.bar(["Pandas", "Polars"], [pandas_time, polars_time], orientation="horizontal")
    plt.title("Groupby Operation Performance")
    plt.xlabel("Time (seconds)")
    plt.show()

def main():
    console.print("[bold cyan]Welcome to the Pandas vs Polars Demo!")
    console.print("Generating sample data...")
    df = generate_sample_data()
    console.print("[bold green]Sample data generated successfully!")

    pandas_time = run_pandas_demo(df)
    polars_time = run_polars_demo(df)
    display_performance_comparison(pandas_time, polars_time)

    console.print("\n[bold cyan]Demo completed. Thank you for exploring Pandas and Polars!")

if __name__ == "__main__":
    main()