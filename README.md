# video-to-filename
Prints frames from given video on filenames of text files
## Setup 
run this command in terminal to install OpenCV (assuming python already present)

`pip install opencv-python`

Clone the repository using 

`git clone https://github.com/Gagan163264/video-to-filename.git`

or just download the zip

## Usage
Navigate to directory containing main and run program with

`python3 mainf.py <videosource>.mp4`
  
The program displays metadata on the terminal while converting all the frames to ascii art.
When prompted to start, press enter.
Terminal should display a copy of the frame being printed onto the txt files in /folder, if it doesnt support unicode it shows blocks

Output looks something like https://www.youtube.com/watch?v=Z3J40XcTNXU (but much slower, video has been sped up 2200 times)
