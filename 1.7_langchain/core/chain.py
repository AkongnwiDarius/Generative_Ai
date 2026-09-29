from langchain_core.output_parsers import StrOutputParser
from itertools import chain
from .models import create_model
from config import QWEN
from .prompt_boot import prompt

model = create_model()
parser = StrOutputParser()

announcement = prompt | model | parser





