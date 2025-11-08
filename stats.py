import pandas as pd

def show_stats():
    try:
        data_csv = pd.read_csv("weather_data.csv")

        grouped = data_csv.groupby("station_id")

        for station_id, group in grouped:
            print(f"=== Statystyki dla stacji {station_id} ===")
            print(f"Liczba pomiarów: {len(group)}")
            print(f"Średnia temperatura: {group["temperature"].mean():.2f}")
            print(f"Największa temperatura: {group["temperature"].max():.2f}")
            print(f"Najmniejsza temperatura: {group["temperature"].min():.2f}")
    except Exception as e:
        print(f"Problem z pobraniem danych: {e}")

if __name__ == "__main__":
    show_stats()