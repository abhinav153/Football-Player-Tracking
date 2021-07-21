
# Football-Player-Tracking
Deep Learning based framwork for player tracking and analysis in football videos

Football is one of the most followed sports across the world,in recent years there has been as increasing interest in sport analytics side of this sport. In this project i aim to do Computer Vision based analysis. I was heavily influenced by the ideas given in this [article](https://medium.com/@nicolo.lucchesi?p=745e62b36295)

## Aims
1. Create a labelled Dataset using tracker systems of OpenCV module to create a labelled dataset for multiple objects (maybe YoloV3 format?)
2. Use the labelled dataset to create a object detection framework for a live videostream and transform them to 2d co-ordinate system i.e a 2d footall pitch
3. Use the mapped 2d-co-ordinates systems to calculate average team structure of the team and any other useful metrics

### 1. Creating a labelled dataset
   I am going to use a tracking algorithm implementations provided within the OpenCv module to create a labelled dataset. The motivation behind this is that
   manual annotation of the data is very time consuming.What if we could the train a machine learning model to annotate data for us. Though this procedure might
   not be robust yet, but it is certainly a starting point<br>
   ![video](https://github.com/abhinav153/Football-Player-Tracking/blob/main/clips/clip1.gif)

## References
1. [Football Games Analysis from video stream with Machine Learning](https://medium.com/@nicolo.lucchesi?p=745e62b36295) 
2.
