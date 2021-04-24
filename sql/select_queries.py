
# All valid Male Users retrieveing contents from the application

staging_events = """
    SELECT first_name as user_name, gender, method
    FROM staging_events
    WHERE gender = 'M'
    AND method = 'GET'
    AND user_id IS NOT NULL
    LIMIT 10;
"""

# COUNT ALL songs per artists

staging_songs = """
    SELECT artist_name, COUNT(song_id)
    FROM staging_songs
    WHERE artist_name IS NOT NULL
    GROUP BY artist_name
    ORDER BY artist_name
    LIMIT 10;
"""

# SELECT ALL PAYING FEMALE USERS, the songs they played and duration

songs = """
    SELECT u.first_name, u.last_name, s.title as song_title, s.duration
    FROM users u
    JOIN songplays sp
    ON u.user_id = sp.user_id
    JOIN songs s
    ON sp.song_id = s.song_id
    WHERE u.gender = 'F'
    AND sp.level = 'paid'
    LIMIT 10;
"""

# Ten random artists and their song titles

artists = """
    SELECT a.name as artist_name, s.title as song_title
    FROM artists a
    JOIN songplays sp
    ON a.artist_id = sp.artist_id
    JOIN songs s
    ON sp.song_id = s.song_id
    LIMIT 10;
"""

select_queries = {
    0: {'query_title': 'All valid Male Users retrieveing contents from the application', 'query': staging_events },
    1: {'query_title': 'COUNT ALL songs per artists', 'query': staging_songs },
    2: {'query_title': 'SELECT ALL PAYING FEMALE USERS, the songs they played and duration', 'query': songs },
    3: {'query_title': 'Ten random artists and their song titles', 'query': artists }
}