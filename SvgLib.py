#! /usr/bin/python

FontSize=20
Color="Black"
LineWeight=3
svgWidth=400
svgHeight=400


def svgHeader():
	textout = '<svg xmlns="http://www.w3.org/2000/svg" version="1.1"'
	textout += ' width="' + str(svgWidth)
	textout += '" height="' +str(svgHeight)
	textout += '">\n'
	return textout

def svgFooter():
	return '</svg>'

def svgLine(x1=0,x2=0,y1=400,y2=400):
	textout = '<g stroke="' + Color + '">\n'
	textout += '<line x1="' + str(x1) \
		+ '" y1="' + str(y1) \
		+ '" x2="' + str(x2) \
		+ '" y2="' + str(y2) \
		+ '" stroke-width="' +str(LineWeight)+ '"/>\n'
	textout += '</g>'
	return textout

def svgText(x=200,y=200,inString="TEST"):
	textout = '<text x="'
	textout += str(x)
	textout += '" y="'
	textout += str(y)
	textout += '" font-family="Verdana" font-size="'
	textout += str(FontSize)
	textout += '">\n'
	textout += inString
	textout += "\n</text>\n"
	return textout

def main():
	#Test Image to default place:
	OFile = open("out.svg",'w')
	OFile.write(svgHeader())
	OFile.write(svgLine(200,400,200,200))
	OFile.write(svgText(200,200,"TESTING"))
	OFile.write(svgFooter())
	OFile.close()

if __name__ == "__main__":
	main()