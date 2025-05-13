import sys
import shutil
from ultralytics import YOLO

# 添加本地 YOLO 源码路径
sys.path.insert(0, './ultralytics')

def main():
    # 加载使用 GSConv 的结构配置
    model = YOLO("gshead.yaml")

    # 启动训练
    model.train(
        data="C:/Users/user/PycharmProjects/Yolov8ncloud/Datasets/dataset.yaml",
        epochs=500,                       # 只跑2轮
        imgsz=640,
        batch=112,
        device=0,                       # 使用GPU，或改为 'cpu'
        project="gshead",                # 统一输出路径
        name="test1",           # 子目录名，便于管理
        exist_ok=True                  # 如果存在就继续写入（不报错）
    )


if __name__ == "__main__":
    main()
