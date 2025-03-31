import fastf1
import pandas as pd


class F1DataFetcher:
    def __init__(self):
        self.races = [
            (2025, 1), (2025, 2), (2025, 3), (2025, 4), (2025, 5), (2025, 6), (2025, 7), (2025, 8), (2025, 9), (2025, 10), # Races before België in 2025
            (2024, 14),  # Belgische GP 2024
            (2023, 14)   # Belgische GP 2023
        ]

    def get_qualifying_data(self, year, round_number):
        session = fastf1.get_session(year, round_number, 'Q')
        session.load()
        
        data = []
        for drv in session.drivers:
            laps = session.laps.pick_driver(drv)
            q1 = laps.loc[laps['LapNumber'] == 1, 'LapTime'].min()
            q2 = laps.loc[laps['LapNumber'] == 2, 'LapTime'].min()
            q3 = laps.loc[laps['LapNumber'] == 3, 'LapTime'].min()

            # Converteer naar seconden
            def to_seconds(td):
                return td.total_seconds() if pd.notna(td) else None
            
            data.append({
                'Driver': session.get_driver(drv)['Abbreviation'],
                'Team': session.get_driver(drv)['TeamName'],
                'Q1': to_seconds(q1),
                'Q2': to_seconds(q2),
                'Q3': to_seconds(q3),
                'Year': year,
                'Round': round_number
            })
        
        return pd.DataFrame(data)

    def fetch_all_data(self):
        df_list = [self.get_qualifying_data(year, rnd) for year, rnd in self.races]
        df = pd.concat(df_list, ignore_index=True)
        return df
