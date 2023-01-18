import cv2
import os
from tinytag import TinyTag

# get metadata of the file using ffmpeg
path = r'/mnt/c/Users/ferbo/Desktop/nhl_videos_images/video_#1'
path = os.path.join(path,'match1.mp4')

# get video metadata
video = TinyTag.get(path)
print(video.duration)

# get fps of the file
video = cv2.VideoCapture(path)
fps = video.get(cv2.CAP_PROP_FPS)
print('frames per second =',fps)

#get the frameID from the selected time

minutes = 0

for seconds in range(1, 500):
    frame_id = int(fps*(minutes*60 + seconds))

# read frame in frame_id 
    video.set(cv2.CAP_PROP_POS_FRAMES, frame_id)
    ret, frame = video.read()

# save the frame
    path = r'/mnt/c/Users/ferbo/Desktop/nhl_videos_images/frames_#1'
    path = os.path.join(path,'frame_{0}_sec.png'.format(seconds))
    cv2.imwrite(path, frame)