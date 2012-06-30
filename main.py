#!/usr/bin/env python
# System information
import psutil
import datetime
import time
import airspeed

def RecordState():
	# Get the date and time
	now = datetime.datetime.now()

	# Open log file
	log = open('cpu.ministat', 'a')

	# Write our info.
	log.write(str(now.microsecond) + ',' + str(psutil.cpu_percent(interval=1))+'\n')
	log.close

def GenerateHTML(cpu, memory):
	t = airspeed.Template("""
	<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
	<html>
	 <head>
	    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	    <title>Flot Examples</title>
	    <link href="layout.css" rel="stylesheet" type="text/css">
	    <!--[if lte IE 8]><script language="javascript" type="text/javascript" src="../excanvas.min.js"></script><![endif]-->
	    <script language="javascript" type="text/javascript" src="jquery.js"></script>
	    <script language="javascript" type="text/javascript" src="jquery.flot.js"></script>

		<script type="text/JavaScript">
		<!--
		function timedRefresh(timeoutPeriod) {
			setTimeout("location.reload(true);",timeoutPeriod);
		}
		//   -->
		</script>

	 </head>
	    <body onload="JavaScript:timedRefresh(5000);">
	    <!--<h1>Memory</h1>
	    <div id="memory" style="width:600px;height:300px;"></div>--!>
	    <h1>CPU</h1>
	    <div id="cpu" style="width:600px;height:150px;"></div>

	<script id="source">
	$(function () {
	    var cpu = [
	#foreach ($r in $cpu)
	[$r.datestamp,$r.value],
	#end
	]; 

	    var memory = [
	#foreach ($r in $memory)
	[$r.datestamp,$r.value],
	#end
	]; 

	    $.plot($("#cpu"), [cpu], { xaxis: { mode: "time" }, line: { show: true } });

	    $.plot($("#memory"), [memory], { xaxis: { mode: "time" }, line: { show: true } });
	});
	</script>

	 </body>
	</html>
	""")
	#print t.merge(locals())

	log = open('out.html', 'w')
	log.write(t.merge(locals()))
	log.close()


def GetCPU():
	# Read from the log file, turn the CSV into an assiative array and pass it to the GenerateHTML function.
	print "Getting CPU informaion"

	rtn = []
	# Load in the CPU data.
	for line in  open('cpu.ministat', 'r'):
		data = line.split(',')
		rtn.append({'datestamp': data[0], 'value': data[1]})

	return rtn

def GetMemory():
	# Read from the log file, turn the CSV into an assiative array and pass it to the GenerateHTML function.
	print "Getting Memory information"
	return [{'datestamp': '969871', 'value': 34.6}, {'datestamp': '969871', 'value': 67.6},{'datestamp': '969871', 'value': 87.6} ]


# Main loop.
while True:
	# Get information.
	RecordState()
	# Sleep for 3s
	time.sleep(3)
	# Regenerate the HTML
	GenerateHTML(GetCPU(), GetMemory())