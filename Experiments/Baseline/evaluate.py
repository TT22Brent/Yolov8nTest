import time
import sys
import os
from ultralytics import YOLO
from datetime import datetime

sys.path.insert(0, "./ultralytics")  # 使用本地 ultralytics 源码

def evaluate(model_path, data_yaml, save_preds=True, tag="baseline_test"):
    print(f"\n📦 正在加载模型: {model_path}")
    model = YOLO(model_path)

    # 模型结构信息
    print("\n📊 模型结构分析：")
    model_info = model.info(verbose=True)

    # 精度评估（测试集）
    print("\n🎯 精度评估（测试集 mAP）")
    metrics = model.val(data=data_yaml, split='test', verbose=False)
    mAP50 = metrics.box.map50
    mAP5095 = metrics.box.map

    print(f"\n✅ mAP@0.5     : {mAP50:.4f}")
    print(f"✅ mAP@0.5:0.95: {mAP5095:.4f}")

    # 推理速度评估
    print("\n⚡ 推理速度评估中（FPS）...")
    t0 = time.time()
    results = model.predict(
        source="../../Datasets/images/test",
        save=save_preds,
        conf=0.25,
        project="runs",
        name=f"eval_{tag}",
        exist_ok=True,
        verbose=False
    )
    t1 = time.time()
    n = len(results)
    total_time = t1 - t0
    fps = n / total_time

    print(f"\n📸 推理图片数：{n}")
    print(f"⏱️ 总耗时：{total_time:.2f}s")
    print(f"🚀 平均FPS：{fps:.2f} 张/秒")

    # 保存评估结果到模型所在目录
    eval_text = f"""Model Evaluation Summary
Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Model path: {model_path}
Image size: 640

📊 Model Info:
{model_info}

🎯 Accuracy:
mAP@0.5     : {mAP50:.4f}
mAP@0.5:0.95: {mAP5095:.4f}

⚡ Inference:
Image count : {n}
Total time  : {total_time:.2f}s
FPS         : {fps:.2f}
"""

    model_dir = os.path.dirname(model_path)
    eval_path = os.path.join(model_dir, "best_eval.txt")
    with open(eval_path, "w", encoding="utf-8") as f:
        f.write(eval_text)

    print(f"\n📄 评估结果已保存到：{eval_path}")

if __name__ == "__main__":
    evaluate(
        model_path="C:/Users/user/Desktop/best.pt",
        data_yaml="data.yaml",
        save_preds=True,
        tag="baseline_test"
    )
