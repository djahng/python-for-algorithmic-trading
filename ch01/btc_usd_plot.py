import os
import matplotlib.pyplot as plt
import quandl as q
import seaborn as sns
from dotenv import load_dotenv


# Setup environment and load API key
load_dotenv()
QUANDL_API_KEY = os.getenv("QUANDL_API_KEY")

sns.set_theme()

def run():
    q.ApiConfig.api_key = QUANDL_API_KEY
    d = q.get("BCHAIN/MKPRU")

    # Calculate simple moving average and plot
    d["SMA"] = d["Value"].rolling(100).mean()
    d.loc["2016-1-1":].plot(title="BTC/USD Exchange Rate", figsize=(10, 6))
    plt.show()


if __name__ == "__main__":
    run()
