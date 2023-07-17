def create_youtube_video(title,description):
	video = {"title": title,"description": description,"likes":0,"dislikes":0,"comments":{}}
	return video

def like(video):
	if "likes" in video:
		video["likes"] += 1
	return video

def dislike(video):
	if "dislikes" in video:
		video["likes"] += 1
	return video
def add_comment(video,username,comment_text):
	video["comments"]={username:comment_text}




video = create_youtube_video("hi","hey")
print(video)
like(video)




