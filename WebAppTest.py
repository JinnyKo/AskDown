import logging
import random
import streamlit
from streamlit.commands.page_config import RANDOM_EMOJIS
from revChatGPT.V1 import Chatbot

# Streamlit 페이지 설정
streamlit.set_page_config(page_title="Jinny Bot", page_icon=random.choice(RANDOM_EMOJIS), menu_items={})
streamlit.title("Jinny ASkDown Demo with GPT3.0 ")
streamlit.sidebar.header("History")
streamlit.sidebar.info("Chat1")
streamlit.sidebar.info("Chat2")
streamlit.sidebar.info("Chat3")

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
element = streamlit.empty()

# OpenAI GPT-3.0에 대한 요청 함수 정의
def request_to_rev_openai(query):
    # Chatbot 인스턴스 생성
    chatbot = Chatbot(config={
        "access_token": "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"
    })

    # GPT-3.0을 사용하여 대답 생성 및 출력
    prev_text = ""
    for data in chatbot.ask(prompt=query):
        prev_text = data["message"]
        element.write(prev_text, unsafe_allow_html=True)

# 사용자 입력을 받고 GPT-3.0에 요청하는 함수
def app_main():
    user_query = streamlit.text_input("Enter").strip()
    if user_query is not None and user_query and user_query != "":
        # 사용자의 질문을 OpenAI GPT-3.0에 전달하여 대답 요청
        request_to_rev_openai(user_query)

        # 대답에 대한 키워드 생성
        # 이 부분에서는 임시로 랜덤한 키워드를 생성하도록 하겠습니다.
        keywords = ["Keyword1", "Keyword2", "Keyword3"]
        
        # 사용자에게 키워드를 제시하고 선택하도록 함
        selected_keyword = streamlit.selectbox("Select a keyword:", keywords)
        
        # 선택된 키워드에 대한 추가 정보를 표시
        if selected_keyword:
            # 여기에 선택된 키워드에 관련된 추가 정보를 표시하는 코드를 추가하세요.
            streamlit.write(f"More information about {selected_keyword}")
# 임시 대답 생성 함수
def generate_temporary_response():
    responses = [
        "임시로 생성된 대답입니다.",
        "다른 대답을 생성하면 무엇을 도와드릴까요?",
        "이것은 임시 대답입니다. 더 자세한 내용을 알고 싶으신가요?"
    ]
    return random.choices(responses, k=3)  # 랜덤하게 3개의 대답을 선택

# 사용자 입력 받기
user_question = streamlit.text_input("질문을 입력하세요:")

# 사용자가 질문을 입력한 경우
if user_question:
    # 임시 대답 생성
    temp_responses = generate_temporary_response()

    # 생성된 대답 표시
    streamlit.write("임시 대답:")
    for response in temp_responses:
        streamlit.write("- ", response)

    # 사용자가 선택할 수 있는 키워드 목록
    keywords = ["키워드1", "키워드2", "키워드3"]

    # 사용자가 선택한 키워드 표시
    selected_keywords = streamlit.multiselect("키워드 선택:", keywords)

    # 사용자가 선택한 키워드에 관한 추가 정보 표시
    for keyword in selected_keywords:
        streamlit.write(f"선택한 키워드: {keyword}")
        # 선택한 키워드에 관한 추가 정보를 여기에 표시할 수 있습니다.

# 메인 애플리케이션 실행
app_main()
