def transform(self):
    def select_columns(df) -> pd.DataFrame:

        df = df[["flight_date",
                "flight_status",
                "departure.iata",
                "departure.scheduled",
                "departure.actual",
                "arrival.iata",
                "arrival.scheduled",
                "arrival.actual",
                "airline.name",
                "airline.iata",
                "flight.number",
                "flight.iata",
                "aircraft.registration",
                "aircraft.iata",
                "aircraft.icao",
                "aircraft.icao24"]]

        df = df.rename(columns = {
                        "departure.iata": "departure_iata",
                        "departure.scheduled": "departure_scheduled",
                        "departure.actual": "departure_actual",
                        "arrival.iata": "arrival_iata",
                        "arrival.scheduled": "arrival_scheduled",
                        "arrival.actual": "arrival_actual",
                        "airline.name": "airline_name",
                        "airline.iata": "airline_iata",
                        "flight.number": "flight_number",
                        "flight.iata": "flight_iata",
                        "aircraft.registration": "aircraft_registration",
                        "aircraft.iata": "aircraft_iata",
                        "aircraft.icao": "aircraft_icao",
                        "aircraft.icao24": "aircraft_icao24",

                    })

                    return df

    self.df = select_columns(self.df)

    self.df['flight_date'] = self.df['flight_date'].apply(lambda x: (datetime.strptime(x, "%Y-%m-%d")).date() if x else None)
    self.df['departure_scheduled'] = self.df['departure_scheduled'].apply(lambda x: datetime.strptime(x, "%Y-%m-%dT%H:%M:%S+00:00") if x else None)
    self.df['departure_actual'] = self.df['departure_actual'].apply(lambda x: datetime.strptime(x, "%Y-%m-%dT%H:%M:%S+00:00") if x else None)
    self.df['arrival_scheduled'] = self.df['arrival_scheduled'].apply(lambda x: datetime.strptime(x, "%Y-%m-%dT%H:%M:%S+00:00") if x else None)
    self.df['arrival_actual'] = self.df['arrival_actual'].apply(lambda x: datetime.strptime(x, "%Y-%m-%dT%H:%M:%S+00:00") if x else None)

    OutputSchema.validate(self.df)

    logger.info(f"transform complete")