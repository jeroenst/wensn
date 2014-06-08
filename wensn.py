#!/usr/bin/python
import sys
import usb.core
import time
import os


#assert dev is not None

#print dev

#print hex(dev.idVendor) + ', ' + hex(dev.idProduct)


while 1:
	peak = 0
	average = 0
	count = 0
	while count < 5 :
		try:
			dev = usb.core.find(idVendor=0x16c0, idProduct=0x5dc)
			ret = dev.ctrl_transfer(0xC0, 4, 0, 0, 200)

			dB = (ret[0] + ((ret[1] & 3) * 256)) * 0.1 + 30
		except:
			dB = 0
		average = average + dB
		if dB > peak:
			peak = dB
	
		count = count + 1

		f = open("/tmp/wensn_now.tmp", 'w')
		f.write(str(round(dB,1)))
		f.close()
		os.system("mv /tmp/wensn_now.tmp /tmp/wensn_now");
		
		time.sleep(1)
		

	#print dB
	#print peak

	average = average / 5
	
	f = open("/tmp/wensn_average.tmp", 'w')
	f.write(str(round(average,1)))
	f.close()

	f = open("/tmp/wensn_peak.tmp", 'w')
	f.write(str(round(peak,1)))
	f.close()

	os.system("mv /tmp/wensn_average.tmp /tmp/wensn_average");
	os.system("mv /tmp/wensn_peak.tmp /tmp/wensn_peak");

