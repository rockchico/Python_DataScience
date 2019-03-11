empty_dict = {}
empty_dict2 = dict()

grades = {"kkk": 90, "www": 78, "ddd": 89}

kkk_grade = grades["kkk"]

print(kkk_grade)

print ("ddd" in grades)



tweet	=	{
    "user"	:	"joelgrus",
	"text"	:	"Data	Science	is	Awesome",
	"retweet_count"	:	100,
	"hashtags"	:	["#data",	"#science",	"#datascience",	"#awesome",	"#yolo"]
}

tweet_keys = tweet.keys()
tweet_values = tweet.values()
tweet_items = tweet.items()

print(list(tweet_keys))
print(list(tweet_values))
print(list(tweet_items))
