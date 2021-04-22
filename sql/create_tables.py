staging_events_table_create= ("""
    CREATE TABLE IF NOT EXISTS staging_events (
        event_id    BIGINT IDENTITY(0,1)    NOT NULL,
        artist      VARCHAR                 NULL,
        auth        VARCHAR                 NULL,
        first_name   VARCHAR                 NULL,
        gender      VARCHAR                 NULL,
        item_in_session VARCHAR               NULL,
        last_name    VARCHAR                 NULL,
        length      VARCHAR                 NULL,
        level       VARCHAR                 NULL,
        location    VARCHAR                 NULL,
        method      VARCHAR                 NULL,
        page        VARCHAR                 NULL,
        registration VARCHAR                NULL,
        session_id   INTEGER                 NOT NULL SORTKEY DISTKEY,
        song        VARCHAR                 NULL,
        status      INTEGER                 NULL,
        ts          BIGINT                  NOT NULL,
        user_agent   VARCHAR                 NULL,
        user_id      INTEGER                 NULL
    );
""")
staging_songs_table_create = ("""
    CREATE TABLE IF NOT EXISTS staging_songs (
        num_songs           INTEGER         NULL,
        artist_id           VARCHAR         NOT NULL SORTKEY DISTKEY,
        artist_latitude     VARCHAR         NULL,
        artist_longitude    VARCHAR         NULL,
        artist_location     VARCHAR   NULL,
        artist_name         VARCHAR   NULL,
        song_id             VARCHAR         NOT NULL,
        title               VARCHAR   NULL,
        duration            DECIMAL      NULL,
        year                INTEGER         NULL
    );
""")

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays (
        songplay_id INT IDENTITY(0,1) NOT NULL,
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
        user_id INT NOT NULL, 
        first_name VARCHAR NOT NULL, 
        last_name VARCHAR NOT NULL, 
        gender VARCHAR(1) NOT NULL, 
        level VARCHAR NOT NULL
    );
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs (
        song_id VARCHAR NOT NULL, 
        title VARCHAR NOT NULL, 
        artist_id VARCHAR NOT NULL, 
        year INTEGER NOT NULL, 
        duration DECIMAL NOT NULL
    );
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists (
        artist_id VARCHAR NOT NULL, 
        name VARCHAR NOT NULL, 
        location VARCHAR, 
        lattitude NUMERIC, 
        longitude NUMERIC
    );
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time (
        start_time TIMESTAMP NOT NULL, 
        hour INTEGER NOT NULL, 
        day INTEGER NOT NULL, 
        week INTEGER NOT NULL, 
        month INTEGER NOT NULL, 
        year INTEGER NOT NULL, 
        weekday INTEGER NOT NULL
    );
""")

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]