"""
Train YOLOv3 model using Ultralytics YOLO.
Update data.yaml to point to your train/test images and labels.
"""

from ultralytics import YOLO

def main():
    # Load YOLOv3 model (pretrained or new)
    model = YOLO('yolov3.pt')  # Download automatically if not found

    # Train
    model.train(
        data='data/data.yaml',    # Path to data config
        epochs=50,
        imgsz=640,
        batch=16,
        name='geo-ai-ml-yolov3'
    )

if __name__ == "__main__":
    main()
