# 🧠 Topic Modelling using K-Means Clustering

This project uses **K-Means Clustering**, an unsupervised machine learning algorithm, to perform **topic modelling** on a large dataset of customer reviews. The goal is to group similar reviews together and identify underlying topics being discussed.

---

## 📌 Project Objective

- Perform **text mining** on customer reviews
- Apply **K-Means clustering** to group similar reviews
- Use **topic modelling** techniques to uncover hidden themes
- Demonstrate how businesses (e.g., e-commerce platforms) can extract insights from customer feedback

---

## 📂 Project Structure

| File | Description |
|------|-------------|
| `realistic_customer_reviews_with_metadata.csv` | Dataset with 10,000 realistic customer reviews including Name, Date, Rating, and Review |
| `topic_modelling_kmeans.py` | Python code to clean, vectorize, and cluster the reviews using K-Means |
| `Topic_Modelling_Presentation.pptx` | PowerPoint presentation explaining the project methodology, dataset, code, and results |
| `README.md` | This file, explaining the full project overview |

---

## 🧾 Dataset Overview

- **Rows**: 10,000
- **Columns**:
  - `Name` – Fake customer name
  - `Date` – Date of review (last 2 years)
  - `Rating` – Customer rating (1 to 5)
  - `Review` – Text used for topic modelling

👉 Only the `Review` column is used in clustering, while other fields provide context.

---

## 🛠️ Tools & Technologies

- **Language**: Python
- **Libraries**: 
  - pandas
  - scikit-learn
  - NLTK
- **Algorithm**: K-Means Clustering
- **Techniques**: Text preprocessing, TF-IDF vectorization, unsupervised learning

---

## 📊 Steps Performed

1. **Text Cleaning**: Removed punctuation, stopwords, lowercased text
2. **Vectorization**: Applied TF-IDF to convert text into numerical format
3. **Clustering**: Used K-Means to group reviews into topic clusters
4. **Visualization**: Analyzed and displayed topic groups

---

## 📈 Real-World Applications

- Grouping customer feedback for **e-commerce** or **support teams**
- Organizing **large volumes of textual data** (emails, reviews, comments)
- Identifying **common issues or praise areas** in product feedback

---

## ✅ Outcome

The final output shows clearly grouped reviews, allowing businesses to quickly understand what topics customers frequently talk about — such as delivery issues, product quality, price satisfaction, and more.

---

## 👨‍💻 Author

Project by [Your Name]  
[Optional: University Name / Course]  
[Date of Submission]

