import textwrap
from PIL import Image, ImageDraw, ImageFont

def captionImage(filename, caption):
    wrapper = textwrap.TextWrapper(width=40) 
    word_list = wrapper.wrap(text=caption) 
    caption_new = ''
    for ii in word_list[:-1]:
        caption_new = caption_new + ii + '\n'
    caption_new += word_list[-1]

    image = Image.open(filename)
    draw = ImageDraw.Draw(image)

    # Download the Font and Replace the font with the font file. 
    font = ImageFont.truetype('Arial.ttf', size=40)
    shadowcolor = "#000000"
    fillcolor = "#FFFFFF"
    w,h = draw.textsize(caption_new, font=font)
    W,H = image.size
    x,y = 0.5*(W-w),0.90*H-h

    # thin border
    # draw.text((x-1, y), caption_new, font=font, fill=shadowcolor)
    # draw.text((x+1, y), caption_new, font=font, fill=shadowcolor)
    # draw.text((x, y-1), caption_new, font=font, fill=shadowcolor)
    # draw.text((x, y+1), caption_new, font=font, fill=shadowcolor)

    # thicker border
    draw.text((x-1, y-1), caption_new, font=font, fill=shadowcolor)
    draw.text((x+1, y-1), caption_new, font=font, fill=shadowcolor)
    draw.text((x-1, y+1), caption_new, font=font, fill=shadowcolor)
    draw.text((x+1, y+1), caption_new, font=font, fill=shadowcolor)

    draw.text((x, y), caption_new, font=font, fill=fillcolor)

    image.save(filename)


# from PIL import Image, ImageDraw, ImageFont
 

# def drawText(text, filename):
#     img = Image.new('RGB', (1920, 1080), color = (73, 109, 137))
     
#     fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 100)
#     d = ImageDraw.Draw(img)
#     d.text((10,10), text, font=fnt, fill=(255, 255, 0))

#     img.save(filename)

# drawText('Hello World!', 'testing.jpg')
