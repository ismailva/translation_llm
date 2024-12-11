from typing import Any
from langchain_openai import ChatOpenAI
from src.utils import SingletonClass, timer
from src.constants import OPENAI_KEY

class GPT_4o_model:
    def __init__(self):
        self.model = ChatOpenAI(model="gpt-4o", api_key=OPENAI_KEY, timeout=60, temperature=0, max_retries=0)
    
    @timer("gpt4o took: ")
    def __call__(self,query, *args, **kwds):
        response = self.model.invoke(query)
        return response.content

        
class LLMModel(metaclass=SingletonClass):
    def get_model(model_name:str="gpt4o") -> Any:
        if model_name == "gpt4o":
            model_instance = GPT_4o_model()
        return model_instance
