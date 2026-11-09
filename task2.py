
# Stock Portfolio Tracker

# Stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 400,
    "AMZN": 190
}

portfolio = []
total_investment = 0

print("================================")
print("     STOCK PORTFOLIO TRACKER")
print("================================")

while True:
    stock_name = input("\nEnter Stock Name (or done): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Stock not available!")
        continue

    try:
        quantity = int(input("Enter Quantity: "))

        if quantity <= 0:
            print("Please enter a positive quantity.")
            continue

        price = stock_prices[stock_name]
        investment = price * quantity

        total_investment += investment

        portfolio.append(
            [stock_name, quantity, price, investment]
        )

        print("Stock Added Successfully!")

    except ValueError:
        print("Please enter a valid quantity.")

print("\n========== PORTFOLIO ==========")

for stock in portfolio:
    print("Stock:", stock[0])
    print("Quantity:", stock[1])
    print("Price:", stock[2])
    print("Investment:", stock[3])
    print("----------------------------")

print("Total Investment:", total_investment)

# Save result in text file
with open("portfolio.txt", "w") as file:
    file.write("STOCK PORTFOLIO REPORT\n")
    file.write("======================\n")

    for stock in portfolio:
        file.write(
            f"{stock[0]} - Quantity: {stock[1]}, "
            f"Price: {stock[2]}, Investment: {stock[3]}\n"
        )

    file.write(f"\nTotal Investment: {total_investment}")

print("\nPortfolio saved successfully!")
print("Thank you!")
  
