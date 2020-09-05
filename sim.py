from pandas_datareader import data

snp = data.DataReader('^GSPC', 'yahoo')
print(snp)
