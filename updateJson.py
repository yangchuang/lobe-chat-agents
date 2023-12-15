## 提取下载下来的agent文件中的有效节点
import os
import json

# 定义文件夹路径
folder_path = './agents'

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        file_path = os.path.join(folder_path, filename)
        
        # 读取json文件
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # 提取"sessions"节点的第一个object
        extracted_session = data['state']['sessions'][0]
        
        # 覆盖原始的json文件
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(extracted_session, file, ensure_ascii=False, indent=4)