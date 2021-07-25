'''
The following script is to be used for creating longer videos clips of existing video dataset 
please give the start and end time of the match recording you want to extract.
Note: each video recordings is of 3 sec, so please enter times in mutiples of 3

script will store the file names in files.txt file, following which a terminal command will
be executed

Eg: if you want the recoding between minute 2 and 3 and want to save the 
output file as output.mp4, script call would be
python concatenate_videos.py '2:00' '3:00' 'output'

concatenated videos will be saved in concatenated videos folder
'''
import sys
import glob
import ffmpeg
import os


if __name__ == '__main__':
	
	start_time = sys.argv[1].split(':')
	end_time = sys.argv[2].split(':')
	file_name = sys.argv[3] + ".mp4"

	start_segment_no = int((60 * int(start_time[0]) + int(start_time[1]))/3)
	end_segment_no   = int((60 * int(end_time[0]) + int(end_time[1]))/3)


	video_files = sorted(glob.glob('../video_dataset/SVPPD/*.h264'))[start_segment_no:end_segment_no]
	
	with open('files.txt', 'w') as f:
		for file in video_files:
			f.write('file ' + "'" + file +"'" +'\n')



	#executing shell command
	os.system("ffmpeg -f concat -safe 0 -i  files.txt -vf scale=1080:-1 -vcodec mpeg4 -b:v 1000k "+"../concatenated_videos/"+file_name)



 

	