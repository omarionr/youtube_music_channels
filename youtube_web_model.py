# -*- coding:utf8 -*-
import re
import requests
from bs4 import BeautifulSoup


def get_videos_by_channel(channel_id):
    url = "https://www.youtube.com/channel/%s/videos" % channel_id
    res = requests.get(url)
    ret_txt = res.text
    search_obj = re.findall("watch\?v=.{11}", ret_txt)
    video_set = set()
    for item in search_obj:
        video_set.add(item[-11:])
    return list(video_set)


def get_video_info(video_id):
    url = "https://www.youtube.com/watch?v=%s" % video_id
    res = requests.get(url)
    soup = BeautifulSoup(res.text)
    channel_info_ret = soup.find_all(itemprop='channelId')
    genre_info_ret = soup.find_all(itemprop='genre')
    channel_id = ""
    genre = ""
    for item in channel_info_ret:
        channel_id = item.attrs.get("content")
    for item in genre_info_ret:
        genre = item.attrs.get("content")
    return channel_id, genre


def get_video_genre(video_id):
    url = "https://www.youtube.com/watch?v=%s" % video_id
    res = requests.get(url)
    print res.text
    soup = BeautifulSoup(res.text)
    genre_info_ret = soup.find_all(itemprop='genre')
    genre = ""
    for item in genre_info_ret:
        genre = item.attrs.get("content")
    return genre


if __name__ == "__main__":
    print get_video_info("jIYQfMBjjXY")
    print get_video_genre("jIYQfMBjjXY")