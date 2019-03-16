import praw
from res import look, min_break, summon
import random
import time
# TODO Maybe add support for thesaurus lookups to produce more undefined behavior

# 03/15/19 get login working

# client_id eDZ6LmgUNC24Jw
# client_secret P5MTRkvIFkuIFvU-lRdwr-epgIM
# username HedonismBotBot
# password djambichocolateicing


def getRandomQuote():
    l = random.choice(look.values())  # Get random set of quotes
    return random.choice(l)  # return random quote from that list


def getQuoteFromContext(context):
    # Get all the keys from the look up and try to match words to them
    for k in look.keys():
        for e in k:
            if e in context.lower():
                return random.choice(look[k])
    # Otherwise get a random quote
    return None


def timeLimitPost(msg, p):
    # Only print if we have exceeded the min break
    if time.time() - last_post > min_break:
        p.reply(msg)
        last_post = time.time()


if __name__ == '__main__':
    reddit = praw.Reddit(client_id='eDZ6LmgUNC24Jw', client_secret='P5MTRkvIFkuIFvU-lRdwr-epgIM',
                         username='HedonismBotBot', password='djambichocolateicing', user_agent='test for /u/HedonismBotBot')

    subreddit = reddit.subreddit('HedonisticPosts')

    print(subreddit.display_name)
    print(subreddit.title)
    print(subreddit.description)

    comments = subreddit.stream.comments()

    last_post = 0 # Will try to automatically post when it starts

    posts_visited = list() # List of the posts we have already posted in automatically.

    for comment in comments:

        print("Post Title: " + comment.submission.title + '\n\n')

        un = comment.submission.author.name

        print("Tick")



        if comment.body == summon:
            try:
                parent_comment = reddit.comment(
                    id=comment.parent_id.split('_')[-1])
                if getQuoteFromContext(parent_comment.body) != None:
                    msg = getQuoteFromContext(
                        parent_comment.body).format(parent_comment.author)
                else:
                    msg = getRandomQuote().format(parent_comment.author)
                print("I was summoned to comment on upper comment with: {}".format(msg))
                comment.reply(msg)
            except:
                continue
        elif summon in comment.body:
            if getQuoteFromContext(comment.body) != None:
                msg = getQuoteFromContext(comment.body).format(comment.author)
            else:
                msg = getRandomQuote().format(comment.author)
            print("Replying to a user's request to hedbot themselves with: {}".format(msg))
            comment.reply(msg)
        # Automatic posting option, happens once per hour and only once per post
        elif getQuoteFromContext(comment.body) != None:
            if time.time() - last_post > min_break and comment.submission.id not in posts_visited:
                msg = getQuoteFromContext(comment.body)
                print("Replying automatically to a post with: {}".format(msg))
                comment.replay(msg)
                last_post = time.time()
                posts_visited.append(comment.submission.id)

        if getQuoteFromContext(comment.submission.title) != None:
            # Get quote based on title of post
            msg = getQuoteFromContext(comment.submission.title).format(un)

            # Post the quote as a top level comment
            if time.time() - last_post > min_break and comment.submission.id not in posts_visited:
                print("Replying to this post because of the title with: {}\n".format(msg))
                comment.submission.reply(msg)
                last_post = time.time()
                posts_visited.append(comment.submission.id)
            


