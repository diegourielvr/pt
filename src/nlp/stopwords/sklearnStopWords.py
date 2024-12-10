from sklearn.feature_extraction.text import CountVectorizer
#sklearn solo tiene una lista de stopwords en inglés
# Para eliminar stopwords en español se necesita de un lista

def sk_es_stopword(token, lang):
    vectorizer = None
    if lang == "es":
        vectorizer = CountVectorizer(analyzer="word")
    if lang == "en":
        vectorizer = CountVectorizer(analyzer="word", stop_words='english')
    analyzer = vectorizer.build_analyzer()
    return analyzer(token) == []

def sk_texto_sin_stopword(texto, lang):
    # Devuelve una lista con las palabras que no son stopwords
    vectorizer = None
    if lang == "es":
        vectorizer = CountVectorizer(analyzer="word", stop_words='spanish')
    if lang == "en":
        vectorizer = CountVectorizer(analyzer="word", stop_words='english')
    analyzer = vectorizer.build_analyzer()
    return analyzer(texto)

def sk_tokenizer(texto):
    """
    No divide posesivos del inglés

    """
    vectorizer = CountVectorizer(analyzer='word')
    # convierte en minu y devuelve un str
    preprocessor = vectorizer.build_preprocessor()
    # convierte en minus, elimina signos de puntuacion y devuelve una lista de str
    tokenizer = vectorizer.build_tokenizer()
    return tokenizer(preprocessor(texto))



if __name__ == '__main__':
    #res = sk_remover_stop_words("Hi my name is diego uriel", "es")
    #print(res)
    print(sk_tokenizer("HELLO MY name`s Diego Uriel and you?"))
    print(sk_texto_sin_stopword("artificial intelligence", "en"))
    print(sk_texto_sin_stopword("you", "en"))
    print(sk_es_stopword("you", "en"))
