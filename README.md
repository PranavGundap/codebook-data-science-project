#  CodeBook Data Science Project

##  Overview
This project is a simple simulation of a social media recommendation system built using pure Python (without external libraries).

It demonstrates how platforms suggest:
-  People you may know (friend recommendations)
-  Pages you might like (content recommendations)

The goal of this project is to understand how real-world recommendation systems work using basic logic and data structures.

---

##  Features

### 1. Data Loading
- Reads user and page data from a JSON file
- Structures the data into Python dictionaries for processing

### 2. Data Cleaning
- Removes users with missing names
- Eliminates duplicate friend entries
- Removes inactive users (no friends & no liked pages)
- Deduplicates pages using unique IDs

### 3. People You May Know (Friend Recommendation)
- Suggests new users based on **mutual friends**
- Also shows:
  - Mutual friend names
  - Number of mutual connections (strength of recommendation)

### 4. Pages You Might Like (Content Recommendation)
- Recommends pages based on **shared interests**
- Uses a simple form of **collaborative filtering**
- If two users like similar pages, their other liked pages are recommended

---

##  How It Works

###  Friend Recommendation Logic
1. Take a user
2. Look at their direct friends
3. Look at friends of those friends
4. Suggest users who:
   - Are not already friends
   - Share mutual connections

 More mutual friends = stronger recommendation

---

### 📄 Page Recommendation Logic
1. Take pages liked by a user
2. Compare with other users
3. Find users with **common liked pages**
4. Recommend pages those users like (but current user doesn’t)

 This is called **Collaborative Filtering**:
> “People with similar interests may like similar content”

---

##  How to Run

1. Make sure Python is installed  
2. Open terminal in project folder  
3. Run:

```bash
python main.py
