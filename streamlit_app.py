"""
用于文件下载
"""
import os
import json

import streamlit as st

from src import utils as u


cfg_path = u.read_json_file("./config/path.json")

# options = st.multiselect(
#     "多选选框",
#     ["Green", "Yellow", "Red", "Blue"],
#     ["Yellow", "Red"])

# st.write("You selected:", options)


# st单选box
option = st.selectbox(
   "你想查看什么代码文件？",
   u.get_file_names(cfg_path["cpp"]),
   index=None,
   placeholder="请选择第几节课",
)