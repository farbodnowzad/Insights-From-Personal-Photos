# Insights-From-Personal-Photos
Categorizing users into lifestyle categories. 

## Summary ##
The purpose of this project is to categorize an individual into a specific lifestyle category based on their photos.
The training set of images is organized by lifestyle. Using the Clarifai API, image tags are generated for each photo.
We then aggregate the tags and classifications in order to build a word2vec model. This repository has sample lifestyle categories 
such as 'foodie', 'outdoorsy', 'family', and 'sporty'. Given the current dataset and categories, the testing accuracy falls
slighlty below 80%. With more niche or discminate categories, it is likely to achieve a higher accurracy.

There are two main scripts in this repo: *tag_generator.py* and *Insights_From_Photos_word2vec.ipynb*.

## tag_generator.py ##
