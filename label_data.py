'''
The script to be used is for creation of labelled data,based on the tracking algorithms 
used to generate the co-ordinates and class labels for the data

Eg.
python label_data.py 'CSRT' 'video1'
'''

import cv2
import sys

class Tracker:
    #creating a dictionary of object trackers available in OpenCV
    TrDict = {
        'CSRT':cv2.legacy.TrackerCSRT_create,
        'KCF':cv2.TrackerKCF_create,
        'BOOSTING':cv2.legacy.TrackerBoosting_create,
        'MIL':cv2.TrackerMIL_create,
    
    }

    @staticmethod
    def create_tracker(tracker_name):
        '''
        to initialize a tracker based on particular algorithm as given tracker dictionary
        '''
        tracker = Tracker.TrDict[tracker_name]()

        return tracker

    @staticmethod
    def initialize_tracker(tracker,frame):

        '''
        initialize the tracker on a particluar frame with a particular ROI
        '''
        cv2.imshow('frame',frame)
        #select the Region of Interest(ROI) we want to track within the video stream by first drawing a bounding box around it
        bbox = cv2.selectROI('frame',frame)

        #next lets initialize a tracker with the frame and bounding box
        tracker.init(frame,bbox)

        cv2.destroyAllWindows()

        return bbox

    @staticmethod
    def create_multi_tracker():
        '''
        Create container for keeping track of multiple trackers
        '''
        multi_tracker = cv2.legacy.MultiTracker_create()

        return multi_tracker







if __name__ == '__main__': 

    #read the arguments passed to the script
    tracker_name = sys.argv[1]
    video_file = "concatenated_videos/" +sys.argv[2]+".mp4"
    no_of_trackers = int(sys.argv[3])
    print(video_file)


    #capture the video stream to run the tracker algorithm on
    video_stream  = cv2.VideoCapture(r'{}'.format(video_file))

    #read the first frame of the video
    ret,frame = video_stream.read()

    #initiliaze a multitracker
    multi_tracker = Tracker.create_multi_tracker()

    for i in range(no_of_trackers):
        #create a tracker
        tracker = Tracker.create_tracker(tracker_name)

        #initialize tracker
        bbox = Tracker.initialize_tracker(tracker,frame)

        #add tracker
        multi_tracker.add(tracker,frame,bbox)



    #now lets track this ROI over the video_stream
    while True:

        #read the next frame
        ret,frame = video_stream.read()
        
        #break out of the loop if the video stream ends
        if not ret:
            break
        
        #else let the tracker find the updated position of the ROI
        (success,boxes) = multi_tracker.update(frame)
        
        #if we have found the box, we wil draw a rectangle around it
        if success:
            i=1
            for box in boxes:
                (x,y,w,h) = [int(a) for a in box]
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),)
                text = 'Player '+str(i)+': '+str(x)+','+str(y)
                cv2.putText(frame,text,(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.4,(0,255,0))
                cv2.imshow('frame',frame)
                i+=1
        
        #to quit video_stream
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    #release the video_stream object
    video_stream.release()
    cv2.destroyAllWindows()


	

