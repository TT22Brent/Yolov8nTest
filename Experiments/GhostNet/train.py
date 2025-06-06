import sys
sys.path.insert(0, "./ultralytics")

from ultralytics import YOLO

def main():
    model = YOLO("yolov8n_ghostconv.yaml")
    model.train(
        data="C:/Users/user/PycharmProjects/Yolov8ncloud/Datasets/dataset.yaml",
        epochs=500,
        imgsz=640,
        batch=112,
        device=0,
        project="ghostnet_result",
        name="ghostnet",
        exist_ok=True
    )

if __name__ == "__main__":
    main()

