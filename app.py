import streamlit as st
from openai import OpenAI
import json

client = OpenAI(
    api_key='sk-aDn1hpDc32Cm8DGE9lbudSpcVcRusb70qMntDZkEdw0c52YP',
    base_url='https://api.opentyphoon.ai/v1'
)

def load_data(file_path): 
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def generate_response(prompt):
    chat_completion = client.chat.completions.create(
        model="typhoon-v1.5x-70b-instruct",
        messages=[{"role": "user", "content": prompt}]
    )
    return chat_completion.choices[0].message.content

def ask_question(data, question):
    prompt = f"Based on the following information about Pathum Thani development: {data}, answer this question: {question}"
    response = generate_response(prompt)
    return response

def main():
    st.title("GrowthVision Pathum Chatbot")
    st.write("Ask questions related to Pathum Thani development.")
    data_path = 'Data/Factsheets/markdown_output.json'
    pathum_thani_data = load_data(data_path)
    question = st.text_input("Enter your question:")
    if st.button("Ask"):
        if question:
            answer = ask_question(pathum_thani_data, question)
            st.write("Answer:", answer)
        else:
            st.write("Please enter a question.")

if __name__ == "__main__":
    main()
