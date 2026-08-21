# 🎬 MovieMatch — Movie Recommendation System

MovieMatch is an interactive movie recommendation application that uses Machine Learning to recommend movies based on genre similarity, ratings, popularity, and user-selected filters.

The application is built with Python and Streamlit, using a K-Nearest Neighbors (KNN) recommendation approach with a custom rating and popularity weighting scheme.

## 🚀 Key Features

- 🎭 Genre-based movie recommendations
- 🤖 KNN-based similarity model
- ⭐ Rating and popularity-based ranking
- 🔎 Filter recommendations by:
  - Genre
  - Minimum vote count
  - Release year
  - Number of recommendations
- 📊 Interactive EDA and Plotly visualizations
- ❤️ Personal movie watchlist
- 📥 Export recommendations to CSV
- 🎨 Custom Streamlit UI
- 📈 Movie rating, popularity, and genre analysis

## 🍿 What is MovieMatch?

**MovieMatch** is a Machine Learning-powered movie recommendation application designed to help users discover movies based on their preferred **genres, ratings, popularity, release year, and voting activity**.

Instead of simply sorting movies by rating, MovieMatch combines **K-Nearest Neighbors (KNN)** with a customized ranking strategy to find movies that are actually similar to the user's selected preferences.

> 🎯 **Select a genre → Tune your preferences → Get personalized movie recommendations.**

---

## 🎞️ The MovieMatch Experience

```text
        🎭 SELECT GENRE
              │
              ▼
      ⚙️ CUSTOMIZE FILTERS
              │
              ▼
      🤖 KNN RECOMMENDATION
              │
              ▼
       🔎 FILTER CANDIDATES
              │
              ▼
     ⭐ RANK BY RATING
              +
        🔥 POPULARITY
              │
              ▼
       🎬 MOVIEMATCH RESULTS
```

---

# ✨ Features

| Feature                      | Description                                     |
| ---------------------------- | ----------------------------------------------- |
| 🎭 **Genre Recommendations** | Discover movies based on selected genres        |
| 🤖 **KNN Recommendation**    | Uses `NearestNeighbors` to find similar movies  |
| ⭐ **Smart Ranking**          | Combines weighted ratings with popularity       |
| 🎚️ **Dynamic Filters**      | Control year, votes, result count and sorting   |
| 📊 **Interactive Analytics** | Explore ratings, popularity and genre patterns  |
| 🖼️ **Grid / List View**     | Switch between different recommendation layouts |
| ❤️ **Watchlist**             | Save movies you're interested in                |
| 📥 **CSV Export**            | Export your recommendations for later           |
| 🎨 **Custom UI**             | Cinema-inspired Streamlit interface             |
| 📈 **EDA Dashboard**         | Explore important patterns in the movie dataset |

---

# 🧠 Machine Learning Behind MovieMatch

MovieMatch transforms every movie into a numerical feature representation.

### Feature Engineering

Each movie is represented using:

```text
Genre Features
     +
Scaled Popularity
     +
Scaled Rating
     ↓
Movie Feature Vector
```

Genres are converted into numerical features using:

* `MultiLabelBinarizer`
* `MinMaxScaler`

The resulting feature matrix is used to train a:

```python
NearestNeighbors()
```

model from Scikit-learn.

---

# 🔥 Recommendation Pipeline

### 01 — Movie Data

The system starts with a dataset containing approximately **10,000 TMDB movies**.

### 02 — Feature Engineering

Movie genres are converted into one-hot encoded features while rating and popularity are scaled.

### 03 — Similarity Search

A `NearestNeighbors` model identifies movies closest to the user's selected genre/query vector.

### 04 — Candidate Filtering

Recommendations are filtered according to:

* 🎭 Genre
* 🗳️ Minimum vote count
* 📅 Release year
* 🔢 Number of results

### 05 — Smart Re-ranking

Candidates are ranked using:

**Weighted Rating + Popularity**

This prevents movies with a tiny number of votes from unfairly dominating the recommendation list.

### 06 — Interactive Results

The final recommendations are displayed through the Streamlit interface.

---

# 📊 Explore the Data

MovieMatch isn't just about recommendations — it also includes exploratory analysis of the dataset.

### 🔥 Correlation Analysis

<img src="Project%20Assets/eda_correlation_heatmap.png" width="750"/>

### 📈 Feature Distributions

<img src="Project%20Assets/eda_distributions.png" width="750"/>

### 🎭 Genre Distribution

<img src="Project%20Assets/eda_genre_counts.png" width="750"/>

### 🧬 PCA Projection

<img src="Project%20Assets/eda_pca_projection.png" width="750"/>

### 🏆 Top Movies by Weighted Rating

<img src="Project%20Assets/eda_top10_weighted.png" width="750"/>

---

# 🎛️ Recommendation Controls

MovieMatch gives users control over the recommendation process.

```text
🎭 Genre
   └── Choose your preferred genre

🔢 Number of Results
   └── Decide how many movies to display

🗳️ Minimum Vote Count
   └── Remove movies with insufficient voting data

📅 Release Year
   └── Set your preferred year range

🏆 Sort By
   ├── Best Match
   ├── Highest Rated
   ├── Most Popular
   ├── Newest
   └── Oldest
```

---

# 📁 Project Architecture

```text
MovieMatch/
│
├── 📂 Project Assets/
│   ├── 🖼️ eda_correlation_heatmap.png
│   ├── 🖼️ eda_distributions.png
│   ├── 🖼️ eda_genre_counts.png
│   ├── 🖼️ eda_pca_projection.png
│   └── 🖼️ eda_top10_weighted.png
│
├── 🐍 app.py.py
├── 🤖 movies1.pkl
├── 📊 top10K-TMDB-movies.csv
├── 📖 README.md
├── 📑 MovieMatch_Presentation.pptx
└── 📄 Report.docx
```

### 📦 Core Components

**`app.py.py`**

The main Streamlit application containing:

* Recommendation engine
* UI
* Filters
* Watchlist
* Visualizations
* CSV export

**`movies1.pkl`**

Serialized Machine Learning bundle containing the trained recommendation model and processed data.

**`top10K-TMDB-movies.csv`**

Movie dataset used for analysis and recommendations.

**`Project Assets/`**

Contains EDA visualizations generated during the data analysis phase.

---

# 🛠️ Tech Stack

### Programming

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)

### Machine Learning

![Scikit Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge\&logo=scikit-learn\&logoColor=white)

* K-Nearest Neighbors
* NearestNeighbors
* MinMaxScaler
* MultiLabelBinarizer

### Data Science

![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge\&logo=pandas\&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge\&logo=numpy\&logoColor=white)

### Visualization & UI

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge\&logo=streamlit\&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge\&logo=plotly\&logoColor=white)

---

# 🚀 Installation

## 1️⃣ Clone the Repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd MovieMatch
```

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 3️⃣ Run MovieMatch

```bash
streamlit run app.py.py
```

> ⚠️ Make sure `movies1.pkl` is present in the project directory before launching the application.

---

# 🎮 How to Use

### Step 1

Launch the Streamlit application.

### Step 2

Select your preferred **movie genre**.

### Step 3

Customize:

* Number of recommendations
* Minimum vote count
* Release year range
* Sorting preference

### Step 4

Click:

> 🎬 **Get Recommendations**

### Step 5

Explore your recommendations.

### Step 6

Add interesting movies to your:

> ❤️ **Personal Watchlist**

### Step 7

Export your recommendations as a CSV file.

---

# 📊 Dataset

MovieMatch uses a TMDB-based movie dataset containing approximately **10,000 movies**.

### Key Attributes

```text
title
genre / genre_list
overview
release_year
vote_average
vote_count
popularity
weighted_rating
```

These attributes are used for:

* Exploratory Data Analysis
* Feature engineering
* Similarity calculation
* Recommendation ranking

---

# 🧮 Why Weighted Ratings?

A movie with:

> ⭐ 9.5 rating from 20 votes

shouldn't automatically outrank:

> ⭐ 8.7 rating from 100,000 votes.

MovieMatch therefore uses a **Bayesian-style weighted rating** to create a more reliable ranking.

This makes the recommendation system less vulnerable to movies with extremely high ratings but very little voting data.

---

# 🔬 Project Highlights

```text
📊 ~10,000 Movies
🎭 18+ Genres
🤖 KNN Recommendation
⭐ Weighted Rating
🔥 Popularity Ranking
📈 Interactive Analytics
❤️ Watchlist
📥 CSV Export
🎨 Custom Streamlit UI
```

---

# 🗺️ Future Roadmap

MovieMatch can be taken much further.

### 🎞️ Movie Posters

Integrate the **TMDB API** to dynamically retrieve:

* Movie posters
* Backdrops
* Cast
* Directors
* Release information

### 🧠 Semantic Recommendations

Use:

```text
TF-IDF
   ↓
Text Embeddings
   ↓
Semantic Similarity
   ↓
Better Recommendations
```

This would allow users to discover movies based on their **story and plot**, not only their genre.

### 👥 Collaborative Filtering

Use user interaction history to answer:

> "Users who liked this movie also liked..."

### 🔀 Hybrid Recommendation Engine

Combine:

```text
Genre Similarity
       +
Plot Similarity
       +
User Preferences
       +
Collaborative Filtering
       +
Ratings
       +
Popularity
```

to build a more advanced recommendation engine.

### ☁️ Deployment

Potential deployment platforms:

* Streamlit Cloud
* Render
* Hugging Face Spaces

---

# 🌟 Project Vision

MovieMatch started as a genre-based recommendation system, but the long-term goal is to evolve it into a **hybrid movie intelligence platform**.

> **From "What genre do you like?" → to "What kind of movie are you in the mood for?"**

Future versions could understand natural-language requests such as:

```text
"Recommend me a dark psychological thriller
with a strong storyline and high ratings."
```

and automatically generate personalized recommendations.

---

# 📚 Project Documentation

Additional project material is available in the repository:

| Resource                          | Purpose                 |
| --------------------------------- | ----------------------- |
| 📑 `MovieMatch_Presentation.pptx` | Project presentation    |
| 📄 `Report.docx`                  | Detailed project report |
| 📊 `top10K-TMDB-movies.csv`       | Movie dataset           |
| 🤖 `movies1.pkl`                  | Trained ML model bundle |
| 📈 `Project Assets/`              | EDA visualizations      |

---

# 👨‍💻 Author

### Priyanka Pal

**Machine Learning • Data Science • Python • Streamlit**


### 🎬 MovieMatch

**Discover. Recommend. Watch. Repeat. 🍿**

⭐ If you found this project interesting, consider giving the repository a star!

