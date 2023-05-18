playlist = {
    "title": "hashtable",
    "author": "harry",
    "tracks": [
        {
            "title": "song1",
            "artist": ["artist1"],
            "album": "album1",
            "url": "url1",
            "date": "test",
            "duration": 2.34,
        },
        {
            "title": "song2",
            "artist": ["artist2"],
            "album": "album2",
            "url": "url2",
            "date": "test",
            "duration": 3.42,
        },
        {
            "title": "song2",
            "artist": ["artist2"],
            "album": "album2",
            "url": "url2",
            "date": "test",
            "duration": 4.54,
        }
    ]
}


total_duration = 0
for track in playlist["tracks"]:
    total_duration += track["duration"]
    print(total_duration)
