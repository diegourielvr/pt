from sklearn.feature_extraction.text import CountVectorizer

def skTokenizerTest(texto):
    # Elimina algunas palabras como 'i'
    vectorizer = CountVectorizer(analyzer='word')
    analyze = vectorizer.build_analyzer() # Función que vectoriza
    return analyze(texto)

def skTokenizerStopWordsEn(texto):
    vectorizer = CountVectorizer(analyzer='word', stop_words='english')
    analyze = vectorizer.build_analyzer()
    #print(vectorizer.get_stop_words())
    return analyze(texto)


if __name__ == '__main__':
    textEn= "the President of United States of America is now Donald Trump and i have $100 dollars"
    textEs = "¡Hola! mi nombre es Diego Uriel me gusta la Inteligencia Artificial y el machine learning y tomo el metro para llegar a la escuela aunque cuesta $4.99 pesos mexicanos ¿que me dices de ti?"
    print("SWT")
    print(skTokenizerTest(textEn))
    print(skTokenizerTest(textEs))
    print("SWT and StopWords")
    print(skTokenizerStopWordsEn(textEn))