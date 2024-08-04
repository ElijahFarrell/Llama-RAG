import getpass
import os
from dotenv import load_dotenv

load_dotenv()
from huggingface_hub import login
login()

#hugging_face_token = os.getenv("HuggingFaceToken")
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3.1-70B",
    task="text-generation",
    max_new_tokens=10000,
    do_sample=False,
    repetition_penalty=1.03,
)

chat_model = ChatHuggingFace(llm=llm)

response =chat_model.invoke("Can you give me an example of headings I should write out on a business plan?")

print(response.content)