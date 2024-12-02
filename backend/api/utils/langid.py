# langid.py
"""
Yeh file language detect karne ke liye hai
"""

import langid

def detect_language(text):
    """
    Yeh function text ka language detect karega.
    Returns:
        - Language code (jaise 'en', 'hi', 'es', etc.)
        - Probability of the language
    """
    lang, prob = langid.classify(text)
    return lang, prob
