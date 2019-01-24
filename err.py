#!/usr/bin/python3
import time
from selenium import webdriver


try:
	x=input("enter the first no.:")
	y=input("enter the second no.:")
	print (int(x)+int(y))

except:
	print("tumse na ho payega:")
	print (dir(time))
	print (time.sleep(5))
	browser=webdriver.Firefox()
	browser.get("https://www.google.com/search?client=firefox-b-ab&ei=DxJKXITZBMj5rQG50KfgAQ&q=calculator&oq=cal&gs_l=psy-ab.3.0.0i67l10.990.2698..4892...0.0..0.150.434.0j3......0....1..gws-wiz.....0..0.RwecN_Mh6sA")
