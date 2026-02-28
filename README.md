# Netflix Movie Recommendation System
## Project Overview
* Content-Based Movie Recommendation System built using the TMDB Movie Dataset
* Dataset contains 21,000+ movies
* Recommends movies based on similarity between:
  * Overview
  * Genres
  * Keywords
* Uses Natural Language Processing (NLP) techniques
* Implements Cosine Similarity for recommendation ranking
* Demonstrates practical implementation of text-based feature engineering and recommendation systems

## Dataset Information
  * ### Dataset Used: TMDB Movie Dataset
  * ### Total Movies: 21,000+

## Key Features Used

* Movie ID
* Title
* Overview
* Keywords
* Genres
* Poster Path
* Removed unnecessary columns
* Handled missing values during preprocessing

## Technologies Used
* Python
* Pandas
* NumPy
* Scikit-learn
* NLTK
* Streamlit
* Pickle

## Project Workflow
### 1. Data Preprocessing
* Removed irrelevant columns
* Handled missing values
* Combined overview + genres + keywords into a single feature
* Applied text cleaning and stemming

### 2. Feature Engineering
* Converted text data into numerical format using Bag-of-Words
* Limited vocabulary to Top 10,000 most frequent words

### 3. Similarity Computation
* Calculated Cosine Similarity between all movie vectors
* Generated a 21,000 × 21,000 similarity matrix
* Stored similarity matrix using Pickle for faster loading

### 4. Recommendation Generation
* User selects a movie
* System retrieves similarity scores
* Movies are sorted based on similarity
* Top 5 most similar movies are recommended

## Application
* Deployed using Streamlit
* Users select a movie from a dropdown
* System displays:
  * Top 5 similar movies
  * Movie posters

## Model Characteristics
* Type: Content-Based Filtering
* Vectorization Method: Bag-of-Words
* Maximum Features: 10,000
* Similarity Metric: Cosine Similarity
* Dataset Size: 21K+ movies

## Project Structure
* Recommendation System.ipynb
* tmdbdf.csv
* movies similarity.pkl
* app.py
* requirements.txt
* README.md

## Key Learnings

* Implementation of NLP in recommendation systems
* Advanced text preprocessing and feature engineering
* Understanding of vector space modeling
* Practical use of Cosine Similarity
* Model serialization using Pickle
* Deployment of ML apps using Streamlit

## Future Enhancements
* Implement Collaborative Filtering
* Develop a Hybrid Recommendation System
* Optimize memory usage for large similarity matrices
* Deploy on cloud platforms
* Enhance UI with advanced filtering options

## Conclusion
* Built a scalable Content-Based Recommendation System
* Applied NLP, feature engineering, and similarity metrics
* Demonstrated real-world Machine Learning application deployment
* Showcased strong understanding of recommendation system architecture
