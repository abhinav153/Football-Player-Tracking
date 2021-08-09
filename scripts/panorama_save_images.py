'''
This file will be used to save the images to be used for generating the pannoramic view of the football field
To generate the panoramic view , we need to select series of images which are representative of different views of the football pitch .
This script will save images of the first 2 minutes of the match to generate the panoramic view.

This views will be stiched together to to generate a panoramic view using homography
'''

import cv2
import time




def calculate_fps(prev_frame_time,next_frame_time):
    fps = 1/(next_frame_time-prev_frame_time)
    return int(fps)

    

if __name__ == '__main__': 

    panoramic_frames = []


    file_path = '../video_dataset/FULL MATCH _ Chelsea_vs_ Manchester_United _ Emirates FA Cup Semi-Final 2019-20.mp4'

    #capture video stream
    video_stream = cv2.VideoCapture(r'{}'.format(file_path))
    

    #read the first frame of the video
    ret,frame = video_stream.read()

    prev_frame_time = 0
    start = time.time()

    i=1
    #iterate over frames
    while True:

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
        frame = cv2.resize(frame,(1200,800))

        #time elapsed in seconds
        elapsed = int(time.time() - start)

        #save images if elapsed time is less that equal to 120seconds
        if elapsed<=120:
            cv2.imwrite('../panoramic_images/current_buffer/frame'+str(elapsed)+'.jpeg',frame)

       
      
        cv2.putText(frame, 'fps:'+str(fps), (0,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),1) 
        cv2.putText(frame,'time: '+str(elapsed),(1000,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255))
        cv2.imshow('frame',frame)


        prev_frame_time = next_frame_time

        key =cv2.waitKey(1)
        if key == ord('q'):
            break


    #release the video_stream object and keyboard listener
    video_stream.release()
    cv2.destroyAllWindows()
    
