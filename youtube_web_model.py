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
    soup = BeautifulSoup(res.text)
    genre_info_ret = soup.find_all(itemprop='genre')
    genre = ""
    for item in genre_info_ret:
        genre = item.attrs.get("content")
    return genre


def get_video_view_count(video_id):
    url = "https://www.youtube.com/watch?v=%s" % video_id
    res = requests.get(url)
    soup = BeautifulSoup(res.text)
    genre_info_ret = soup.find_all(itemprop='interactionCount')
    view_count = ""
    for item in genre_info_ret:
        view_count = item.attrs.get("content")
    return view_count


def get_video_title(video_id):
    url = "https://www.youtube.com/watch?v=%s" % video_id
    res = requests.get(url)
    soup = BeautifulSoup(res.text)
    title_info_ret = soup.find_all(itemprop='name')
    title = ""
    for item in title_info_ret:
        title = item.attrs.get("content")
    return title


def sniff_channel_fans_country_title(channel_id):
    url = "https://www.youtube.com/channel/%s/about" % channel_id
    res = requests.get(url)
    soup = BeautifulSoup(res.text)
    fans_count_soup_ret = soup.find_all(class_='yt-subscription-button-subscriber-count-branded-horizontal')
    fans_count = 0
    country_info = ""
    channel_title = ""
    for item in fans_count_soup_ret:
        fans_count = item.text.replace(",", "")
    country_soup_ret = soup.find_all(class_='country-inline')

    for item in country_soup_ret:
        country_info = item.text.strip()
    channel_title_soup_ret = soup.find_all(class_='qualified-channel-title-wrapper')

    for item in channel_title_soup_ret:
        channel_title = item.text

    view_count_soup_ret = soup.find_all(class_='about-stat')
    view_count = 0
    if len(view_count_soup_ret) == 3:
        view_count = view_count_soup_ret[1].text.split(" ")[2].replace(",", "")
    print fans_count, country_info, channel_title, int(view_count)
    return fans_count, country_info, channel_title, view_count


if __name__ == "__main__":
    # sniff_channel_fans_country_title("UCcxNwqGMkPjf-EwBxvMA1jg")
    # print get_video_view_count("Hq2NVTdApJ8")
    # print get_video_title("Hq2NVTdApJ8")
    print get_video_genre("Je_ZAk1IVrs")