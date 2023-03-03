from python import tradingeconomics as te


def compare_financial_data(country1, country2):
    financial_data_country1=_compare_financial_data(country1)
    financial_data_country2=_compare_financial_data(country2)
    return financial_data_country1, financial_data_country2

def _compare_financial_data(country):
    financial_data=te.getFinancialsData(country= country, output_type="df")
    return financial_data

print('ama')
if __name__ == '__main__':
    print('HHHHHH')