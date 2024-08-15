Here's a draft for your `README.md` file:

---

# Book Recommendation System Using K-Nearest Neighbors

## Overview

This project involves developing a book recommendation system using the K-Nearest Neighbors (KNN) algorithm. The system is built using the [Book-Crossings](http://www2.informatik.uni-freiburg.de/~cziegler/BX/) dataset, which contains 1.1 million ratings (scale of 1-10) for 270,000 books by 90,000 users. The goal is to create a function that recommends similar books based on a given book title.

## Features

- **Data Cleaning:** The dataset is preprocessed by removing users with fewer than 200 ratings and books with fewer than 100 ratings to ensure statistical significance.
- **KNN Model:** Utilizes the Nearest Neighbors algorithm from the `sklearn.neighbors` package to find and recommend books that are similar to a given book title.
- **Recommendation Function:** The `get_recommends()` function takes a book title as an argument and returns a list of 5 similar books along with their distances from the queried book.

## Requirements

- Python 3.x
- Pandas
- NumPy
- Scikit-learn

You can install the necessary packages using:

```bash
pip install pandas numpy scikit-learn
```

## Dataset

The dataset used in this project is the [Book-Crossings Dataset](http://www2.informatik.uni-freiburg.de/~cziegler/BX/). Ensure that the dataset is downloaded and placed in the correct directory before running the code.

## Usage

1. **Importing the Dataset:**  
   Make sure the dataset is properly loaded and cleaned by following the steps outlined in the code.

2. **Training the Model:**  
   The KNN model is trained using the `NearestNeighbors` class, with appropriate parameters to find similar books.

3. **Getting Recommendations:**  
   Use the `get_recommends()` function to get book recommendations. For example:

   ```python
   recommendations = get_recommends("The Queen of the Damned (Vampire Chronicles (Paperback))")
   print(recommendations)
   ```

   This will return a list with the queried book title and 5 recommended books along with their similarity scores.

4. **Sample Output:**

   ```python
   [
     'The Queen of the Damned (Vampire Chronicles (Paperback))',
     [
       ['Catch 22', 0.793983519077301], 
       ['The Witching Hour (Lives of the Mayfair Witches)', 0.7448656558990479], 
       ['Interview with the Vampire', 0.7345068454742432],
       ['The Tale of the Body Thief (Vampire Chronicles (Paperback))', 0.5376338362693787],
       ['The Vampire Lestat (Vampire Chronicles, Book II)', 0.5178412199020386]
     ]
   ]
   ```

## Contributing

Contributions to enhance this project are welcome. Please feel free to submit a pull request or open an issue if you find any bugs or have suggestions for improvements.

## License

This project is open-source and available under the MIT License.

---

This `README.md` should give users a clear understanding of your project, how to use it, and what to expect from the recommendations.