
staging_events_table_create= ("""
    CREATE TABLE IF NOT EXISTS staging_events (
        event_id    BIGINT IDENTITY(0,1),
        artist      VARCHAR,
        auth        VARCHAR,
        first_name   VARCHAR,
        gender      VARCHAR,
        item_in_session INTEGER,
        last_name    VARCHAR,
        length      NUMERIC,
        level       VARCHAR,
        location    VARCHAR,
        method      VARCHAR,
        page        VARCHAR,
        registration VARCHAR,
        session_id   INTEGER SORTKEY DISTKEY,
        song        VARCHAR,
        status      INTEGER,
        ts          BIGINT,
        user_agent   VARCHAR,
        user_id      INTEGER
    );
""")
staging_songs_table_create = ("""
    CREATE TABLE IF NOT EXISTS staging_songs (
        num_songs           INTEGER,
        artist_id           VARCHAR SORTKEY DISTKEY,
        artist_latitude     VARCHAR,
        artist_longitude    VARCHAR,
        artist_location     VARCHAR,
        artist_name         VARCHAR,
        song_id             VARCHAR,
        title               VARCHAR,
        duration            NUMERIC,
        year                INTEGER
    );
""")

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays (
        songplay_id INT IDENTITY(0,1) PRIMARY KEY NOT NULL,
        start_time TIMESTAMP NOT NULL,
        user_id INTEGER NOT NULL,
        level VARCHAR(5) NOT NULL,
        song_id VARCHAR NOT NULL,
        artist_id VARCHAR NOT NULL,
        session_id INTEGER NOT NULL,
        location VARCHAR NOT NULL,
        user_agent VARCHAR NOT NULL
    );
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INT PRIMARY KEY NOT NULL, 
        first_name VARCHAR NOT NULL, 
        last_name VARCHAR NOT NULL, 
        gender VARCHAR(1) NOT NULL, 
        level VARCHAR NOT NULL
    );
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs (
        song_id VARCHAR PRIMARY KEY NOT NULL, 
        title VARCHAR NOT NULL, 
        artist_id VARCHAR NOT NULL, 
        year INTEGER NOT NULL, 
        duration NUMERIC NOT NULL
    );
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists (
        artist_id VARCHAR PRIMARY KEY NOT NULL, 
        name VARCHAR NOT NULL, 
        location VARCHAR, 
        lattitude NUMERIC, 
        longitude NUMERIC
    );
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time (
        start_time TIMESTAMP PRIMARY KEY NOT NULL, 
        hour INTEGER NOT NULL, 
        day INTEGER NOT NULL, 
        week INTEGER NOT NULL, 
        month INTEGER NOT NULL, 
        year INTEGER NOT NULL, 
        weekday INTEGER NOT NULL
    );
""")

# STAGING TABLES


# FINAL TABLES

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]