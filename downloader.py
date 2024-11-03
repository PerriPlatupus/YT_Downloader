from pytubefix import YouTube
dict = {}
keylist = []
# Получаем список разрешений
def Resolution(video_url):
    yt = YouTube(video_url)
    for i in yt.streams:
        try:
            key = i.resolution + " " + i.mime_type
            if not ((i.resolution + " " + i.mime_type) in keylist):
                itag = (str(i.itag))
                dict[key] = itag
                keylist.append(i.resolution + " " + i.mime_type)
                key=""
                print(dict)
        except:
            a="audio"


def Download(ytag,video_url,output):
    YouTube(video_url).streams.filter(res=ytag).first().download(output)


