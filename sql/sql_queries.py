from config import ARN, LOG_JSONPATH, SONG_DATA, LOG_DATA

staging_events_copy = ("""
    COPY staging_events
    FROM {}
    iam_role {}
    JSON {}
""").format(LOG_DATA, ARN, LOG_JSONPATH)

staging_songs_copy = ("""
    COPY staging_songs
    FROM {}
    iam_role {}
    JSON 'auto'
""").format(SONG_DATA, ARN)


songplay_table_insert = ("""
    INSERT INTO songplays (
        start_time,
        user_id,
        level,
        song_id,
        artist_id,
        session_id,
        location,
        user_agent
    )
""")

user_table_insert = ("""
    INSERT INTO users (
        user_id,
        first_name,
        last_name,
        gender,
        level
    )
""")

song_table_insert = ("""
    INSERT INTO songs (
        song_id,
        title,
        artist_id,
        year,
        duration
    )
""")

artist_table_insert = ("""
    INSERT INTO artists (
        artist_id, 
        name, 
        location, 
        lattitude, 
        longitude
    )
""")

time_table_insert = ("""
    INSERT INTO TIME (
        start_time, 
        hour, 
        day, 
        week, 
        month, 
        year, 
        weekday
    )
""")

# QUERY LISTS

copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
