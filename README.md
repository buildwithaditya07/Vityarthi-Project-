# 🎬 CineMatch - Simple Movie Recommendation System

A console-based Python project that recommends movies based on your favourite genre, film industry, and OTT platform.

---

## 📖 Overview

CineMatch helps you decide what to watch next. Instead of scrolling endlessly through streaming apps, you just answer three quick questions - **genre**, **industry** and **OTT platform** - and the program shows you a list of matching movies, sorted from the highest IMDb rating to the lowest.

The project has a built-in collection of around 100 popular Hollywood and Bollywood movies. Each movie is stored as a tuple in the following format:

```
(movie name, genre, industry, IMDb rating, OTT platform)
```

This project is written using only basic Python concepts (lists, tuples, loops, conditions, functions and user input), which makes it easy to read and understand for beginners.

---

## ✨ Features

- Recommend movies by **genre** (Action, Comedy, Crime, Drama, Fantasy, Horror, Romance, Sci-Fi, Thriller, War, Western)
- Filter by **industry** (Hollywood / Bollywood)
- Filter by **OTT platform** (Netflix / Prime Video / Disney+)
- Type **`Any`** for any question to skip that filter
- Input is **case-insensitive** and extra spaces are ignored (`  DRAMA `, `drama` and `Drama` all work)
- Results are **sorted by IMDb rating** (highest first) using a simple manual sorting loop
- Clean output showing the movie name, genre, industry, IMDb rating and OTT platform
- Friendly message when **no movies match** your choices

---

## 🛠️ Technologies / Tools Used

| Tool | Purpose |
|------|---------|
| Python 3 | Programming language |
| Command line / terminal | Running the program |
| Any code editor (VS Code, IDLE, PyCharm) | Writing and editing the code |

No external libraries or packages are required - only Python's built-in features are used.

---

## 🚀 Steps to Install & Run the Project

1. **Install Python 3** (version 3.6 or above) from [python.org](https://www.python.org/downloads/).
   Check that it is installed:
   ```bash
   python --version
   ```

2. **Get the project files.** Either clone the repository:
   ```bash
   git clone <your-repository-link>
   cd <project-folder>
   ```
   or simply download the `.py` file and place it in a folder.

3. **Open a terminal** inside the project folder.

4. **Run the program:**
   ```bash
   python cinematch.py
   ```
   *(Replace `cinematch.py` with the actual name of your file. On some systems, use `python3` instead of `python`.)*

5. **Answer the prompts** for genre, industry and OTT platform, and view your recommendations.

### Sample Run

```
=======================================================
          CINEMATCH MOVIE RECOMMENDER
=======================================================

--- CineMatch Movie Recommendation ---

Available Genres:
Action, Comedy, Crime, Drama, Fantasy, Horror, Romance,
Sci-Fi, Thriller, War, Western

Enter genre (or type Any): Comedy
Enter industry Hollywood/Bollywood (or type Any): Bollywood
Enter OTT Netflix/Prime Video/Disney+ (or type Any): Netflix

Recommended Movies
----------------------------------------------------------------------
1 . 3 Idiots
    Genre: Comedy
    Industry: Bollywood
    IMDb: 8.4
    OTT: Netflix
...
```

---

## 🧪 Instructions for Testing

Run the program several times with different inputs and compare the output with the expected result below.

| # | Genre | Industry | OTT | Expected Result |
|---|-------|----------|-----|-----------------|
| 1 | `Comedy` | `Bollywood` | `Netflix` | Bollywood comedies on Netflix, starting with **3 Idiots** (8.4) |
| 2 | `Sci-Fi` | `Hollywood` | `Prime Video` | Sci-Fi movies like Inception, Interstellar, The Matrix, highest rating first |
| 3 | `Any` | `Any` | `Any` | The complete movie list sorted by rating (**The Shawshank Redemption**, 9.3, first) |
| 4 | `drama` | `  BOLLYWOOD ` | `netflix` | Same as `Drama / Bollywood / Netflix` (tests case and space handling) |
| 5 | `Western` | `Bollywood` | `Any` | *"No movies found for your choices."* |
| 6 | `Horror` | `Any` | `Disney+` | *"No movies found for your choices."* |

**What to check:**
- Movies are always listed from the highest to the lowest IMDb rating.
- Typing `Any` correctly skips that filter.
- Upper/lower case and extra spaces do not affect the result.
- A combination with no matching movie shows the "No movies found" message instead of crashing.

---

## 📂 Project Structure

```
CineMatch/
│── cinematch.py      # Main program
│── README.md         # Project documentation
```

---

## 🔮 Future Improvements

- Add a minimum IMDb rating filter
- Add more movies and more industries (South Indian, Korean, etc.)
- Let the user search by movie name
- Load the movie data from a CSV/JSON file
- Build a GUI or web version

---


Aditya Prasad 
26BAI10330
VIT Bhopal






