#!/usr/bin/python


import feedparser

def rss(phenny, input):
	query = input.group(2)
	values = { "bbctech": "http://feeds.bbci.co.uk/news/technology/rss.xml", "bbctop": "http://feeds.bbci.co.uk/news/rss.xml", "tf": "http://feed.torrentfreak.com/Torrentfreak/" }

	feed_url = values.get(query, query)

	feed = feedparser.parse(feed_url)
	latest = feed["items"][0]
	phenny.say("\002"+feed["channel"]["title"]+"\002 - "+latest["date"]+" - "+latest["title"]+" "+latest["summary"])
	phenny.say(latest["summary"])
rss.commands = ['rss']
