import feedparser
import pandas as pd
##Enter Your Local News Feed if desired
##CNN RSS sometimes returns no description
##https://www.wyff4.com/topstories-rss
local_news_rss_link = ""
newsfeed = feedparser.parse(local_news_rss_link)
cnnnewsfeed = "http://rss.cnn.com/rss/cnn_topstories.rss"
globalnewsfeed = feedparser.parse(cnnnewsfeed)

def news_feed():
    if (len(local_news_rss_link)==0):
        cnnstart_df = pd.DataFrame(globalnewsfeed.entries)
        cnnfinal_df = cnnstart_df.iloc[:,[0,9,3]]
        cnnfinal_df.columns.values[0] = "Story"
        cnnfinal_df.columns.values[1] = "Summary"
        cnnfinal_df.columns.values[2] = "Link"
        return cnnfinal_df
    else:
        start_df = pd.DataFrame(newsfeed.entries)
        final_df = start_df.iloc[:, [0,4,3]]
        final_df.columns.values[0] = "Story"
        final_df.columns.values[1] = "Summary"
        final_df.columns.values[2] = "Link"
        final_df['Description'] = final_df.Summary.str.replace(r'<[^>]+>', '')
        return final_df.iloc[:, [0,3,2]]