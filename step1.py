from googleapiclient.discovery import build
import pandas as pd
import seaborn as sns

api_key='AIzaSyD437jMpyE701yL2G5NVWFoWOkjcU3IAkY'
channel_ids=['MayapurTVOfficial',
             'GaurGopalDas',
            'tseries']

youtube=build('youtube','v3',developerKey=api_key)

##Function to get channel statistics
def get_channel_stats(youtube,channel_ids):
    all_data=[]
    request = youtube.channels.list(
        part='snippet,contentDetails,statistics',
        id=','.join(channel_ids))
    response=request.execute()

    for i in range(len(response['items'])):
        data = dict(Channel_name = response['items'][i]['snippet']['title'],
        Subscribers=response['items'][i]['statistics']['SubsriberCount'],
        Views = response['items'][i]['statistics']['ViewCount'],
        TotalVideos = response['items'][i]['statistics']['videoCount'])

        all_data.append(data)

    print(response)    
    print(all_data)
    return response

get_channel_stats(youtube,channel_ids)