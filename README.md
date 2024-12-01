# SnappSense

**SnappSense** is a web application designed to help app developers and product managers capture and analyze user feedback from mobile apps on the Google Play Store. It provides sentiment analysis, feedback categorization, and valuable insights into user reviews, enabling better decision-making for app improvement.

### 🚀 **Features**
- **Sentiment Analysis**: Categorizes user reviews into five sentiment categories: Delighted, Happy, Neutral, Angry, and Frustrated.
- **Sentiment Trends**: Track sentiment trends over different time periods: 1 week, 1 month, 3 months, 6 months, and 1 year.
- **All-Time Sentiment Distribution**: Visualize the overall sentiment distribution of all reviews.
- **Categorized Feedback**: Group feedback into categories like feature requests and bug reports with potential solutions.
- **Review Translation**: Translate reviews in different languages to the user’s preferred language using **LibreTranslate**.
- **CSV Export**: Export categorized feedback and sentiment data to CSV for further analysis.
- **Interactive Visuals**: Hover over charts for detailed insights, including percentage breakdowns of sentiments.

### 💻 **Tech Stack**
- **Frontend**:
  - **React.js**: For building dynamic and responsive user interfaces.
  - **CSS3**: For fast styling with utility-first CSS classes.
  - **Chart.js**: For visualizing sentiment trends and feedback data.
  - **Lottie.js**: For displaying lightweight animations (e.g., loading indicators).

- **Backend**:
  - **Flask**: Python web framework for handling backend logic.
  - **google-play-scraper**: To scrape user reviews from the Google Play Store.
  - **langdetect**: For detecting review languages.
  - **LibreTranslate**: For translating reviews into the user's preferred language.
  - **Redis**: For caching to speed up responses for apps with many reviews.


### 🌍 **Platform Capabilities**
- **Sentiment Analysis**: Categorizes reviews into different sentiments and tracks how sentiment evolves over time.
- **Review Breakdown**: Categorizes reviews into useful feedback (e.g., bug reports, feature requests) with actionable suggestions.
- **Language Support**: Reviews are translated for users who speak different languages, improving accessibility.
- **Interactive Charts**: Users can interact with charts to see detailed sentiment distributions and trends.

### 🧰 **Issues**
If you encounter any issues or bugs, please feel free to open an issue in the repository, and it will be addressed.

---

**SnappSense** is your go-to tool for understanding and analyzing user sentiment for mobile apps. Capture user feedback, make data-driven decisions, and improve your app’s experience. 🚀
