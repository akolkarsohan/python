import re

total_bites=32
final_ip_number_per_region=[]

with open("ip-ranges.json") as origin_file:
  for line in origin_file:
      if "ip_prefix" in line:
#        print (line)
        cidr_prefix=line[-5:-3]
#        print (cidr_prefix)
        total_ip_addresses=pow(2, (total_bites - int(cidr_prefix)))
#        print(total_ip_addresses)
        final_ip_number_per_region.append(total_ip_addresses)
      if "region" in line:
        line.split(":",1)[1]

#  print(final_ip_number_per_region)
  
final_number_per_all_regions = sum(final_ip_number_per_region)
