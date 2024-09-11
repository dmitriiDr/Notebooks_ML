
# Acoustic and meta features of albums and songs on the Billboard 200

A database containing the following tables:

- 574,000 rows containing all albums in the Billboard 200 from 1/5/1963 to 1/19/2019. Each row contains the album’s place in the charts, the week of the chart, album name, artist name, and where available from Spotify and not null in the table, the number of tracks, and length of the album in milliseconds. This table is titled “albums”.

- 340,000 rows containing acoustic data for tracks from Billboard 200 albums from 1/5/1963 to 1/19/2019. Each row contains track ID on Spotify, track name, album name, artist name, values for Spotify EchoNest acoustic data (acousticness, danceability, energy, instrumentalness, liveness, loudness, speechiness, key, time signature, and valence), duration in milliseconds, album ID on Spotify, and release date of the album. Contains no null values. This table is titled “acoustic_features”.


## More info

- Type: Sqlite
- Size: 117 mb
- By: Andrew Thompson
- Last modified: April 7, 2019
- Added: April 7, 2019

## Source

https://components.one/datasets/billboard-200/
