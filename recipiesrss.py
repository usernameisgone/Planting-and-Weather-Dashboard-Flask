import feedparser
import pandas as pd
foodfeed = feedparser.parse("https://www.bonappetit.com/feed/recipes-rss-feed/rss")


def food_news_feed():
    start_df = pd.DataFrame(foodfeed.entries)
    final_df = start_df.iloc[:, [0,9,3]]
    final_df.columns.values[0] = "Title"
    final_df.columns.values[1] = "Summary"
    final_df.columns.values[2] = "Link"
    return final_df
