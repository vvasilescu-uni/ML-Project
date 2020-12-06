import pandas as pd
import matplotlib.pyplot as plt

plt.close('all')

train_data = pd.read_csv('data/train.csv', index_col=0)
test_data = pd.read_csv('data/test.csv', index_col=0)

print(train_data.describe())
