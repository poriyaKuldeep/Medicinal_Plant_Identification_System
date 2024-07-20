import streamlit as st
from PIL import Image
import requests
import json

global class_name 

label=False


st.title('Plant identification')

model = 0
class_names = 'dummy' 

st.header('please upload a plant image')

with st.sidebar:
        st.image('Myplant.jpg')
        st.title("PlantMed")
        st.markdown("Identification of plant species offers important knowledge on the categorization and properties of plants. Many plants are richly having medicinal ingredients and contain medicinal active ingredients. The manual identification of medicinal plants takes time and the assistance of plant identification experts is necessary. To solve this problem, it is essential for human beings to **_automatically recognize_** and classify medicinal plants.")



# file = st.file_uploader('', type=['jpeg','jpg','png'] ,label_visibility="hidden")

uploaded_image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"], key="image")


if uploaded_image is not None:
#     image = Image.open(file).convert('RGB')
    st.image(uploaded_image, use_column_width=True ,caption="Uploaded Image")

    files = {"file": uploaded_image}


    res=requests.post(url='http://127.0.0.1:8000/predict',files=files)


    st.subheader(f"Potential Name of the plant = {res.text}")
    class_name=res.text

    # st.subheader(f"Potential Name of the plant :                {class_name}")

    # st.write("""   """)

    st.sidebar.success(f"Potential Name of the plant : {class_name}")
    label=True



           



if label:
    
    import os
    from dotenv import load_dotenv
    from langchain.prompts import PromptTemplate

    import google.generativeai as genai
    from langchain_google_genai import ChatGoogleGenerativeAI
    from langchain.memory import ConversationBufferWindowMemory
    from langchain.chains import ConversationChain
    from langchain.chains.question_answering import load_qa_chain
    


    from langchain.prompts import (
        SystemMessagePromptTemplate,
        HumanMessagePromptTemplate,
        ChatPromptTemplate,
        MessagesPlaceholder
    )
    from streamlit_chat import message
    from langchain.llms import google_palm
    # from langchain_community.llms.google_palm import GooglePalm
    from langchain_google_genai import GoogleGenerativeAI
    from langchain.schema.output_parser import StrOutputParser

    load_dotenv()
    os.getenv("GOOGLE_API_KEY")
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

    # st.set_page_config('plant info app')
    # st.header('chat with your plant name')

    from langchain.prompts import PromptTemplate
    from langchain.chains.llm import LLMChain

    template = "Give a comprehensive overview of the medicinal plant name {class_name}, including its description Into 150 words and natural habitat, and medicinal uses In point wise . Give me Into human readable simple language"
    prompt = PromptTemplate(input_variables=["class_name"], template=template)

    
    model = GoogleGenerativeAI(model="models/text-bison-001", google_api_key=os.environ["GOOGLE_API_KEY"], temperature=0.1)


    
    chain=LLMChain(llm=model,prompt=prompt)
    response=chain.run(class_name=class_name)
    st.write(response)










    #
    # model = ChatGoogleGenerativeAI(model="gemini-pro",
    #                             temperature=0.3)

    # from langchain.prompts import ChatPromptTemplate
    # from langchain.schema.output_parser import StrOutputParser

    # # prompt=ChatPromptTemplate.from_template(
    # #     f"Give a comprehensive overview of the medicinal plant name {class_name}, including its description Into 150 words and natural habitat, and medicinal uses In point wise . Give me Into human readable simple language")

    # output_parser=StrOutputParser()


    # chain=prompt | model | output_parser 
    # response=chain.invoke({"class_name":class_name})
    # st.write(response)




    #conversation part:


    st.header("If you want to know more about plant Our AI assistane Is here to help you")

    if 'responses' not in st.session_state:
        st.session_state['responses'] = ["How can I assist you?"]

    if 'requests' not in st.session_state:
        st.session_state['requests'] = []

    if 'buffer_memory' not in st.session_state:
                st.session_state.buffer_memory=ConversationBufferWindowMemory(k=3,return_messages=True)




    def get_response(query):
            template = """The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

            Current conversation:
            {history}
            Human: {input}
            AI Assistant:"""
            PROMPT = PromptTemplate(input_variables=["history", "input"], template=template)
            conversation = ConversationChain(
                prompt=PROMPT,
                llm=model,
                verbose=True,
                memory=ConversationBufferWindowMemory(ai_prefix="AI Assistant"),
            )
            return conversation.predict(input=query)
        
    def get_response_final(user_query, chat_history):

        template = """
        You are a helpful assistant. Answer the following questions considering the history of the conversation:

        Chat history: {chat_history}

        User question: {user_question}
        """

        prompt = ChatPromptTemplate.from_template(template)

        output_parser=StrOutputParser()
            
        chain = prompt | model | output_parser
        
        return chain.stream({
            "chat_history": chat_history,
            "user_question": user_query,
        })      




                
    from langchain_core.messages import HumanMessage,AIMessage
    st.title('Medical bot')   

    if "chat_history" not in st.session_state:
        st.session_state.chat_history=[]

    user_query=st.chat_input("Your message")


    #conversation:
    for message in st.session_state.chat_history:
        if isinstance(message,HumanMessage):
                with st.chat_message("Human"):
                        st.markdown(message.content)
        else:
                with st.chat_message("AI"):
                        st.markdown(message.content)
                
    if user_query:
        st.session_state.chat_history.append(HumanMessage(user_query))

        with st.chat_message("Human"):
                st.markdown(user_query)
        with st.chat_message("AI"):
                ai_response = st.write_stream(get_response_final(user_query, st.session_state.chat_history))

        st.session_state.chat_history.append(AIMessage(ai_response))

            
       

# async def main():
#       await fun1()
#       await func2()

# asyncio.run(main())






