#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Python     :   3.9
@Date       :   2024/4/2 15:13

'''
import streamlit as st
from streamlit_chat import message

GLM_LOGO = "data:image/png;base64,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"
PEOPLE_LOGO = "https://chatglm.cn/img/user_head.49ce25cd.svg"

if "past" not in st.session_state:
    st.session_state.past = []

if "generated" not in st.session_state:
    st.session_state.generated = []

if "role_desc_input" not in st.session_state:
    st.session_state.role_desc_input = ""

st.set_page_config(
    page_title="st-chart示例",
    layout="wide"
)
st.title("st-chart示例")
st.text_input("请输入角色相关的描述（可为空）", key="role_desc_input")

import random,time
def example_response():
    for i in range(20):
        yield str(random.randint(10,100))+" "
        time.sleep(0.05)

def on_input_change():
    user_input = st.session_state.user_input
    if user_input:
        st.session_state.past.append(user_input)
        st.session_state.generated.append(example_response())

def on_clear_msg_click():
    del st.session_state.past[:]
    del st.session_state.generated[:]



chat_placeholder = st.empty()
with chat_placeholder.container():
    for i in range(len(st.session_state['generated'])):
        message(st.session_state['past'][i], is_user=True, key=f"{i}_user", logo=PEOPLE_LOGO)
        if isinstance(st.session_state['generated'][i], str):
            message(
                st.session_state['generated'][i],
                key=f"{i}_glm", logo=GLM_LOGO,
                allow_html=True,
                is_table=False
            )
        else:
            r = st.write_stream(st.session_state['generated'][i])
            st.session_state['generated'][i] = "".join(r)

with st.container():
    st.button("清空消息", on_click=on_clear_msg_click)
    st.text_input("用户输入:", key="user_input", on_change=on_input_change)