#Script to change key parameters of sen2cor to recommended values.
#5 key parameters are changed to "AUTO" instead of a default value.

import lxml.etree as ET
import os

#Set directory
datadir = r'/home/user/'
os.chdir(datadir)

#Parse the xml
with open ('L2A_GIPP.xml') as myfile:
    tree = ET.parse(myfile)
root = tree.getroot()

#Loops at the root to look for elements and performs changes
print "1.NUMBER OF PROCESSES = AUTO - the processor determines the number of processes automatically, using cpu_count"
for i in root.iter('Nr_Processes'):
    i.text = i.text.replace('1', 'AUTO')

print "2.AEROSOL TYPE = AUTO"
for i in root.iter('Aerosol_Type'):
    i.text = i.text.replace('RURAL', 'AUTO')

print "3.CLIMATE = AUTO"
for i in root.iter('Mid_Latitude'):
    i.text = i.text.replace('SUMMER', 'AUTO')

print "4.CIRRUS CORRECTION = AUTO"
for i in root.iter('Cirrus_Correction'):
    i.text = i.text.replace('0', 'AUTO')

print "5.BRDF CORERCTION = AUTO"
for i in root.iter('BRDF_Correction'):
    i.text = i.text.replace('0', 'AUTO')

tree.write('L2A_GIPP.xml')







#q=''
#def main ():
#    q = 'quit'
#    command = raw_input('Processor/SceneMedianFilter/Aerosol/MidLatitude')
#    while command != q:
#        if command == Processor:
#            process= raw_input()
