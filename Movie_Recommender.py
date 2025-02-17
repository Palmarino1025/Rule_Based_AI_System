def recommend_movies(genres=None, moods=None):
    recommendations = set()  # Use a set to prevent duplicate movies

    # Define movies based on genre (keys are lowercase)
    genre_based = {
        "action": ["Mad Max: Fury Road", "John Wick", "Gladiator"],
        "comedy": ["Superbad", "Step Brothers", "Anchorman"],
        "horror": ["The Conjuring", "Hereditary", "A Nightmare on Elm Street"],
        "sci-fi": ["Blade Runner 2049", "Interstellar", "Arrival"],
        "drama": ["The Shawshank Redemption", "Forrest Gump", "The Green Mile"]
    }

    # Define movies based on mood (keys are lowercase)
    mood_based = {
        "exciting": ["Inception", "Mission Impossible", "The Dark Knight"],
        "funny": ["Dumb and Dumber", "The Hangover", "Ghostbusters"],
        "thought-provoking": ["The Matrix", "Ex Machina", "2001: A Space Odyssey"],
        "dark": ["Joker", "Se7en", "Nightcrawler"],
        "scary": ["It", "The Babadook", "Sinister"],
        "relaxing": ["Forrest Gump", "The Secret Life of Walter Mitty", "Paddington 2"],
        "thrilling": ["A Quiet Place", "Alien", "Don't Breathe"]
    }

    # Combined rules for genre + mood (keys are lowercase)
    combined_rules = {
        ("action", "exciting"): ["Mad Max: Fury Road", "John Wick", "Gladiator"],
        ("comedy", "funny"): ["Superbad", "Step Brothers", "Anchorman"],
        ("horror", "scary"): ["The Conjuring", "Hereditary", "A Nightmare on Elm Street"],
        ("sci-fi", "thought-provoking"): ["Blade Runner 2049", "Interstellar", "Arrival"],
        ("sci-fi", "dark"): ["Ex Machina", "The Terminator", "Annihilation"],
        ("drama", "relaxing"): ["Forrest Gump", "The Green Mile", "Good Will Hunting"]
    }

    # Convert input strings to lowercase lists (split by commas)
    genre_list = [g.strip().lower() for g in genres.split(",")] if genres else []
    mood_list = [m.strip().lower() for m in moods.split(",")] if moods else []

    # Get movies from genre-based rules
    for genre in genre_list:
        if genre in genre_based:
            recommendations.update(genre_based[genre])

    # Get movies from mood-based rules
    for mood in mood_list:
        if mood in mood_based:
            recommendations.update(mood_based[mood])

    # Get movies from combined rules (matching genre and mood)
    for genre in genre_list:
        for mood in mood_list:
            if (genre, mood) in combined_rules:
                recommendations.update(combined_rules[(genre, mood)])

    # If no valid input, provide a default list
    if not recommendations:
        recommendations.update(["The Shawshank Redemption", "Inception", "The Dark Knight"])

    return list(recommendations)  # Convert set back to a list


# User input and function call
user_genres = input("Enter preferred genres (Please use commas for multiple choices)(e.g., Action, Comedy, Horror, Sci-Fi, Drama or press Enter to skip): ").strip()
user_moods = input("Enter preferred moods (Please use commas for multiple choices)(e.g., Exciting, Funny, Thought-provoking, Dark, Scary, Relaxing, Thrilling or press Enter to skip): ").strip()

movies = recommend_movies(user_genres if user_genres else None, user_moods if user_moods else None)

print("\nWe recommend these movies for you:", movies)
