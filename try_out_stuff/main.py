


import glob
from custom_classes import Images,Features,Matcher,Homography


if __name__== '__main__':

    #load image paths
    image_paths = glob.glob('../panoramic_images/*.jpg')

    #load images and store in a list
    images = Images.load_images(image_paths)


    #Images.show_imgs(images)

    #compute features for list of images
    sift = Features('sift')
    sift.compute_features(images)

    image_features = sift.get_features()
  
    #initializa a matcher and find matches between each possible pair of images
    matcher =Matcher('bruteforce','L2')
    matcher.find_matches(image_features,2)

    #filter out the good matches
    matcher.filter_good_matches()

    #draw a homgraphy for each pair
    for image_pair in matcher.good_matches.keys():

        split = image_pair.split('&')

        img1_features = sift.image_features[int(split[0])]
        img2_features = sift.image_features[int(split[1])]

        good_matches = matcher.good_matches[image_pair]

        Homography.draw_panorama(img1_features,img2_features,good_matches)






