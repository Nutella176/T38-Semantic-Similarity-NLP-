import spacy

nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp('cat apple monkey banana ') 
for token1 in tokens:
 for token2 in tokens:
    print(token1.text, token2.text, token1.similarity(token2))
    
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go", "Hello, there is my car",
"I\'ve lost my car in my car", "I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence) 
    print(sentence + " - ", similarity)   

# Write a note about what you found interesting about the similarities between cat, monkey and banana and think of an example of your own.
    # Cat and monkey have a similarity of 59% both being animals
    # Monkey and banana have a similarity of 40% because monkeys eat bananas
    # Cat and bananas don't have much in common hence the similarity is 22%


# Run the example file with the simpler language model ‘en_core_web_sm’ and write a note on what you notice is different from the model 'en_core_web_md'.
    # A user warning W007 is displayed. The warning indicates that the model being used does not have pre-trained word vectors loaded. 
    # Because of this the model relies solely on syntactic and grammatical features to calculate similarity, which may not be sufficient in all cases.
