from pytube import YouTube

from function_file_handling import on_complete, on_progress

list_of_link = input('Give the path of the file that contains list of youtube link that you want to download. \n> ')
path = open(list_of_link, 'r')
path_link = path.read()


url_list = open(path_link, 'r')
for url in url_list.readlines():
    video_object = YouTube(
        url,
        on_progress_callback=on_progress,
        on_complete_callback=on_complete)

    video_object.streams.get_highest_resolution().download(output_path='/home/kali/Downloads')
    
print('Your video is on Downloads file')
    


