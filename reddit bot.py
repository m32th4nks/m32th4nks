import praw
import os
import random

import config
import thanks
import spit

reddit = praw.Reddit(username = config.username,
                        password = config.password,
                        client_id = config.client_id,
                        client_secret = config.client_secret,
                        user_agent = "Me too thanks bot (pls don't ban me admins...)")
print("Logged into Reddit...")

thanks = thanks.thanks
spit = spit.spitfacts
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
print("")

for comment in subreddit.stream.comments():
    commentTally += 1

    #try/except because attempting to comment in a banned sub will throw an error
    #ps: beware of large if statment block. Reader discretion is advised
    try:

        print('{:,}'.format(commentTally) + " : " + str(replyTally) +  " | " + comment.id + " | " + str(comment.author.name) + ":")
                
        if "me too thanks" in comment.body.lower() in comment.body.lower() and comment.author != reddit.user.me() and comment.id not in comments_replied_to:
            comments_replied_to.append(str(comment.id))
            with open ("comments_replied_to.txt", "a") as f:
                f.write(comment.id + "\n")

            comment.reply(random.choice(thanks))
            replyTally += 1

        elif "u/m32th4nks" in comment.body.lower() in comment.body.lower() and comment.author != reddit.user.me() and comment.id not in comments_replied_to:
            comments_replied_to.append(str(comment.id))
            with open ("comments_replied_to.txt", "a") as f:
                f.write(comment.id + "\n")

            comment.reply("Oh hey that's me ^^^too ^^^thanks")
            replyTally += 1

        elif "me two thanks" in comment.body.lower() in comment.body.lower() and comment.author != reddit.user.me() and comment.id not in comments_replied_to:
            comments_replied_to.append(str(comment.id))
            with open ("comments_replied_to.txt", "a") as f:
                f.write(comment.id + "\n")

            comment.reply("Me three thanks")
            replyTally += 1

        elif "good bot" in comment.body.lower() in comment.body.lower() and comment.author != reddit.user.me() and comment.id not in comments_replied_to:
            if comment.parent().author == reddit.user.me():
                comments_replied_to.append(str(comment.id)) 
                with open ("comments_replied_to.txt", "a") as f:
                    f.write(comment.id + "\n")
                    
                comment.reply("You humans make me so happy :')")
                replyTally += 1 

        elif "bad bot" in comment.body.lower() in comment.body.lower() and comment.author != reddit.user.me() and comment.id not in comments_replied_to:
            if comment.parent().author == reddit.user.me():
                comments_replied_to.append(str(comment.id))
                with open ("comments_replied_to.txt", "a") as f:
                    f.write(comment.id + "\n")
                    
                comment.reply("I-I didn't even like you anyways... ^:(")
                replyTally += 1

        elif "hit me with them spitfacts boi" in comment.body.lower() in comment.body.lower() and comment.author != reddit.user.me() and comment.id not in comments_replied_to:
            if comment.parent().author == reddit.user.me():
                comments_replied_to.append(str(comment.id))
                with open ("comments_replied_to.txt", "a") as f:
                    f.write(comment.id + "\n")
                    
                comment.reply(random.choice(spit))
                replyTally += 1

        elif "spit facts" in comment.body.lower() in comment.body.lower() and comment.author != reddit.user.me() and comment.id not in comments_replied_to:
            if comment.parent().author == reddit.user.me():
                comments_replied_to.append(str(comment.id))
                with open ("comments_replied_to.txt", "a") as f:
                    f.write(comment.id + "\n")
                    
                comment.reply(random.choice(spit))
                replyTally += 1

        elif "spitfacts" in comment.body.lower() in comment.body.lower() and comment.author != reddit.user.me() and comment.id not in comments_replied_to:
            if comment.parent().author == reddit.user.me():
                comments_replied_to.append(str(comment.id))
                with open ("comments_replied_to.txt", "a") as f:
                    f.write(comment.id + "\n")
                    
                comment.reply(random.choice(spit))
                replyTally += 1
            
    except:
        pass
    

