from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import textwrap

FONT = 'verdanab.ttf'
#"verdanab.ttf"
def wallpaper(filename, title, text):
	im = Image.open(filename).convert('RGBA')
	
	lines = textwrap.wrap(text, width = 10, break_long_words = False)
	lines = text.splitlines()
	title_font = ImageFont.truetype(FONT, 32)
	text_font = ImageFont.truetype(FONT, 18)
	buff = 10
	ybuff = buff/2
	(xmax, ymax) = (0,0)
	for line in lines:
		(xtext, ytext) = text_font.getsize(line)
		xmax = max(xmax, xtext)
		ymax = max(ymax, ytext)

	txt = Image.new('RGBA', im.size, (255, 255, 255, 0))

	draw = ImageDraw.Draw(txt)
	(xim, yim) = im.size

	xcoord = xim - xtext - 2*buff
	ycoord = yim - ytext - 2*buff
	
	
	# Draw text
	for line in reversed(lines):
		(xtext, ytext) = text_font.getsize(line)
		xcoord = xim - xtext - 2*buff
		draw.rectangle([xcoord - buff, ycoord-buff, 
					xcoord + xtext + buff, ycoord+ytext+2*ybuff], (255, 255, 255, 140))
		draw.text((xcoord,ycoord),line, fill=(0, 0, 0, 255), font = text_font)
		
		ycoord-=(ymax+3*ybuff)
		
	# Draw title
	(xtitle, ytitle) = title_font.getsize(title)
	xct = xim - xtitle - 2*buff
	yct = ycoord - ytitle + ymax - 2*ybuff
	draw.rectangle([xct - buff, yct, xct + xtitle + buff, yct+ytitle+ybuff], 
					(255, 255, 255, 140))
	draw.text((xct,yct),title, fill=(0, 0, 0, 255), font = title_font)
	
	draw = ImageDraw.Draw(im)
	
	out = Image.alpha_composite(im, txt)
	outfile = filename[:len(filename)-4] + '.jpg'
	out.save(outfile, quality=80)
	return outfile
