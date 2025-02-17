import streamlit as st
from streamlit.components.v1 import html
import base64


st.code("print('这是要截图的内容')",line_numbers=True,wrap_lines=True)

# 嵌入自定义 HTML/JavaScript
html_code = """
<script src="https://cdnjs.cloudflare.com/ajax/libs/dom-to-image/2.6.0/dom-to-image.min.js"></script>
<div id="target-element" style="background: #f5f5f5; padding: 1rem; border-radius: 5px; font-family: monospace;">
print('这是要截图的内容')
</div>
<button onclick="capture()">截图</button>

<script>
function capture() {
    domtoimage.toPng(document.getElementById('target-element'))
        .then(function (dataUrl) {
            // 将图片数据传回 Streamlit
            const link = document.createElement('a');
            link.href = dataUrl;
            link.download = 'code_image.png';
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        });
}
</script>
"""

# 显示前端组件
html(html_code, height=200)