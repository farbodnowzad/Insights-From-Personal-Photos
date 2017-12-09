from clarifai import rest
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import os
from os import listdir
from os.path import isfile, join
import json
import glob

app = ClarifaiApp(api_key='[YOUR CLARIFAI API KEY]')
model = app.models.get("general-v1.3")

index = 0
img_counter = 0
batch_size = 32
img_num = 0

# locate all the image files in the training set at destination mypath
mypath= '[DESTINTION OF TRAINING SET]'
files = [(mypath + '/' + f) for f in listdir(mypath) if isfile(join(mypath, f))]
total_files = len(files)

while (img_counter < total_files):
    print("Processing batch " + str(index+1))
    imageList=[]
    
    for x in range(img_counter, img_counter+batch_size-1):
        try:
            imageList.append(ClImage(filename=files[x]))

        except IndexError:
            break
            
    # convert each file into a Clarifai Image
    app.inputs.bulk_create_images(imageList)

    # predict the tags for each image
    data = model.predict(imageList)
    
    # convert the list of tags for each photo into a txt file
    data_json = json.dumps(data)
    data_loaded = json.loads(data_json)
    for d in data_loaded['outputs']:
        out = '[NAME OF OUTPUT FOLDER]/[NAME OF OUTPUT FILE]' + str(img_num) + '.txt'
        with open(out, 'w') as outfile:
            concepts = d['data']['concepts']
            json.dump(concepts, outfile)
        img_num += 1

        img_counter=img_counter+batch_size
        index=index+1
        print()
