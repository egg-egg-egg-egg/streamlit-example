"""
用于文件下载
"""
# import os
# import json

# import streamlit as st
# import streamlit.components.v1 as components

# from src import utils as u


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




# def run():
# 	iframe_src = "https://flowus.cn/share/6781489a-d317-4da7-b07d-7414ab3def45?code=DD8PQT&embed=true"
# 	components.iframe(iframe_src,height=1000,width=1000)  # 你可以为组件添加高度和宽度

# if __name__ == "__main__":
# 	run()
import streamlit as st
from execbox import execbox

st.set_page_config(
    page_title="My Awesome App",
    page_icon=":shark:",
    layout="centered",
    initial_sidebar_state="expanded"  # 设置侧边栏初始为展开状态
)

# 可以在这个路径修改运行按钮的英文"D:\ProgramData\anaconda3\envs\EduTools\Lib\site-packages\streamlit_ace\frontend\build\static\js\main.707cd2a5.chunk.js"
# 放置在侧边栏
with st.sidebar:
    execbox("""
import streamlit as st

open = None
a = 10
b = 20
st.write(a + b)
    """,autorun=True)
# try:
#     exec(content, local_scope)
# except Exception as e:
#     st.exception(e)

# def _new_sandbox():
#     import types
#     module = types.ModuleType("__main__")
#     return module.__dict__
# local_scope = _new_sandbox()

# exec("""
# open = None
# print = st.write
# print(open)
# """, local_scope)
# # print(local_scope)
