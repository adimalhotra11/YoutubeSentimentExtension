import Hidden #import API key and service details
import CommentExtractor
import RemoveEmoji
from apiclient.discovery import build

youtube = build(Hidden.YOUTUBE_API_SERVICE_NAME,
              Hidden.YOUTUBE_API_VERSION,
              developerKey=Hidden.api_key)

comments = []  #this will store all the comments we will be extracting using the API

limit = 100 #top 100 comments to be extracted (Enough to Find the Sentiment of a video.)
vid = input("Enter video id: ")
video_id = vid


match = CommentExtractor.get_comment_threads(youtube, video_id, limit)
next_page_token = match["nextPageToken"]
CommentExtractor.load_comments(match) 

filtered_comments=[]

for comment in comments:
    com = RemoveEmoji.remove_emoji(comment)
    filtered_comments.append(com)
print(filtered_comments)
