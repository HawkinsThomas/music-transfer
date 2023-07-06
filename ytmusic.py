from ytmusicapi import YTMusic
import json
ytmusic = YTMusic("oauth.json")

search_results = ytmusic.get_liked_songs(3000)

# parsed = json.loads(search_results)

# print(search_results)

extract_name = lambda x: x['name']

tracks = []

for track in search_results['tracks']:
    names = map(extract_name, track['artists'])
    tracks.append({ 'title': track['title'], 'artists': ", ".join(names) })
filename = "likes.json"

with open(filename, 'w') as file:
    json.dump(tracks, file)