ProfitPulse: Your Financial Data Guide

This chatbot is designed to provide insights and answer queries based on financial data for various companies and years. It offers a range of responses for standard financial queries and can creatively handle imaginative queries by comparing financial metrics to interesting scenarios.

Supported Queries

Standard Queries
Total Revenue: Retrieves the total revenue for a specific company and year.
Net Income: Shows the net income for a company in a given year.
Total Assets: Provides the total assets for a company in a specified year.
Total Liabilities: Delivers information on the total liabilities for a company in a given year.
Cash Flow: Provides cash flow from operating activities for a specific company and year.

Creative Queries
Legendary Treasure: Compares the total revenue to a legendary treasure.
Fleet of Rockets: Compares the net income to the cost of a fleet of rockets.
Mountain Comparison: Compares total assets to the height of a mountain.
High-Tech Spaceship: Compares total liabilities to the cost of a high-tech spaceship.
Road Trips: Compares cash flow to the number of road trips it could fund.
Giant Golden Treasure Chest: Imagines total revenue as a giant treasure chest.
Blockbuster Movie: Compares net income to the budget of a blockbuster movie.
Skyscraper: Imagines total liabilities as the cost of building a skyscraper.
Epic World Tour: Compares cash flow to funding an epic world tour.
Mega Amusement Park: Compares total assets to the value of a mega amusement park.
Usage

Prepare the Data File: Ensure that the financial data CSV file is available at:

C:\Users\Admin\Desktop\Data Science\Internship\BCG gen AI\Cleared data\chatbot\data\financial_data.csv
The CSV file should include columns for Company, Year, Total Revenue, Net Income, Total Assets, Total Liabilities, and Cash Flow from Operating Activities.

Run the Script: Execute the chatbot.py script to start interacting with the chatbot. You can test various queries by running the script:

code
python chatbot.py
Testing Queries: Use predefined queries to test the chatbot’s functionality. Examples include:

python-code
print(simple_chatbot("What is the total revenue for Microsoft in 2024?"))
print(simple_chatbot("How does Microsoft's revenue in 2024 compare to the legendary treasure of ancient kings?"))

Limitations

Predefined Responses: The chatbot responds only to predefined query formats. It may not handle free-form or unrecognized queries effectively.
Data Dependency: The accuracy of responses depends on the completeness and correctness of the financial data CSV file.

How to Run

Install Dependencies: Ensure that you have the required Python packages installed. You can install the necessary packages using pip:

bash-code
pip install pandas

Prepare Data: Place the financial data CSV file in the data folder as specified in the script.

Execute the Script: Run the chatbot.py script to start the chatbot and interact with it using the provided queries.