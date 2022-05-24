# will need to install these packages, and then for gis follow the instructions in the URL below
# https://pypi.org/project/Google-Images-Search/
from google_images_search import GoogleImagesSearch
import cv2
import os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
pathToDir = os.path.dirname(os.path.abspath(__file__))

finalPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\frontend\\public"

def GenerateComic(word1, word2, word3, phr1, phr2, phr3):
    gis = GoogleImagesSearch('AIzaSyBKY3VW35ZrzMSok_VL63wMkbEmR9d29sU', 'f24b6ddc7bc034296')

    _search_params = {
        'q': '...',
        'num': 1,
        'fileType': 'jpg',
        'rights': 'cc_publicdomain|cc_attribute|cc_sharealike|cc_noncommercial|cc_nonderived',
        'safe': 'safeUndefined',  ##
        'imgType': 'imgTypeUndefined',  ##
        'imgSize': 'imgSizeUndefined',  ##
        'imgDominantColor': 'imgDominantColorUndefined',
        ##
        'imgColorType': 'imgColorTypeUndefined'  ##
    }
    print(pathToDir)
    _search_params['q'] = word1
    gis.search(search_params=_search_params, width=500, height=500, path_to_dir=pathToDir)
    print(gis.results()[0])
    word1Loc = gis.results()[0].path.split('\\')[-1]

    _search_params['q'] = word2
    gis.search(search_params=_search_params, width=500, height=500, path_to_dir=pathToDir)
    print(gis.results()[0])
    word2Loc = gis.results()[0].path.split('\\')[-1]

    _search_params['q'] = word3
    gis.search(search_params=_search_params, width=500, height=500, path_to_dir=pathToDir)
    print(gis.results()[0])
    word3Loc = gis.results()[0].path.split('\\')[-1]

    # add text to images
    addWords(word1Loc, phr1, '1')
    addWords(word2Loc, phr2, '2')
    addWords(word3Loc, phr3, '3')

    # search done. now concatenate images
    img1 = cv2.imread('1.png')
    img2 = cv2.imread('2.png')
    img3 = cv2.imread('3.png')

    try:
        os.remove(word1Loc)
    except:
        pass
    try:
        os.remove(word2Loc)
    except:
        pass
    try:
        os.remove(word3Loc)
    except:
        pass
    os.remove('1.png')
    os.remove('2.png')
    os.remove('3.png')

    comicpictures = cv2.hconcat([img1, img2, img3])
    cv2.imwrite(os.path.join(finalPath, 'comicpictures.jpg'), comicpictures)

#shamelessly stolen from https://blog.lipsumarium.com/caption-memes-in-python/
def addWords(word, phrase, num):
    img = Image.open(word)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("impact.ttf", 40)
    w, h = draw.textsize(phrase, font) # measure the size the text will take

    lineCount = 1
    if w > img.width:
        lineCount = int(round((w / img.width) + 1))

    print("lineCount: {}".format(lineCount))

    lines = []
    if lineCount > 1:
        lastCut = 0
        isLast = False
        for i in range(0,lineCount):
            if lastCut == 0:
                cut = (len(phrase) / lineCount) * i
            else:
                cut = lastCut

            if i < lineCount-1:
                nextCut = (len(phrase) / lineCount) * (i+1)
            else:
                nextCut = len(phrase)
                isLast = True

            print("cut: {} -> {}".format(cut, nextCut))
            nextCut = round(nextCut)
            cut = round(cut)
            # make sure we don't cut words in half
            if nextCut == len(phrase) or phrase[nextCut] == " ":
                print("may cut")
            else:
                print("may not cut")
                while phrase[nextCut] != " ":
                    nextCut += 1
                print("new cut: {}".format(nextCut))

            line = phrase[cut:nextCut].strip()

            # is line still fitting ?
            w, h = draw.textsize(line, font)
            if not isLast and w > img.width:
                print("overshot")
                nextCut -= 1
                while phrase[nextCut] != " ":
                    nextCut -= 1
                print("new cut: {}".format(nextCut))

            lastCut = nextCut
            lines.append(phrase[cut:nextCut].strip())

    else:
        lines.append(phrase)

    print(lines)

    lastY = -h

    for i in range(0, lineCount):
        w, h = draw.textsize(lines[i], font)
        x = img.width/2 - w/2
        y = lastY + h
        draw.text((x - 2, y - 2), lines[i], (0, 0, 0), font=font)
        draw.text((x + 2, y - 2), lines[i], (0, 0, 0), font=font)
        draw.text((x + 2, y + 2), lines[i], (0, 0, 0), font=font)
        draw.text((x - 2, y + 2), lines[i], (0, 0, 0), font=font)
        draw.text((x, y), lines[i], (255, 255, 255), font=font)
        lastY = y
    img.save(num + '.png')

#GenerateComic("samoyed","cat","steak","it's a dog","it's a cat","roasty toasty")
