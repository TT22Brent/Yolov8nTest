import os
import shutil
import glob

def remove_path(path):
    if os.path.isfile(path):
        os.remove(path)
        print(f"🗑️ 删除文件: {path}")
    elif os.path.isdir(path):
        shutil.rmtree(path)
        print(f"🗑️ 删除文件夹: {path}")

def main():
    base_dir = os.path.abspath(".")  # 当前目录

    # 1. 删除训练输出文件夹
    run_dirs = [
        os.path.join(base_dir, "output", "step1_ghostconv"),
    ]

    # 2. 删除缓存文件
    dataset_dir = r"C:\Users\user\PycharmProjects\Yolov8ncloud\Datasets\labels"
    cache_files = [
        os.path.join(dataset_dir, "train.cache"),
        os.path.join(dataset_dir, "val.cache"),
        os.path.join(dataset_dir, "test.cache"),
    ]

    # 3. 删除下载的预训练权重（如有）
    weight_files = glob.glob(os.path.join(base_dir, "*.pt"))

    # 4. 执行清理
    print("🚧 开始清理运行痕迹...\n")
    for path in run_dirs + cache_files + weight_files:
        if os.path.exists(path):
            remove_path(path)
        else:
            print(f"✅ 跳过不存在: {path}")

    print("\n✅ 清理完成！")

if __name__ == "__main__":
    main()
