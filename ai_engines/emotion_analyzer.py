from textblob import TextBlob

class EmotionAnalyzer:
    def analyze(self, text):
        analysis = TextBlob(text)
        polarity = analysis.sentiment.polarity
        if polarity > 0.5:
            return "alegría"
        elif polarity > 0.1:
            return "esperanza"
        elif polarity < -0.5:
            return "ira"
        elif polarity < -0.1:
            return "tristeza"
        else:
            return "neutral"
