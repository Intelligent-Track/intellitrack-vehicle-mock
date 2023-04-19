from fastapi import FastAPI
import random

status = [ 'Tired', 'Sad', 'Bored', 'Angry', 'Normal', 'Dizzy', 'Sick' ]
max_speed = 180
max_fuel = 100
max_lat = 6.5
max_long = -77
min_lat = 2.5
min_long = -69

app = FastAPI()

@app.get("/sensor/{vehicle_id}")
async def vehicle_sensor(vehicle_id):
    random.seed(vehicle_id)
    current_status = status[ random.randint( 0, len( status ) - 1 ) ]
    current_speed = random.uniform( 0, max_speed )
    current_fuel = random.randint( 0, max_fuel )
    current_lat = random.uniform( min_lat, max_lat )
    current_long = random.uniform( min_long, max_long )
    return { "status": current_status , "speed": current_speed, "fuel_level": current_fuel, "latitude": current_lat, "longitude": current_long }

