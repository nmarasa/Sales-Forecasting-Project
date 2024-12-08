# Sales-Forecasting-Project

## Project Description
This project aims to create a sales forecasting system tailored for small businesses. By leveraging historical sales data, the project provides actionable predictions to support inventory management, budgeting, and strategic planning. The forecasting model was implemented using Python and PostgreSQL, with visualization tools like Matplotlib.

## Features
- **Database Setup**: A PostgreSQL database for structured storage of historical sales data.
- **Data Cleaning**: Handling duplicates and ensuring data consistency.
- **Modeling**: A Linear Regression model to predict future sales trends.
- **Visualization**: Graphs showing historical sales trends and future predictions.

## Tools and Technologies
- **PostgreSQL**: For structured data storage.
- **Python Libraries**:
  - `psycopg2`: For database connectivity.
  - `Matplotlib`: For data visualization.
  - `Scikit-learn`: For building and training the Linear Regression model.
- **Data**: Simulated sales data for analysis and predictions.

## File Structure
- **`analyze_sales.py`**: Main script for data analysis and forecasting.
- **`sales_trends_with_predictions.png`**: Graph showing historical and predicted sales trends.
- **`sales_report.txt`**: Text file summarizing insights and predictions.

## How to Run the Project
1. **Setup PostgreSQL Database**:
   - Create a database named `sales_forecasting`.
   - Insert the sales data using the provided SQL script.
  
2. **Install Required Libraries**:
   ```bash
   pip install psycopg2 matplotlib scikit-learn
   ```

3. **Run the Script**:
   - Execute the main script to analyze sales and generate predictions:
     ```bash
     python3 analyze_sales.py
     ```

4. **Outputs**:
   - View the `sales_trends_with_predictions.png` for graphs.
   - Review the `sales_report.txt` for key insights and predictions.

## Future Enhancements
- Incorporate advanced time-series models like ARIMA or Prophet.
- Add support for handling seasonal trends and external variables.
- Develop an interactive web-based dashboard for visualization.

## Contact
For questions or support, contact **Nadia Marasa** at marasanadia1@gmail.com

