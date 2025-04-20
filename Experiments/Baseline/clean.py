import os
import shutil

def delete_if_exists(path):
    if os.path.isfile(path):
        os.remove(path)
    elif os.path.isdir(path):
        shutil.rmtree(path)

def main():
    print("🧹 开始清理项目中所有非必要的临时文件...")

    # 1. 删除结果目录
    delete_if_exists("results")

    # 2. 删除 ultralytics 中的 runs 和缓存
    delete_if_exists("ultralytics/runs")
    delete_if_exists("ultralytics/runs/detect/train.cache")
    delete_if_exists("ultralytics/runs/detect/val.cache")

    # 3. 删除所有 __pycache__ 和 .pyc/.pyo 文件
    for root, dirs, files in os.walk("."):
        for d in dirs:
            if d == "__pycache__":
                full_path = os.path.join(root, d)
                print(f"🔴 删除目录：{full_path}")
                shutil.rmtree(full_path)
        for f in files:
            if f.endswith(".pyc") or f.endswith(".pyo") or f.endswith(".cache"):
                full_path = os.path.join(root, f)
                print(f"🔴 删除文件：{full_path}")
                os.remove(full_path)

    print("✅ 清理完成！你现在可以安全打包上传云端，重新开始训练。")

if __name__ == "__main__":
    main()
