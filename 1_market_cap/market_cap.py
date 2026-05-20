def calculate_market_cap(price, shares_outstanding):
    return price * shares_outstanding
    


if __name__ == "__main__":
    price = float(input("Enter the share price: "))
    shares_outstanding = int(input("Enter the number of shares outstanding: "))
    market_cap = calculate_market_cap(price, shares_outstanding)
    print(f"Market cap: {market_cap:,.2f}")   