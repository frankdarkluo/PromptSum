import scoring
from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("t5-base")
model = T5ForConditionalGeneration.from_pretrained("t5-base")

prefix="summarize: "
text="Amanda : I baked cookies . Do you want some ? | Jerry : Sure ! | Amanda : I'll bring you tomorrow"
input=prefix+text
input_ids = tokenizer(input, return_tensors="pt").input_ids
outputs = model.generate(input_ids)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
