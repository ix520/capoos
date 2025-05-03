import os

# 定义文件夹路径
folder_path = r'E:\GitHub\capoos\capoo'

# 获取文件夹内的所有文件
files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
files.sort()

# 遍历文件并进行重命名
for index, file in enumerate(files, start=1):
    # 生成新的文件名，固定后缀为.gif
    new_file_name = f"{index}.gif"
    # 构建旧文件路径和新文件路径
    old_file_path = os.path.join(folder_path, file)
    new_file_path = os.path.join(folder_path, new_file_name)
    # 重命名文件
    os.rename(old_file_path, new_file_path)

print("文件重命名完成")