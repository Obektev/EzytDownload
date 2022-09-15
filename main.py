from pydoc import resolve
from googleapiclient.discovery import build
import pandas as pd
import seaborn as sns

api_key = 'AIzaSyCopCP-3NGlgIitn7Tyd-HS_9U69Z8xA98'
#channel_id = 'UCnz-ZXXER4jOvuED5trXfEA'
#channel_id = input("Input channel url here: ").split("https://www.youtube.com/channel/",1)[1]
channel_id = "UCh-GSoWgO7_SK7bnV8EBqWQ"
youtube = build('youtube', 'v3', developerKey=api_key)

def get_channel_stats(youtube, channel_id):
    all_data = []
    request = youtube.videos().list(
                part='snippet',
                id=channel_id)
    response = request.execute() 
    print(response, "  \n\n\n")
    print(response['items'])
    for i in range(len(response['items'])):
        data = dict(Channel_name = response['items'][i]['snippet']['title'],
                    Subscribers = response['items'][i]['statistics']['subscriberCount'],
                    Views = response['items'][i]['statistics']['viewCount'],
                    Total_videos = response['items'][i]['statistics']['videoCount'],
                    playlist_id = response['items'][i]['contentDetails']['relatedPlaylists']['uploads'])
        all_data.append(data)
    
    return all_data

channel_statistics = get_channel_stats(youtube, channel_id)
print(pd.DataFrame(channel_statistics))