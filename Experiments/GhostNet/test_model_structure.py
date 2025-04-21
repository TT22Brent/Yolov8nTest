import sys
sys.path.insert(0, './ultralytics')

from ultralytics import YOLO
from ultralytics.nn.tasks import attempt_load_one_weight
import traceback

def test_yolov8n_ghost():
    print("🔍 正在测试 yolov8n_ghost.yaml 模型结构...")
    try:
        # 尝试构建模型
        model = YOLO("yolov8n_ghost.yaml")
        print("✅ 模型结构成功构建！")

        # 打印模型结构摘要
        model.info()
    except Exception as e:
        print("❌ 结构构建失败！错误详情如下：")
        traceback.print_exc()
        return False

    return True

if __name__ == "__main__":
    success = test_yolov8n_ghost()
    if success:
        print("🎉 GhostNet 模型结构测试通过！")
    else:
        print("⚠️ 请检查 GhostConv / GhostC2f 参数定义及 YAML 格式")
