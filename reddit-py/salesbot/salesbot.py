import praw
import re
import os
keywords = {'GPU', 'Monitor', 'Keyboard'}
combined = '(' + ')|('.join(keywords) + ')'
reddit = praw.Reddit('bot1')
user = reddit.redditor('annesocks')
# read databse containing id's for each submission
if not os.path.isfile('sale_ids.txt'):
    sale_ids = []
else:
    with open('sale_ids.txt', 'r') as f:
        sale_ids = f.read()
        sale_ids = sale_ids.split('\n')
        sale_ids = list(filter(None, sale_ids))

subreddit = reddit.subreddit('buildapcsales')
for submission in subreddit.new(limit=10):
    if submission.id not in sale_ids:
        result = re.search(combined, submission.title, re.IGNORECASE)
        if result:
            print(submission.title)
            user.message(result.group(0).upper(),submission.title + '\n' + submission.shortlink)
            sale_ids.append(submission.id)

with open('sale_ids.txt', 'w') as f:
    for sale in sale_ids:
        f.write(sale + '\n')