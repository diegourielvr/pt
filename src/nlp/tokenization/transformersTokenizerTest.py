from transformers import AutoTokenizer
from transformers import BasicTokenizer

def tfTokenizerTest(texto):
    # Seleccionar el modelo (en este caso uno entrenado para español)
    tokenizer = AutoTokenizer.from_pretrained("dccuchile/bert-base-spanish-wwm-cased")

    # Tokenización
    tokens = tokenizer.tokenize(texto)
    tokens_ids = tokenizer.encode(texto, add_special_tokens=True)

    # Mostrar tokens y sus IDs
    #print("Tokens:", tokens)
    #print("IDs de tokens:", tokens_ids)
    return tokens

def tfSimpleTokenizer(texto):
    # Crear el tokenizador básico
    basic_tokenizer = BasicTokenizer(do_lower_case=False)

    # Tokenización por palabras completas
    tokens = basic_tokenizer.tokenize(texto)

    return tokens


if __name__ == '__main__':
    textEn = "President of United States of America is now Donald Trump! and i have $100 dollars"
    textEs = "¡Hola! mi nombre es Diego Uriel me gusta la Inteligencia Artificial y el machine learning y tomo el metro para llegar a la escuela aunque cuesta $4.99 pesos mexicanos ¿que me dices de ti?"
    print("SWT")
    print(tfSimpleTokenizer(textEn))
    print(tfSimpleTokenizer(textEs))


