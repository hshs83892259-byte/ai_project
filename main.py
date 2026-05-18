import streamlit as st
st.title('나의 첫 웹서비스 만들기')
a=st.text_input('야 기분 딱 좋다')
b=st.selectbox('뭐 좋아하노',['응디','게이','똥꼬'])
if st.button('응디'):
  st.write(a+'님, 요로시쿠')
st.info('하이요')
st.warning('b+ 이것을 좋아하시나봐요')
st.error('tlqkf')
st.baiioons
