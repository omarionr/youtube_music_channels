# -*- coding:utf8 -*-
import youtube_web_model
import multiprocessing


def write_music_channel(line):
    write_line = line
    line = line.strip()
    item_list = line.split(";", 3)
    channel_id, fans_count, country_code, channel_title = item_list
    channel_id = channel_id.strip()
    video_ids = youtube_web_model.get_videos_by_channel(channel_id)
    if video_ids:
        video_id = video_ids[0]
        genre = youtube_web_model.get_video_genre(video_id)
        if genre == "Music":
            write_file = open("rank_out.txt", "a")
            write_file.write(write_line)
            write_file.close()


def main():
    process_num = 8
    pool = multiprocessing.Pool(processes=process_num)
    with open("channel_ids.txt") as f:
        for line in f.readlines():
            pool.apply_async(write_music_channel, (line,))
    pool.close()
    pool.join()


def filter_channel():
    ret_items = []
    with open("channel_ids.txt") as f:
        for line in f.readlines():
            line = line.strip()
            item_list = line.split(";", 3)
            channel_id, fans_count, country_code, channel_title = item_list
            channel_id = channel_id.strip()
            fans_count = fans_count.strip()
            country_code = country_code.strip()
            channel_title = channel_title.strip()
            video_ids = youtube_web_model.get_videos_by_channel(channel_id)
            if video_ids:
                video_id = video_ids[0]
                genre = youtube_web_model.get_video_genre(video_id)
                if genre == "Music":
                    item = (channel_id, country_code, fans_count, channel_title)
                    ret_items.append(item)
    sort_items = sorted(ret_items, key=lambda d: d[1])
    write_file = open("out.txt", "w")
    for item in sort_items:
        write_file.writelines("%s %s %s %s" % (item[0], item[1], item[2], item[3]))
    write_file.close()


if __name__ == "__main__":
    main()
