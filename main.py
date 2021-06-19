import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time 


st.title('streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!!'

latest_iteration = st.empty()
bar = st.progress(0)

#for i in range(100):
    
#    latest_iteration.text(f'Iteration {i+1} ')
#    bar.progress(i+1)
#    time.sleep(0.1)

'Done!!'


st.write('Display Image')


left_column ,right_column = st.beta_columns(2)
btn =left_column.button('右からむに文字を表示')
if btn :
    right_column.write('ここは右です')


expander = st.beta_expander('問い合わせ')
expander.text_input('問い合わせ内容を書いてください')

if st.checkbox('Show Image'):

    img = Image.open('esashi.png')
    st.image(img,caption = '江刺さんの画像',use_column_width = True)


option = st.selectbox(
    'あなたが好きな数字は？',
    list(range(1,10))
)
'あなたが好きな数字は', option ,'です'

st.write('Interactive Wigets')

text = st.text_input('あなたの趣味は？')
'あなたの趣味は',text

cond = st.slider('あなたの調子は？',0,100,25)

'あなたの調子は',cond
