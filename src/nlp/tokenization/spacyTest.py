import spacy

def SWT(texto, lang="es"):
    if lang == "en":
        nlp = spacy.load("en_core_web_sm")
    else:
        nlp = spacy.load("es_core_news_sm")

    doc = nlp(texto)
    return [f'{token.text}' for token in doc]

def MWT(texto, lang="es"):
    if lang == "en":
        nlp = spacy.load("en_core_web_sm")
    else:
        nlp = spacy.load("es_core_news_sm")
    doc = nlp(texto)
    with doc.retokenize() as retokenizer:
        for ent in doc.ents:
            retokenizer.merge(ent)
    return [f'{token.text}' for token in doc]

def preprocess(texto, lang):
    if lang == "en":
        nlp = spacy.load("en_core_web_sm")
    else:
        nlp = spacy.load("es_core_news_sm")
    doc = nlp(texto)
    for token in doc:


if __name__ == '__main__':
    textEn= "President of united states of america is now Donald Trump! and i have $100 dollars"
    textEs = "¡Hola! mi nombre es Diego Uriel me gusta la Inteligencia Artificial y el machine learning y tomo el metro para llegar a la escuela aunque cuesta $4.99 pesos mexicanos ¿que me dices de ti?"
    print("SWT:")
    res = SWT(textEn, "en")
    #print(SWT(textEs, "es"))
    print("MWT:")
    print(MWT(textEn, "en"))
    #print(MWT(textEs, "es"))
    print(MWT(res))
