from google_play_scraper import app, reviews

def get_reviews(app_url):
    # Extract the app ID from the URL (Assume URL is something like https://play.google.com/store/apps/details?id=com.example.app)
    app_id = app_url.split('id=')[-1]

    # Get the reviews using the google-play-scraper
    result = reviews(app_id, lang='en', country='us')  # Get reviews for the app
    
    reviews_list = []
    for review in result:
        reviews_list.append(review['content'])  # Collecting the content of each review

    return reviews_list
