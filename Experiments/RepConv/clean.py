import os
import shutil

def safe_rmdir(path):
    if os.path.exists(path):
        shutil.rmtree(path)
        print(f"🗑️ 已删除目录：{path}")
    else:
        print(f"✅ 路径不存在，跳过：{path}")

def safe_rmfile(path):
    if os.path.exists(path):
        os.remove(path)
        print(f"🗑️ 已删除文件：{path}")
    else:
        print(f"✅ 路径不存在，跳过：{path}")

def main():
    base = "C:/Users/user/PycharmProjects/Yolov8ncloud/Experiments/RepConv"

    # 清理训练结果目录
    safe_rmdir(os.path.join(base, "results", "repconv_exp1"))
    safe_rmdir(os.path.join(base, "runs"))

    # 清理数据集缓存
    dataset_dir = "C:/Users/user/PycharmProjects/Yolov8ncloud/Datasets"
    safe_rmfile(os.path.join(dataset_dir, "train.cache"))
    safe_rmfile(os.path.join(dataset_dir, "val.cache"))
    safe_rmfile(os.path.join(dataset_dir, "test.cache"))

if __name__ == "__main__":
    main()
