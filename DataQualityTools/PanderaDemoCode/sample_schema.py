from datetime import datetime, date
from pandera import Column, DataFrameSchema

InputSchema = DataFrameSchema(
    {
        "flight_date": Column(str, nullable = True),
        "flight_status": Column(str, nullable = True),
        "departure.iata": Column(str, nullable = True),
        "departure.scheduled": Column(str, nullable = True),
        "departure.actual": Column(str, nullable = True),
        "arrival.iata": Column(str, nullable = True),
        "arrival.scheduled": Column(str, nullable = True),
        "arrival.actual": Column(str, nullable = True),
        "airline.name": Column(str, nullable = True),
        "airline.iata": Column(str, nullable = True),
        "flight.number": Column(str, nullable = True),
        "flight.iata": Column(str, nullable = True),
        "aircraft.registration": Column(str, nullable = True),
        "aircraft.iata": Column(str, nullable = True),
        "aircraft.icao": Column(str, nullable = True),
        "aircraft.icao24": Column(str, nullable = True),
    }
)

OutputSchema = DataFrameSchema(
    {
        "flight_date": Column(date, nullable = True, coerce = True),
        "flight_status": Column(str, nullable = True, coerce = True),
        "departure_iata": Column(str, nullable = True, coerce = True),
        "departure_scheduled": Column(datetime, nullable = True, coerce = True),
        "departure_actual": Column(datetime, nullable = True, coerce = True),
        "arrival_iata": Column(str, nullable = True, coerce = True),
        "arrival_scheduled": Column(datetime, nullable = True, coerce = True),
        "arrival_actual": Column(datetime, nullable = True, coerce = True),
        "airline_name": Column(str, nullable = True, coerce = True),
        "airline_iata": Column(str, nullable = True, coerce = True),
        "flight_number": Column(str, nullable = True, coerce = True),
        "flight_iata": Column(str, nullable = True, coerce = True),
        "aircraft_registration": Column(str, nullable = True, coerce = True),
        "aircraft_iata": Column(str, nullable = True, coerce = True),
        "aircraft_icao": Column(str, nullable = True, coerce = True),
        "aircraft_icao24": Column(str, nullable = True, coerce = True),
    }
)