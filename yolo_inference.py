from ultralytics import YOLO

model = YOLO('yolov8x')

result = model.predict("input_videos/08fd33_4.mp4", save = True)
print("==============================================")
print(result[0])
for box in result[0].boxes:
    print(box)



