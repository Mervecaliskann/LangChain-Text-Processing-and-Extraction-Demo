
# Create OpenAI Function Runnable Chain

# Create OpenAI Function Runnable Chain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from typing import Optional
from langchain.chains.openai_functions import create_openai_fn_runnable

import os
from dotenv import load_dotenv

load_dotenv()

my_key_openai = os.getenv("openai_apikey")

class Insan(BaseModel):
    """Bir insan hakkında tanımlanacak bilgiler"""
    isim: str = Field(..., description="Kisinin ismi")
    yas: int = Field(..., description="Kisinin yasi")
    meslek: Optional[str] = Field(None, description="Kisinin meslegi")

class Sehir(BaseModel):
    """Bir sehir hakkında tanımlanacak bilgiler"""
    isim: str = Field(..., description="Sehrin ismi")
    plaka_no: str = Field(..., description="Sehrin plaka numarasi")
    iklim: Optional[str] = Field(None, description="Sehrin iklimi")

llm = ChatOpenAI(model="gpt-4-0125-preview", api_key=my_key_openai)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "Sen veri kaydı konusunda dünyanın en başarılı algoritmasıısın"),
        ("human", "Şu verdigim girdileri veri kaydı için gerekli fonksiyonlara çağır yap: {input}"),
        ("human", "İpucu: Doğru formatta yazıldığından emin ol!")
    ]
)

chain_2 = create_openai_fn_runnable([Insan, Sehir], llm, prompt)

print(chain_2.invoke({"input": "Aydın 34 yaşında, başarılı bir bilgisayar mühendisiydi"}))
print(chain_2.invoke({"input": "Aydın'da hava her zaman sıcakçaktır ve bu yüzden 09 plakalı araçlar hep klima çalıştırır"}))




# # Create Stuff Documents Chain
# from langchain_openai import ChatOpenAI
# from langchain_core.documents import Document
# from langchain.prompts import ChatPromptTemplate
# from langchain.chains.combine_documents import create_stuff_documents_chain

# import os
# from dotenv import load_dotenv

# load_dotenv()

# my_key_openai = os.getenv("openai_apikey")

# llm = ChatOpenAI(model="gpt-4-0125-preview", api_key=my_key_openai)

# prompt = ChatPromptTemplate.from_messages(
#     [("system", "Burada ismi geçen kişilerin en sevdiği rengi tek tek yaz:\n\n{context}")]
# )

# docs = [
#     Document(page_content="Gamze kırmızı sever ama sarılıyı sevmez"),
#     Document(page_content="Murat yeşili sever ama maviyi sevdiği kadar değil"),
#     Document(page_content="Burak'a sorsan favori rengim yok der ama belli ki turuncu rengi seviyor")
# ]

# chain_1 = create_stuff_documents_chain(llm, prompt)

# print(chain_1.invoke({"context": docs}))

