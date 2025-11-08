from confluent_kafka import Consumer

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

    def start_consuming(self):
        while True:
            pass


if __name__ == "__main__":
    consumer = WeatherDataConsumer()
    consumer.start_consuming()