import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("HistoricalPrices.csv")
df.columns.str.strip().str.upper()
num_df=df.select_dtypes(include='number')
corr_matrix=num_df.corr()
sns.heatmap(corr_matrix,annot=True,cmap="coolwarm",linewidths="0.9")
plt.title("Corraltion - Heat Map")
plt.show()
