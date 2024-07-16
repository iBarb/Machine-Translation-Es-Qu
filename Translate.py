from transformers import MarianMTModel, MarianTokenizer
import torch

# Cargar el modelo y el tokenizer guardados
model_name = './es-qu-MarianMTModel-Best'
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

# Utilizar la GPU si está disponible
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Función para traducir una frase
def translate_sentence(sentence, model, tokenizer):
    inputs = tokenizer(sentence, return_tensors='pt', max_length=128, truncation=True, padding='max_length').to(device)
    with torch.no_grad():
        generated_ids = model.generate(**inputs)
    translated_sentence = tokenizer.decode(generated_ids[0], skip_special_tokens=True)
    return translated_sentence

# Ejemplo de uso
if __name__ == "__main__":
    sentence = "El perro está haciendo asustara mi hermanito"
    translated = translate_sentence(sentence, model, tokenizer)
    print(f"Original: {sentence}")
    print(f"Traducido: {translated}")
