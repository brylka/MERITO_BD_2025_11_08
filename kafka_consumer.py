import json

from confluent_kafka import Consumer, KafkaError
import requests

class WeatherDataConsumer:
    def __init__(self):
        conf = {
            "bootstrap.servers": "127.0.0.1:9092",
            "group.id": "weather_data_group",
            "auto.offset.reset": "latest"
        }
        # latest - tylko nowe wiadomości (od momentu uruchomienia konsumenta)
        # earliest - wszystkie woadomości (w tym przetworzone w przeszłości)

        self.consumer = Consumer(conf)
        self.consumer.subscribe(['weather_data'])
        print("Konsument zainicjowany i nasłuchuje na topicu: weather_data")

    def fetch_weather_data(self, station_id):
        try:
            print(f"Pobieranie danych dla stacji {station_id}")

            response = requests.get(f"http://127.0.0.1:8000/weather/{station_id}")

            if response.status_code == 200:
                data = response.json()
                temp = data["temperature"]

                if temp > 30:
                    print(f"WYSOKA TEMPERATURA: {temp:.2f} na stacji {station_id}")

                return temp
            else:
                print(f"Błąd HTTP: {response.status_code}")
                return None
        except Exception as e:
            print(f"Błąd pobierania danych: {e}")
            return None

    def start_consuming(self):
        while True:
            msg = self.consumer.poll(1.0)

            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(f"Błąd Kafka: {msg.error()}")
                    break
            try:
                data = json.loads(msg.value().decode("utf-8"))
                station_id = data["station_id"]
                print(f"Otrzymano zadanie dla stacji: {station_id}")

                weather_data = self.fetch_weather_data(station_id)

                if weather_data:
                    temperature = weather_data["temperature"]
                    humidity = weather_data["humidity"]
                    timestamp = weather_data["timestamp"]

                    print(f"Stacja: {station_id}")
                    print(f"Temperatura: {temperature:.2f}")
                    print(f"Wilgotność: {humidity:.2f}")
                    print(f"Timestamp: {timestamp}")
                else:
                    print(f"Nie udało sie pobrać danych dla stacji: {station_id}")
            except Exception as e:
                print(f"Błąd przetwarzania wiadomości: {e}")



if __name__ == "__main__":
    consumer = WeatherDataConsumer()
    consumer.start_consuming()