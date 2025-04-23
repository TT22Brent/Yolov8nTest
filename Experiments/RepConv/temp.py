import sys
sys.path.insert(0, "./ultralytics")

from ultralytics import YOLO

def main():
    model = YOLO("yolov8n_ghostconv.yaml")
    model.train(
        data="/home/g1467167830/Yolov8ncloud/Datasets/dataset.yaml",
        epochs=500,
        imgsz=640,
        batch=112,
        device=0,
        project="ghostnet_C2f_result",
        name="repconv_exp",
        exist_ok=True
    )

if __name__ == "__main__":
    main()