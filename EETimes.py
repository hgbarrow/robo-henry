import robohenry, time

last_status = ""

while True:
	[EETitle, EELink] = robohenry.newsgrab.getEETimes()
	if last_status != EETitle:
		robohenry.tweetLink(EETitle, EELink)
		last_status = EETitle
	time.sleep(30)
	print last_status