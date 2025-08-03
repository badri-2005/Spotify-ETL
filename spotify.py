from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pandas as pd
import matplotlib.pyplot as plt
import re
# Regular Expression
import mysql.connector
import pymysql

# DB Config

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='Badri@312',
    database='spotify_db',
)
cursor = connection.cursor()


#Set up Client Credentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials
    (client_id = "9f5c29986f484fe6bc1f376ccddf9b19",
     client_secret = "805c6db119714ee780b09d5540cbb245"

))

# Full Track URL 
track_url = "https://open.spotify.com/track/3n3Ppam7vgaVa1iaRUc9Lp"

# Extract track id directly from the URL
track_id = re.search(r'track/([a-zA-Z0-9]+)', track_url).group(1)

# Get track information
track = sp.track(track_id)

# Extracting the track name and artist

track_data = {

    'Track Name' : track['name'],
    'Artist' : track['artists'][0]['name'],
    'Album' : track['album']['name'],
    'Popularity' : track['popularity'],
    'Duration (ms)' : track['duration_ms'] /60000,  # Convert to minutes
}

# Insert  Query

insert_query = """
INSERT INTO spotify_tracks (track_name, artist, album, popularity, duration_ms)
VALUES (%s, %s, %s, %s, %s)
"""

cursor.execute(insert_query , (
    track_data['Track Name'],
    track_data['Artist'],
    track_data['Album'],
    track_data['Popularity'],
    track_data['Duration (ms)']
      # Convert back to milliseconds)
))

connection.commit()

print("Track data inserted into the database successfully.")
print("Track data:", track_data)

# Close the database connection
cursor.close()



# Print the track data
print(f"Track Name: {track_data['Track Name']}")
print(f"Artist: {track_data['Artist']}")
print(f"Album: {track_data['Album']}")
print(f"Popularity: {track_data['Popularity']}")
print(f"Duration: {track_data['Duration (ms)']} minutes")


df = pd.DataFrame([track_data])
print("Track Data as DataFrame:")
print(df)


# Save the DataFrame to a CSV file
df.to_csv('spotify_track_data.csv', index=False)

# Visualize the track's popularity

features = ['Popularity', 'Duration (ms)']
values = [track_data['Popularity'], track_data['Duration (ms)']]
plt.figure(figsize=(10, 5))
plt.bar(features, values, color=['blue', 'green'])
plt.title('Track Popularity and Duration')
plt.xlabel('Features')
plt.ylabel('Values')
plt.show()