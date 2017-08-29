import praw
import os
import random

import config
import thanks

reddit = praw.Reddit(username = config.username,
                        password = config.password,
                        client_id = config.client_id,
                        client_secret = config.client_secret,
                        user_agent = "Me too thanks bot (pls don't ban me admins...)")
print("Logged into Reddit...")

thanks = thanks.thanks
print("Loaded 'thanks.py...'")

if not os.path.isfile("comments_replied_to.txt"):
    comments_replied_to = []
else:
    with open("comments_replied_to.txt", "r") as f:
        comments_replied_to = f.read()
        comments_replied_to = comments_replied_to.split("\n")
print("Loaded 'comments_replied_to.txt'...")

commentTally = 0
replyTally = 0

subreddit = reddit.subreddit("all")
print("Preparing to stream...")

for comment in subreddit.stream.comments():
    
    commentTally += 1

    if(comment.author != reddit.user.me()):
        print(str(commentTally) + ":" + str(replyTally) + " | " + comment.id + " | " + str(comment.author))
    else:
        print(str(commentTally) + ":" + str(replyTally) + " | " + comment.id + " | " + str(comment.author) + " ******")

    try:
        if "Me too thanks" in comment.body in comment.body and comment.author != reddit.user.me() and comment.id not in comments_replied_to:
            comments_replied_to.append(str(comment.id))
            with open ("comments_replied_to.txt", "a") as f:
                    f.write(comment.id + "\n")

            comment.reply(random.choice(thanks))
            print("")
            print("*** Replied to comment " + comment.author.name)
            print("")
            
            replyTally += 1
            
        elif "me too thanks" in comment.body in comment.body and comment.author != reddit.user.me() and comment.id not in comments_replied_to:
            comments_replied_to.append(str(comment.id))
            with open ("comments_replied_to.txt", "a") as f:
                    f.write(comment.id + "\n")

            comment.reply(random.choice(thanks))
            print("")
            print("Replied to comment " + comment.author.name)
            print("")
            
            replyTally += 1

        elif "m32th4nks" in comment.body in comment.body and comment.author != reddit.user.me() and comment.id not in comments_replied_to:
            comments_replied_to.append(str(comment.id))
            with open ("comments_replied_to.txt", "a") as f:
                    f.write(comment.id + "\n")

            comment.reply("Yup that's me ^^^too ^^^thanks")
            print("")
            print("Replied to comment " + comment.author.name)
            print("")
            
            replyTally += 1
    except:
        pass
    
