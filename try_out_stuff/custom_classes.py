
import cv2
import numpy as np



class Images:

    '''
    Usefull for some image processing operations
    '''

    @staticmethod
    def load_image(path,grayscale = False):
        '''
        Given an image returns the numpy array of the image; if grayscale is given as true, returns a grayscale image otherwise BGR images
        '''
        if grayscale == False:
            img = cv2.imread(path)
        else:
            img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
        
        return img  


    @staticmethod
    def load_images(paths,grayscale = False):
        '''
        Given an list of image paths, returns a list containing a numpy array of images; if grayscale is given as true returns grayscale images otherwise BGR images
        '''
        if grayscale == False:
            images = [cv2.imread(path) for path in paths]
        else:
            images = [cv2.imread(path,cv2.IMREAD_GRAYSCALE) for path in paths]

        return images

    @staticmethod
    def show_img(img,i=1):
        '''
        displays image 
        '''

        cv2.imshow('frame ' +str(i),img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    @staticmethod
    def show_imgs(images):
        '''
        Display a list of images
        '''

        for (i,image) in enumerate(images):
            Images.show_img(image,i+1)


class Features:

    '''
    useful for generating image features
    '''

    def __init__(self,type):

        if type == 'sift':

            self.feature = cv2.SIFT_create()
            self.name = 'SIFT'
            self.image_features = {}

    def __repr__(self):
        return 'Feature being used {}'.format(self.name)

    def describe(self):
        print('Feature being used {}'.format(self.name))
        print('No of images: {}'.format(len(self.image_features.keys())))


    def compute_features(self,images):
        '''
        will compute the feature for the object based on the feature with which it was initialised and store it in a dictionary for each image in an image list.
        If it just a single image it returns keypoints and descriptors for it
        '''
        if isinstance(images,list):
            for (i,img) in enumerate(images):
                keypoints,descriptors = self.feature.detectAndCompute(img,None)
                self.image_features[i+1] = [img,keypoints,descriptors]
        else:
            keypoints,desscriptors = self.feature.detectAndCompute(img,None)
            return keypoints,desscriptors

    def get_features(self):
        '''
        Return the list of features of images computed in a list
        '''
        if not bool (self.image_features):
            print('No features have been computed yet')

        else:
            return self.image_features


class Matcher:
    '''
    Is used fot feature matching between the images
    '''
    def __init__(self,type,norm,crossCheck = False): 
        '''
        create a matcher object
        type = bruteforce/?
        crosscheck = only find best match if true
        norm = L1,L2
        '''
        if type=='bruteforce':
            if norm == 'L1':    
                self.matcher = cv2.BFMatcher_create(cv2.NORM_L1,crossCheck)
            elif norm == 'L2':  
                self.matcher = cv2.BFMatcher_create(cv2.NORM_L2,crossCheck)

        self.matches = {}
        self.good_matches = {}

    def find_matches(self,image_features,k):
        '''
        find matches between images
        k = No of best matching features  for a pair of images
        '''  
       
        no_of_images = len(list(image_features.keys()))  
        for i in range(1,no_of_images+1):
            for j in range(i+1,no_of_images+1):
                desecriptor1 = image_features[i][2]
                desecriptor2 = image_features[j][2]
                print('finding matches between image ',i,'&',j)
                matches = self.matcher.knnMatch(desecriptor1,desecriptor2,k)
                self.matches[str(i)+'&'+ str(j)] = {'matches':matches,'images':[image_features[i][0],image_features[j][0]]}
            print('***')

    def filter_good_matches(self,ratio_thresh = 0.6):
        '''
        Applies Lowes ratio test to filter out good matches and store for each image pair

        '''
        for image_pair in self.matches.keys():
            self.good_matches[image_pair] = []
            for m,n in self.matches[image_pair]['matches']:  
                if m.distance < ratio_thresh * n.distance:
                    self.good_matches[image_pair].append(m)



class Homography:
    '''
    Will be used to create a panoroma with the good image matches
    '''

    @staticmethod
    def draw_panorama(img1_features,img2_features,good_matches):  
        '''
        draw panorama images for image pair matchings
        '''

        if not good_matches:  
                return


        img1,kp1,desc1 = img1_features[0],img1_features[1],img1_features[2]
        img2,kp2,desc2 = img2_features[0],img2_features[1],img2_features[2]
        
        reference_pts = np.array([kp2[match.trainIdx].pt for match in good_matches],dtype = np.float32)
        query_pts     = np.array([kp1[match.queryIdx].pt for match in good_matches],dtype = np.float32)


        if len(reference_pts) >= 4 and len(query_pts) >=4:
            h,status = cv2.findHomography(query_pts,reference_pts,cv2.RANSAC,1.0)

            Images.show_img(cv2.warpPerspective(img2,h,(img2.shape[0],img2.shape[1])))