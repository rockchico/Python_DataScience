grades = {}

grades = {'jose': 45, 'joao': 78}

jose_tem_notas = 'jose' in grades
maria_tem_notas = 'maria' in grades

print(jose_tem_notas)
print(maria_tem_notas)

jose_nota = grades.get('jose', 0)
maria_nota = grades.get('maria', 0)

print(maria_nota)

grades['maria'] = 12

print(len(grades))


tweet = {
    "user" : "joelgrus",
    "text" : "Data Science is Awesome",
    "retweet_count" : 100,
    "hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}

tweet_keys = tweet.keys() # list of keys
print(tweet_keys)
tweet_values = tweet.values() # list of values
print(tweet_values)
tweet_items = tweet.items() # list of (key, value) tuples
print(tweet_items)
"user" in tweet_keys # True, but uses a slow list in
"user" in tweet # more Pythonic, uses faster dict in
