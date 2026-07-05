movies = {
    "Action": ["KGF", "Pushpa", "Salaar", "Jawan"],
    "Comedy": ["Jathi Ratnalu", "F2", "DJ Tillu", "MAD"],
    "Drama": ["Jersey", "Hi Nanna", "Sita Ramam"],
    "Sci-Fi": ["Interstellar", "Inception", "The Matrix"],
    "Thriller": ["Drishyam", "Hit", "Agent Sai Srinivasa Athreya"]
}

print("Available Genres:")
for genre in movies:
    print("-", genre)

choice = input("\nEnter your favorite genre: ")

if choice in movies:
    print("\nRecommended Movies:")
    for movie in movies[choice]:
        print(movie)
else:
    print("Genre not found!")