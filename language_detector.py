
# language_detector.py
# AI-Based Language Detection using langdetect library

from langdetect import detect, DetectorFactory

# Fix randomness for consistent results
DetectorFactory.seed = 0

def detect_language(text):
    try:
        lang = detect(text)
        return lang
    except:
        return "Could not detect language."

# Language Code Reference (optional for user understanding)
language_names = {
    "en": "English",
    "fr": "French",
    "es": "Spanish",
    "de": "German",
    "ur": "Urdu",
    "hi": "Hindi",
    "ar": "Arabic",
    "zh-cn": "Chinese",
    "ru": "Russian"
}

# --- Main Program ---
print("=== AI Language Detector ===")
user_input = input("Enter a sentence: ")
code = detect_language(user_input)
language = language_names.get(code, "Unknown Language")

print(f"\nDetected Language Code: {code}")
print(f"Detected Language: {language}")
