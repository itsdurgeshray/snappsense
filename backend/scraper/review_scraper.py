"""
Yeh file app reviews ko scrape karne aur unhe process karne ke liye hai.
"""

from google_play_scraper import Sort, reviews
from translator import translate_text  # Translator function import kar rahe hain

def get_reviews(app_id, lang="en", count=100):
    """
    Yeh function Google Play Store se reviews scrape karta hai.
    Agar review non-English hoga, toh usse translate bhi karega.
    Args:
        - app_id: App ka unique ID (package name)
        - lang: Language (default English)
        - count: Total number of reviews (default 100)
    Returns:
        - Reviews ka ek list with 'content' and 'translated' fields
    """
    # Reviews scrape karte hain
    raw_reviews, _ = reviews(
        app_id,
        lang=lang,  # Primary language
        sort=Sort.MOST_RELEVANT,  # Relevant reviews sabse pehle
        count=count  # Max number of reviews
    )

    processed_reviews = []  # Final processed reviews store karenge

    for review in raw_reviews:
        # Content extract karte hain
        content = review.get("content", "")
        
        # Agar review English mein nahi hai, toh translate karte hain
        if lang != "en":
            translated_content = translate_text(content)
        else:
            translated_content = content  # Agar English hai, no translation needed

        # Review ka data store karte hain
        processed_reviews.append({
            "original": content,
            "translated": translated_content,
            "rating": review.get("score", None),  # Rating extract karte hain
            "date": str(review.get("at", "")),  # Date format karte hain
        })

    return processed_reviews
