import os
import json

import streamlit as st

def get_file_names(directory:str):
    """
    获取指定目录下的所有文件名（不包括子目录中的文件）。
    
    :param directory: 目录路径。
    :return: 文件名列表。
    """
    try:
        # 列出指定目录下的所有条目
        entries = os.listdir(directory)
        # 过滤出文件（排除目录）
        file_names = (name for name in entries if os.path.isfile(os.path.join(directory, name)))
        return file_names
    except Exception as e:
        print(f"Error occurred: {e}")
        return ()

@st.cache_data
def read_json_file(file_path: str):
    """
    读取指定路径的JSON文件并返回其内容。
    :param file_path: JSON文件的路径。
    :return: 成功时返回JSON解析后的Python对象（通常是字典或列表），失败时返回None。
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return f"错误：文件 {file_path} 未找到。"
    except json.JSONDecodeError:
        return f"错误：文件 {file_path} 不是有效的JSON格式。"
    except Exception as e:
        return f"读取文件时发生未知错误：{e}"
    
def create_folder(folder_path):
	if not os.path.exists(folder_path):
		os.makedirs(folder_path)
		return True
	else :
		return False

def save_image(image: bytes, file_path: str):
    """Saves an image to the specified file path.
    
    :param image: The image data to save.
    :param file_path: The path where the image will be saved.
    """
    with open(file_path, "wb") as f:
        f.write(image)
    

def get_subdirectory_names(directory: str):
    """
    获取指定目录下的所有子目录名（不包括子目录中的子目录）。
    
    :param directory: 目录路径。
    :return: 子目录名列表。
    """
    try:
        # 列出指定目录下的所有条目
        entries = os.listdir(directory)
        # 过滤出子目录（排除文件）
        subdirectory_names = [name for name in entries if os.path.isdir(os.path.join(directory, name))]
        return subdirectory_names
    except Exception as e:
        print(f"Error occurred: {e}")
        return []