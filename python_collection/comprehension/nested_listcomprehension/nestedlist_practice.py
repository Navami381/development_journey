"""
================================================================================
          PYTHON LIST & DATA STRUCTURE ASSESSMENT WORKBOOK
================================================================================

This document contains Python datasets structured as nested lists along with 
practice questions and column-by-column assessment tasks.

--------------------------------------------------------------------------------
SECTION 1: MOVIES DATASET
--------------------------------------------------------------------------------

Dataset Structure:
[Title (str), Language (str), Duration in mins (int), Release Year (int), Rating (float)]

Python Code Definition:
movies_data = [
    ["dangal", "hindi", 161, 2016, 8.3],       # 0
    ["premam", "malayalam", 156, 2015, 8.3],   # 1
    ["inception", "english", 148, 2010, 8.8],  # 2
    ["vikram", "tamil", 175, 2022, 8.3],       # 3
    ["parasite", "korean", 132, 2019, 8.5],    # 4
    ["rrr", "telugu", 187, 2022, 7.8],         # 5
    ["drishyam", "malayalam", 160, 2013, 8.3], # 6
    ["avatar", "english", 162, 2009, 7.9],     # 7
    ["kumbalangi nights", "malayalam", 135, 2019, 8.5], # 8
    ["sholay", "hindi", 204, 1975, 8.1]        # 9
]

Assessment Tasks for Movies Dataset:

Basic Filtering:
  Q1. Find by Language: Print the titles of all Malayalam movies.
  Q2. Find by Year: Print the titles of all movies released after the year 2015.
  Q3. Find by Rating: Count how many movies have a rating of 8.5 or higher.

Intermediate Calculations:
  Q4. Average Duration: Calculate the average duration (in minutes) of all the movies in the dataset.
  Q5. Multiple Conditions: Print the titles of movies that are longer than 150 minutes AND have a rating greater than 8.0.

Advanced Searching:
  Q6. Highest Rating: Find and print the entire record for the movie with the highest rating.
  Q7. Oldest Movie: Find the title and release year of the oldest movie in the dataset.


--------------------------------------------------------------------------------
SECTION 2: BOOKS DATASET
--------------------------------------------------------------------------------

Dataset Structure:
[Title (str), Genre (str), Price in USD (int), Release Year (int), Rating (float)]

Python Code Definition:
books_data = [
    ["The Hobbit", "Fantasy", 15, 1937, 4.8],           # 0
    ["Dune", "Sci-Fi", 18, 1965, 4.7],                 # 1
    ["Project Hail Mary", "Sci-Fi", 22, 2021, 4.9],    # 2
    ["Atomic Habits", "Self-Help", 16, 2018, 4.8],     # 3
    ["1984", "Dystopian", 12, 1949, 4.6],             # 4
    ["The Silent Patient", "Mystery", 14, 2019, 4.5],  # 5
    ["Sapiens", "History", 20, 2014, 4.7],            # 6
    ["Harry Potter", "Fantasy", 25, 1997, 4.9],        # 7
    ["Educated", "Memoir", 17, 2018, 4.4],             # 8
    ["Klara and the Sun", "Sci-Fi", 13, 2021, 4.2]     # 9
]

Column Breakdown & Target Analysis:
--------------------------------------------------------------------------------
Index | Column Name  | Data Type | Target Analysis
--------------------------------------------------------------------------------
  0   | Title        | String    | Text processing & searching
  1   | Genre        | String    | Categorical grouping & distinct counts
  2   | Price ($)    | Integer   | Min/Max aggregation & arithmetic sums
  3   | Year         | Integer   | Time calculations & range filters
  4   | Rating       | Float     | Threshold filtering & averages
--------------------------------------------------------------------------------

Column-by-Column Assessment Tasks:

Column 0: Title (Index 0)
  Task 0.1: Print the titles of all books that contain more than 10 characters.
  Task 0.2: Find and print all titles that start with the word "The".

Column 1: Genre (Index 1)
  Task 1.1: Create a set or list containing all unique genres present in the dataset (without duplicates).
  Task 1.2: Count how many total books belong to the "Sci-Fi" genre.

Column 2: Price (Index 2)
  Task 2.1: Calculate the total cost if a customer buys one copy of every book in the dataset.
  Task 2.2: Find and print the title and price of the cheapest book (lowest price).

Column 3: Release Year (Index 3)
  Task 3.1: Print each book's title along with its age in years (using 2026 as the current year).
  Task 3.2: Filter and display all books published before the year 2000.

Column 4: Rating (Index 4)
  Task 4.1: Calculate the average rating of all 10 books in the dataset.
  Task 4.2: Count how many books have a rating of 4.8 or higher.

Multi-Column Capstone Challenge:
  Capstone Task: Write a script to find the title of the most expensive "Sci-Fi" book published after 2010.

================================================================================
"""