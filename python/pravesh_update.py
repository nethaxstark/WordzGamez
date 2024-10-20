import random
import emoji

emojis = {
    "😂": "comedy",
    "💥": "action",
    "🎭": "drama",
    "💕": "romance",
    "🚀": "sci-fi",
    "🔪": "thriller",
    "🎬": "animation",
    "🧙‍♂️": "fantasy",
    "👻": "horror",
}

# Map words to their corresponding genres
genre_mapping = {
    "funny": "comedy",
    "action": "action",
    "dramatic": "drama",
    "love": "romance",
    "science fiction": "sci-fi",
    "scary": "horror",
    "animated": "animation",
    "fantasy": "fantasy",
    "thrilling": "thriller",
}

def recommend_movie(genre):
    """Recommends a random movie from the given genre."""
    movies = {
        "comedy": [
            "The Hangover (2009)",
            "21 Jump Street (2012)",
            "The Office (2005-2013)",
        ],
        "action": [
            "Mad Max: Fury Road (2015)",
            "The Matrix (1999)",
            "Inception (2010)",
        ],
        "drama": [
            "The Shawshank Redemption (1994)",
            "Schindler's List (1993)",
            "The Godfather (1972)",
        ],
        "romance": [
            "The Notebook (2004)",
            "Titanic (1997)",
            "When Harry Met Sally (1989)",
        ],
        "sci-fi": [
            "Interstellar (2014)",
            "Blade Runner 2049 (2017)",
            "Arrival (2016)",
        ],
        "thriller": [
            "Parasite (2019)",
            "Gone Girl (2014)",
            "The Silence of the Lambs (1991)",
        ],
        "animation": [
            "Spirited Away (2001)",
            "Spider-Man: Into the Spider-Verse (2018)",
            "Howl's Moving Castle (2004)",
        ],
        "fantasy": [
            "The Lord of the Rings: The Fellowship of the Ring (2001)",
            "Harry Potter and the Sorcerer's Stone (2001)",
            "Avatar (2009)",
        ],
        "horror": [
            "The Shining (1980)",
            "Get Out (2017)",
            "Hereditary (2018)",
        ],
    }

    # Check if the genre is in the mapping, if so, get the corresponding genre
    if genre in genre_mapping:
        genre = genre_mapping[genre]

    if genre not in movies:
        print(f"Sorry, I don't have any recommendations for the {genre} genre.")
        return

    movie = random.choice(movies[genre])
    emoji_char = [k for k, v in emojis.items() if v == genre]
    emoji_str = emoji.emojize(emoji_char[0]) if emoji_char else ""
    print(f"I recommend {movie} {emoji_str}")

if __name__ == "__main__":
    while True:
        genre = input("Enter a movie genre (or 'quit' to exit): ").lower()

        if genre == "quit":
            break

        recommend_movie(genre)
