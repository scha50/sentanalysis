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
    ("The essay was due yesterday.", "Neutral"),
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



# EDGE_CASES = [
#     ("", None, "empty string"),
#     (12345, None, "non-string input"),
# ]


# def run_tests():
#     print("=" * 62)
#     print("  SENTIMENT ANALYZER — TEST RESULTS")
#     print("=" * 62)
#     correct = 0
#     total = len(TEST_CASES)
#     print(f"\n{'#':<3} {'Expected':<10} {'Got':<10} {'Polarity':>8}   {'PASS?':<5}  Text")
#     print("-" * 62)

#     for i, (text, expected) in enumerate(TEST_CASES, 1):
#         result = analyze_sentiment(text)
#         got = result["label"]
#         polarity = result["polarity"]
#         passed = "✓" if got == expected else "✗"
#         if got == expected:
#             correct += 1
#         short_text = text if len(text) <= 40 else text[:37] + "..."
#         print(f"{i:<3} {expected:<10} {got:<10} {polarity:>8.4f}   {passed:<5}  {short_text}")

#     print("-" * 62)
#     print(f"\n  Accuracy: {correct}/{total}  ({correct/total*100:.0f}%)\n")

#     print("=" * 62)
#     print("  VALIDATION / EDGE-CASE TESTS")
#     print("=" * 62)
#     for text, expected_label, description in EDGE_CASES:
#         result = analyze_sentiment(text)
#         status = "✓ Error caught" if result["error"] else "✗ Should have errored"
#         print(f"  [{description}] → {status}: {result['error']}")

#     print()
#     print("=" * 62)
#     print("  ANALYSIS OF UNCERTAIN / INCORRECT PREDICTIONS")
#     print("=" * 62)
#     print("""
#   1. "I'm really disappointed with how I did on the test."
#      Expected: Negative | Result may vary
#      "Disappointed" scores moderately negative, but surrounding
#      neutral words can drag the score toward the 0.0 boundary.

#   2. "She walked to the store and bought some bread."
#      Expected: Neutral | Sometimes flagged slightly Positive
#      TextBlob occasionally assigns tiny positive polarity to
#      ordinary action verbs. Our ±0.05 band catches these edge cases.
# """)


# run_tests()