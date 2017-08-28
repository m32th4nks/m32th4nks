import praw
import config
import thanks
import time
import os
import random

#saves 'Me too thanks' variations to memory
thanks = thanks.thanks

reddit = praw.Reddit(username = config.username,
                        password = config.password,
                        client_id = config.client_id,
                        client_secret = config.client_secret,
                        user_agent = "Me too thanks bot")
print("Logged in")
print("")

#saves all previous comment ID's to memory
if not os.path.isfile("comments_replied_to.txt"):
    comments_replied_to = []
else:
    with open("comments_replied_to.txt", "r") as f:
        comments_replied_to = f.read()
        comments_replied_to = comments_replied_to.split("\n")
print("Loaded 'comments_replied_to.txt'")
print("")

#specifies which subreddit comments will be streamed from
subreddit = reddit.subreddit("me_irl+meirl+4chan+absolutelynotme_irl+2meirl4meirl+dankmemes+fellowkids+woof_irl+hentai_irl")
#subreddit = reddit.subreddit("all")

#streams all comments from specified subreddit
while True:
    for comment in subreddit.stream.comments():
        try:
            #sees if comment has 'the goods', and if so replies with random 'Me too thanks'. This is where the magic happens
            if "Me too thanks" in comment.body or "me too thanks" in comment.body and comment.id not in comments_replied_to and comment.author != "m32th4nks" and comment.author != "me_too-thanks":
                if(comment.author != "m32th4nks"):
                    comments_replied_to.append(comment.id)
                    print("Replied to comment " + comment.id + " by " + str(comment.author))
                    with open ("comments_replied_to.txt", "a") as f:
                        f.write(comment.id + "\n")
                    comment.reply(random.choice(thanks))

            if comment.id not in comments_replied_to:
                print("---")
                print(comment.body)
                print("---")
                print("Reply by: " + '"' + str(comment.author) + '"')
                print("")
            elif comment.author != "m32th4nks":
                print("Comment: " + str(comment.id) + " already responded to")
                print("")
            else:
                print("******")
                print(comment.body)
                print("******")
                print("Reply by: " + '"' + str(comment.author) + '"')
                print("")
                    
        except Exception as e:
            pass


