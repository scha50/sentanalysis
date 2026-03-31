# Sentiment Analyzer

A Python sentiment analysis tool using TextBlob that classifies text as Positive, Negative, or Neutral.

## Setup

1. Install dependencies:
```
pip install textblob
python -m textblob.download_corpora
```

2. Run the test suite:
```
python sentanalysis.py
```

## How it works

TextBlob gives each sentence a polarity score from -1.0 to 1.0.

- Above 0.05 → Positive
- Below -0.05 → Negative
- In between → Neutral

## Input Validation

- Empty strings return an error
- Non-string inputs return an error

## Example Output
```
I absolutely love this product, it's amazing | Result: Positive | Expected: Positive | Passed: True
The service was terrible and the waiter was awful | Result: Negative | Expected: Negative | Passed: True
The meeting is scheduled on Tuesday.        | Result: Neutral  | Expected: Neutral  | Passed: True

Edge Case Tests
empty string      | Error caught: True | Message: Input must not be empty.
non-string input  | Error caught: True | Message: Input must be a string.
```
