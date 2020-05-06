# Object-Detection

**OBJECT DETECTION USING YOLO AND MASK RCNN**

**YOLO(You only look once):**
1.  The name itself says that the image is processed or passed into the model only for once, unlike a traditional RCNN.
2.  This method takes an input image and divides that image into multiple grids. Each grid is responsible for predicting at least 5 bounding boxes.

<p align="center">
  <img src="yolo_data/yolo.jpg" width = 480>
</p>

3. Each grid is associated with 8X1 dimensional vector which has the probability of the presence of an object, dimension of the bounding box, class of the object.
4. Each object is assigned to one grid cell even if it doesn't fall under its respective cell completely. The model only looks for the midpoint of the object under a cell and labels that object to that particular cell.
4. Then it repeatedly does the above process for each grid cell and gives output as an 8X1 dimensional vector.
5. At the end of the process, all these  vectors are passed to some threshold function which determines actual objects and then outputs the image.
<p align="center">
  <img src="yolo_data/yolo1.png" width = 480>
</p>

The whole model is based on a single network which multiple CNN layers in it and this network will run both forward and backward propagation:

<p align="center">
  <img src="yolo_data/yolo2.png" width = 480>
</p>

# Credits:
YOLO: https://www.pyimagesearch.com/2018/11/12/yolo-object-detection-with-opencv/  
