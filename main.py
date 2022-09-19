from pydoc import resolve
import re
from googleapiclient.discovery import build
import pandas as pd
import seaborn as sns
from pytube import YouTube

SAVE_PATH = 'download/'


api_key = 'AIzaSyCopCP-3NGlgIitn7Tyd-HS_9U69Z8xA98'
#channel_id = 'UCnz-ZXXER4jOvuED5trXfEA'
channel_id = 'UCX-USfenzQlhrEJR1zD5IYw'
#channel_id = input("Input channel url here: ").split("https://www.youtube.com/channel/",1)[1]
#channel_id = "UCh-GSoWgO7_SK7bnV8EBqWQ"
youtube = build('youtube', 'v3', developerKey=api_key)

videos = []
all_data = []

####################################################################################################### 
def video_download(video_link):
        
    getVideo = YouTube(video_link)
    videoStream = getVideo.streams[3]
    try:
        videoStream.download(SAVE_PATH)
        print("#DOWNLOAD SUCCESSFULY")
    except:
        print('SOME ERRORS HERE')
####################################################################################################### 

####################################################################################################### 
def get_channel_videos(youtube, playlist_id):
    request = youtube.playlistItems().list(
        part='snippet,contentDetails,status',
        playlistId=playlist_id,
        maxResults=100
    )
    response = request.execute()
    for i in range(len(response['items'])):
        video = dict( Video_name = response['items'][i]['snippet']['title'],
                      Video_link = 'https://www.youtube.com/watch?v='+response['items'][i]['contentDetails']['videoId'])
        videos.append(video)
#######################################################################################################     

#######################################################################################################
def get_channel_stats(youtube, channel_id):

    request = youtube.channels().list(
                part='snippet, statistics, contentDetails',
                id=channel_id)
    response = request.execute() 
    
    for i in range(len(response['items'])):
        data = dict(Channel_name = response['items'][i]['snippet']['title'],
                    Subscribers = response['items'][i]['statistics']['subscriberCount'],
                    Views = response['items'][i]['statistics']['viewCount'],
                    Total_videos = response['items'][i]['statistics']['videoCount'],
                    playlist_id = response['items'][i]['contentDetails']['relatedPlaylists']['uploads'])
        all_data.append(data)
    playlist_idABOBA = data['playlist_id']
#######################################################################################################    

get_channel_stats(youtube, channel_id)
get_channel_videos(youtube, all_data[0]['playlist_id'])
print(pd.DataFrame(all_data))
print(len(videos))
print('\n',pd.DataFrame(videos))