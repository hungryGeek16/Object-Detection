# Structure of the code files:

1. ```main.py```: this file contains all the main code which runs to detect persons in the image.How function works and it's functionalities have been documented in that code file itself.

2. ```helper.py```: this file contains three helper functions. The purpose of making a helper function file for three is to maintain code readablity.

### How to Run:
```python
console:~$ main.py --videopath /path/to/the/video/file
# Above lines output a window which runs the application
```
**Output looks like this:**

<p align="center">
![Social](video.gif)
</p>


3. The output window has four string on the top left corner.  
```Persons Detected: Total no of persons detected in each frame```  
```People at high risk: Total no of people who are not following social distancing.```  
```People at low risk: Total no of people who are somewhat following social distancing.```  
```People at no risk: Total no of people who are following social distancing.```  
**Hence based on these four paramters social distancing can be monitored**
