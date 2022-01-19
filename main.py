from fastapi import FastAPI
from transformers import pipeline
import torch
from transformers import AutoModelForSequenceClassification
from transformers import BertTokenizerFast

#class Item(BaseModel):
    text: "Не важно.Всё нормально"

app = FastAPI()
#classifier = pipeline("sentiment-analysis")

@app.get("/")
def root():
    return {"message": "Hello UrFU"}

@app.post("/predict/")
#def predict(item: Item):
    #return classifier(item.text)[0]
    
tokenizer = BertTokenizerFast.from_pretrained('blanchefort/rubert-base-cased-sentiment-rusentiment')
model = AutoModelForSequenceClassification.from_pretrained('blanchefort/rubert-base-cased-sentiment-rusentiment', return_dict=True)

@torch.no_grad()
def predict(text):
    inputs = tokenizer(text, max_length=512, padding=True, truncation=True, return_tensors='pt')
    outputs = model(**inputs)
    predicted = torch.nn.functional.softmax(outputs.logits, dim=1)
    predicted = torch.argmax(predicted, dim=1).numpy()
    return     
   
