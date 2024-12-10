from nltk import NLTKWordTokenizer, MWETokenizer, casual_tokenize
from nltk import TweetTokenizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def tweetTokenizerTest(texto):
    """
    Divide el texto en palabras y toma los signos de puntuacion como tokens individuales.
    Separa en tokens individuales símbolos como: :) :-(
    Reduce  signos de puntiacion que se repiten más de 3 veces de manera consecutiva (!!!!!!!! -> !!!)
    """
    return TweetTokenizer().tokenize(texto)

def nltkWordTokenizerTest(texto):
    # Tokeniza el texto y cada signo de puntiacion por separado. Permite sustituir parentesis por otros simbolos
    return NLTKWordTokenizer().tokenize(texto)

def wordTokenizerTest(texto):
    return word_tokenize(texto)

def mweTokenizerTest(tokens):
    # Toma un string que ya ha sido dividido y lo retokeniza uniendo expresiones multipalabra como un solo token.
    #Es necesario agregar la lista de expresiones multipalabra
    tk = MWETokenizer([('Donald', 'Trump'),("Diego", "Uriel")],separator=' ')
    tk.add_mwe(('United','States'))
    return tk.tokenize(tokens)

def showStopWordsList():
    print(stopwords.fileids())


if __name__ == '__main__':
    textEn = "President of United States of America is now Donald Trump and i have $100 dollars :) :-("
    textEs = "¡Hola! mi nombre es Diego Uriel me gusta la Inteligencia Artificial y el machine learning y tomo el metro para llegar a la escuela aunque cuesta $4.99 pesos mexicanos ¿que me dices de ti?"
    print("TweetTokenizer")
    print(tweetTokenizerTest(textEn))
    print(tweetTokenizerTest(textEs))
    print("NLTKWordTokenizer")
    print(nltkWordTokenizerTest(textEn))
    print(nltkWordTokenizerTest(textEs))
    print("WordTokenizer")
    print(wordTokenizerTest(textEn))
    print(wordTokenizerTest(textEs))
    print("Multi Word Expression")
    print(mweTokenizerTest(textEn.split()))
    print(mweTokenizerTest(textEs.split()))
