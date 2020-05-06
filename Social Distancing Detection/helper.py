import cv2

def network():
    weights = 'yolov3-tiny.weights'
    configPath = 'yolov3-tiny.cfg'
    net = cv2.dnn.readNetFromDarknet(configPath, weights)
    ln = net.getLayerNames()
    ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    return ln ,net

def isclose(p1, p2):
    c_d = calibrated_dist(p1, p2)
    calib = (p1[1] + p2[1]) / 2
    if 0 < c_d < 0.15 * calib: # For high risk personality
        return 1
    elif 0 < c_d < 0.2 * calib: # For low risk personality
        return 2
    else:                      # For no risk personality
        return 0

def calibrated_dist(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + 550 / ((p1[1] + p2[1]) / 2) * (p1[1] - p2[1]) ** 2) ** 0.5

def params():

    font = cv2.FONT_HERSHEY_SIMPLEX   
    # org 
    org = (80, 80)  
   # fontScale 
    fontScale = 1
   # Blue color in BGR 
    color = (0,0,0) 
   # Line thickness of 2 px 
    thickness = 2
    return font,org,fontScale,color,thickness
