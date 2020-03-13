from ipaddress import ip_address
from ipaddress import ip_network
from ipaddress import summarize_address_range

#
# Þetta má nota til að smíða lista af IP tölum út frá CIDR formi
# þ.e. 10.0.20.0/24 í þessu tilfelli
#
cidr = "10.0.20.0/24"
nw = ip_network(cidr)
print(nw)
for ip in nw:
	print(str(ip))

#
# Þetta má nota til að smíða lista af IP tölum út frá netrange þ.e. 
# 10.0.20.10 til 10.0.20.50 i þessu dæmi.
#
for r in summarize_address_range(ip_address("10.0.20.10"), ip_address("10.0.20.50")):
	nw = ip_network(r)
	for ip in nw:
		print(str(ip))

