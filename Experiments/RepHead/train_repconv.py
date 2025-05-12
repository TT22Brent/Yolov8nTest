import sys
import os
from ultralytics import YOLO

# 使用本地源码
sys.path.insert(0, os.path.abspath("./ultralytics"))

def main():
    model = YOLO("rephead.yaml")  # 你的结构配置文件（在当前目录）

    model.train(
        data="C:/Users/user/PycharmProjects/Yolov8ncloud/Datasets/dataset.yaml",  # 数据路径
        epochs=500,
        imgsz=640,
        batch=16,
        device=0,  # 使用 GPU 0
        project="rephead",               # 输出目录
        name="test1",            # 子目录名
        exist_ok=True                   # 允许覆盖
    )

if __name__ == "__main__":
    main()
