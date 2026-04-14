# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

---

## How The System Works

Real-world recommendations work by combining behavior (user clicks, skips, likes; both implicit and explicit signals), content data (song's information such as mood and tempo), and context data (when user listens to songs, current events/trends) with machine learning algorithms. Initial response: (This helps give optimal recommendations. In my system, the Recommender uses each Song's mood, energy, and danceability to compute a score for each song. My UserProfile stores the user's preferred mood, energy, and danceability value for ideal songs. The Recommender computes a score for each song through the following math formula: score = (0.5 * mood_score) + (0.3 * energy_score) + (0.2 * danceability_score), where mood_score = 0 or 1 (match or not), energy_score = 1 - (song_energy - target_energy), and danceability_score = 1- (song_danceability - target_danceability). This system prioritizes mood, then energy, then danceability, and this is how the recommender works.)

Algorithm Recipe: 
The system takes a user profile and song dataset.
The user profile is given as:
class UserProfile:
    favorite_mood: str  # Primary mood preference
    mood_tolerance: List[str]  # Secondary acceptable moods ["chill", "focused"]
    target_energy: float  # 0.6
    target_danceability: float  # 0.7
    preferred_genres: List[str]  # ["pop", "indie pop"]
    likes_acoustic: bool  # True/False to prefer acoustic vs. electronic
    min_valence: float  # e.g., 0.5 (avoid sad/melancholic songs)

Then, system loops through each song while filtering out those with irrelevent valence (to filter out songs which are clearly not matches). For each remaining song, it computes feature scores such as mood_score ∈ {1.0 (exact match), (acceptable match, in tolerance list), 0.0 (not a match)}, genre_score ∈ {1.0 (exact match), 0.2 (not a match)}, energy_score = 1 - |song.energy - user.target_energy|, and danceability_score = 1 - |song.danceability - user.target_danceability|. It then combines them using a weighted formula:
score = 0.40*mood_score + 0.30*genre_score + 0.15*energy_score + 0.15*danceability_score.

All (song, score) pairs are stored and sorted in descending order of score.
Finally, the system returns the top K songs as personalized recommendations.

Here is the mermaid diagram:
![alt text](image.png)


Biases: 
Because of the weighted formula (0.40*mood_score + 0.30*genre_score + 0.15*energy_score + 0.15*danceability_score), this system will consider mood and genre matches more heavily than energy, danceability. This system will prioritize valence compatability, mood/feel of the song, and the song's classified genre the most, ignoring more technical aspects like acoustics.

## Sample Terminal Output:
High Energy/Pop Profile:
![High Energy/Pop Recommendations](image-1.png)

Sad Gym Junkie (Edge Case) Profile:
![Edge Case Recommendations](image-2.png)

Chill Lofi Profile:
![Chill Lofi Recommendations](image-3.png)

Deep Intense Rock Profile:
![Deep Intense Rock Recommendations](image-4.png)


---



## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried
I tested my recommender on four different user profiles: happy/pop, lofi/chill, edge case (prefer high energy but sad genre), and heavy rock. For each of these cases, I looked at the songs recommended and their corresponding genres, moods, and energy levels, and for all cases, the recommendations seemed accurate and reasonable. None of the recommendations surprised me too much.

---

## Limitations and Risks
One weakness I discovered during my experiments is that my system favors labels over actual music. Since genre and mood account for about 70% of a song's score, and both of these are just labels of a song rather than the song's actual music, my system favors easily classifiable songs.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name
MusicMind 1.0

---

## 2. Intended Use
This music recommender is meant for users to find more songs that fit their music taste. It assumes that the user has a good idea of what music they like and is not meant to be used to figure out new kinds of music interests. This can be used by real users.

---

## 3. How It Works (Short Explanation)
My scoring approach takes into consideration the user's preferred music mood, genre, energy, and danceability, filtering by valence first. The model turns those into a score using a weighted average, considering mood and genre the most. This means that genre and mood compatability is considerd more than energy compatability. I changed the number of components considered from the starter logic to make this score calculation more accurate and less biased.

---

## 4. Data
The model uses a dataset of 22 songs, most of which are English-language songs. A variety of genres are represented here, ranging from pop to lofi to rock. I added 12 more songs than originally provided so that the model has a larger set of songs to recommend, allowing more personalized recommendations by music taste. I think that, for the most part, this dataset is good at representing a variety of different music tastes.


---

## 5. Strengths
My system works well for a wide range of music preferences. For all cases I tested my system on, the recommendations seemed reasonable. This is because my system heavily considers genre and mood, making sure that the vibe of each recommended song mirrors user preferences.


---

## 6. Limitations and Bias
One weakness I discovered during my experiments is that my system favors labels over actual music. Since genre and mood account for about 70% of a song's score, and both of these are just labels of a song rather than the song's actual music, my system favors easily classifiable songs. For example, songs that can easily be classified as "happy" mood and "pop" genre are more likely to appear correctly versus songs that fit under multiple moods and genres are less likely to be recommended. My system also struggles to output a diverse set of song recommendations, and does not allow room for the user to listen to new kinds of songs.

---

## 7. Evaluation

How did you check your system

Examples:
I tested my recommender on four different user profiles: happy/pop, lofi/chill, edge case (prefer high energy but sad genre), and heavy rock. For each of these cases, I looked at the songs recommended and their corresponding genres, moods, and energy levels, and for all cases, the recommendations seemed accurate and reasonable. None of the recommendations surprised me too much.
Since many of the songs in my dataset are easily classifiable, the recommendations did not really change too much even after I eliminated the genre feature from scoring. However, I did notice that once I removed the genre feature, some songs that sort of sound like a particular genre, such as Takedown sounding like pop but being classified under rock, showed up under happy/pop. Removing genre gave more preference to actual musical content rather than labels, which can be good or bad depending on perspective.
---

## 8. Future Work
To improve the model, I would try and group together similar genres and moods to diversify the music recommendations. Currently, the model looks for exact matches in mood/genre but I think it would be better if the model also recommended similar mood/genre songs so that the user could explore more songs and figure out other kinds of songs they like, to get familiar with more songs.


---

## 9. Personal Reflection
I learned that recommender systems are much more complex than I previously imagined. They not only consider explicit user behavior but they also consider implicit user behavior such as time spent on certain songs. I discovered that, to be the most accurate, recommender systems must consider a variety of components when giving recommendations. I also learned that there must be weighting when giving a score to a particular candidate, and that it is important to prioritize the right components when scoring. This project made me realize that each recommendation system is biased in its own way (which is not a bad thing), and that one must clearly define what they want the recommendation system to prioritize beforehand. AI was especially helpful in this process to write out all the code, so that I could focus on the overall system design.

