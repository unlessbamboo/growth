"""
移除水印
"""


from PIL import Image


def LoadImage(sourcePath, maskPath):
    try:
        imageSource = Image.open(sourcePath)
        imageMask = Image.open(maskPath)
        return [imageSource, imageMask]
    except BaseException:
        print("ERROR: Unable to load image")
        return []


def CalculateMaskInfo(pair1, pair2):
    maskColor = [0, 0, 0]
    maskAlpha = 0.0

    for p in range(3):
        source1 = (pair1[0] >> ((2 - p) * 8)) & 0xFF
        source2 = (pair2[0] >> ((2 - p) * 8)) & 0xFF
        masked1 = (pair1[1] >> ((2 - p) * 8)) & 0xFF
        masked2 = (pair2[1] >> ((2 - p) * 8)) & 0xFF

        solvable = (source2 - source1) - (masked2 - masked1)
        if solvable == 0:
            print("ERROR: Faild to calculate the mask info !")
            return []
        alpha = 1 - ((float)(masked1 - masked2) / (source1 - source2))
        maskAlpha += alpha
        maskColor[p] = round((masked1 - (1 - alpha) * source1) / alpha)
        if(maskColor[p] < 0x00):
            maskColor[p] = 0x00
        if(maskColor[p] > 0xFF):
            maskColor[p] = 0xFF

    maskAlpha = maskAlpha / 3
    if maskAlpha < 0.0:
        maskAlpha = 0.0
    if maskAlpha > 1.0:
        maskAlpha = 1.0

    print("MaskInfo:")
    print("    Color ", maskColor)
    print("    Alpha ", maskAlpha)
    return [maskColor, maskAlpha]


def ModifyImage(imageSource, imageMask, maskInfo, targetPath):
    sourceSize = imageSource.size
    imageWidth = sourceSize[0]
    imageHeight = sourceSize[1]
    if (imageWidth != imageMask.size[0] or imageHeight != imageMask.size[1]):
        print("ERROR: Resolutions of source and mask unmatch")
        return
    maskColor = maskInfo[0]
    maskAlpha = maskInfo[1]
    imageTarget = imageSource

    for x in range(imageWidth):
        for y in range(imageHeight):
            maskPixel = imageMask.getpixel((x, y))
            print(maskPixel, x, y)
            if isinstance(maskPixel, int):
                continue
            if(maskPixel[0] != maskPixel[1] or maskPixel[1] != maskPixel[2]):
                continue
            grayAlpha = 1 - maskPixel[0] / 255.0
            alpha = maskAlpha * grayAlpha
            if(abs(alpha) < 1e-5):
                continue

            pixel = imageSource.getpixel((x, y))
            newR = round((pixel[0] - alpha * maskColor[0]) / (1.0 - alpha))
            newG = round((pixel[1] - alpha * maskColor[1]) / (1.0 - alpha))
            newB = round((pixel[2] - alpha * maskColor[2]) / (1.0 - alpha))
            if(newR < 0x00):
                newR = 0x00
            if(newR > 0xFF):
                newR = 0xFF
            if(newG < 0x00):
                newG = 0x00
            if(newG > 0xFF):
                newG = 0xFF
            if(newB < 0x00):
                newB = 0x00
            if(newB > 0xFF):
                newB = 0xFF
            imageTarget.putpixel((x, y), (newR, newG, newB))
    # imageTarget.show()
    try:
        imageTarget.save(targetPath, 'PNG')
        print("Save Success!")
    except BaseException:
        print("ERROR: Save Failed")


def DeWaterMark(sourcePath, maskPath, pair1, pair2, targetPath):
    info = CalculateMaskInfo(pair1, pair2)
    if(len(info) < 2):
        return
    images = LoadImage(sourcePath, maskPath)
    if(len(images) < 2):
        return
    ModifyImage(images[0], images[1], info, targetPath)


###
p1 = (0xfff0e0, 0xa1c9dd)
p2 = (0xea6a77, 0x988faf)
DeWaterMark('sample.png', 'mask.png', p1, p2, 'pyOutput.png')
###
