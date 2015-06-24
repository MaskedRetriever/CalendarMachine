import SvgLib
import datetime
import math

#SPR2015 3-29 - 6-13
#SUM2015 6-22 - 8-21
#AUT2016 9-30 - 12-18
#WIN2016 1-4 - 3-18
#SPR2016 3-28 - 6-10
#SUM2016 6-20 - 8-19

YMDStart = datetime.datetime(2015,9,27) #For now always start on the relevant Sunday
YMDEnd = datetime.datetime(2015,12,19)

pxW=850
pxH=1100


# Make SVG
calout = open("out.svg",'w')
SvgLib.svgWidth=pxW
SvgLib.svgHeight=pxH
calout.write(SvgLib.svgHeader())

for i in range(0,8):
	calout.write(SvgLib.svgLine(pxW*i/7,pxW*i/7,0,pxH))

total_days=(YMDEnd-YMDStart).days+1
daylist = []
for daynumber in range(total_days):
	day=(YMDStart+datetime.timedelta(days=daynumber)).date()
	daylist.append(day.day)

numweeks = math.ceil(total_days/7)

for i in range(0,int(numweeks)+1):
	y=i*pxH/numweeks
	calout.write(SvgLib.svgLine(0,pxW,y,y))
	
for i,daylabel in enumerate(daylist):
	y=math.floor(i/7)*(pxH/numweeks)
	x=i%7*(pxW/7)
	calout.write(SvgLib.svgText(x+4,y+20,str(daylabel)))
	if daylabel==1:
		calout.write(SvgLib.svgLine(x-1,x-1,y,y+pxH/numweeks))
	if daylabel<8:
		calout.write(SvgLib.svgLine(x,x+pxW/7,y+2,y+2))



calout.write(SvgLib.svgFooter())
calout.close()