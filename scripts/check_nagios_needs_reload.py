#!/usr/bin/python
# Checks if nagios service needs a reload


try:
	import sys
	sys.path.append('/opt/pynag')
	
	from pynag.Parsers import config
	
	c = config(cfg_file='/etc/nagios/nagios.cfg')
	c.parse()
	result = c.needs_reparse()
	
	if result == True:
		print "Nagios configuration has changed since last restart"
		sys.exit(1)
	else:
		print "Nagios service has been restarted since last config change"
		sys.exit(0)
except Exception, e:
	print "Error running script: %s" % e
	sys.exit(3)
