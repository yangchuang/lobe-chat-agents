import os
import json

# 定义文件夹路径
folder_path = './agents'

# 获取文件夹中的所有文件
file_list = os.listdir(folder_path)

# 遍历文件列表
for file_name in file_list:
    if file_name.endswith('.json'):
        # 读取JSON文件内容
        with open(os.path.join(folder_path, file_name), 'r', encoding='utf-8') as file:
            json_data = json.load(file)
        
        # 添加"identifier"和"schemaVersion"节点
        identifier = file_name.replace('.zh-CN.json', '')
        json_data["identifier"] = identifier
        json_data["schemaVersion"] = 1

        # 将修改后的内容写回文件
        with open(os.path.join(folder_path, file_name), 'w', encoding='utf-8') as file:
            json.dump(json_data, file, ensure_ascii=False, indent=4)