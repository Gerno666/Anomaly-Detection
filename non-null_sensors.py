import pandas as pd

# Caricamento dei dati
df = pd.read_csv('data.csv')

# Definizione dei valori di t e W
t_values = [1000, 2000, 3000, 4000, 4500]
W_values = [100, 200, 300, 400, 500]

# Lista di tutti i possibili sensori (assumendo che SensorID siano numeri consecutivi a partire da 0)
all_sensors = set(df['SensorID'].unique())

# Funzione per calcolare il numero di sensori non nulli per una finestra temporale
def calculate_non_null_sensors(t, W):
    # Filtraggio dei dati per la finestra temporale da t - W a t
    window_data = df[(df['SampleTime'] >= t - W) & (df['SampleTime'] <= t)]

    # Sensori presenti nella finestra temporale
    sensors_in_window = set(window_data['SensorID'].unique())

    # Sensori non nulli: quelli presenti nella finestra
    non_null_sensors = sensors_in_window

    return len(non_null_sensors)

# Iterazione su tutti i valori di t e W
results = []

for t in t_values:
    for W in W_values:
        non_null_sensors_count = calculate_non_null_sensors(t, W)
        results.append({'t': t, 'W': W, 'Non-Null Sensors': non_null_sensors_count})
        print(f"Per t = {t} e W = {W}, numero di sensori non nulli: {non_null_sensors_count}")

# Creazione di un DataFrame per visualizzare i risultati
results_df = pd.DataFrame(results)
print("\nRisultati finali:")
print(results_df)

# Opzionalmente, puoi salvare i risultati in un file CSV
results_df.to_csv('non-null_sensors_results.csv', index=False)