import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

excel1 = 'mercury.xlsx'

login_data = pd.read_excel(excel1, sheet_name= 'first')

print(login_data)