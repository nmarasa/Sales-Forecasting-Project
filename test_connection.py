import psycopg2

try:
    connection = psycopg2.connect(
        database="sales_forecasting",
        user="postgres",
        password="babynadia123",
        host="localhost",
        port="5432" 
    )
    print("Connected to PostgreSQL successfully!")
    connection.close()
except Exception as e:
    print(f"Error: {e}")

import psycopg2

try:
    connection = psycopg2.connect(
        database="sales_forecasting",
        user="postgres", 
        password="babynadia123",
        host="localhost",
        port="5432" 
    )

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM sales;")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    connection.close()
except Exception as e:
    print(f"Error: {e}")

import psycopg2

try:
    connection = psycopg2.connect(
        database="sales_forecasting",
        user="postgres",
        password="babynadia123",
        host="localhost",
        port="5432"
    )
    cursor = connection.cursor()

    delete_query = """
    DELETE FROM sales
    WHERE id NOT IN (
        SELECT MIN(id)
        FROM sales
        GROUP BY date, sales
    );
    """
    cursor.execute(delete_query)
    connection.commit()
    print("Duplicates removed successfully!")

    cursor.execute("SELECT * FROM sales;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    connection.close()
except Exception as e:
    print(f"Error: {e}")

import psycopg2

# Import libraries for visualization
import matplotlib.pyplot as plt

try:
    # Connect to PostgreSQL
    connection = psycopg2.connect(
        database="sales_forecasting",
        user="postgres",
        password="babynadia123",
        host="localhost",
        port="5432"
    )

    cursor = connection.cursor()

    # Query data
    cursor.execute("SELECT date, sales FROM sales ORDER BY date;")
    rows = cursor.fetchall()

    # Extract dates and sales for visualization
    dates = [row[0] for row in rows]
    sales = [row[1] for row in rows]

    # Close the connection
    cursor.close()
    connection.close()

    print("Data fetched successfully!")

except Exception as e:
    print(f"Error: {e}")
