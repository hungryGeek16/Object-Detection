import cv2
import numpy as np

from helper import *

import argparse

parser = argparse.ArgumentParser(description="SocialDistancing")
parser.add_argument(
    "--videopath", type=str, default="video.mp4", help="Path to the video file"
)
args = parser.parse_args()

input_video = args.videopath

video_output = None


cap = cv2.VideoCapture(input_video)  # Path to the video input 
(W, H) = (None, None) # Initialize width and height variables
q = 0  # to store intital value of width and reduce the width of the image 
frame_count = 0

ln,net = network()  #Call network from helper file
while True:

    (grabbed, frame) = cap.read() #reads image frame by frame
    frame_count += 1
    if not grabbed: # If no frame left then loop breaks.(grabbed is a bool value which tells whether frame is present or not)
        break

    if W is None or H is None: #The whole purpose of loop is to initialize the height and width of the vidoe frame
        (H, W) = frame.shape[:2] # for once
        q = W

    frame = frame[0:H, 200:q] #Reduced some amount of frame width
    (H, W) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416),
                                 swapRB=True, crop=False) # Initialization of blob of size 416,416 from the input frame
    net.setInput(blob)  # Passing on the input to yolo architecture
    layerOutputs = net.forward(ln) # Outputs the array containing bounding boxes,confidences and class Ids.
    # yolo is big architecture so it outputs values at checkpoints named yolo_16 and yolo_23.
    boxes = []
    confidences = []
    classIDs = []

    for output in layerOutputs:  # For each output checkpoint

        for detection in output: # For each detection in those checkpoints

            scores = detection[5:] # Scores are appended at every output of layers in yolo architecture.
            # We consider the best or the max value among them
            classID = np.argmax(scores)
            confidence = scores[classID] # Score of the detected person
            if classID == 0: # Here yolo is basically object detection but we need only persons for our problems
            # Hence filter all those class labels which are not humans.    
                if confidence > 0.5: # Confidence thresholding
                    box = detection[0:4] * np.array([W, H, W, H]) # Detections are scaled values, hence bringing them back to original sizes
                    (centerX, centerY, width, height) = box.astype("int")

                    x = int(centerX - (width / 2)) # Here we determine the starting point of bounding box
                    y = int(centerY - (height / 2))

                    boxes.append([x, y, int(width), int(height)])
                    confidences.append(float(confidence))
                    classIDs.append(classID)

    idxs = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.3) # Non Maximum Supression for redudant bounding boxes.

    if len(idxs) > 0:
        contact = list()   
        persons = idxs.flatten() # Flatten all those detected value indices
        persons_in_risk =list() # Initialize list for persons at risk
        low_risk = list() #Initialize list for persons at risk
        centers = list() # Initialize centers list for every detected bounding box
        distance = list()
        for i in persons:
            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])
            centers.append([int(x + w / 2), int(y + h / 2)]) # calculate center of bounding box for every person detected.

            contact.append(0) # initialize contact list with zeros
        for i in range(len(centers)):  # Now calculate  distances from every bounding box center and classifiy them
            # into three categories, high risk,low risk and no risk.
            for j in range(i+1,len(centers)):
                flag = isclose(centers[i], centers[j])
                if flag == 1:
                    persons_in_risk.append([centers[i], centers[j]])
                    contact[i] = 1
                    contact[j] = 1
                elif flag == 2:
                    low_risk.append([centers[i], centers[j]])
                    contact[i] = 2
                    contact[j] = 2

        all_persons = len(centers) # Keep count of all category persons
        people_at_low_risk = contact.count(2)
        people_at_high_risk = contact.count(1)
        people_at_no_risk = contact.count(0)
        kk = 0

        for i in persons:
            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])
            if contact[kk] == 1:
                # Construction of rectange in every category
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 150), 4)
            elif contact[kk] == 0:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 4)

            else:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 120, 255), 4)

            kk += 1
            # Show risk lines between high and low risk categories
        for h in persons_in_risk:
            cv2.line(frame, tuple(h[0]),tuple(h[1]), (0, 0, 255), 2)
        for b in low_risk:
            cv2.line(frame, tuple(b[0]), tuple(b[1]), (0, 255, 255), 2)
            
        # Plot count of every category person on the detection screen and monitor social distancing.    
        tot_str = "Persons detected: " + str(all_persons)
        high_str = "People at high risk:(Red_Boxes):" + str(people_at_high_risk)
        low_str = "People at low risk(Orange_boxes):" + str(people_at_low_risk)
        safe_str = "People at no risk(Green_boxes): " + str(people_at_no_risk) 
               
        font,org,fontScale,color,thickness  = params()
        cv2.putText(frame,tot_str , (80,50), font, fontScale, color, thickness, cv2.LINE_AA)
        
        cv2.putText(frame,high_str , (80,80), font, fontScale, (0,0,255), thickness, cv2.LINE_AA)
        
        cv2.putText(frame,low_str , (80,110), font, fontScale, (0,165,255), thickness, cv2.LINE_AA)
        
        cv2.putText(frame,safe_str , (80,150), font, fontScale, (0,255,0),thickness, cv2.LINE_AA)
        

        cv2.imshow('Social Distancing', frame)
        if video_output is None:
            fourcc = cv2.VideoWriter_fourcc(*"MJPG")
            video_output = cv2.VideoWriter("video_out.mp4", fourcc, 30,(frame.shape[1], frame.shape[0]), True)

        video_output.write(frame)
        if cv2.waitKey(1) &0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
