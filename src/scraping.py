# Make HTTP requests
import requests# Scrape data from an HTML document
from bs4 import BeautifulSoup# I/O
import os# Search and manipulate strings
import re

GENIUS_API_TOKEN='duv0uA_KKZDyL2GAmxKwNyyDyaCNY7EZODEOAgYJzEzdYFF0Yt0OTMn7g_85wA2x'

def request_artist_info(artist_name, page):
    base_url = 'https://api.genius.com'
    headers = {'Authorization': 'Bearer ' + GENIUS_API_TOKEN}
    search_url = base_url + '/search?per_page=10&amp;page=' + str(page)
    data = {'q': artist_name}
    response = requests.get(search_url, data=data, headers=headers)
    return response  # Get http://Genius.com song url's from artist object

def request_song_url(artist_name, song_cap):
    page = 1
    songs = []

    while True:
        response = request_artist_info(artist_name, page)
        json = response.json()  # Collect up to song_cap song objects from artist
        song_info = []
        for hit in json['response']['hits']:
            if artist_name.lower() in hit['result']['primary_artist']['name'].lower():
                song_info.append(hit)

        # Collect song URL's from song objects
        for song in song_info:
            if (len(songs) < song_cap):
                url = song['result']['url']
                songs.append(url)

        if (len(songs) == song_cap):
            break
        else:
            page += 1

    # print('Found {} songs by {}'.format(len(songs), artist_name))
    return songs

# DEMO

# Scrape lyrics from a http://Genius.com song URL
def scrape_song_lyrics(url):
    page = requests.get(url)
    html = BeautifulSoup(page.text, 'html.parser')
    cs = html.select('div[class^="Lyrics__Container"]')

    def get_text(elements):
        text = ''
        for c in elements:
            for t in c.select('a, span'):
                t.unwrap()
            if c:
                c.smooth()
                text += c.get_text(strip=True, separator='\n')
        return text
    if cs:
        lyrics = get_text(cs)
    else:
        lyrics = get_text(html.select('.lyrics'))

    #remove identifiers like chorus, verse, etc
    lyrics = re.sub(r'[\(\[].*?[\)\]]', '', lyrics)
    #remove empty lines
    lyrics = os.linesep.join([s for s in lyrics.splitlines() if s])
    return(lyrics)# DEMO

# x= request_song_url('Lana Del Rey', 2)
# for url in x:
#     scrape_song_lyrics(url)
def write_lyrics_to_file(artist_name, song_count):
    f = open('lyrics/' + 'lyrics' + '.txt', 'ab')
    urls = request_song_url(artist_name, song_count)
    for url in urls:
        lyrics = scrape_song_lyrics(url)
        f.write(lyrics.encode("utf8"))
    f.close()
    #num_lines = sum(1 for line in open('lyrics/' + artist_name.lower() + '.txt', 'rb'))
   # print('Wrote {} lines to file from {} songs'.format(num_lines, song_count))

# DEMO

artists=['Bartika eam Rai', 'Narayan Gopal', 'Jerusha Rai', 'Ankit Shrestha', 'Simma Rai']

for artist in artists:
    write_lyrics_to_file(artist, 1)
#