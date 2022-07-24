from genericpath import exists
from os.path import exists 
from os import mkdir
from pytube import YouTube

# file handling function
def create_file(name, path):
    file_exits = exists(path)
    if file_exits == False:
        mkdir(path)
    else:
        pass

    file = open(f'{path}/{name}','w')
    file.close()
    

def input_entry(name, path):
    while True:
        input_entry = input('Youtube link (to stop the entry -> quit/exit): \n> ')

        if input_entry == 'quit' or input_entry == 'exit':
            break
        else:
            file = open(f'{path}/{name}', 'a')
            file.writelines(input_entry + '\n')
            file.close()


def new_func():
    input_entry = ''


def main_file():
    # the name of file
    print("Name of file (Default name would be 'youtube_link.txt')")
    name_input = input('> ').lower()

    # the path of file
    print('Path to save the document (Default path would be /kali/home/Download/youtube link/)')
    path_input = input('> ').lower()

    # making a default name and path if the input does not filled by user
    if name_input == '':
        name_input = 'youtube_link_download.txt'
    if path_input == '':
        path_input = '/home/kali/py_examples/file_handling/youtube link'

    return name_input, path_input


# test for the functions
# file_name = 'youtube_link_download.txt'
# file_path = '/home/kali/py_examples/file_handling/youtube link'
# create_file(name=file_name, path=file_path)
# input_entry(name=file_name, path=file_path)


# pytube function
def on_progress(stream, chunk, bytes_remaining):
    print(round(100 - (bytes_remaining / stream.filesize) * 100, 2))


def on_complete(stream, file_path):
    print(f' Download completed \nFile location: {file_path}')


def video_information(video_object):
    # video information
    print('Video Information: ')
    # print(f'Title: {video_object.title}')
    # print(f'Author: {video_object.author}')
    # print(f'Duration: {video_object.length / 60} minutes')
    # print(f'Views: {video_object.views} viewers')
    # print(f'Channel URL: {video_object.channel_url}')
    inform = {
        'Title' : '{video_object.title}',
        'Author' : '{video_object.author}',
        'Duration' : '{video_object.length}',
        'Views' : '{video_object.views}',
        'Channel URL' : '{video_object.channel_url}'
    }


def download(youtube_link):
    print(f'download {youtube_link} is completed')

def file_size(path):
    link_source = open(path, 'r')
    for url in link_source.readlines():
        video_object = YouTube(url)
        file_size = video_object.streams.get_lowest_resolution().filesize
        file_size = round(file_size / (1024*1024), 1)

        return file_size
        # print(file_size)

