from pytube import YouTube
def download(link):
    youtubeObject=YouTube(link)
    youtubeObject=youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occured")
    print("DOWNLOAD IS COMPLETED SUCCESSfully") 
link=input("enter the youtube video link: ")
download(link)           
