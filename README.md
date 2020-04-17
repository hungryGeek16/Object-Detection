# Object-Detection

**OBJECT DETECTION USING YOLO AND MASK RCNN**

**YOLO(You only look once):**
1.  The name itself says that the image is processed or passed into the model only for once, unlike a traditional RCNN.
2.  This method takes an input image and divides that image into multiple grids. Each grid is responsible for predicting at least 5 bounding boxes.

![baggage_claim](/uploads/68e83bd363580f52c720bf13867ff1cc/baggage_claim.jpg)

3. Each grid is associated with 8X1 dimensional vector which has the probability of the presence of an object, dimension of the bounding box, class of the object.
4. Each object is assigned to one grid cell even if it doesn't fall under its respective cell completely. The model only looks for the midpoint of the object under a cell and labels that object to that particular cell.
4. Then it repeatedly does the above process for each grid cell and gives output as an 8X1 dimensional vector.
5. At the end of the process, all these  vectors are passed to some threshold function which determines actual objects and then outputs the image.

![Screenshot__34_](/uploads/01d47fb8f2eb724d2d9e56ef307d3aba/Screenshot__34_.png)

The whole model is based on a single network which multiple CNN layers in it and this network will run both forward and backward propagation:

![Capture](/uploads/0ab4dc48d5590ef26c4f2c38b40db8ea/Capture.PNG)

**Mask R-CNN(Regional Convolutional Neural Networks):**
1.  Mask R-CNN gives information about what pixel belong to the object and background.
2. It's basically an algorithm based on Instance Segmentation, where it determines pixel-wise mask for every object present in the image.

![Capture1](/uploads/3e874e3ec055a79eea21210ea28da4bd/Capture1.PNG)

3.  An input image is passed to the model and the model extracts regions which may potentially contain objects using selective search algorithm.
4.  By using transfer learning method, specifically, feature extraction model computes features for each extracted region using the pre-trained CNN. 
5. At last the extracted regions where an object is identified are passed to SVM classifier for final prediction of the class of the object which it belongs to.

![Capture2](/uploads/9a9cf5d1691bbc4258db091e3fd932a0/Capture2.PNG)

**Parameters which I have tried:**
**Number of Objects:**

![Screenshot__58_](/uploads/9c0768448d3b85fb20a75703222f6692/Screenshot__58_.png)

YOLO detects more images than Mask R-CNN.

**Quality of Image:**

![Screenshot__60_](/uploads/226d8716aebd1e417f54a7ce1027513f/Screenshot__60_.png)

YOLO is more effective than Mask R-CNN. But R-CNN is more conscious about what it is detecting.  


**YOLO:** https://www.pyimagesearch.com/2018/11/12/yolo-object-detection-with-opencv/

**Mask-RCNN:** https://www.pyimagesearch.com/2018/11/19/mask-r-cnn-with-opencv/
