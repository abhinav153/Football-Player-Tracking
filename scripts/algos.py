
'''
This file will describe custom classes built on existing libraries to be used
for image processing
'''

import glob
import cv2


class Feature_matching:
    
    @staticmethod
    def initialize_sift():
        return cv2.SIFT_create()

    @staticmethod
    def detect_kp_desc(sift,img):
        return sift.detectAndCompute(img,None)

    @staticmethod
    def draw_keypoints(kp,img):

        return cv2.drawKeypoints(img,kp,None)

    @staticmethod
    def match_descriptors(desc1,desc2):

        #brute force matching
        matcher = cv2.BFMatcher(cv2.NORM_L2,crossCheck = True)
        matches = matcher.match(desc1,desc2)

        return sorted(matches,key=lambda x : x.distance)

    @staticmethod
    def draw_matches(matches,img1,img2,kp1,kp2):

        return cv2.drawMatches(img1,kp1,img2,kp2,matches,None)





if __name__ == '__main__':

    #lets load the images
    image_files = sorted(glob.glob('../panoramic_images/*.jpg'))
    
    img1 = cv2.imread(image_files[0])
    #cv2.imshow('first image',img1)
    #cv2.waitKey(0)


    img2 = cv2.imread(image_files[-2])
    #cv2.imshow('second  image',img2)
    #cv2.waitKey(0)

    sift = Feature_matching.initialize_sift()

    keypoints_1,descriptors_1 = Feature_matching.detect_kp_desc(sift,img1)
    keypoints_2,descriptors_2 = Feature_matching.detect_kp_desc(sift,img2)

    matches = Feature_matching.match_descriptors(descriptors_1,descriptors_2)

    matching_result = Feature_matching.draw_matches(matches[:10],img1,img2,keypoints_1,keypoints_2)

    cv2.imshow('matches',matching_result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()



    
