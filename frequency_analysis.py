import pandas as pd

school_names = ["yale", "princeton", "columbia",
                "cornell", "dartmouth", "upenn", "brownu", "harvard"]
file_types = ["comments", "posts"]

for school_name in school_names:
    for file_type in file_types:
        parsed = pd.read_csv("r-Harvard data/" + school_name + "_" + file_type + ".csv",
                             usecols=["body", "timestamp"])
        parsed.dropna(subset=["body"], inplace=True)

        num_mentions = 0
        harvard_posts = []
        num_mentions_total = 0

        for row in parsed:
            for i in range(0, parsed[row].size):
                text = parsed[row].iloc[i].lower()
                num_mentions_total += text.count("harvard")
                if("harvard" in text):
                    harvard_posts.append(text)
                    num_mentions += 1

        harvard_posts = pd.DataFrame(
            harvard_posts, columns=['body'])

        csv_name = school_name + '_' + file_type + '_final.csv'
        harvard_posts.to_csv(csv_name)
        print(school_name.upper(), file_type, "#COMMENTS", num_mentions)
        print(school_name.upper(), file_type,
              "#MENTIONS TOTAL", num_mentions_total)
