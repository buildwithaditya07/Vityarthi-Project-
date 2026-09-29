# CineMatch - Simple Movie Recommendation System
# Python console-based project

# Each movie is stored as:
# [movie name, genre, industry, IMDb rating, OTT platform]

movies = [('The Shawshank Redemption', 'Drama', 'Hollywood', 9.3, 'Prime Video'), ('The Godfather', 'Crime', 'Hollywood', 9.2, 'Prime Video'), 
          ('The Dark Knight', 'Action', 'Hollywood', 9.0, 'Prime Video'), ('The Godfather Part II', 'Crime', 'Hollywood', 9.0, 'Prime Video'), 
          ('12 Angry Men', 'Drama', 'Hollywood', 9.0, 'Prime Video'), ('The Lord of the Rings: The Return of the King', 'Fantasy', 'Hollywood', 9.0, 'Prime Video'), 
          ("Schindler's List", 'Drama', 'Hollywood', 9.0, 'Prime Video'), ('Pulp Fiction', 'Crime', 'Hollywood', 8.9, 'Netflix'), ('The Lord of the Rings: The Fellowship of the Ring', 'Fantasy', 'Hollywood', 8.9, 'Prime Video'), 
          ('The Good, the Bad and the Ugly', 'Western', 'Hollywood', 8.8, 'Prime Video'), ('Forrest Gump', 'Drama', 'Hollywood', 8.8, 'Netflix'), ('Fight Club', 'Drama', 'Hollywood', 8.8, 'Prime Video'), 
          ('Inception', 'Sci-Fi', 'Hollywood', 8.8, 'Prime Video'), ('The Lord of the Rings: The Two Towers', 'Fantasy', 'Hollywood', 8.8, 'Prime Video'), ('The Matrix', 'Sci-Fi', 'Hollywood', 8.7, 'Prime Video'), 
          ('Goodfellas', 'Crime', 'Hollywood', 8.7, 'Prime Video'), ('Interstellar', 'Sci-Fi', 'Hollywood', 8.7, 'Prime Video'), ("One Flew Over the Cuckoo's Nest", 'Drama', 'Hollywood', 8.6, 'Prime Video'), 
          ('Se7en', 'Crime', 'Hollywood', 8.6, 'Netflix'), ('The Silence of the Lambs', 'Thriller', 'Hollywood', 8.6, 'Prime Video'), ('Saving Private Ryan', 'War', 'Hollywood', 8.6, 'Prime Video'), 
          ('The Green Mile', 'Drama', 'Hollywood', 8.6, 'Prime Video'), ('City of God', 'Crime', 'Hollywood', 8.6, 'Netflix'), ('Life Is Beautiful', 'Comedy', 'Hollywood', 8.6, 'Prime Video'), 
          ('Terminator 2: Judgment Day', 'Action', 'Hollywood', 8.6, 'Prime Video'), ('Back to the Future', 'Sci-Fi', 'Hollywood', 8.5, 'Prime Video'), ('The Pianist', 'Drama', 'Hollywood', 8.5, 'Prime Video'), 
          ('Gladiator', 'Action', 'Hollywood', 8.5, 'Prime Video'), ('The Departed', 'Crime', 'Hollywood', 8.5, 'Prime Video'), ('The Prestige', 'Drama', 'Hollywood', 8.5, 'Prime Video'), ('Whiplash', 'Drama', 'Hollywood', 8.5, 'Netflix'), 
          ('The Intouchables', 'Comedy', 'Hollywood', 8.5, 'Netflix'), ('The Dark Knight Rises', 'Action', 'Hollywood', 8.4, 'Prime Video'), ('Avengers: Endgame', 'Action', 'Hollywood', 8.4, 'Disney+'), 
          ('Spider-Man: No Way Home', 'Action', 'Hollywood', 8.2, 'Netflix'), ('The Avengers', 'Action', 'Hollywood', 8.0, 'Disney+'), ('Guardians of the Galaxy', 'Action', 'Hollywood', 8.0, 'Disney+'), ('Iron Man', 'Action', 'Hollywood', 7.9, 'Disney+'), 
          ('The Hangover', 'Comedy', 'Hollywood', 7.7, 'Prime Video'), ('Titanic', 'Romance', 'Hollywood', 7.9, 'Disney+'), ('The Conjuring', 'Horror', 'Hollywood', 7.5, 'Prime Video'), ('A Quiet Place', 'Horror', 'Hollywood', 7.5, 'Prime Video'), 
          ('Get Out', 'Horror', 'Hollywood', 7.8, 'Prime Video'), ('The Truman Show', 'Drama', 'Hollywood', 8.2, 'Prime Video'), ('The Wolf of Wall Street', 'Crime', 'Hollywood', 8.2, 'Prime Video'), ('Django Unchained', 'Western', 'Hollywood', 8.5, 'Netflix'), 
          ('Dune', 'Sci-Fi', 'Hollywood', 8.0, 'Prime Video'), ('Dune: Part Two', 'Sci-Fi', 'Hollywood', 8.5, 'Prime Video'), ('Oppenheimer', 'Drama', 'Hollywood', 8.2, 'Prime Video'), ('Parasite', 'Thriller', 'Hollywood', 8.5, 'Prime Video'), 
          ('3 Idiots', 'Comedy', 'Bollywood', 8.4, 'Netflix'), ('Taare Zameen Par', 'Drama', 'Bollywood', 8.3, 'Netflix'), ('Dangal', 'Drama', 'Bollywood', 8.3, 'Netflix'), ('Lagaan', 'Drama', 'Bollywood', 8.1, 'Netflix'), ('Rang De Basanti', 'Drama', 'Bollywood', 8.1, 'Netflix'), 
          ('Dil Chahta Hai', 'Comedy', 'Bollywood', 8.1, 'Netflix'), ('Swades', 'Drama', 'Bollywood', 8.2, 'Netflix'), ('Andhadhun', 'Thriller', 'Bollywood', 8.2, 'Prime Video'), ('Drishyam', 'Thriller', 'Bollywood', 8.2, 'Prime Video'), ('Drishyam 2', 'Thriller', 'Bollywood', 8.2, 'Prime Video'), 
          ('Gangs of Wasseypur', 'Crime', 'Bollywood', 8.2, 'Netflix'), ('Gangs of Wasseypur - Part 2', 'Crime', 'Bollywood', 8.2, 'Netflix'), ('Queen', 'Comedy', 'Bollywood', 8.1, 'Netflix'), ('Barfi!', 'Romance', 'Bollywood', 8.1, 'Netflix'), ('Zindagi Na Milegi Dobara', 'Comedy', 'Bollywood', 8.2, 'Netflix'), 
          ('Jab We Met', 'Romance', 'Bollywood', 7.9, 'Netflix'), ('Rockstar', 'Drama', 'Bollywood', 7.7, 'Netflix'), ('Tamasha', 'Drama', 'Bollywood', 7.3, 'Netflix'), ('Kapoor & Sons', 'Drama', 'Bollywood', 7.7, 'Netflix'), ('Kahaani', 'Thriller', 'Bollywood', 8.1, 'Netflix'), 
          ('Kahaani 2', 'Thriller', 'Bollywood', 6.6, 'Prime Video'), ('Special 26', 'Crime', 'Bollywood', 8.0, 'Netflix'), ('A Wednesday!', 'Thriller', 'Bollywood', 8.1, 'Netflix'), ('Baby', 'Action', 'Bollywood', 7.9, 'Netflix'), ('Uri: The Surgical Strike', 'Action', 'Bollywood', 8.2, 'Prime Video'), 
          ('Shershaah', 'War', 'Bollywood', 8.3, 'Prime Video'), ('Sardar Udham', 'Drama', 'Bollywood', 8.4, 'Prime Video'), ('Chak De! India', 'Drama', 'Bollywood', 8.1, 'Netflix'), ('Bhaag Milkha Bhaag', 'Drama', 'Bollywood', 8.2, 'Netflix'), ('Paan Singh Tomar', 'Drama', 'Bollywood', 8.2, 'Netflix'), 
          ('Maqbool', 'Crime', 'Bollywood', 8.0, 'Prime Video'), ('Omkara', 'Crime', 'Bollywood', 8.1, 'Prime Video'), ('Haider', 'Drama', 'Bollywood', 8.0, 'Netflix'), ('Mard Ko Dard Nahi Hota', 'Action', 'Bollywood', 7.4, 'Netflix'), ('Stree', 'Horror', 'Bollywood', 7.5, 'Prime Video'), ('Tumbbad', 'Horror', 'Bollywood', 8.2, 'Prime Video'), 
          ('Bhool Bhulaiyaa', 'Horror', 'Bollywood', 7.4, 'Prime Video'), ('Kantara', 'Drama', 'Bollywood', 8.6, 'Prime Video'), ('12th Fail', 'Drama', 'Bollywood', 8.8, 'Prime Video'), ('Laapataa Ladies', 'Comedy', 'Bollywood', 8.4, 'Netflix'), ('Article 15', 'Crime', 'Bollywood', 8.1, 'Netflix'), ('Masaan', 'Drama', 'Bollywood', 8.1, 'Netflix'), 
          ('Newton', 'Comedy', 'Bollywood', 7.6, 'Prime Video'), ('The Lunchbox', 'Romance', 'Bollywood', 7.8, 'Netflix'), ('Piku', 'Comedy', 'Bollywood', 7.6, 'Netflix'), ('Vicky Donor', 'Comedy', 'Bollywood', 7.8, 'Prime Video'), ('Bajrangi Bhaijaan', 'Drama', 'Bollywood', 8.1, 'Prime Video'), 
          ('PK', 'Comedy', 'Bollywood', 8.1, 'Netflix'), ('Munna Bhai M.B.B.S.', 'Comedy', 'Bollywood', 8.1, 'Netflix'), 
          ('OMG - Oh My God!', 'Comedy', 'Bollywood', 7.5, 'Netflix')]


def show_movies(movie_list):
    """Display a list of movies."""
    if len(movie_list) == 0:
        print("\nNo movies found for your choices.")
        return

    print("\nRecommended Movies")
    print("-" * 70)

    number = 1

    for movie in movie_list:
        print(number, ".", movie[0])
        print("    Genre:", movie[1])
        print("    Industry:", movie[2])
        print("    IMDb:", movie[3])
        print("    OTT:", movie[4])
        print()
        number = number + 1


def recommend_movies():
    """Take user preferences and find matching movies."""

    print("\n--- CineMatch Movie Recommendation ---")

    print("\nAvailable Genres:")
    print("Action, Comedy, Crime, Drama, Fantasy, Horror, Romance,")
    print("Sci-Fi, Thriller, War, Western")

    genre = input("\nEnter genre (or type Any): ")
    industry = input("Enter industry Hollywood/Bollywood (or type Any): ")
    ott = input("Enter OTT Netflix/Prime Video/Disney+ (or type Any): ")

    genre = genre.strip().lower()
    industry = industry.strip().lower()
    ott = ott.strip().lower()

    recommendations = []

    for movie in movies:

        movie_genre = movie[1].lower()
        movie_industry = movie[2].lower()
        movie_ott = movie[4].lower()

        genre_match = genre == "any" or movie_genre == genre
        industry_match = industry == "any" or movie_industry == industry
        ott_match = ott == "any" or movie_ott == ott

        if genre_match and industry_match and ott_match:
            recommendations.append(movie)

    # Sort manually using a simple loop.
    # This avoids advanced sorting concepts.
    for i in range(len(recommendations)):
        for j in range(i + 1, len(recommendations)):
            if recommendations[i][3] < recommendations[j][3]:
                temp = recommendations[i]
                recommendations[i] = recommendations[j]
                recommendations[j] = temp

    show_movies(recommendations)


print("=" * 55)
print("          CINEMATCH MOVIE RECOMMENDER")
print("=" * 55)

recommend_movies()

print("\nThank you for using CineMatch!")
