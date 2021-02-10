import json

# All files can be retrived via online API by accessing 'https://mtgjson.com/api/v5/<name of .json file>'

# First we open the .json file so that we can start parsing it:
with open('./AtomicCards/AtomicCards.json', encoding='utf-8') as f:
    atomicCardsData = json.load(f)

# okay, lets start making some getter functions!

def getAsciiName(cardsData, cardName):
    try:
        return cardsData['data'][cardName][0]['asciiName'] # returns String
    except KeyError:
        return 'N/A'

def getColorIdentity(cardsData, cardName):
    return cardsData['data'][cardName][0]['colorIdentity'] # returns List of Strings

def getColorIndicator(cardsData, cardName):
    try:
        return cardsData['data'][cardName][0]['colorIndicator'] # returns List of Strings
    except KeyError:
        return []

def getColors(cardsData, cardName):
    return cardsData['data'][cardName][0]['colors'] # returns List

def getConvertedManaCost(cardsData, cardName):
    return cardsData['data'][cardName][0]['convertedManaCost'] # returns Float

def getEdhrecRank(cardsData, cardName):
    try:
        return cardsData['data'][cardName][0]['edhrecRank'] # returns Integer
    except KeyError:
        return -1

def getFaceConvertedManaCost(cardsData, cardName):
    try:
        return cardsData['data'][cardName][0]['faceConvertedManaCost'] # returns Float
    except KeyError:
        return -1

def getFaceName(cardsData, cardName):
    try:
        return cardsData['data'][cardName][0]['faceName'] # returns String
    except KeyError:
        return 'N/A'

# Function Block for foreignData key goes here

# the getHandModifier function is really only useful when dealing with Vanguard cards
def getHandModifier(cardsData, cardName):
    try:
        return cardsData['data'][cardName][0]['hand'] # returns String
    except KeyError:
        return 'N/A'

def hasAlternativeDeckLimit(cardsData, cardName):
    try:
        return cardsData['data'][cardName][0]['hasAlternativeDeckLimit'] # returns Boolean
    except KeyError:
        return False

def getIdentifiers(cardsData, cardName): # this should return a Dictionary
    ids = []
    for id in cardsData['data'][cardName][0]['identifiers'].keys():
        ids.append(id + ': ' + cardsData['data'][cardName][0]['identifiers'][id])
    return ids # returns List of Strings

def getCardKingdomFoilID(cardsData, cardName):
    try:
        return cardsData['data'][cardName][0]['identifiers']['cardKingdomFoilId'] # returns String
    except KeyError:
        return 'N/A'

def getCardKingdomID(cardsData, cardName):
    try:
        return cardsData['data'][cardName][0]['identifiers']['cardKingdomId'] # returns String
    except KeyError:
        return 'N/A'

def getMcmID(cardsData, cardName):
    try:
        return cardsData['data'][cardName][0]['identifiers']['mcmId'] # returns String
    except KeyError:
        return 'N/A'

def getMcmMetaID(cardsData, cardName):
    try:
        return cardsData['data'][cardName][0]['identifiers']['mcmMetaId'] # returns String
    except KeyError:
        return 'N/A'

def getMtgArenaID(cardsData, cardName):
    try:
        return cardsData['data'][cardName][0]['identifiers']['mtgArenaId'] # returns String
    except KeyError:
        return 'N/A'

def getMtgoFoilID(cardsData, cardName):
    try:
        return cardsData['data'][cardName][0]['identifiers']['mtgoFFoilId'] # returns String
    except KeyError:
        return 'N/A'

def getMtgoID(cardsData, cardName):
    try:
        return cardsData['data'][cardName][0]['identifiers']['mtgoId'] # returns String
    except KeyError:
        return 'N/A'

def getMtgjsonV4ID(cardsData, cardName):
    try:
        return cardsData['data'][cardName][0]['identifiers']['mtgjsonV4Id'] # returns String
    except KeyError:
        return 'N/A'

def getMultiverseID(cardsData, cardName):
    try:
        return cardsData['data'][cardName][0]['identifiers']['multiverseId'] # returns String
    except KeyError:
        return 'N/A'

def getScryfallID(cardsData, cardName):
    try:
        return cardsData['data'][cardName][0]['identifiers']['scryfallId'] # returns String
    except KeyError:
        return 'N/A'

def getScryfallOracleID(cardsData, cardName):
    try:
        return cardsData['data'][cardName][0]['identifiers']['scryfallOracleId'] # returns String
    except KeyError:
        return 'N/A'

def getScryfallIllustrationID(cardsData, cardName):
    try:
        return cardsData['data'][cardName][0]['identifiers']['scryfallIllustrationId'] # returns String
    except KeyError:
        return 'N/A'

def getTcgplayerProductID(cardsData, cardName):
    try:
        return cardsData['data'][cardName][0]['identifiers']['tcgplayerProductId'] # returns String
    except KeyError:
        return 'N/A'

def isReserved(cardsData, cardName):
    try:
        return cardsData['data'][cardName][0]['isReserved'] # returns Boolean
    except KeyError:
        return False

def getKeywords(cardsData, cardName):
    try:
        return cardsData['data'][cardName][0]['keywords'] # returns List of Strings
    except KeyError:
        return []

def getLayout(cardsData, cardName):
    return cardsData['data'][cardName][0]['layout'] # returns String

def getLeadershipSkills(cardsData, cardName): # this should return a Dictionary 
    skills = []
    try:
        for skill in cardsData['data'][cardName][0]['leadershipSkills'].keys():
            skills.append(skill + ': ' + str(cardsData['data'][cardName][0]['leadershipSkills'][skill]))
        return skills # returns List of Booleans
    except KeyError:
        return []

def canBeCommander(cardsData, cardName):
    try:
        return cardsData['data'][cardName][0]['leadershipSkills']['commander'] # returns Boolean
    except KeyError:
        return False

def canBeBrawlCommander(cardsData, cardName): # this method seems to be bugged; it marks legal Brawl commanders as 'False'...
    try:
        return cardsData['data'][cardName][0]['leadershipSkills']['brawl'] # returns Boolean
    except KeyError:
        return False

def canBeOathbreaker(cardsData, cardName):
    try:
        return cardsData['data'][cardName][0]['leadershipSkills']['oathbreaker'] # returns Boolean
    except KeyError:
        return False

def getName(cardsData, cardName):
    return cardsData['data'][cardName][0]['name'] # returns String

# might have to use the BeautifulSoup library to grab the actual price data from the webpage...OR use the AllPrices.json file to grab data
def getPurchaseURLs(cardsData, cardName): # this should return a Dictionary 
    urls = []
    for url in cardsData['data'][cardName][0]['purchaseUrls'].keys():
        urls.append(url + ': ' + cardsData['data'][cardName][0]['purchaseUrls'][url])
    return urls # returns List of Strings

def getCardKingdomPurchaseURL(cardsData, cardName):
    try:
        return cardsData['data'][cardName][0]['purchaseUrls']['cardKingdom'] # returns String
    except KeyError:
        return 'N/A'

def getCardKingdomFoilPurchaseURL(cardsData, cardName):
    try:
        return cardsData['data'][cardName][0]['purchaseUrls']['cardKingdomFoil'] # returns String
    except KeyError:
        return 'N/A'

def getCardMarketPurchaseURL(cardsData, cardName):
    try:
        return cardsData['data'][cardName][0]['purchaseUrls']['cardmarket'] # returns String
    except KeyError:
        return 'N/A'

def getTcgplayerPurchaseURL(cardsData, cardName):
    try:
        return cardsData['data'][cardName][0]['purchaseUrls']['tcgplayer'] # returns String
    except KeyError:
        return 'N/A'

def getLegalities(cardsData, cardName): # this should return a Dictionary 
    legalities = []
    try:
        for legality in cardsData['data'][cardName][0]['legalities'].keys():
            legalities.append(legality + ': ' + cardsData['data'][cardName][0]['legalities'][legality])
        return legalities # returns List of Strings
    except KeyError:
        return []

def getBrawlLegality(cardsData, cardName):
    try:
        return cardsData['data'][cardName][0]['legalities']['brawl'] # returns String
    except KeyError:
        return 'N/A'

def getCommanderLegality(cardsData, cardName):
    try:
        return cardsData['data'][cardName][0]['legalities']['commander'] # returns String
    except KeyError:
        return 'N/A'

def getDuelLegality(cardsData, cardName):
    try:
        return cardsData['data'][cardName][0]['legalities']['duel'] # returns String
    except KeyError:
        return 'N/A'

def getFutureLegality(cardsData, cardName):
    try:
        return cardsData['data'][cardName][0]['legalities']['future'] # returns String
    except KeyError:
        return 'N/A'

def getFrontierLegality(cardsData, cardName):
    try:
        return cardsData['data'][cardName][0]['legalities']['frontier'] # returns String
    except KeyError:
        return 'N/A'

def getGladiatorLegality(cardsData, cardName):
    try:
        return cardsData['data'][cardName][0]['legalities']['gladiator'] # returns String
    except KeyError:
        return 'N/A'

def getHistoricLegality(cardsData, cardName):
    try:
        return cardsData['data'][cardName][0]['legalities']['historic'] # returns String
    except KeyError:
        return 'N/A'

def getLegacyLegality(cardsData, cardName):
    try:
        return cardsData['data'][cardName][0]['legalities']['legacy'] # returns String
    except KeyError:
        return 'N/A'

def getModernLegality(cardsData, cardName):
    try:
        return cardsData['data'][cardName][0]['legalities']['modern'] # returns String
    except KeyError:
        return 'N/A'

def getPauperLegality(cardsData, cardName):
    try:
        return cardsData['data'][cardName][0]['legalities']['pauper'] # returns String
    except KeyError:
        return 'N/A'

def getPennyLegality(cardsData, cardName):
    try:
        return cardsData['data'][cardName][0]['legalities']['penny'] # returns String
    except KeyError:
        return 'N/A'

def getPioneerLegality(cardsData, cardName):
    try:
        return cardsData['data'][cardName][0]['legalities']['pioneer'] # returns String
    except KeyError:
        return 'N/A'

def getStandardLegality(cardsData, cardName):
    try:
        return cardsData['data'][cardName][0]['legalities']['standard'] # returns String
    except KeyError:
        return 'N/A'

def getVintageLegality(cardsData, cardName):
    try:
        return cardsData['data'][cardName][0]['legalities']['vintage'] # returns String
    except KeyError:
        return 'N/A'

def getRulings(cardsData, cardName): # this should return a Dictionary 
    rules = []
    for rule in cardsData['data'][cardName][0]['rulings']:
        rules.append(rule['date'] + ': ' + rule['text'])
    return rules # returns List of Strings

def getSubtypes(cardsData, cardName):
    return cardsData['data'][cardName][0]['subtypes'] # returns List of Stings

def getSupertypes(cardsData, cardName):
    return cardsData['data'][cardName][0]['supertypes'] # returns List of Strings

def getRulesText(cardsData, cardName):
    try:
        return cardsData['data'][cardName][0]['text'] # returns String
    except KeyError:
        return 'N/A'


# Let's test these functions out!

# things to keep in mind forchoosing the search tearm (cardNameToSearch, in this case): split cards are listed under one name in the following pattern: <Front-Face Name> // <Back-Face Name>
cardNameToSearch = "Once Upon a Time" # input('Enter your card to search: ')

print('Color Identity: ', end='')
for colorIdentity in getColorIdentity(atomicCardsData, cardNameToSearch):
    print(colorIdentity, end=', ')
print('\n', end='') 

print('Colors: ', end='')
for color in getColors(atomicCardsData, cardNameToSearch):
    print(color, end=', ')
print('\n', end='') 

print('Converted Mana Cost: ' + str(getConvertedManaCost(atomicCardsData, cardNameToSearch)))
print('EDHREC Rank: ' + str(getEdhrecRank(atomicCardsData, cardNameToSearch)))
print('Card Layout: ' + getLayout(atomicCardsData, cardNameToSearch))
print('Card Name: ' + getName(atomicCardsData, cardNameToSearch))

print('Purchase URLs: ')
for link in getPurchaseURLs(atomicCardsData, cardNameToSearch):
    print(link)

print('Rulings: ')
for ruling in getRulings(atomicCardsData, cardNameToSearch):
    print(ruling)

print('Subtypes: ', end='')
for subtype in getSubtypes(atomicCardsData, cardNameToSearch):
    print(subtype, end=', ')
print('\n', end='') 

print('Supertypes: ', end='')
for supertype in getSupertypes(atomicCardsData, cardNameToSearch):
    print(supertype, end=', ')
print('\n', end='') 

print('Rules Text: ' + getRulesText(atomicCardsData, cardNameToSearch))
print('Ascii Name: ' + getAsciiName(atomicCardsData, cardNameToSearch))

print('Color Indicator: ', end='')
for colorIndication in getColorIndicator(atomicCardsData, cardNameToSearch):
    print(colorIndication, end=', ')
print('\n', end='') 

print('Face Converted Mana Cost: ' + str(getFaceConvertedManaCost(atomicCardsData, cardNameToSearch)))
print('Face Name: ' + getFaceName(atomicCardsData, cardNameToSearch))
print('Hand Modifier: ' + getHandModifier(atomicCardsData, cardNameToSearch))
print('Has Alternative Deck Limit: ' + str(hasAlternativeDeckLimit(atomicCardsData, cardNameToSearch)))
print('Is Reserved: ' + str(isReserved(atomicCardsData, cardNameToSearch)))

print('Keywords: ', end='')
for keyword in getKeywords(atomicCardsData, cardNameToSearch):
    print(keyword, end=', ')
print('\n', end='') 

print('CardKingdom Purchase URL: ' + getCardKingdomPurchaseURL(atomicCardsData, cardNameToSearch))
print('CardKingdom Foil Purchase URL: ' + getCardKingdomFoilPurchaseURL(atomicCardsData, cardNameToSearch))
print('CardMarket Purchase URL: ' + getCardMarketPurchaseURL(atomicCardsData, cardNameToSearch))
print('TCGPlayer Purchase URL: ' + getTcgplayerPurchaseURL(atomicCardsData, cardNameToSearch))

print('Identifiers: ')
for identity in getIdentifiers(atomicCardsData, cardNameToSearch):
    print(identity)

print('CardKingdom Foil ID: ' + getCardKingdomFoilID(atomicCardsData, cardNameToSearch))
print('CardKingdom ID: ' + getCardKingdomID(atomicCardsData, cardNameToSearch))
print('CardMarket ID: ' + getMcmID(atomicCardsData, cardNameToSearch))
print('CardMarket Meta ID: ' + getMcmMetaID(atomicCardsData, cardNameToSearch))
print('MTG Arena ID: ' + getMtgArenaID(atomicCardsData, cardNameToSearch))
print('MTG Online Foil ID: ' + getMtgoFoilID(atomicCardsData, cardNameToSearch))
print('MTG Online ID: ' + getMtgoID(atomicCardsData, cardNameToSearch))
print('MTGJSON V4 ID: ' + getMtgjsonV4ID(atomicCardsData, cardNameToSearch))
print('Multiverse ID: ' + getMultiverseID(atomicCardsData, cardNameToSearch))
print('Scryfall ID: ' + getScryfallID(atomicCardsData, cardNameToSearch))
print('Scryfall Oracle ID: ' + getScryfallOracleID(atomicCardsData, cardNameToSearch))
print('Scryfall Illustration ID: ' + getScryfallIllustrationID(atomicCardsData, cardNameToSearch))
print('TCGplayer Product ID: ' + getTcgplayerProductID(atomicCardsData, cardNameToSearch))

print('Leadership Skills: ')
for skill in getLeadershipSkills(atomicCardsData, cardNameToSearch):
    print(skill)

print('Can Be Commander: ' + str(canBeCommander(atomicCardsData, cardNameToSearch)))
print('Can Be Brawl Commander: ' + str(canBeBrawlCommander(atomicCardsData, cardNameToSearch)))
print('Can Be Oathbreaker: ' + str(canBeOathbreaker(atomicCardsData, cardNameToSearch)))

print('Legalities: ')
for legality in getLegalities(atomicCardsData, cardNameToSearch):
    print(legality)

print('Brawl Legality: ' + getBrawlLegality(atomicCardsData, cardNameToSearch))
print('Commander Legality: ' + getCommanderLegality(atomicCardsData, cardNameToSearch))
print('Duel Legality: ' + getDuelLegality(atomicCardsData, cardNameToSearch))
print('Future Legality: ' + getFutureLegality(atomicCardsData, cardNameToSearch))
print('Frontier Legality: ' + getFrontierLegality(atomicCardsData, cardNameToSearch))
print('Gladiator Legality: ' + getGladiatorLegality(atomicCardsData, cardNameToSearch))
print('Historic Legality: ' + getHistoricLegality(atomicCardsData, cardNameToSearch))
print('Legacy Legality: ' + getLegacyLegality(atomicCardsData, cardNameToSearch))
print('Modern Legality: ' + getModernLegality(atomicCardsData, cardNameToSearch))
print('Pauper Legality: ' + getPauperLegality(atomicCardsData, cardNameToSearch))
print('Penny Legality: ' + getPennyLegality(atomicCardsData, cardNameToSearch))
print('Pioneer Legality: ' + getPioneerLegality(atomicCardsData, cardNameToSearch))
print('Standard Legality: ' + getStandardLegality(atomicCardsData, cardNameToSearch))
print('Vintage Legality: ' + getVintageLegality(atomicCardsData, cardNameToSearch))