1.Put target images in 'images' folder
2.Run command:
python yolo.py --image images/image_name.jpg --yolo yolo-coco
3.for videos:
save  videos in 'video' folder and then run:
python yolo_video.py --input videos/video_name.mp4 \
	--output output/video_name.extension --yolo yolo-coco
your output will be saved in 'output' folder.

Source:https://www.pyimagesearch.com/2018/11/12/yolo-object-detection-with-opencv/