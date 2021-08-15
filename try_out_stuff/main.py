


import glob
from custom_classes import Images,Features


if __name__== '__main__':

    image_paths = glob.glob('../panoramic_images/*.jpg')

    images = Images.load_images(image_paths)


    #Images.show_imgs(images)

    sift = Features('sift')

    sift.compute_features(images)

    image_features = sift.get_features()








