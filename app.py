
import streamlit as st
import google.generativeai as gen_ai



# Cấu hình cài đặt trang Streamlit
st.set_page_config(
    page_title="Trò chuyện với Gemini-Pro!",
    page_icon="🤖",  # Biểu tượng Favicon
    layout="centered",  # Tùy chọn bố cục trang
)

# Thiết lập mô hình AI Gemini-Pro của Google
gen_ai.configure(api_key='AIzaSyCb_qq6aqOHM_6jwMTJiW0v0kb9FkPnsos')
model = gen_ai.GenerativeModel('gemini-pro')


# Hàm để dịch vai trò giữa Gemini-Pro và thuật ngữ của Streamlit
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role


# Khởi tạo phiên trò chuyện trong Streamlit nếu chưa có
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])


# Hiển thị tiêu đề chatbot trên trang
st.title("Gemini - ChatBot")

# Hiển thị lịch sử trò chuyện
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# Trường nhập liệu cho tin nhắn của người dùng
user_prompt = st.chat_input("Hỏi Gemini-Pro...")
if user_prompt:
    # Thêm tin nhắn của người dùng vào trò chuyện và hiển thị nó
    st.chat_message("user").markdown(user_prompt)

    # Gửi tin nhắn của người dùng đến Gemini-Pro và nhận phản hồi
    gemini_response = st.session_state.chat_session.send_message(user_prompt)

    # Hiển thị phản hồi của Gemini-Pro
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)
