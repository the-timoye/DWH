
staging_events_table_create= ("""
    CREATE TABLE IF NOT EXISTS staging_events (
        staging_events_id IDENTITY(0,1) NOT NULL
        artist VARCHAR(50) NOT NULL,
        auth VARCHAR(10) NOT NULL,
        first_name VARCHAR(20) NOT NULL,
        gender VARCHAR(1) NOT NULL,
        item_in_session INT NOT NULL,
        last_name, VARCHAR(20) NOT NULL
        length DECIMAL NOT NULL,
        level VARCHAR(5) NOT NULL,
        location VARCHAR(50) NOT NULL,
        method VARCHAR(6) NOT NULL,
        page VARCHAR(15) NOT NULL,
        registration VARCHAR(20) NOT NULL,
        session_id INTEGER NOT NULL,
        song VARCHAR(50) NOT NULL,
        status INTEGER NOT NULL,
        ts TIMESTAMP NOT NULL,
        user_agent VARCHAR(50) NOT NULL,
        user_id INTEGER NOT NULL
    )
""")

staging_songs_table_create = ("""
    CREATE TABLE IF NOT EXISTS staging_songs (
        staging_songs_id IDENTITY(0,1) NOT NULL
        num_songs INT NOT NULL,
        artist_id VARCHAR(20) NOT NULL,
        artist_latitude NUMERIC,
        artist_longitude NUMERIC,
        artist_location VARCHAR(50),
        artist_name VARCHAR(50) NOT NULL,
        song_id VARCHAR(25) NOT NULL,
        title VARCHAR(20) NOT NULL,
        duration NUMERIC NOT NULL,
        year INTEGER NOT NULL
    )
""")

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays (
        songplay_id IDENTITY(0,1) NOT NULL,
        start_time VARCHAR NOT NULL,
        user_id INTEGER NOT NULL,
        level VARCHAR(5) NOT NULL,
        song_id VARCHAR(25) NOT NULL,
        artist_id VARCHAR(20) NOT NULL,
        session_id INTEGER NOT NULL,
        location VARCHAR NOT NULL,
        user_agent VARCHAR(50) NOT NULL
    )
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INT NOT NULL, 
        first_name VARCHAR(25) NOT NULL, 
        last_name VARCHAR(25) NOT NULL, 
        gender VARCHAR(1) NOT NULL, 
        level VARCHAR(5) NOT NULL
    )
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs (
        song_id VARCHAR NOT NULL, 
        title VARCHAR(20) NOT NULL, 
        artist_id VARCHAR(20) NOT NULL, 
        year INTEGER NOT NULL, 
        duration DECIMAL NOT NULL
    )
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists (
        artist_id VARCHAR NOT NULL, 
        name VARCHAR(25) NOT NULL, 
        location VARCHAR NOT NULL, 
        lattitude NUMERIC, 
        longitude NUMERIC
    )
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time (
        start_time VARCHAR NOT NULL, 
        hour INTEGER NOT NULL, 
        day INTEGER NOT NULL, 
        week INTEGER NOT NULL, 
        month INTEGER NOT NULL, 
        year INTEGER NOT NULL, 
        weekday INTEGER NOT NULL
    )
""")

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]