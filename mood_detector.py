from textblob import TextBlob

# Load quotes
with open("quotes.txt", "r", encoding="utf-8") as f:
    quotes = f.readlines()

print("Mood Detector for Literary Quotes 💭")
print("-------------------------------------")

for line in quotes:
    line = line.strip()
    if line:
        analysis = TextBlob(line)
        polarity = analysis.sentiment.polarity
        if polarity > 0:
            mood = "Positive 🙂"
        elif polarity < 0:
            mood = "Negative 🙁"
        else:
            mood = "Neutral 😐"
        print(f"\nQuote: \"{line}\"\nMood: {mood}")
