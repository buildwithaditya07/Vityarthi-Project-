# CineMatch - Project Statement

## 1. Problem Statement

With so many movies available on streaming platforms like Netflix, Prime Video and Disney+, people often spend more time searching for something to watch than actually watching it. Browsing through endless titles, checking ratings on one site and availability on another, is confusing and time-consuming.

There is a need for a simple tool that lets a user quickly narrow down movies based on what they actually care about - the **genre** they are in the mood for, the **industry** (Hollywood or Bollywood) they prefer, and the **OTT platform** they already subscribe to - and then shows the best-rated options first.

---

## 2. Scope of the Project

**What the project covers:**

- A console-based Python application that runs in the terminal
- A built-in collection of around 100 popular Hollywood and Bollywood movies
- Each movie record stores the name, genre, industry, IMDb rating and OTT platform
- Filtering of movies by genre, industry and OTT platform (any combination, or "Any" to skip a filter)
- Sorting the matching movies by IMDb rating, from highest to lowest
- Displaying the results in a clean, readable format
- Handling cases where no movie matches the user's choices

**What the project does not cover:**

- No graphical or web interface
- No internet connection or live data - ratings and OTT availability are fixed in the code
- No user accounts, watch history or personalised learning
- No search by movie name, actor or director
- Only Hollywood and Bollywood movies are included

---

## 3. Target Users

- **Movie lovers** who want a quick suggestion without scrolling through multiple apps
- **OTT subscribers** who want to see only what is available on the platform they already pay for
- **Friends and families** deciding what to watch together
- **Beginner Python learners and students** who can use the project to understand lists, tuples, loops, conditions, functions and user input in a practical way

---

## 4. High-Level Features

- **Genre-based recommendation** - choose from Action, Comedy, Crime, Drama, Fantasy, Horror, Romance, Sci-Fi, Thriller, War and Western
- **Industry filter** - Hollywood or Bollywood
- **OTT platform filter** - Netflix, Prime Video or Disney+
- **"Any" option** - skip any filter to widen the results
- **Rating-based sorting** - the best-rated movies appear first
- **Flexible input handling** - not case-sensitive and ignores extra spaces
- **Detailed output** - shows genre, industry, IMDb rating and OTT platform for every recommendation
- **Friendly error message** - tells the user when no movies match their choices
