from ip_splitter import IPSplitter
import pprint

needed_bits = {"2": "1",
               "3": "2",
               "4": "2",
               "5": "3",
               "6": "3",
               "7": "3",
               "8": "3",
               "9": "4",
               "10": "4",
               "11": "4",
               "12": "4",
               "13": "4",
               "14": "4",
               "15": "4",
               "16": "4",
               "17": "5",
               "18": "5",
               "19": "5",
               "20": "5",
               "21": "5",
               "22": "5",
               "23": "5",
               "24": "5",
               "25": "5",
               "26": "5",
               "27": "5",
               "28": "5",
               "29": "5",
               "30": "5",
               "31": "5",
               "32": "5",
               "33": "6",
               "34": "6",
               "35": "6",
               "36": "6",
               "37": "6",
               "38": "6",
               "39": "6",
               "40": "6",
               "41": "6",
               "42": "6",
               "43": "6",
               "44": "6",
               "45": "6",
               "46": "6",
               "47": "6",
               "48": "6",
               "49": "6",
               "50": "6",
               }
ip = input("Enter network address with cidr(x.x.x.x/x): ")
ipsplit = ip.split("/")

needs = input("Enter number of subnets needed(max 50): ")
need_calc = int(needed_bits[needs])
prefix = need_calc + int(ipsplit[1])

s = IPSplitter(ip)

print(pprint.pformat(s.get_subnet(prefix, count=int(needs))))
