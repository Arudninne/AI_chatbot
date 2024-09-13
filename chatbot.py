import pandas as pd
import re

# Load the financial data
data = pd.read_csv(r'C:\Users\Admin\Desktop\Data Science\Internship\BCG gen AI\Cleared data\chatbot\data\financial_data.csv')

# Function to get total revenue for a company and year
def total_revenue(company, year):
    result = data[(data['Company'] == company) & (data['Year'] == year)]
    if not result.empty:
        revenue = result.iloc[0]['Total Revenue']
        return f"📈 The grand total revenue for {company} in {year} is a whopping ${revenue}! 💸"
    else:
        return "Oops! I couldn't find the revenue data for that year. 📉"

# Function to get net income for a company and year
def net_income(company, year):
    result = data[(data['Company'] == company) & (data['Year'] == year)]
    if not result.empty:
        net_income = result.iloc[0]['Net Income']
        return f"💰 {company}'s net income for {year} is ${net_income}. Quite impressive, right? 🌟"
    else:
        return "Sorry, I couldn’t locate the net income for the year you’re interested in. 🤔"

# Function to get total assets for a company and year
def total_assets(company, year):
    result = data[(data['Company'] == company) & (data['Year'] == year)]
    if not result.empty:
        assets = result.iloc[0]['Total Assets']
        return f"🏦 {company} had a total of ${assets} in assets for the year {year}. That's a lot of value! 💼"
    else:
        return "Hmmm, I can't find the total assets for that year. Maybe they were hiding? 😅"

# Function to get total liabilities for a company and year
def total_liabilities(company, year):
    result = data[(data['Company'] == company) & (data['Year'] == year)]
    if not result.empty:
        liabilities = result.iloc[0]['Total Liabilities']
        return f"💳 {company} had total liabilities of ${liabilities} in {year}. Managing finances, one step at a time! 📊"
    else:
        return "It seems the liabilities data is missing for that year. Try another year? 🤷"

# Function to get cash flow from operating activities for a company and year
def cash_flow(company, year):
    result = data[(data['Company'] == company) & (data['Year'] == year)]
    if not result.empty:
        cash_flow = result.iloc[0]['Cash Flow from Operating Activities']
        return f"💵 {company}'s cash flow from operating activities in {year} was ${cash_flow}. A good sign of operational health! 🚀"
    else:
        return "Sorry, the cash flow data seems to be missing for that year. Let's try a different one! 🌟"

# Function to handle creative queries
def handle_creative_query(query):
    if "legendary treasure" in query:
        return total_revenue("Microsoft", 2024) + " How about that treasure chest? 🏆"
    elif "fleet of rockets" in query:
        return net_income("Tesla", 2023) + " Enough to fuel a space journey? 🚀"
    elif "mountain" in query:
        return total_assets("Apple", 2022) + " It would reach the Himalayas! 🏔️"
    elif "high-tech spaceship" in query:
        return total_liabilities("Microsoft", 2021) + " Could this fund a spaceship? 🚀"
    elif "road trips" in query:
        return cash_flow("Tesla", 2024) + " How many road trips would that fund? 🌍"
    elif "giant golden treasure chest" in query:
        return total_revenue("Apple", 2024) + " Imagine it as a treasure chest! 🏆"
    elif "blockbuster movie" in query:
        return net_income("Tesla", 2022) + " Enough for a blockbuster? 🎬"
    elif "skyscraper" in query:
        return total_liabilities("Microsoft", 2021) + " Could this build a skyscraper? 🏙️"
    elif "epic world tour" in query:
        return cash_flow("Apple", 2024) + " Could it fund an epic world tour? 🌏"
    elif "mega amusement park" in query:
        return total_assets("Tesla", 2023) + " Imagine it as a mega amusement park! 🎢"
    else:
        return "Hmm, I didn’t quite catch that. Could you please rephrase your question? 😊"

# Main chatbot function to handle user queries
def simple_chatbot(user_query):
    # Remove special characters from the query
    cleaned_query = re.sub(r'[^\w\s]', '', user_query)
    
    # Parse the user query
    parts = cleaned_query.split(' ')
    
    if len(parts) >= 4:
        company = parts[-3]
        try:
            year = int(parts[-1].strip('?'))
        except ValueError:
            return "I couldn’t extract a valid year from your question. Please specify a valid year. 📅"
        
        if "total revenue" in user_query:
            return total_revenue(company, year)
        elif "net income" in user_query:
            return net_income(company, year)
        elif "total assets" in user_query:
            return total_assets(company, year)
        elif "total liabilities" in user_query:
            return total_liabilities(company, year)
        elif "cash flow from operating activities" in user_query:
            return cash_flow(company, year)
        else:
            return handle_creative_query(user_query)
    else:
        return "Oops! The query format seems off. Please make sure to specify the company and year. 📅"

# Testing the chatbot
if __name__ == "__main__":
    print(simple_chatbot("What is the cash flow from operating activities for Apple in 2024?"))
    print(simple_chatbot("Tell me about Tesla’s total liabilities in 2023."))
    print(simple_chatbot("How much were Apple's total assets in 2021?"))
    print(simple_chatbot("Can you provide the net income for Microsoft in 2022?"))
    print(simple_chatbot("What’s the revenue of Apple compared to a giant golden treasure chest in 2024?"))