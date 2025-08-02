import pandas as pd

df = pd.read_csv('baccarat_results_1000000.csv')

# Calculate winning streaks
def calculate_streaks(df):
    streaks = []
    current_streak_type = None
    current_streak_length = 0
    for index, row in df.iterrows():
        winner = row['winner']
        if winner == current_streak_type:
            current_streak_length += 1
        else:
            current_streak_type = winner
            current_streak_length = 1
        streaks.append(current_streak_length)
    return streaks

df['streak'] = calculate_streaks(df)

# Calculate winning ratios (example: simple rolling ratio)
df['player_win'] = (df['winner'] == 'Player').astype(int)
df['banker_win'] = (df['winner'] == 'Banker').astype(int)
df['tie'] = (df['winner'] == 'Tie').astype(int)

# Rolling window for ratios (e.g., last 10 games)
window_size = 10
df['player_ratio'] = df['player_win'].rolling(window=window_size).mean()
df['banker_ratio'] = df['banker_win'].rolling(window=window_size).mean()
df['tie_ratio'] = df['tie'].rolling(window=window_size).mean()

# Fill NaN values created by rolling window (e.g., with 0 or mean)
df = df.fillna(0)

# Save the processed data
df.to_csv('baccarat_features.csv', index=False)
print('Ingénierie des caractéristiques terminée et données sauvegardées dans baccarat_features.csv')

# Display some descriptive statistics and head of the dataframe
print("\nStatistiques descriptives:")
print(df.describe())
print("\nPremières lignes du DataFrame avec les nouvelles caractéristiques:")
print(df.head())


