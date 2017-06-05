import praw
import config
import time
import os
import requests
#example_list = ["Test","Hello","123",0]
#example_list.append(32.10)
#print example_list
def bot_login():
    print "loggin in..."
    r=praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = "naweel1496's joke comment responder v0.1")
    print "Logged in !"
    return r
def run_bot(r,comments_replied_to):
    print "obtaining 25 seconds..."
    for comment in r.subreddit('test').comments(limit=25):
        if "dog" in comment.body and comment.id not in comments_replied_to and comment.author != r.user.me():
            print "String with \"!joke\"found in comment" + comment.id
            comment_reply = "You requested a Chunk Norris joke. Here it is:\n\n"
            joke = requests.get('http://api.icndb.com/jokes/random').json()['value']['joke']
            #comment_reply = commnent_reply + joke
            comment_reply += ">" + joke
            comment_reply += "\n\n This joke come from [ICNDb.com](http://icndb.com)."
            #comment.reply ("I also love dogs! [Here](http://www.wallpapermania.eu/images/lthumbs/2013-04/4816_Look-at-me-Im-sweet-beautiful-small-dog.jpg) is an image of one")
            print "Replied to comment" + comment.id

            comments_replied_to.append(comment.id)
            with open("comments_replied_to.txt" , "a") as f:
                f.write(comment.id + "\n")
    print "sleep for 10 seconds"
    time.sleep(10)
def get_saved_comments():
    if not os.path.isfile("comments_replied_to.txt"):
        comments_replied_to = []
    else:
        with open("comments_replied_to.txt", "r") as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")
    return comments_replied_to

r = bot_login()
comments_replied_to = get_saved_comments()
print comments_replied_to 

while True:
    
    run_bot(r,comments_replied_to)

