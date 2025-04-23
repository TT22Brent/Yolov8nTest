import shutil
import os

def remove_path(path):
    if os.path.exists(path):
        shutil.rmtree(path)
        print(f"🧹 已删除目录: {path}")
    else:
        print(f"✅ 跳过：{path} 不存在")

def main():
    # 设置你要清除的目录路径（绝对路径或相对路径）
    paths_to_clean = [
        "runs/gsconv_trial",
        "ultralytics/runs/train",             # 若意外写进源码包了
        "ultralytics/runs/detect/gsconv_trial",
        "runs/detect/gsconv_trial",
        "runs/train/gsconv_trial",
        "__pycache__",
        ".cache"
    ]

    for path in paths_to_clean:
        remove_path(path)

    # 清除残留权重（可选）
    for file in ["best.pt", "last.pt"]:
        for root, _, files in os.walk("."):
            if file in files:
                full_path = os.path.join(root, file)
                try:
                    os.remove(full_path)
                    print(f"🗑️  已删除权重文件: {full_path}")
                except Exception as e:
                    print(f"⚠️  删除失败: {full_path} - {e}")

    print("\n✅ 清理完成，环境已重置")

if __name__ == "__main__":
    main()
