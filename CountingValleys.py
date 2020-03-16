s = "UDDDUDUU"
time = 0
sealevel = 0
for i in range(len(s)):
	if s[i]=='U':
		sealevel += 1
	else:
		sealevel -= 1
	if(sealevel == 0 and s[i]=='U'):
		# whenever the valley is present the person should always step up to reach the sea level
		time += 1
print(time)
