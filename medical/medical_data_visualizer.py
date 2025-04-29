import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
# Add 'overweight' column
df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2 > 25).astype(int)

# Нормалізуємо дані, зробивши 0 завжди хорошим, а 1 завжди поганим. Якщо значення «cholestorol» або «gluc» дорівнює 1,
# зробити значення 0. Якщо значення більше 1, зробити значення 1.
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)


# Draw Categorical Plot
def draw_cat_plot():
    # Створіть DataFrame для діаграми categoria за допомогою `pd.melt`, використовуючи лише значення з 'cholesterol', 'gluc', 'smoke',
    # 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=['cardio'],
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Групуємо та переформатовуємо дані, щоб розділити їх за «cardio»
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index()
    df_cat = df_cat.rename(columns={0: 'total'})

    # Малюємо catplot за допомогою "sns.catplot()"
    graph = sns.catplot(data=df_cat, kind="bar", x="variable", y="total", hue="value", col="cardio")
    fig = graph.fig

    # Не змінюємо наступні два рядки
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Очищаємо дату
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
                 (df['height'] >= df['height'].quantile(0.025)) &
                 (df['height'] <= df['height'].quantile(0.975)) &
                 (df['weight'] >= df['weight'].quantile(0.025)) &
                 (df['weight'] <= df['weight'].quantile(0.975))
                 ]

    # Обчислюємо кореляційну матрицю
    corr = df_heat.corr()

    # Генеруємл маску для верхнього трикутника
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Налаштовуємо графік
    fig, ax = plt.subplots(figsize=(16, 9))

    # Малюємо heatmap за допомогою "sns.heatmap()"
    sns.heatmap(corr, mask=mask, square=True, linewidths=0.5, annot=True, fmt="0.1f")

    # Не змінюємо наступні два рядки
    fig.savefig('heatmap.png')
    return fig

draw_cat_plot()
draw_heat_map()
