import transformers
import convert


device = "cuda:0" if torch.cuda.is_available() else "cpu"

if device == "cuda:0":
    transformers.models.gptj.modeling_gptj.GPTJBlock = convert.GPTJBlock

def download_model():
    
    # do a dry run of loading the huggingface model, which will download weights
    if device == 'cpu':
        print("Tokenizer loading...")
        transformers.AutoTokenizer.from_pretrained("Cedille/fr-boris")
        print("done")
        print("Model loading...")
        convert.AutoModelForCausalLM.from_pretrained("Cedille/fr-boris")
        print("done")
    else:
        print("Tokenizer loading...")
        transformers.AutoTokenizer.from_pretrained("yvan237/cedille-GPT-J-6B-8bit")
        print("done")
        print("Model loading...")
        convert.GPTJForCausalLM.from_pretrained("yvan237/cedille-GPT-J-6B-8bit")
        print("done")

if __name__ == "__main__":
    download_model()
