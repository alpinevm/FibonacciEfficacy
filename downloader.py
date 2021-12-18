import yfinance as yf
def main():
    dir = "data"
    tick_list = [
    "SPY",
    "QQQ",
    "IWM",
    "BTC-USD"
    ]   
    open("{dir}/tickers.csv".format(dir=dir), "w+")
    [open("{dir}/tickers.csv".format(dir=dir), "a").write("{x}{c}".format(x=x, c= "" if tick_list.index(x) == len(tick_list)-1 else "\n")) and open("{dir}/{x}.csv".format(dir=dir, x=x), "w+").write(yf.Ticker(x).history(start="2017-01-01").to_csv(sep=' ', index=True, header=True)) for x in tick_list]
    print("Done, {n} files downloaded.".format(n=len(tick_list)))
if __name__ == "__main__":
    main()