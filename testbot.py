import praw
import time

# Login to reddit.
reddit = praw.Reddit(user_agent = "TestBot by Toqoz /u/Qhosts")
reddit.login()

# Define words to match in an array.
words_to_match = ['test', 'test2']
# A cache for comments that have already been responded to.
cache = []


def run_bot():
    # Get stuff from the subreddit 'test'
    subreddit = reddit.get_subreddit("test")
    # Get comments from that subreddit, 25
    comments = subreddit.get_comments(limit=25)
    # For each comment, search and respond.
    for comment in comments:
        comment_text = comment.body.lower()
        isMatch = any(string in comment_text for string in words_to_match)
        # Respond to the comment (if it hasnt already).
        if comment.id not in cache and isMatch:
            comment.reply("this is a test.")
            cache.append(comment.id)

while True:
    run_bot() # Run the bot!
    time.sleep(10) # Not too often…
