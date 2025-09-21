"""
Run inference (testing) on test images using trained YOLOv3 model.
"""

from ultralytics import YOLO

def main():
    model = YOLO('runs/detect/geo-ai-ml-yolov3/weights/best.pt')  # Path to best weights
    results = model.predict(source='data/test/images', save=True, conf=0.25)
    print("Inference complete. Results are saved in runs/detect/predict/.")

if __name__ == "__main__":
    main()
