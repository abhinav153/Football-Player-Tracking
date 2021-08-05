
# Football-Player-Tracking
Computer vision based and deep learning based framework for player tracking and analysis in football videos

## Description
In this project i aim is to do Computer Vision based analysis on a live football video stream or a recorded football match which can be used as a football analytics tool. My plan is primarily based on the ideas preseneted in this paper [[1]](https://openaccess.city.ac.uk/18380/8/paper319.pdf) with the end goal that the same system can be portable to be used in other sports too. Generally a video stream from a live match only gives view of a certain section of the pitch(shown in below gif), one of  things i aim to  is to be able to convert it to whole pitch representation i.e a panoramic view for easier interpration in terms of a global view.<br><br>
![A general stream of a football match](clips/clip2.gif)<br><br>
Along the with the panoramic view generator, i will also try to make 2d pitch representation of the pitch to map the live player positions on to it.The 2-d mappings will be used to calculate various foobtall metrics like player trajectories, team structures etc.<br><br>
![2d-pitch-representation](clips/2d-pitch-representation.png)<br><br>
I plan to read to more research papers on basis of the use-cases of which tools will be required to do the above mentioned stuff<br>
Some of the topics covered in this project would be:<br>
**Position mapping** - positions from the video are mapped to a physical reference frame, in our case the soccer pitch<br>
**Detect and track objects of interest** - In case of team sport video analysis, these are typically the
teams’ players and the ball possibly using deep learning object tracking algorithms<br>


Datasets that can be used:[Soccer video & Position dataset](https://datasets.simula.no/alfheim/)



## Aims
1. Using homography to <br>
  1.1 Create panoramic views<br>
  1.2 Projecting current video frame to panoramic view<br>
  1.3 Projecting current video frame to to 2d pitch representation
3. Try out various player tracking approaches to identify player positions on the 2d homagraphic pitch view using CNN's and other such architectures
4. Calculate various football analysis metric possible,like<br>
  4.1 Player trajectories<br>
  4.2 Team structure<br>


## Literature review
1. [Bring it to the Pitch: Combining Video and Movement Data to
Enhance Team Sport Analysis - 2018](https://openaccess.city.ac.uk/18380/8/paper319.pdf)
