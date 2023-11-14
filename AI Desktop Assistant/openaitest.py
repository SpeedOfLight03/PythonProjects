# This code is for v1 of the openai package: pypi.org/project/openai
from openai import OpenAI
from config import apikey

client = OpenAI(api_key=apikey)

response = client.completions.create(
    model="text-davinci-003",
    prompt="write an email to my boss for resignation",
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
)
