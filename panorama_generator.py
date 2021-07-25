'''
This file will be used to save the images to be used fot generating the pannoramic view of the football field
To generate the panoramic view , we need to manually select series of images 
which are representative of different views of the football pitch .
This views will be stiched together to to generate a panoramic view using homography
'''

import cv2
import time
from pynput.keyboard import Key, Listener



def calculate_fps(prev_frame_time,next_frame_time):
    fps = 1/(next_frame_time-prev_frame_time)
    return int(fps)

def save_frames(frame):
    '''
    if a particular key 's' is holded for some ,the particular frame is stored in a list, 
    which will later be used to generate a panoramic view
    '''
    global panoramic_frames 
    panoramic_frames.append(frame)
    print(len(panoramic_frames))

def on_press(key):
    global frame
      
    try:
        if key == Key.caps_lock:
            save_frames(frame)
    except:
        print('error')

def on_release(key):
    pass


def create_panorama(frames):
    print('started creating panorama')
    stitcher = cv2.Stitcher.create()
    (status,result) = stitcher.stitch(frames)

    if (status == cv2.STITCHER_OK):
        cv2.imshow('panorams',result)
        print('panorama generated')
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    else:
        print('panorama not generated')

if __name__ == '__main__': 

    panoramic_frames = []


    file_path = 'video_dataset/FULL MATCH _ Chelsea_vs_ Manchester_United _ Emirates FA Cup Semi-Final 2019-20.mp4'

    #capture video stream
    video_stream = cv2.VideoCapture(r'{}'.format(file_path))

    #setting fps
    video_stream. set(cv2.CAP_PROP_FPS, 60)


    #read the first frame of the video
    ret,frame = video_stream.read()

    prev_frame_time = 0

    listener = Listener(
    on_press=on_press,
    on_release=on_release)
    listener.start()

    #iterate over frames
    while True:

        video_stream.set(cv2.CAP_PROP_FPS, 60)
        _,frame = video_stream.read()


        #if video ended break
        if not _:
            break

        next_frame_time = time.time()

        #setting fps rate we want
        fps_rate = 40 #should help us get 30 fps in video

        #setting delay time to adjust fps
        time.sleep(1/fps_rate)

        fps = calculate_fps(prev_frame_time,next_frame_time)

        #resize frame
        frame = cv2.resize(frame,(500,300))

       
      
        cv2.putText(frame, 'fps:'+str(fps), (0,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),1) 
        cv2.imshow('frame',frame)


        prev_frame_time = next_frame_time

        key =cv2.waitKey(0)
        if key == ord('q'):
            break
        else:
            continue

      



    #release the video_stream object and keyboard listener
    video_stream.release()
    cv2.destroyAllWindows()
    listener.stop()

    '''
    #lets iterate over the saved frames
    i=1
    for frame in panoramic_frames:
        frame = cv2.resize(frame,(500,300))
        cv2.imshow('frame'+str(i),frame)
        cv2.waitKey(0)
        i+=1
        cv2.destroyAllWindows()
    '''

    #lets create the panorama view now
    #create_panorama(panoramic_frames)