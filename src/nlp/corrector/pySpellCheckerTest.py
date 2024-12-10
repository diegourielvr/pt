from spellchecker import SpellChecker

def pySpellCheckerTest():

    text = "Hola a tods mi nombre es Diego Uriel Vázquez Ramírez ¿Como se llaman ustedes?"
    lang = 'es'
    #print(pySpellCheckerTest(textEs, langEs))
    text = "Hello evryone. My names Diego Uriel Vázquez Ramírez. What are you names?" # Hello everyone. My name is Diego Uriel Vázquez Ramírez. What are your names?
    lang = 'en'
    #print(pySpellCheckerTest(textEn, langEn))
    # https://pyspellchecker.readthedocs.io/en/latest/quickstart.html
    spell = SpellChecker(distance=2, language=lang)
    tokens = text.split()

    for i, token in enumerate(tokens):
        if spell.unknown([token]): # Encuentra una palabra desconocida
            new = spell.correction(token) # obtiene la correcion
            print(f"Desconocido: {token}, nueva: {new}")
            if new: # Si existe una correcion, la cambiamos. DE lo contrario se mantiene la palabra desconocida
                tokens[i] = new
        else:
            print(f"Conocido: {token}")
    return " ".join(tokens)
