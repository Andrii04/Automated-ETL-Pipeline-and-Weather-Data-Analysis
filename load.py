import psycopg2 as pg2
import sqlalchemy as sqla
from sqlalchemy.exc import SQLAlchemyError
import pandas as pd
from clean_transform import clean_data
from db_config import DB_CONFIG

def load_data():

    dataFrames = clean_data()
    df_raw = dataFrames["df_raw"]
    df_daily = dataFrames["df_daily"]
    df_hourly = dataFrames["df_hourly"]

    try:

        engine = sqla.create_engine(f"postgresql+psycopg2://"
                                    f"{DB_CONFIG['user']}:{DB_CONFIG['password']}@"
                                    f"{DB_CONFIG['host']}:{DB_CONFIG['port']}/"
                                    f"{DB_CONFIG['database']}")

        with engine.connect() as conn:
            df_raw.to_sql("weather_raw", con=conn, if_exists="replace", index=False)
            df_daily.to_sql("weather_daily", con=conn, if_exists="replace", index=False)
            df_hourly.to_sql("weather_hourly", con=conn, if_exists="replace", index=False)

    except SQLAlchemyError as e:
        print("Database error:", e)
    except Exception as e:
        print("Unexpected error:", e)