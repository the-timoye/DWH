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
    ) (
        SELECT DISTINCT
            TO_TIMESTAMP(ts, YYYY-MM-DD HH-MI-SS),
            user_id,
            level,
            song_id,
            artist_id,
            session_id,
            location,
            user_agent
        FROM staging_events
        WHERE page = 'NextSong'
        AND user_id IS NOT NULL
        AND song_id IS NOT NULL
    )
""")

user_table_insert = ("""
    INSERT INTO users (
        user_id,
        first_name,
        last_name,
        gender,
        level
    ) (
        SELECT DISTINCT
            user_id,
            first_name,
            last_name,
            gender,
            level
        FROM staging_events
        WHERE user_id IS NOT NULL OR user_id != ""
    )
""")

song_table_insert = ("""
    INSERT INTO songs (
        song_id,
        title,
        artist_id,
        year,
        duration
    ) (
        SELECT DISTINCT
            song_id,
            title,
            artist_id,
            year,
            duration
        FROM staging_events se
        JOIN staging_songs ss
        ON se.artist = ss.artist_name
        WHERE song_id != "" OR song_id IS NOT NULL
    )
""")

artist_table_insert = ("""
    INSERT INTO artists (
        artist_id, 
        name, 
        location, 
        lattitude, 
        longitude
    )(
        SELECT DISTINCT
            ss.artist_id,
            se.artist,
            ss.artist_location,
            ss.artist_latitude,
            ss.artist_longitude
        FROM staging_events se
        JOIN staging_songs ss
        ON se.artist = ss.artist_name
        WHERE ss.artist_id IS NOT NULL
    )
""")

time_table_insert = ("""
    INSERT INTO time (
        start_time, 
        hour, 
        day, 
        week, 
        month, 
        year, 
        weekday
    ) (
        SELECT DISTINCT
            TO_TIMESTAMP(ts, YYYY-MM-DD HH-MI-SS),
            EXTRACT(HOUR FROM TIMESTAMP ts),
            EXTRACT(DAY FROM TIMESTAMP ts),
            EXTRACT(WEEK FROM TIMESTAMP ts),
            EXTRACT(MONTH FROM TIMESTAMP ts),
            EXTRACT(YEAR FROM TIMESTAMP ts),
            EXTRACT(DOW FROM TIMESTAMP ts),
    )""")

# QUERY LISTS

copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
