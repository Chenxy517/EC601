import google.cloud

client = google.cloud.language.LanguageServiceClient()

text = input('')
document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)

sentiment = client.analyze_sentiment(request={"document": document}).document_sentiment

print("Text: {}".format(text))
print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))