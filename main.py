import sys
import spotipy
import spotipy.util as util
from plotly.graph_objs import Bar, Layout
from plotly import offline
from secrets import cid, secret, uri

scope = 'user-top-read'

def main():
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print("Usage: %s username" % (sys.argv[0],))
        sys.exit()
    
    token = util.prompt_for_user_token(username,
                                    scope,
                                    client_id=cid,
                                    client_secret=secret,
                                    redirect_uri=uri)
    if token:        
        question_1 = input("If you want your top artists. Type 'artists'. " \
         "If you want your top tracks. Type 'tracks': ")
        if question_1.lower() == 'artists':
            sp = spotipy.Spotify(auth=token) 
            artists = sp.current_user_top_artists(limit=20, offset=0, time_range='medium_term')
            makeChartArtists(artists)
        elif question_1.lower() == 'tracks':
            sp = spotipy.Spotify(auth=token)
            tracks = sp.current_user_top_tracks(limit=20, offset=0, time_range='medium_term')
            makeChartTracks(tracks)
        else:
            print("Wrong Response. Try Again")
            main()
        
    else:
        print("Can't get token for", username)

def makeChartArtists(artists):
    artists_names = []
    artists_popularity = []
    for i in range(20):
        artists_names.append(artists['items'][i]['name'])
        artists_popularity.append(artists['items'][i]['popularity'])

    # Visualize the Results
    x_values = artists_names
    y_values = artists_popularity
    data = [Bar(x=x_values, y=y_values, marker={'color': 'rgba(252, 198, 3, 1)'})]

    x_axis_config = {'title': 'Your Top Artists'}
    y_axis_config = {'title': 'Popularity'}
    my_layout = Layout(title='Top Listened to Artists and their Popularity', xaxis=x_axis_config, yaxis=y_axis_config)
    offline.plot({'data': data, 'layout': my_layout}, filename='artists.html')

def makeChartTracks(tracks):
    tracks_names = []
    tracks_popularity = []
    for i in range(20):
        tracks_names.append(tracks['items'][i]['name'])
        tracks_popularity.append(tracks['items'][i]['popularity'])

    # Visualize the Results
    x_values = tracks_names
    y_values = tracks_popularity
    data = [Bar(x=x_values, y=y_values, marker={'color': 'rgba(233, 1, 117, 1)'})]

    x_axis_config = {'title': 'Your Top Songs'}
    y_axis_config = {'title': 'Popularity'}
    my_layout = Layout(title='Top Listened to Songs and their Popularity', xaxis=x_axis_config, yaxis=y_axis_config)
    offline.plot({'data': data, 'layout': my_layout}, filename='songs.html')
    


main()

# How to run the program
# >>python main.py {spotify uri}
# Example >>python main.py 11726172616sdksdj