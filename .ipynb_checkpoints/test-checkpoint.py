import requests
import time

start = time.time()

model_inputs = {'prompt': "Je suis un jeune", 
               'max_new_tokens': 50}

res = requests.post('http://127.0.0.1:5000/generate', data = model_inputs)

print(res.json())
print((time.time() - start)/60)