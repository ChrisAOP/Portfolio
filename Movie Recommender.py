#This program takes in movie descriptions from a .txt file and compares them with a description of a recently watched movie.
#NOTE: Requires the movies.txt file to work.
#It then returns the title of the most similar movie description according to spacy's en_core_web_md module as a suggested next watch.

import spacy
nlp = spacy.load('en_core_web_md')

#Read the movies.txt file and save its contents as lines
with open("movies.txt", "r") as file:
    lines = file.readlines()

#Function to compare each line to a given sentence
def recommend_a_movie(sentence_to_compare):

    #Creates two variables to store values in the function
    most_similar = 0
    recommended_movie = ""

    #For each line in lines, strip the whitespaces and save it as description
    for line in lines:
        line = line.strip() 
        description = nlp(line)

        #Compare the current description to the given sentence, and store the value as similarity
        similarity = description.similarity(nlp(sentence_to_compare))  

        #If the similarity is more than the most_similar value, update most_similar to be the current value
        if similarity > most_similar:       
            most_similar = similarity       
            #And update the recommended_movie variable to show the first 2 words of the description by
            #splitting it into individual words and then joining the words
            recommended_movie = " ".join(description.text.split()[:2])  
    
    #After looping through all the lines, print the recommended_movie title to the user (which will be the title of the most similar comparison)
    return recommended_movie


#Saves the description of Planet Hulk to compare it
sentence_to_compare = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."

#Runs the function with the sentence_to_compare variable as its parameter
recommend_a_movie(sentence_to_compare)

#Prints a next movie recommendation using the value returned by the function
print("Your next movie should be", recommend_a_movie(sentence_to_compare))

