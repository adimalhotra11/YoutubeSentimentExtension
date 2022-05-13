import Hidden #import API key and service details
import CommentExtractor
from apiclient.discovery import build

youtube = build(Hidden.YOUTUBE_API_SERVICE_NAME,
              Hidden.YOUTUBE_API_VERSION,
              developerKey=Hidden.api_key)

comments = []  #this will store all the comments we will be extracting using the API

limit1 = 100
limit = int(input("Enter number of comments: "))
vid = input("Enter video id: ")
video_id = vid

if limit>100:
  if limit%100==0:
    count=limit/100-1
  else:
    count=limit/100
else:
  count=0
  limit1=limit

match = CommentExtractor.get_comment_threads(youtube, video_id, limit1)
next_page_token = match["nextPageToken"]
CommentExtractor.load_comments(match) 

print(len(comments))