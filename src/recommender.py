from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """Represents a song with audio features and metadata used for recommendations."""
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """Represents a user's music preferences and target listening characteristics."""
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """Encapsulates logic for generating and explaining song recommendations."""
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Returns the top k recommended songs for a given user profile."""
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Provides a human-readable explanation for why a song was recommended."""
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Loads song data from a CSV file and converts fields to appropriate types."""
    print(f"Loading songs from {csv_path}...")
    songs = []
    with open(csv_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convert numerical values
            row['id'] = int(row['id'])
            row['energy'] = float(row['energy'])
            row['tempo_bpm'] = float(row['tempo_bpm'])
            row['valence'] = float(row['valence'])
            row['danceability'] = float(row['danceability'])
            row['acousticness'] = float(row['acousticness'])
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Computes a weighted relevance score and explanation for a song given user preferences."""

    reasons = []

    # Filter by valence (min + max)
    if song['valence'] < user_prefs['min_valence']:
        return (-1.0, [f"Filtered out: valence {song['valence']} < {user_prefs['min_valence']}"])
    if song['valence'] > user_prefs.get('max_valence', 1.0):
        return (-1.0, [f"Filtered out: valence {song['valence']} > {user_prefs['max_valence']}"])

    # Mood Score
    if song['mood'] == user_prefs['favorite_mood']:
        mood_score = 1.0
        mood_points = 0.40 * mood_score
        reasons.append(f"Mood match ({song['mood']}) (+{mood_points})")
    elif song['mood'] in user_prefs['mood_tolerance']:
        mood_score = 0.7
        mood_points = 0.40 * mood_score
        reasons.append(f"Mood acceptable ({song['mood']}) (+{mood_points})")
    else:
        mood_score = 0.0
        mood_points = 0.0
        reasons.append(f"Mood mismatch ({song['mood']}) (+0.00)")

    # Genre Score
    if song['genre'] in user_prefs['preferred_genres']:
        genre_score = 1.0
        genre_points = 0.30 * genre_score
        reasons.append(f"Genre match ({song['genre']}) (+{genre_points})")
    else:
        genre_score = 0.2
        genre_points = 0.30 * genre_score
        reasons.append(f"Not a great genre match ({song['genre']}) (+{genre_points})")

    # Energy Score
    energy_score = 1 - abs(song['energy'] - user_prefs['target_energy'])
    energy_score = max(0.0, energy_score)
    energy_points = 0.15 * energy_score
    reasons.append(f"Energy similarity ({song['energy']}) (+{energy_points})")

    # Danceability Score
    danceability_score = 1 - abs(song['danceability'] - user_prefs['target_danceability'])
    danceability_score = max(0.0, danceability_score)
    dance_points = 0.15 * danceability_score
    reasons.append(f"Danceability similarity ({song['danceability']}) (+{dance_points})")

    # Final Score
    score = mood_points + genre_points + energy_points + dance_points

    return (score, reasons)

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Ranks songs by score and returns the top k recommendations with explanations."""
    scored = [
        (song, *score_song(user_prefs, song))  # (song, score, reasons)
        for song in songs
    ]

    # Filter out invalid songs
    scored = [x for x in scored if x[1] >= 0]

    # Sort + take top k
    top_k = sorted(scored, key=lambda x: x[1], reverse=True)[:k]

    # Format output
    return [
        (song, score, "; ".join(reasons))
        for song, score, reasons in top_k
    ]