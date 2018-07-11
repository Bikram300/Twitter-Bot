import tweepy
import time
#mainmenu
while True:
    print("1.Retrive Tweets")
    print("2.Count the followers")
    print("3.Determine the sentiment")
    print("4.Determine location,language and time zone")
    print("5.compare tweets")
    print("6.Analyre top usage")
    print("7.Tweet a message")
    print("8.exit")
    choice=int(input("Enter your choice: "))
    consumer_key='nUryARrGKjKe9WAsiNn4XzkFI'
    consumer_secret='78ME9d7ed8wvAYzOz0q2F7y4sCz88JBUskdBwhbPoFo5hoSi93'
    access_token='1011137809758019584-CkwfiGz6yPc64fRLLvcUCcUJN4oC9H'
    access_token_secret='rbG4oU4P5l6jujaYoeXVVJbrQKqb2lC422IPW21ebegka'
    auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
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
    def location():
        user_id = input("enter any id to see locatione:")
        user = api.get_user(user_id)
        print("Location: ",user.location)
        print("Time Zone: ",user.time_zone)
        print("Language: ",user.lang)
    def direct_message():
        user_id= input("enter the id to sent message:")
        message=input("eneter any message:")
        api.send_direct_message(user=user_id,text=message)
    def sentimental():
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token,access_token_secret)
        api = tweepy.API(auth)
        username=input("enter any user id:")
        tweets = api.user_timeline(screenname=username, count=20)
        tmp = []
        tweets_for_csv = [tweet.text for tweet in tweets]
        for j in tweets_for_csv:
            tmp.append(j)
        count1 = 0
        count2 = 0
        count3 = 0
        print(tmp)
        from paralleldots import set_api_key,get_api_key,sentiment
        set_api_key("M6aheAI13WZLXrxV9Gv3rsm8Fc8kXYKuYapZ7n2G8Wo")
        get_api_key()
        for  t in tmp:
            a = sentiment(t)
            if a['sentiment'] == 'positive':
               count1 += 1
            if a['sentiment'] == 'negative':
               count2 += 1
            if a['sentiment'] == 'neutral':
                count3+= 1
        if (count1 > count2) and (count1 > count3):
               print("postive")
        if (count2 > count3) and (count2 > count1):
                print("negative")
        if (count3 > count2) and (count3 > count1):
                print("neutral")
    def compare():
            user_id = input("enter 1st id Count the compare:")
            user = api.get_user(user_id)
            a1= user.followers_count
            user_id1 = input("enter 2nd id to compare:")
            user1 = api.get_user(user_id1)
            a2 = user1.followers_count
            if a1>a2:
                print("{} is the best user of twitter".format(user.name))
            else:
                print("{} is the best user of tweeter".format(user1.name))

    if choice==1:
        search()
    if choice==2:
        follow()
    if choice==3:
        status()
    if choice==4:
        location()
    if choice==7:
        direct_message()
    if choice==6:
        sentimental()
    if choice==5:
        compare()
    if choice==8:
        exit()