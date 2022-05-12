from apiclient.discovery import build

api_key = 'AIzaSyDsHvp3BegrkHXnuKp_7lIoHbdWu1Qz4PY'
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

youtube = build(YOUTUBE_API_SERVICE_NAME,
              YOUTUBE_API_VERSION,
              developerKey=api_key)

ucom = []

def load_comments(match):
    for item in match["items"]:
        comment = item["snippet"]["topLevelComment"]
        author = comment["snippet"]["authorDisplayName"]
        text = comment["snippet"]["textDisplay"]
        print("Comment by user {}: {}".format(author, text))
        ucom.append(text)


def get_comment_threads(youtube, video_id, limit):
    results = youtube.commentThreads().list(
        part="snippet",
        maxResults=limit,
        videoId=video_id,
        textFormat="plainText"
    ).execute()
    return results

def get_comment_thread(youtube, video_id, mytoken, limit):
    results = youtube.commentThreads().list(
        part="snippet",
        maxResults=limit,
        videoId=video_id,
        textFormat="plainText",
        pageToken=mytoken
    ).execute()
    return results

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

match = get_comment_threads(youtube, video_id, limit1)
next_page_token = match["nextPageToken"]
load_comments(match)