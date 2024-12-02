"""
Yeh file non-English reviews ko English mein translate karne ke liye hai.
"""

from transformers import MarianMTModel, MarianTokenizer

# Yeh function MarianMT model load karne ke liye
def load_model():
    """
    MarianMT ka model aur tokenizer load karta hai.
    """
    model_name = "Helsinki-NLP/opus-mt-mul-en"  # Multilingual se English ka translation
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    return tokenizer, model

# Tokenizer aur model globally load karte hain for better efficiency
tokenizer, model = load_model()

def translate_text(text):
    """
    Yeh function text ko English mein translate karega.
    Args:
        - text: Input text jo translate karna hai.
    Returns:
        - Translated text
    """
    # Text ko tokenize karte hain
    inputs = tokenizer.encode(text, return_tensors="pt", truncation=True)
    
    # Model se translation predict karte hain
    translated = model.generate(inputs, max_length=512)
    
    # Decode karke readable text return karte hain
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
    return translated_text
