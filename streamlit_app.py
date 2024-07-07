"""
用于文件下载
"""
import os
import json

import streamlit as st
import streamlit.components.v1 as components

from src import utils as u


# cfg_path = u.read_json_file("./config/path.json")

# options = st.multiselect(
#     "多选选框",
#     ["Green", "Yellow", "Red", "Blue"],
#     ["Yellow", "Red"])

# st.write("You selected:", options)


# # st单选box
# option = st.selectbox(
#    "你想查看什么代码文件？",
#    u.get_file_names(cfg_path["cpp"]),
#    index=None,
#    placeholder="请选择第几节课",
# )




def run():
	iframe_src = "https://flowus.cn/share/6781489a-d317-4da7-b07d-7414ab3def45?code=DD8PQT&embed=true"
	components.iframe(iframe_src,height=1000,width=1000)  # 你可以为组件添加高度和宽度

if __name__ == "__main__":
	run()
