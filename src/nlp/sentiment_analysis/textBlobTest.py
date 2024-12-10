from textblob import TextBlob

def getSentimiento():
    #tb = TextBlob("Aprender a programar es una tarea complicada al principio")
    tb = TextBlob("Textblob is amazingly simple to use. What great fun!")

    print(tb.sentiment)
    print(tb.sentiment.polarity)
