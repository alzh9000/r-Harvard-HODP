import pandas as pd
parsed = pd.read_csv("r-Harvard data/columbia_comments.csv",
                     usecols=["body", "timestamp"])
parsed.dropna(subset=["body"], inplace=True)

num_mentions = 0
harvard_posts = []

for row in parsed:
    for i in range(0, parsed[row].size):
        if("harvard" in parsed[row].iloc[i].lower()):
            harvard_posts.append([parsed.body, parsed.timestamp])
            num_mentions += 1

harvard_posts = pd.DataFrame(harvard_posts, columns=['body', 'timestamp'])

harvard_posts.to_csv(r'columbia_comments_final.csv')
print(num_mentions)
