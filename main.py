# -*- coding: utf-8 -*-
"""FinGPT_v2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FduPuzY7ep70VoHiIhRZeJ8w2Q_TKgp4
"""



!pip install protobuf transformers==4.32.0 cpm_kernels torch>=2.0 gradio mdtex2html sentencepiece accelerate

!pip install transformers==4.32.0 peft==0.5.0
!pip install sentencepiece
!pip install accelerate
!pip install torch
!pip install peft
!pip install datasets
!pip install bitsandbytes

#for the `load_in_8bit=True` error


"""## Inference with Single Task: Sentiment"""

from transformers import AutoModel, AutoTokenizer, AutoModelForCausalLM, LlamaForCausalLM, LlamaTokenizerFast
from peft import PeftModel  # 0.5.0

# Load Models
base_model = "NousResearch/Llama-2-13b-hf"
peft_model = "FinGPT/fingpt-sentiment_llama2-13b_lora"
tokenizer = LlamaTokenizerFast.from_pretrained(base_model, trust_remote_code=True)
tokenizer.pad_token = tokenizer.eos_token
model = LlamaForCausalLM.from_pretrained(base_model, trust_remote_code=True, device_map = "cuda:0", load_in_8bit = True,)
model = PeftModel.from_pretrained(model, peft_model)
model = model.eval()

import pandas as pd

AMZNdata = pd.read_csv('amzn_news.csv')
GOOGldata = pd.read_csv('googl_news.csv')
NFLXdata = pd.read_csv('nflx_news.csv')
TSLAdata = pd.read_csv('tsla_news.csv')
NVDAdata = pd.read_csv('nvda_news.csv')

def get_sentiment(stock, title):
    prompt = f"""Instruction: What is the sentiment of this news title for the stock of {stock}? Your task is to analyze news headlines and determine their sentiment with respect to the stock mentioned. Please choose an answer from {{negative, neutral, positive}}.
Input: {title}
Answer: """
    tokens = tokenizer(prompt, return_tensors="pt", padding=True, max_length=512)
    res = model.generate(**tokens, max_length=512)
    res_sentence = tokenizer.decode(res[0], skip_special_tokens=True)
    return res_sentence.split("Answer: ")[-1].strip()

# Read and Process CSV File

results = []

import pandas as pd

def get_sentiment_amzn(title):
    prompt = f"""Instruction: What is the sentiment of this news title for the stock of AMZN? Your task is to analyze news headlines and determine their sentiment with respect to the stock mentioned. Please choose an answer from {{negative, neutral, positive}}.
Input: {title}
Answer: """
    tokens = tokenizer(prompt, return_tensors="pt", padding=True, max_length=512, truncation=True)
    res = model.generate(**tokens, max_length=512)
    res_sentence = tokenizer.decode(res[0], skip_special_tokens=True)
    return res_sentence.split("Answer: ")[-1].strip()

# Process amzn_news.csv
amzn_data = pd.read_csv('amzn_news.csv')
amzn_data['Sentiment'] = amzn_data['Title'].apply(get_sentiment_amzn)

# Save the updated DataFrame
amzn_data.to_csv('amzn_sentiments.csv', index=False)
print("Sentiment analysis for AMZN completed. Saved to 'amzn_sentiments.csv'.")

def get_sentiment_amzn(title):
    prompt = f"""Instruction: What is the sentiment of this news title for the stock of AMZN? Your task is to analyze news headlines and determine their sentiment with respect to the stock mentioned. Please choose an answer from {{negative, neutral, positive}}.
Input: {title}
Answer: """
    tokens = tokenizer(prompt, return_tensors="pt", padding=True, max_length=512, truncation=True)
    res = model.generate(**tokens, max_length=512)
    res_sentence = tokenizer.decode(res[0], skip_special_tokens=True)
    return res_sentence.split("Answer: ")[-1].strip()

# Process amzn_news.csv
amzn_data = pd.read_csv('googl_news.csv')
amzn_data['Sentiment'] = amzn_data['Title'].apply(get_sentiment_amzn)

# Save the updated DataFrame
amzn_data.to_csv('googl_sentiments.csv', index=False)
print("Sentiment analysis for AMZN completed. Saved to 'amzn_sentiments.csv'.")

def get_sentiment_amzn(title):
    prompt = f"""Instruction: What is the sentiment of this news title for the stock of AMZN? Your task is to analyze news headlines and determine their sentiment with respect to the stock mentioned. Please choose an answer from {{negative, neutral, positive}}.
Input: {title}
Answer: """
    tokens = tokenizer(prompt, return_tensors="pt", padding=True, max_length=512, truncation=True)
    res = model.generate(**tokens, max_length=512)
    res_sentence = tokenizer.decode(res[0], skip_special_tokens=True)
    return res_sentence.split("Answer: ")[-1].strip()

# Process amzn_news.csv
amzn_data = pd.read_csv('nflx_news.csv')
amzn_data['Sentiment'] = amzn_data['Title'].apply(get_sentiment_amzn)

# Save the updated DataFrame
amzn_data.to_csv('nflx_sentiments.csv', index=False)
print("Sentiment analysis for AMZN completed. Saved to 'amzn_sentiments.csv'.")

def get_sentiment_amzn(title):
    prompt = f"""Instruction: What is the sentiment of this news title for the stock of AMZN? Your task is to analyze news headlines and determine their sentiment with respect to the stock mentioned. Please choose an answer from {{negative, neutral, positive}}.
Input: {title}
Answer: """
    tokens = tokenizer(prompt, return_tensors="pt", padding=True, max_length=512, truncation=True)
    res = model.generate(**tokens, max_length=512)
    res_sentence = tokenizer.decode(res[0], skip_special_tokens=True)
    return res_sentence.split("Answer: ")[-1].strip()

# Process amzn_news.csv
amzn_data1 = pd.read_csv('nvda_news.csv')
amzn_data1['Sentiment'] = amzn_data1['Title'].apply(get_sentiment_amzn)

# Save the updated DataFrame
amzn_data1.to_csv('nvda_sentiments.csv', index=False)
print("Sentiment analysis for AMZN completed. Saved to 'amzn_sentiments.csv'.")

def get_sentiment_amzn(title):
    prompt = f"""Instruction: What is the sentiment of this news title for the stock of AMZN? Your task is to analyze news headlines and determine their sentiment with respect to the stock mentioned. Please choose an answer from {{negative, neutral, positive}}.
Input: {title}
Answer: """
    tokens = tokenizer(prompt, return_tensors="pt", padding=True, max_length=512, truncation=True)
    res = model.generate(**tokens, max_length=512)
    res_sentence = tokenizer.decode(res[0], skip_special_tokens=True)
    return res_sentence.split("Answer: ")[-1].strip()

# Process amzn_news.csv
amzn_data = pd.read_csv('tsla_news.csv')
amzn_data['Sentiment'] = amzn_data['Title'].apply(get_sentiment_amzn)

# Save the updated DataFrame
amzn_data.to_csv('tsla_sentiments.csv', index=False)
print("Sentiment analysis for AMZN completed. Saved to 'amzn_sentiments.csv'.")
