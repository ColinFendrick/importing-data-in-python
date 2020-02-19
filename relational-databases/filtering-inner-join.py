from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///../_datasets/Chinook.sqlite')

# Execute query and store records in DataFrame: df
df = pd.read_sql_query(
    'SELECT * FROM PlaylistTrack INNER JOIN Track on PlaylistTrack.TrackId = Track.TrackID WHERE Milliseconds < 250000', engine)

# Print head of DataFrame
print(df.head())
