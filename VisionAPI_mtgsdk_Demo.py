import os, io, re, difflib
import pandas as pd
from google.cloud import vision
from mtgsdk import Card
from mtgsdk import Set
from mtgsdk import Type
from mtgsdk import Supertype
from mtgsdk import Subtype
from mtgsdk import Changelog

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'MTGCardScanner-GoogleVisionAPI-ServiceAccountToken.json'

client = vision.ImageAnnotatorClient()

scannedCardName = ''
scannedCardTypeline = ''
scannedCardType = ''
scannedCardCreatureType = ''

def findnth(haystack, needle, n):
    parts= haystack.split(needle, n+1)
    if len(parts)<=n+1:
        return -1
    return len(haystack)-len(parts[-1])-len(needle)

def isProperString(str, search=re.compile(r'[a-zA-Z0-9.,]').search):
    return not bool(search(str))

def DetectText(img):
    global scannedCardName
    global scannedCardTypeline
    global scannedCardType
    global scannedCardCreatureType

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
    discoveredText = str(df['description'][0])
    print("discoveredText: " + discoveredText)
    # chars = set('aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ,1234567890 ')
    # if any((c in chars) for c in str(discoveredText[0:discoveredText.find("\n")])):
    if isProperString(str(discoveredText[0:discoveredText.find("\n")])):
        scannedCardName = str(discoveredText[0:discoveredText.find("\n")])
    else:
        scannedCardName = str(discoveredText[0:discoveredText.find("\n")][0:discoveredText[0:discoveredText.find("\n")].rfind(' ')])
    return scannedCardName
    # scannedCardTypeline = str(discoveredText[findnth(discoveredText, '\n', 0):findnth(discoveredText, '\n', 1)])
    # scannedCardType = str(scannedCardTypeline[0:scannedCardTypeline.find(' - ')])
    # if 'Creature' in scannedCardType:
    #     scannedCardCreatureType = str(scannedCardTypeline[scannedCardTypeline.find(' - ')+3:])
    # else:
    #     scannedCardCreatureType = 'Card is not of type "Creature"'
    # return scannedCardName + scannedCardTypeline + scannedCardType + '\n' + scannedCardCreatureType

def retrieveRelatedCardInfo(cardName):
    # for now we will just print the info to the console, but this really should be more of a getter function (with a return statement as opposed to a print statement)
    cards = Card.where(name=cardName).all()
    print('\n----------RESULTS----------\n')
    i=0
    uniqueCardResults = []
    for card in cards:
        if card.name in uniqueCardResults:
            continue
        else:
            uniqueCardResults.append(card.name)
            i=i+1
            print('\n=====Result #' + str(i) + '=====\n')
            print('Card Name: ' + card.name)
            if card.mana_cost != None:
                print('Card Mana Cost: ' + card.mana_cost)
            else:
                print('Card Mana Cost: N/A')
            if card.cmc != None:
                print('Card CMC: ' + str(card.cmc)) # Type of card.cmc is float
            else:
                print('Card CMC: N/A')
            print('Card Color Identity: ', end='') # Type of card.color_identity is list
            for color in card.color_identity:
                print(color)
            print('Card Type: ' + card.type)
            if 'Creature' in card.type:
                print('Card Power/Toughness: ' + card.power + '/' + card.toughness)
            print('Card Rarity: ' + card.rarity)
            print('Card Rules Text: ' + card.text)
            print('Card Unique ID: ' + card.id)

def retrieveExactCardInfo(cardName):
    # for now we will just print the info to the console, but this really should be more of a getter function (with a return statement as opposed to a print statement)
    cards = Card.where(name=cardName).all()
    i=0
    uniqueCardResults = []
    allGathererCardNames = []
    print(cardName)
    for card in cards: # here we construct the list of all related names from Gatherer to use for our difflib.get_close_matches() function
        allGathererCardNames.append(card.name)
    closestNameMatch = difflib.get_close_matches(cardName, allGathererCardNames, n=1)[0] # Now we have the closest name match
    for card in cards:
        if card.name == closestNameMatch:
            if card.name in uniqueCardResults:
                continue
            else:
                uniqueCardResults.append(card.name)
                i=i+1
                print('\n----------RESULT----------\n')
                print('Card Name: ' + card.name)
                if card.mana_cost != None:
                    print('Card Mana Cost: ' + card.mana_cost)
                else:
                    print('Card Mana Cost: N/A')
                if card.cmc != None:
                    print('Card CMC: ' + str(card.cmc)) # Type of card.cmc is float
                else:
                    print('Card CMC: N/A')
                print('Card Color Identity: ', end='') # Type of card.color_identity is list
                for color in card.color_identity:
                    print(color)
                print('Card Type: ' + card.type)
                if 'Creature' in card.type:
                    print('Card Power/Toughness: ' + card.power + '/' + card.toughness)
                print('Card Rarity: ' + card.rarity)
                print('Card Rules Text: ' + card.text)
                print('Card Unique ID: ' + card.id)
        else:
            continue

FILE_NAMES = ['IMG_RebbecArchitectOfAscension_Sleeved.jpeg',
'IMG_RadiantSerraArchangel_Sleeved.jpeg',
'IMG_Plains_Sleeved.jpeg',
'IMG_NinthBridgePatrol_Sleeved.jpeg',
'IMG_AngelOfTheDawn_Unsleeved.jpeg',
'IMG_AncestralBlade_Unsleeved.jpeg']
FOLDER_PATH = r'B:\Nathaniel Dwyer\SCHOOL\Independant Study\Python Venv\VisionAPI\Images'
for x in range(len(FILE_NAMES)):
    # retrieveRelatedCardInfo(DetectText(os.path.join(FOLDER_PATH, FILE_NAMES[x])))
    retrieveExactCardInfo(DetectText(os.path.join(FOLDER_PATH, FILE_NAMES[x])))
 