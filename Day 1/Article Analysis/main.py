from textblob import TextBlob
text = input("Paste the article's title here: ")
textblob1 = TextBlob(text)
sentiment = textblob1.sentiment.polarity
if sentiment<0:
  print ("Negative Article")
elif sentiment == 0:
  print("Neutral Article")
elif sentiment>1:
  print ("Positive Article")