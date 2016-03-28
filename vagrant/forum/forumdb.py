#
# Database access functions for the web forum.
# 

import time
import psycopg2
import bleach

## Database connection
DB = psycopg2.connect("dbname=forum")
c = DB.cursor()

## Get posts from database.
def GetAllPosts():
    '''Get all the posts from the database, sorted with the newest first.

    Returns:
      A list of dictionaries, where each dictionary has a 'content' key
      pointing to the post content, and 'time' key pointing to the time
      it was posted.
    '''
    c.execute("select content, time from posts order by time;")
    rows = c.fetchall()
    posts = [{'content': str(row[0]), 'time': str(row[1])} for row in rows]
	##    posts.sort(key=lambda row: row['time'], reverse=True)
    return posts

## Add a post to the database.
def AddPost(content):
    '''Add a new post to the database.

    Args:
      content: The text content of the new post.
    '''
    t = time.strftime('%c', time.localtime())
    content = bleach.clean(content)
    cmd = "insert into players values(%s, %s);"
    c.execute(cmd, (content, t,))
    DB.commit()
	##   DB.append((t, content))
