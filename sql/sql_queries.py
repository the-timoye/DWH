from config import LOG_JSONPATH, SONG_DATA, LOG_DATA, ROLE_NAME
from aws.helpers import create_aws_clients

iam_client = create_aws_clients('iam')

ARN = roleArn = iam_client.get_role(RoleName=ROLE_NAME)['Role']['Arn']



# STAGING TABLES

staging_events_copy = ("""
    COPY staging_events
    FROM {}
    iam_role {}
    JSON {}
    REGION 'us-west-2';
""").format(LOG_DATA, ARN, LOG_JSONPATH)

staging_songs_copy = ("""
    COPY staging_songs
    FROM {}
    iam_role {}
    JSON 'auto'
    REGION 'us-west-2';
""").format(SONG_DATA, ARN)

# FINAL TABLES

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
            TIMESTAMP 'epoch' + se.ts/1000 \
                * INTERVAL '1 second' AS start_time,
            se.user_id::INTEGER,
            se.level,
            ss.song_id,
            ss.artist_id,
            se.session_id::INTEGER,
            se.location,
            se.user_agent
        FROM staging_events se
        JOIN staging_songs ss
        ON se.song = ss.title
        WHERE page = 'NextSong'
        AND ss.artist_name = artist
        AND user_id IS NOT NULL
        AND ss.song_id IS NOT NULL
    );
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
            user_id::INTEGER,
            first_name,
            last_name,
            gender,
            level
        FROM staging_events
        WHERE user_id IS NOT NULL
    );
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
            ss.song_id,
            ss.title,
            ss.artist_id,
            year::INTEGER,
            ss.duration::NUMERIC
        FROM staging_events se
        JOIN staging_songs ss
        ON se.artist = ss.artist_name
        WHERE ss.song_id IS NOT NULL
        AND ss.artist_id IS NOT NULL
    );
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
            ss.artist_latitude::NUMERIC,
            ss.artist_longitude::NUMERIC
        FROM staging_events se
        JOIN staging_songs ss
        ON se.artist = ss.artist_name
        WHERE ss.artist_id IS NOT NULL
    );
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
    ) (
        SELECT DISTINCT
            TIMESTAMP 'epoch' + se.ts/1000 \
                * INTERVAL '1 second' AS start_time,
            EXTRACT(HOUR FROM start_time),
            EXTRACT(DAY FROM start_time),
            EXTRACT(WEEK FROM start_time),
            EXTRACT(MONTH FROM start_time),
            EXTRACT(YEAR FROM start_time),
            EXTRACT(DOW FROM start_time)
        FROM staging_events se
        WHERE start_time IS NOT NULL
    );
""")

# QUERY LISTS
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
