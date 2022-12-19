import transformers
import torch
import convert


device = "cuda:0" if torch.cuda.is_available() else "cpu"

if device == "cuda:0":
    transformers.models.gptj.modeling_gptj.GPTJBlock = convert.GPTJBlock

def init():
    global model
    global tokenizer
    
    
    if device == 'cpu':
        print("Tokenizer loading on cpu...")
        tokenizer = transformers.AutoTokenizer.from_pretrained("Cedille/fr-boris")
        print("done")
        print("Model loading on cpu...")
        model = transformers.AutoModelForCausalLM.from_pretrained("Cedille/fr-boris")
        print("done")
    else:
        print("Tokenizer loading on cpu...")
        tokenizer = transformers.AutoTokenizer.from_pretrained("yvan237/cedille-GPT-J-6B-8bit")
        print("done")
        print("Model loading on cpu...")
        model = convert.GPTJForCausalLM.from_pretrained("yvan237/cedille-GPT-J-6B-8bit")
        print("done")
    
    if device == "cuda:0":
        print("Model passing on gpu...")
        model.to(device)
    else:
        print("You do not have gpu set in your environment")
        
    tokenizer.pad_token = tokenizer.eos_token
    model.config.pad_token_id = cedille.config.eos_token_id
        

def inference(prompt, max_new_tokens):
    global model
    global tokenizer

    # Parse out your arguments
    if prompt == None:
        return {'message': "No prompt provided"}
    
    prompt = "Je suis un jeune étudiant en"
    # Tokenize input
    input_tokens = tokenizer(prompt, return_tensors='pt')
    input_tokens = {key: value.to(device) for key, value in input_tokens.items()}
    max_length = len(prompt.split(" ")) + max_new_tokens

    # Run the model
    output = model.generate(**input_tokens, min_length=max_length, max_length=max_length, do_sample=True)

    # Decode output token
    output_text = tokenizer.decode(output[0], skip_special_tokens=True)

    result = {"output": output_text}

    # Return the results as a dictionary
    return result

 
# prompt = {key: value.to(device) for key, value in prompt.items()}

# out = gpt.generate(**prompt, min_length=128, max_length=128, do_sample=True)

# tokenizer.decode(out[0], skip_special_tokens=True)
