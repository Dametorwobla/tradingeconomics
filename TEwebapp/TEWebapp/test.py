from websitecomparer.comparer import compare_financial_data
from python import tradingeconomics as te

if __name__ == "__main__":
    te.login('guest:guest')
    res = compare_financial_data("united states", "nigeria")
    print('C1')
    print(res[0])

    print('nC2')
    print(res[1])