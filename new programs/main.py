# Name : Avnish Bharadva
# Roll NO : 2
# Date : 18/8/2022
# BCA 5th A

# First install pytube module using pip install pytube 

from pytube import YouTube

url = input("Enter Video Link : ")

video = YouTube(url)

video = video.streams.get_highest_resolution()

video.download()

print(video.title,"Downloaded")