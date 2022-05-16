import Hidden #import API key and service details
import CommentExtractor
import RemoveEmoji
import SentimentAnalysis
from apiclient.discovery import build

youtube = build(Hidden.YOUTUBE_API_SERVICE_NAME,
              Hidden.YOUTUBE_API_VERSION,
              developerKey=Hidden.api_key)

comments = []  #this will store all the comments we will be extracting using the API

limit = 100
#limit = int(input("Enter number of comments: "))
vid = input("Enter video id: ")   #Get the input from the user.
video_id = vid
if limit>100:
  if limit%100==0:
    count=limit/100-1
  else:
    count=limit/100
else:
  count=0
  #limit1=limit


match = CommentExtractor.get_comment_threads(youtube, video_id, limit)
next_page_token = match["nextPageToken"]
CommentExtractor.load_comments(comments,match) 

while count>0:
    if count==1:
      match1 = CommentExtractor.get_comment_thread(youtube, video_id, next_page_token, (limit-(limit/100)*100))
    else:    
      match1 = CommentExtractor.get_comment_thread(youtube, video_id, next_page_token, 100)
    next_page_token = match1["nextPageToken"]
    CommentExtractor.load_comments(comments,match1)
    count=count-1

filtered_comments=[]
print("\n Filtered comments:")
for comment in comments:
    com = RemoveEmoji.remove_emoji(comment)
    filtered_comments.append(com)
print(filtered_comments)

SentimentAnalysis.SentimentReportGenerator(filtered_comments)