
# Football-Player-Tracking
Deep Learning based framwork for player tracking and analysis in football videos

Football is one of the most followed sports across the world,in recent years there has been as increasing interest in sport analytics side of this sport. In this project i aim to do Computer Vision based analysis. I was heavily influenced by the ideas given in this [article](https://medium.com/@nicolo.lucchesi?p=745e62b36295)<br>

Dataset used:[Soccer video & Position dataset](https://datasets.simula.no/alfheim/)

## Aims
1. Create a labelled Dataset using tracker systems using different algorithms 
2. Use the labelled dataset to create a object detection framework for a live videostream and transform them to 2d co-ordinate system i.e a 2d footall pitch
3. Use the mapped 2d-co-ordinates systems to calculate average team structure of the team and any other useful metrics

### 1. Creating a labelled dataset using various tracking algorithms
   I am going to use a tracking algorithm implementations provided within the OpenCv module to create a labelled dataset. The motivation behind this is that
   manual annotation of the data is very time consuming.What if we could the train a machine learning model to annotate data for us. Though this procedure might
   not be robust yet, but it is certainly a starting point.<br>
   
   ![CSRT tracking system](https://github.com/abhinav153/Football-Player-Tracking/blob/main/clips/clip1.gif)

### 2. Use a custom model for idendtifying players, and mapping to a live 2d pitch system

### 3. Calculate metric based on identified player positions

## References
1. [Football Games Analysis from video stream with Machine Learning](https://medium.com/@nicolo.lucchesi?p=745e62b36295) 
2.
