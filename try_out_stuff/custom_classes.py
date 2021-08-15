
import cv2




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
                keypoints,desscriptors = self.feature.detectAndCompute(img,None)
                self.image_features[i] = [img,keypoints,desscriptors]
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



        