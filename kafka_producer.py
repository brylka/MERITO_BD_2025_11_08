from confluent_kafka import Producer
import time


class WeatherStationMonitor:
    def __init__(self):
        conf = {
            "bootstrap.servers": "127.0.0.1:9092"
        }
        self.producer = Producer(conf)
        self.topic = "weather_data"
        self.monitored_stations = set()

    def add_station(self, station_id):
        self.monitored_stations.add(station_id)
        print(f"Dodano stację do monitorowania: {station_id}")

    def start_monitoring(self):
        while True:
            # Tworzenie zadań dla kafki
            print("Tworzenie zadań")
            time.sleep(10)


if __name__ == "__main__":
    monitor = WeatherStationMonitor()
    for i in range(1,4):
        monitor.add_station(f"STACJA{i:03d}")
    monitor.start_monitoring()
