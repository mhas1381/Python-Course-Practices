facebook_posts = [
    {"like": 5, "comments": 12},
    {"like": 6, "comments": 7},
    {"like": 1, "comments": 2},
    {"comments" : 10 , "shares":3},
    {"comments" : 4 , "shares":6},
    {"like": 2, "comments": 9}
]

total_likes = 0
for post in facebook_posts:
    try:
        total_likes += post['like']
    except KeyError:
        pass


print(total_likes)