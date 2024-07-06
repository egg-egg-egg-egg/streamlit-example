# 设计思路

1. c++/python的代码不允许下载和复制，只能查看
2. 可以下载scratch文件


# 文件说明
```bash
project_name/
│
├── app.py                # Streamlit应用程序的入口点
│
├── assets/               # 存放静态资源如图片、CSS样式等
│   ├── logo.png
│   └── style.css
│
├── data/                 # 存放项目中用到的数据文件或用户可下载的文件
│   ├── sample_data.csv
│   └── ...
│
├── src/                  # 包含所有主要的逻辑和功能模块
│   ├── file_handler.py   # 文件处理相关的函数或类，如读取、准备文件下载等
│   ├── utils.py          # 其他辅助函数或工具类
│   └── ...
│
├── requirements.txt      # 项目依赖列表
│
├── README.md             # 项目说明文档，介绍项目、安装步骤、使用方法等
│
└── .streamlit/           # Streamlit配置文件夹（Streamlit自动管理）
    └── config.toml
```