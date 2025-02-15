import os

from pygments import highlight
from pygments.formatters.img import ImageFormatter
from pygments.lexers.c_cpp import CppLexer
from pygments.lexers.python import PythonLexer

# 如果文件夹路径不存在则创建文件夹
def _create_folder(folder_path):
	if not os.path.exists(folder_path):
		os.makedirs(folder_path)

def code_to_image(code: str, file_path: str, language: str = "cpp",font_name:str=r'C:\Windows\Fonts\msyh.ttc'):
    """
    将代码转换为图片并保存到指定路径。

    参数:
    code (str): 要转换的代码字符串。
    file_path (str): 保存图片的文件路径。
    language (str): 代码的语言类型
    """
    _create_folder(os.path.dirname(file_path))
    lexer_dict = {
        "py": PythonLexer,
        "python": PythonLexer,
        "cpp": CppLexer,
        "c++": CppLexer
    }
    
    # 确保语言键存在于字典中
    if language not in lexer_dict:
        raise ValueError(f"Unsupported language: {language}")

    # 创建词法分析器实例
    lexer = lexer_dict[language]()

    # 使用Pygments库对代码进行语法高亮
    formatter = ImageFormatter(
        # font_name='Consolas', 
        font_name=font_name, 
        font_size=20,
        line_numbers=True,
        style="monokai",
    )
    highlighted_code = highlight(code, lexer, formatter)

    return highlighted_code



if __name__ == "__main__":
    # 测试代码
    code = '''
    #include<bits/stdc++.h>

    using namespace std;
    int n;
    int main(){
        cin>>n;
        printf("hello world");  // 打印
        return 0;
    }

    '''
    
    code_py = """
    # 来电中文
    def hello_world():
        print("hello world")
"""
    path = r"./"
    # import os

    file_path = os.path.join(path, f'{2}.png')
    imag = code_to_image(code_py, file_path, language="python")  # Corrected function name
    from utils import save_image
    save_image(imag, file_path)
