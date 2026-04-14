"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 
    print(f'Loaded songs: {len(songs)}') 

    # Starter example profile
    user_prefs = {
        "min_valence": 0.4,
        "max_valence": 1,
        "favorite_mood": "happy",
        "mood_tolerance": ["chill", "focused"],
        "preferred_genres": ["pop", "indie pop", "k-pop"],
        "target_energy": 0.8,
        "target_danceability": 0.7,
    }

    min_valence: float  # e.g., 0.5 (avoid sad/melancholic son

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n🎧 Top Recommendations 🎧\n")
    print("=" * 50)

    for i, rec in enumerate(recommendations, 1):
        song, score, explanation = rec

        print(f"\n{i}. {song['title']}")
        print(f"   Score: {score:.2f}")
    
        print("   Reasons:")
        for reason in explanation.split("; "):
            print(f"     - {reason}")

    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()
