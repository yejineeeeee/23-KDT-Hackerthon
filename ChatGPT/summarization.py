# https://huggingface.co/models

import pandas as pd
import nltk
nltk.download('punkt')
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

df = pd.read_csv("C:/Users/user/Desktop/house2.csv", encoding='cp949')
# df.columns = ['exp', 'analysis']
# combined_string = '\n'.join(df['analysis'].astype(str))
combined_string = '\n'.join(df.astype(str))
ARTICLE = f'"""\n{combined_string}"""'

model = AutoModelForSeq2SeqLM.from_pretrained('eenzeenee/t5-base-korean-summarization')
tokenizer = AutoTokenizer.from_pretrained('eenzeenee/t5-base-korean-summarization')

prefix = "summarize: "
inputs = [prefix + ARTICLE]


inputs = tokenizer(inputs, max_length=2000, truncation=True, return_tensors="pt")
output = model.generate(**inputs, num_beams=3, do_sample=True, min_length=300, max_length=500)
decoded_output = tokenizer.batch_decode(output, skip_special_tokens=True)[0]
result = nltk.sent_tokenize(decoded_output.strip())[0]

print('RESULT >>', result)