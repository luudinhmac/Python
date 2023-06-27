from lib import filter, filter2
import sys
request="http://localhost:81/DVWA/vulnerabilities/xss_r/?name=<script>alert(document.cookie)</script>"

print(filter(request))
print(filter2(request))
print(sys.path)
