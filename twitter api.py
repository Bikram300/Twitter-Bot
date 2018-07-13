import tweepy
#mainmenu
print("1.Retrive Tweets")
print("2.Count the followers")
print("3.Determine the sentiment")
print("4.Determine location,language and time zone")
print("5.compare tweets")
print("6.Analyre top usage")
print("7.Tweet a message")
print("8.exit")
choice=int(input("Enter your choice: "))
consumer_key='######'
cosumer_secret='########'
access_token='#########'
access_token_secret='##########'
auth=tweepy.OAuthHandler(consumer_key,cosumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)
def search():
    user_search=input("enter any hash tag search")
    tweets=api.search('user_search',lang="en",count=5,tweet_mode="extended")
    print(tweets)
    for tweet in tweets:
         print("--------------")
         print(tweet.full_text)
         print("--------------")
def follow():
        user_id=input("enter any id to count the follower:")
        user=api.get_user(user_id)
        print(user.screen_name)
        print(user.friends_count)
        return
def status():
    status=input("enter any status")
    user_id = input("enter any id to count the follow:")
    api.update_status(status,user_id)
if choice==1:
    search()
if choice==2:
    follow()
if choice==3:
    status()
if choice==8:
    exit()
