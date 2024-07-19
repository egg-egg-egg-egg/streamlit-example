"""
用于文件下载
"""
import json
import os
import time


import streamlit as st
from streamlit_monaco import st_monaco
from src.use_pygment import code_to_image
# import streamlit.components.v1 as components
# from src import utils as u

# cfg_path = u.read_json_file("./config/path.json")

# options = st.multiselect(
#     "多选选框",
#     ["Green", "Yellow", "Red", "Blue"],
#     ["Yellow", "Red"])

# st.write("You selected:", options)


# def run():
# 	iframe_src = "https://flowus.cn/share/6781489a-d317-4da7-b07d-7414ab3def45?code=DD8PQT&embed=true"
# 	components.iframe(iframe_src,height=1000,width=1000)  # 你可以为组件添加高度和宽度
path = "./data/inTeach_img"

st.set_page_config(
	page_title="let me see see",  # 页面标题
	page_icon=":smile:",  # 页面图标
	# layout="wide",  # 页面布局
	initial_sidebar_state="expanded",  # 初始侧边栏状态
	menu_items={
		# 'Get Help': 'https://github.com/',
		# 'Report a bug': "https://github.com/",
		'About': "黄老师耗时一坤天完成的小网站",
	}
)

def create_folder(folder_path):
	if not os.path.exists(folder_path):
		os.makedirs(folder_path)
		return True
	else :
		return False
def save_iamg(imag:bytes,file_path:str):
	with open(file_path, "wb") as f:
		f.write(imag)
	st.toast(f'创建成功 {file_path}',icon='😁')
	


def user_view(cpw):
	cpw_path = os.path.join(path,cpw)
	if not os.path.exists(cpw_path):
		st.toast(f'`{cpw}`口令不存在，请询问老师',icon='🐷')
	else:
		st.write(f"""
		# 口令👌：{cpw}
		""")
		show_img(cpw_path)
		

@st.experimental_fragment
def show_img(cpw_dirpath:str):
	"""
	cpw_dirpath: 基路径+课堂上的口令得到的一个目录
	
	可以选择题目，查看代码
	"""
	# 确保可选项可以实时更新
	try:
		imag_optinos = map(lambda x: x.split('.')[0],os.listdir(cpw_dirpath))
	except Exception as e:
		imag_optinos = []
	# st单选box
	input_text = None
	if imag_optinos:
		input_text = st.selectbox(
		"输入要查看的题目名",
		imag_optinos,
		index=None,
		placeholder="",
		)


	if input_text:
		default_imag_format = "{}.png"
		file_path = os.path.join(cpw_dirpath, default_imag_format.format(input_text))
		st.image(file_path, caption=f'{input_text}题代码',width=700)

@st.experimental_dialog("上传代码")
def dalog_uploadIamg(set_cpw_path:str):
	# 对话框中上传代码

	with st.expander("输入代码"):
		code_text = None
		problem_num_code = st.text_input("输入题目名",key="through_text")
		code_text = st_monaco(height="300px", language="cpp",theme="vs-dark",minimap=True)
		if  code_text and problem_num_code and st.button("点击创建",help="输入题目名和代码后提交",use_container_width=True,key="submitCodeText"):
			# 保存到本地
			file_path = os.path.join(set_cpw_path, f"{problem_num_code}.png")
			highlighted_code = code_to_image(code_text,file_path,language="cpp",font_name="./src/fonts/msyh.ttc")
			# 将高亮的代码写入文件
			save_iamg(highlighted_code,file_path)
			

	# 上传图片组件
	with st.expander("上传图片"):
		problem_num_imag = st.text_input("输入题目名",key="through_imag")
		imag = st.file_uploader("上传图片",type=['png','jpg','jpeg'])
		if  imag and problem_num_imag and st.button("点击创建",help="输入题目名和代码后提交",use_container_width=True,key="submitCodeImag"):
			file_path = os.path.join(set_cpw_path, f"{problem_num_imag}.png")
			# imag 保存到本地
			save_iamg(imag.getvalue(),file_path)
			
	
	

    # if st.button("提交"):
        # st.session_state.vote = {"item": item, "reason": reason}
        # st.rerun()
	

def update_imag(cpw:str|None):
	"""
	管理员界面，可设置口令和添加代码图片，使用设置的目录作为show_imag的路径
	"""

	
	with st.sidebar:
		with st.popover("配置",use_container_width=True):
			set_cpw = st.text_input("设置口令",key="setCPW")
			enter_cpw = st.button("确认口令","confirmSetCPW")
			if enter_cpw and set_cpw:
				set_cpw_path = os.path.join(path, f"{set_cpw}")
				st.session_state.set_cpw = set_cpw
				st.session_state.set_cpw_path = set_cpw_path
				is_create_cpw = create_folder(set_cpw_path)
				if is_create_cpw:
					st.info(f'设置成功 {set_cpw_path}',icon='✔')
				else:
					st.info(f'口令已存在 {set_cpw_path}',icon='🈶')
			elif enter_cpw:
				st.warning(f'口令不能为空',icon='⚠️')
		# 输入组件
		if st.button("提交代码",type='primary',use_container_width=True,key="submitUI") and st.session_state.get("set_cpw_path",None):
			dalog_uploadIamg(st.session_state.set_cpw_path)
	
	if st.session_state.get("set_cpw_path",None):
		st.write(f"""
		# 口令：{st.session_state.set_cpw}
		""")
		show_img(st.session_state.set_cpw_path)


def main():
	
	st.write("""
	# 代码查看器👁
	> 输入老师上课给出的口令，查看老师写的代码
	""")
	st.session_state.cpw = None
	
	temp_st = st.empty()
	with temp_st.popover("配置",use_container_width=True,):
		st.session_state.cpw = st.text_input("填写口令",type="password",key="home_cpw")

	if st.session_state.cpw == st.secrets["admin_pw"]: # 初始口令如果是管理员口令，则进入管理员界面
		temp_st.empty()
		update_imag(st.session_state.cpw)
		
	elif st.session_state.cpw != "":
		user_view(st.session_state.cpw)
	


if __name__ == "__main__":
	main()
	
