#!/usr/bin/env python
# System information
import psutil
import datetime

import airspeed

def RecordState():
	# Get the date and time
	now = datetime.datetime.now()

	# Open log file
	log = open('out.ministat', 'a')

	# Write our info.
	log.write('['+str(now.microsecond)+','+str(psutil.cpu_percent(interval=1))+'],\n')
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
	 </head>
	    <body>
	    <h1>Memory</h1>
	    <div id="memory" style="width:600px;height:300px;"></div>
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

	    $.plot($("#cpu"), [cpu], { xaxis: { mode: "time" }, points: { show: true } });

	    $.plot($("#memory"), [memory], { xaxis: { mode: "time" }, bars: { show: true } });
	});
	</script>

	 </body>
	</html>
	""")
	cpu = [{'datestamp': '969871', 'value': 1.6}, {'datestamp': '969871', 'value': 2.6},{'datestamp': '969871', 'value': 3.6} ]
	memory = [{'datestamp': '969871', 'value': 34.6}, {'datestamp': '969871', 'value': 67.6},{'datestamp': '969871', 'value': 87.6} ]
	#print t.merge(locals())

	log = open('out.html', 'w')
	log.write(t.merge(locals()))
	log.close()


def GetCPU():
	# Read from the log file, turn the CSV into an assiative array and pass it to the GenerateHTML function.
def GetMemory():
	# Read from the log file, turn the CSV into an assiative array and pass it to the GenerateHTML function.
	
# [969871,1.6],
# [540776,1.8],
# [55344,1.1],
# [566065,2.6],
# [258297,2.1],
# [649793,2.8],
# [451371,1.2],
# [80818,3.5]