import requests
import time

start = time.time()

model_inputs = {'prompt': "Je suis un jeune"}

res = requests.post('http://172.17.0.2:80/generate', data = model_inputs)

print(res.json())
print((time.time() - start)/60)