import os
import fastf1
import logging
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("cache", exist_ok=True)
fastf1.Cache.configure(cache_dir="cache")
logging.getLogger("fastf1").setLevel(logging.ERROR)

quali = fastf1.get_session(2021, "Turkey", "Q")
quali.load(telemetry=False, weather=False, messages=False)

print(quali.event["EventName"], "-", quali.name)
r=pd.DataFrame(quali.laps)
print(r.columns)

