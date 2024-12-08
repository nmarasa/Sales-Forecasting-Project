import psycopg2
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression
import numpy as np

try:
    # Connect to the database
    connection = psycopg2.connect(
        database="sales_forecasting",
        user="postgres",
        password="babynadia123",
        host="localhost",
        port="5432"
    )
    print("Connected to PostgreSQL successfully!")

    # Fetch data
    cursor = connection.cursor()
    cursor.execute("SELECT date, sales FROM sales;")
    rows = cursor.fetchall()

    # Process data
    dates = [row[0] for row in rows]
    sales = [row[1] for row in rows]

    # Calculate insights
    avg_sales = sum(sales) / len(sales)
    max_sales = max(sales)
    min_sales = min(sales)
    print(f"Average Sales: {avg_sales}")
    print(f"Maximum Sales: {max_sales}")
    print(f"Minimum Sales: {min_sales}")

    # Train a Linear Regression model
    X = np.arange(len(sales)).reshape(-1, 1)  # Use indices as X values
    y = np.array(sales)
    model = LinearRegression()
    model.fit(X, y)

    # Get the number of days to predict from the user
    days_to_predict = int(input("Enter the number of days to predict: "))
    future_X = np.arange(len(sales), len(sales) + days_to_predict).reshape(-1, 1)
    future_sales = model.predict(future_X)

    print("\n=== Future Sales Predictions ===")
    for i, prediction in enumerate(future_sales, 1):
        print(f"Day {i}: {round(prediction, 2)}")

    # Save insights and predictions to a report
    with open('sales_report.txt', 'w') as file:
        file.write(f"=== Sales Analysis Report ===\n\n")
        file.write(f"Average Sales: {avg_sales:.2f}\n")
        file.write(f"Maximum Sales: {max_sales}\n")
        file.write(f"Minimum Sales: {min_sales}\n")
        file.write("\n=== Predicted Sales for Future Dates ===\n")
        for i, prediction in enumerate(future_sales):
            file.write(f"Day {i+1} Prediction: {prediction:.2f}\n")
    print("Sales report generated: 'sales_report.txt'")

    # Extend the graph with predictions
    future_dates = [dates[-1] + timedelta(days=i) for i in range(1, days_to_predict + 1)]
    plt.figure(figsize=(10, 5))
    plt.plot(dates, sales, marker='o', color='blue', label="Historical Sales")
    plt.plot(future_dates, future_sales, marker='o', color='red', linestyle='--', label="Predicted Sales")
    plt.title("Sales Trends with Predictions")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.grid()
    plt.legend()

    # Annotate data points
    for i, txt in enumerate(sales):
        plt.text(dates[i], sales[i] + 10, str(txt), ha='center')
    for i, txt in enumerate(future_sales):
        plt.text(future_dates[i], txt + 10, str(round(txt, 2)), ha='center', color='red')

    # Save the graph
    plt.savefig('sales_with_predictions.png')
    print("Graph saved as 'sales_with_predictions.png'")
    plt.show()

except Exception as e:
    print(f"Error: {e}")
finally:
    if connection:
        connection.close()
