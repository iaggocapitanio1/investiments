from utils.utils import get_ebitda
import yfinance as yf


ticker = "PETR4.SA"
ebitda = get_ebitda(ticker)
print(f"EBITDA for {ticker}: {ebitda}")
