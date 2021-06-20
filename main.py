import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st
import csv
import base64

st.title('英単語の意味抽出アプリケーション')
st.title('for サッカー英語')

st.write('')

st.write('英単語が書かれたCSVファイルをアップロードしていただくと一括で意味を取得します')
uploaded_file = st.sidebar.file_uploader("ファイルアップロード", type='csv') 

st.write('アップロードするcsvファイルの例')
example_df = pd.DataFrame({
    '英単語':['word1','word2','word3','word4','word5'],
    '     ':['','','','',''],
    '     ':['','','','',''],
    '     ':['','','','',''],
    '     ':['','','','',''],
    '     ':['','','','',''],
    '     ':['','','','',''],

})

st.dataframe(example_df,width = 1000, height = 500)

st.header('読み込みデータの表示')


if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df,width = 1000, height = 500)

    word_list = df['英単語']
    
    url_list = []
    for add_url in word_list:
        url = 'https://ejje.weblio.jp/content/' + str(add_url)
        url_list.append(url)
    
    word_explanations = []


    latest_iteration = st.empty()
    bar = st.progress(0)
    i = 0

    
    for url in url_list:
        try:
            
            res  = requests.get(url)
            soup = BeautifulSoup(res.text,'html.parser')
            word_explanation = soup.find('td',attrs = {'class','content-explanation'})
            word_explanations.append(word_explanation.text)
            latest_iteration.text(f'取得単語数{i+1}語')
            bar.progress((i+1)/len(word_list))
            i = i + 1

        except Exception:
            word_explanations.append('意味を取得できませんでした')
            pass

    
    new_df = pd.DataFrame({

        '英単語':word_list,
        '意味':word_explanations

    })

    st.header('変換後のデータの表示')
    st.write(new_df)

    csv = new_df.to_csv(index = False).encode()

    b64 = base64.b64encode(csv).decode()

    href = f'<a href="data:file/csv;base64,{b64}" download="new_file.csv">Download csv</a>'

    expander = st.beta_expander('csvダウンロード')
    expander.markdown(href, unsafe_allow_html=True)
    


    





