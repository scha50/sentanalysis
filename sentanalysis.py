from textblob import TextBlob

def analyze_sentiment(text):
    if not isinstance(text, str):
        return {"label": None, "polarity": None, "error": "Input must be a string."}
    if text.strip() == "":
        return {"label": None, "polarity": None, "error": "Input must not be empty."}
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.05:
        label = "Positive"
    elif polarity < -0.05:
        label = "Negative"
    else:
        label = "Neutral"
    return {"label": label, "polarity": round(polarity, 4), "error": None}


TEST_CASES = [
    ("I absolutely love this product, it's amazing!", "Positive"),
    ("I am feeling great and grateful.", "Positive"),
    ("The team did an outstanding job on this.", "Positive"),
    ("This is the best food I have ever had.", "Positive"),
    ("I hate waiting in long lines because it makes me frustrated.", "Negative"),
    ("The service was terrible and the waiter was awful.", "Negative"),
    ("This is the worst food I have ever had.", "Negative"),
    ("I'm really disappointed with how I did on the test.", "Negative"),
    ("The meeting is scheduled on Tuesday.", "Neutral"),
    ("I ate a sandwich for lunch.", "Neutral"),
    ("She walked to the store and bought some bread.", "Neutral"),
    ("The essay is about food and science.", "Neutral"),
]

EDGE_CASES = [
    ("", "empty string"),
    (12345, "non-string input"),
]
print("Sentiment Tests")
for text, expected in TEST_CASES:
    result = analyze_sentiment(text)
    short = text[:40] + "..." if len(text) > 40 else text
    passed = result["label"] == expected
    print(short + " | Result: " + result["label"] + " | Expected: " + expected + " | Passed: " + str(passed))

print("\nEdge Case Tests")
for text, description in EDGE_CASES:
    result = analyze_sentiment(text)
    caught = result["error"] is not None
    print(description + " | Error caught: " + str(caught) + " | Message: " + str(result["error"]))

