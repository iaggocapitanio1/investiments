from indicators.indicators import ebitda

ticker = "PETR4.SA"
ebitda = ebitda(ticker)
print(f"EBITDA for {ticker}: {ebitda}")
