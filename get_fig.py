import matplotlib.pyplot as plt
import pandas as pd
csv_path = "D:/myprojects/import_lutein/lutein.csv"
df = pd.read_csv(csv_path)
df_grouped = df.groupby("產地")
country = df_grouped["產地"].count()
X = [1, 2, 3, 4, 5, 6, 7, 8]
plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']
plt.figure(figsize=(8,6))
plt.bar(X, country)
plt.xticks(X, country.index)
for a,b in zip(X,country):
    plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=11)

plt.ylabel("Number of country")
plt.xlabel("place of origin")
plt.title("country of import lutein")
plt.savefig("count_lutein_origin.png")
plt.show()