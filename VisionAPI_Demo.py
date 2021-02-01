import os, io
import pandas as pd
from google.cloud import vision

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'MTGCardScanner-GoogleVisionAPI-ServiceAccountToken.json'

client = vision.ImageAnnotatorClient()

def DetectText(img):
    with io.open(img, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    foundText = response.text_annotations

    df = pd.DataFrame(columns=['locale', 'description'])
    for text in foundText:
        df = df.append(
            dict(
                locale=text.locale,
                description=text.description
                ),
                ignore_index=True
        )
    return df['description'][0]

FILE_NAME = 'IMG_RebbecArchitectOfAscension_Sleeved.jpeg'
FOLDER_PATH = r'B:\Nathaniel Dwyer\SCHOOL\Independant Study\Python Venv\VisionAPI\Images'
print(DetectText(os.path.join(FOLDER_PATH, FILE_NAME)))