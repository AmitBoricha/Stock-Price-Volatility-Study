from bsedata.bse import BSE
import pandas as pd
b = BSE()


df = pd.read_csv('Equity.csv')

print(df)