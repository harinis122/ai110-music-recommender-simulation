# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  
MusicMind 1.0

---

## 2. Intended Use  
This music recommender is meant for users to find more songs that fit their music taste. It assumes that the user has a good idea of what music they like and is not meant to be used to figure out new kinds of music interests. This can be used by real users. 

---

## 3. How the Model Works  
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
I tested my recommender on four different user profiles: happy/pop, lofi/chill, edge case (prefer high energy but sad genre), and heavy rock. For each of these cases, I looked at the songs recommended and their corresponding genres, moods, and energy levels, and for all cases, the recommendations seemed accurate and reasonable. None of the recommendations surprised me too much.
Since many of the songs in my dataset are easily classifiable, the recommendations did not really change too much even after I eliminated the genre feature from scoring. However, I did notice that once I removed the genre feature, some songs that sort of sound like a particular genre, such as Takedown sounding like pop but being classified under rock, showed up under happy/pop. Removing genre gave more preference to actual musical content rather than labels, which can be good or bad depending on perspective.

---

## 8. Future Work  

To improve the model, I would try and group together similar genres and moods to diversify the music recommendations. Currently, the model looks for exact matches in mood/genre but I think it would be better if the model also recommended similar mood/genre songs so that the user could explore more songs and figure out other kinds of songs they like, to get familiar with more songs.

---

## 9. Personal Reflection  
I learned that recommender systems are much more complex than I previously imagined. They not only consider explicit user behavior but they also consider implicit user behavior such as time spent on certain songs. I discovered that, to be the most accurate, recommender systems must consider a variety of components when giving recommendations. I also learned that there must be weighting when giving a score to a particular candidate, and that it is important to prioritize the right components when scoring. This project made me realize that each recommendation system is biased in its own way (which is not a bad thing), and that one must clearly define what they want the recommendation system to prioritize beforehand. AI was especially helpful in this process to write out all the code, so that I could focus on the overall system design.
