"""
Yeh file routes define karti hai, specifically reviews ke liye.
"""

from flask import Blueprint, jsonify, request
from review_scraper.scraper import get_reviews


reviews_route = Blueprint("reviews_route", __name__)  # Blueprint create karte hain

@reviews_route.route("/reviews", methods=["GET"])
def fetch_reviews():
    """
    App reviews ko scrape karne aur return karne ke liye route.
    Query parameters: app_id, lang, count
    """
    # Query parameters ko fetch karte hain
    app_id = request.args.get("app_id", default=None, type=str)
    lang = request.args.get("lang", default="en", type=str)
    count = request.args.get("count", default=100, type=int)

    if not app_id:
        return jsonify({"error": "App ID is required"}), 400

    try:
        # Reviews ko scrape karte hain
        reviews_data = get_reviews(app_id, lang, count)
        return jsonify({"reviews": reviews_data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
