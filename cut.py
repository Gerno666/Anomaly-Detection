import pandas as pd

# Step 1: Leggi il dataset
# Supponendo che il dataset sia in un file chiamato 'dataset.csv'
df = pd.read_csv('data.csv')

# Step 2: Filtra il dataset
df_filtered = df[df['SampleTime'] > 5000]

# Step 3: Salva il dataset filtrato in un nuovo file
# Salva il dataset filtrato in un file chiamato 'dataset_filtrato.csv'
df_filtered.to_csv('reduced_data.csv', index=False)