import pandas
from matplotlib import pyplot as plt
from matplotlib import cycler as mpl_cycler
import fib

def update_plt_params():
    plt.rcParams.update({
        "axes.prop_cycle": mpl_cycler(color=["orange", "#ffffff", "1"]) ,
        "lines.color": "white",
        "patch.edgecolor": "white",
        "text.color": "black",
        "axes.facecolor": "black",
        "axes.edgecolor": "lightgray",
        "axes.labelcolor": "white",
        "xtick.color": "white",
        "ytick.color": "white",
        "grid.color": "lightgray",
        "figure.facecolor": "black",
        "figure.edgecolor": "black",
        "savefig.facecolor": "black",
        "savefig.edgecolor": "black"})

def main():
    update_plt_params()
    #Load data
    dir = "data"
    tickers = open("data/tickers.csv", "r").read().splitlines()
    data = [pandas.read_csv("{dir}/{x}.csv".format(dir=dir, x=x), sep=" ") for x in tickers]

    for i, dt in enumerate(data):
        df = pandas.Series(dt["Close"])
        zz = fib.create_zigzag(df)
        #print(zz)
        #col.plot()
        #plt.show()

if(__name__ == "__main__"):
    main()