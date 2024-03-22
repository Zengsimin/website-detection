import streamlit as st
# Streamlit 应用程序的主体部分
def main():
    st.title("hek")
    # 文本输入框, 用户输入文章URL
    url = st.text_input("请输入一个URL")
# 运行 Streamlit 应用程序
if __name__ == '__main__':
    main()
