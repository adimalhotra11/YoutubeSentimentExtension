def load_comments(comments,match):
    for item in match["items"]:
        comment = item["snippet"]["topLevelComment"]
        author = comment["snippet"]["authorDisplayName"]
        text = comment["snippet"]["textDisplay"]
        print("Comment by user {}: {}".format(author, text))
        comments.append(text)


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