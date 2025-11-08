import time
from datetime import datetime
from fastapi import FastAPI
import uvicorn
import random

app = FastAPI()

@app.get("/weather/{station_id}")
def get_weather_simple(station_id: str):
    time.sleep(random.randint(2,8))
    return {
        "station_id": station_id,
        "temperature": random.uniform(-15,45),
        "humidity": random.uniform(40, 90),
        "timestamp": datetime.now()
    }


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)