#!/usr/bin/env python3

from transformers import AutoTokenizer, AutoModelForSequenceClassification
from torch.nn import Softmax
from torch import squeeze
from tabulate import tabulate
import sys


tokenizer = AutoTokenizer.from_pretrained("roberta-base-openai-detector")

model = AutoModelForSequenceClassification.from_pretrained("roberta-base-openai-detector")

model.eval()


texts = []
with open('gpt-detect-inputs.txt', 'r') as f:
	texts = f.readlines()


results = []

s = 1
sectionno = 1
for text in texts:

	text = text.replace("\n", " ")
	text = text.strip()

	inputs = tokenizer(text, return_tensors="pt")

	classifierOutput = model(**inputs)
	# print(classifierOutput)

	logits = classifierOutput.logits
	# print(f"Logits: {logits}")

	sm = Softmax(dim=1)
	predictions = sm(logits)
	predictions = squeeze(predictions)
	# print(predictions)

	# uneven lines == human
	# even lines == AI
	if (s % 2) != 0:
		results.append([f"Section{sectionno}_Human",predictions[0],predictions[1]])
	else:
		results.append([f"Section{sectionno}_AI",predictions[0],predictions[1]])
		results.append(["---","---","---"])
		sectionno = sectionno + 1
	s = s + 1


print(tabulate(results, headers=["Text", "p_Human", "p_AI"]))
