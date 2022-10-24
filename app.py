from pytwitter import Api
import twitter
import time
import pandas as pd


search_terms = input("list terms: ").split(",")
tweet_id_log = pd.read_csv("CIA/tweet_id.csv")
skip = False

api = Api(
    
    consumer_key=twitter.keys("consumer_key"),
    consumer_secret=twitter.keys("consumer_secret"),
    access_token=twitter.keys("access_token_key"),
    access_secret=twitter.keys("access_token_secret"),
)

while True:
    try:
        #search_terms = ["#nftphotography", "@rawdao", "@obscuradao", "@QuantumNFT"]
        
        
        for term in search_terms:
            
            print(term)
            
            time.sleep(2)
            
            tweets = api.search_tweets(
                query= term, 
                max_results= round(50/len(search_terms))
                )
            
            time.sleep(2)
            me = "1374352984105123842"
            for tweet in tweets.data:
                print(tweet)
                try:
                    time.sleep(3)
                    if skip != True:
                        api.like_tweet(me, tweet_id=tweet.id)
                        tweet_id_log = tweet_id_log.append({'tweet_id': tweet.id}, ignore_index=True)
                        tweet_id_log.to_csv("CIA/tweet_id.csv")
                        print("liked")
                
                except Exception as e:
                    print(e)
                    if (e.message["title"] == "Too Many Requests"):
                        print("skipping")
                        try:
                            time.sleep(20)
                            api.like_tweet(me, tweet_id=tweet.id)
                            tweet_id_log = tweet_id_log.append({'tweet_id': tweet.id}, ignore_index=True)
                            tweet_id_log.to_csv("CIA/tweet_id.csv")
                        except:
                            skip = True
        
        time.sleep(300)
        skip = False

        
    except Exception as e:
        print(e)
