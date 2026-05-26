Python
import streamlit as st

# サイトのタイトル
st.title("テスト用ファイルアップローダー")
st.write("ここにファイルをアップロードしてテストができます。")

# ファイルアップロード機能（これだけで画面が作れます）
uploaded_file = st.file_uploader("ファイルをここにドラッグ＆ドロップしてください")

# ファイルがアップロードされたら動く処理
if uploaded_file is not None:
    st.success(f"🎉 アップロード成功: {uploaded_file.name}")
    
    # テスト用にファイルの詳細を表示
    st.subheader("アップロードされたファイルの情報")
    st.write(f"- **ファイル名:** {uploaded_file.name}")
    st.write(f"- **サイズ:** {uploaded_file.size} バイト")
    st.write(f"- **データの種類:** {uploaded_file.type}")
