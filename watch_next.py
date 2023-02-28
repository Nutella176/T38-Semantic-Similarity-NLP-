import spacy

nlp = spacy.load("en_core_web_md")


def watch_next(description):
    # Opening and reading movies.txt file
    with open("movies.txt", "r") as f:
        movies = [line.strip() for line in f.readlines()]

    # Calculating the similarity between the description and each movie
    similarities = []
    for movie in movies:
        doc1 = nlp(description)
        doc2 = nlp(movie)
        similarity = doc1.similarity(doc2)
        similarities.append(similarity)

    # Finding the index of the movie with the highest similarity
    max_index = similarities.index(max(similarities))

    # Printing the title of the most similar movie
    print(movies[max_index])


description = """Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, 
                the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace.    
                Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."""

watch_next(description)
