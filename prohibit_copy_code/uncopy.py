import streamlit as st
from streamlit.components.v1 import html

# 防复制 CSS + JavaScript 代码
anti_copy_code = """
<style>
.no-copy {
    user-select: none;          /* 禁止选择文本 */
    -webkit-user-select: none; /* Safari */
    -moz-user-select: none;    /* Firefox */
    -ms-user-select: none;     /* IE/Edge */
}

.no-copy::selection {
    background: transparent;   /* 隐藏选中高亮 */
}
</style>

<script>
document.addEventListener('keydown', e => {
    if (e.key === 'F12' || (e.ctrlKey && e.shiftKey && e.key === 'I')) {
        e.preventDefault();
        alert('禁止查看源码！');
    }
});

document.addEventListener('keydown', e => {{
    if (e.key === 'F12' || (e.ctrlKey && e.shiftKey && e.key === 'I')) {{
        e.preventDefault();
        alert('禁止查看源码！');
    }}
}});

document.addEventListener('DOMContentLoaded', function() {{
    // 禁用右键菜单
    document.addEventListener('contextmenu', e => e.preventDefault());
    
    // 禁用 Ctrl+C / Cmd+C 快捷键
    document.addEventListener('keydown', e => {{
        if ((e.ctrlKey || e.metaKey) && e.key === 'c') {{
            e.preventDefault();
            alert('禁止复制！');
        }}
    }});

    // 定时检查控制台是否打开
    setInterval(function() {{
        if (window.console && (console.firebug || console.table && /firebug/i.test(console.table()))) {{
            alert('禁止查看源码！');
            window.close();
        }}
    }}, 1000);

    // 解码并显示代码块
    const encodedCode = "{encoded_code}";
    const decodedCode = atob(encodedCode);
    document.getElementById('code-block').innerText = decodedCode;
}});
</script>
"""

# 在 Streamlit 中渲染一个防复制的代码块
html(f"""
{anti_copy_code}
<div class="no-copy" style="
    background: #f5f5f5;
    padding: 1rem;
    border-radius: 5px;
    font-family: monospace;
">
print('这是一个不可复制的代码块')
</div>
""", height=80)