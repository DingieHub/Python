# Bitvavo API documentation: https://github.com/bitvavo/python-bitvavo-api#get-orders-open

from python_bitvavo_api.bitvavo import Bitvavo
from tabulate import tabulate

APIKEY = 'd73247b8143a711f44444124ddb61285f7be0025fd9ff50f794bd80e4dbea6cf'
APISECRET = 'e74f66b769b3809f482e584c3d3b3aff2751792bdc962971f8745f538e730206176e92e20d6791b77777821818628a74e120eca3d53a9baac1f9b2c4d2a01141'
HEADERS = ['market', 'amount', 'price', 'onHold', 'orderType']

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def FilterKeys(d, filter_in):
  d_accent = {}
  for key in d:
    if key in filter_in:
      d_accent[key] = d[key]
  
  return d_accent

def GetSubTotal(d, key, total):
  return float(d[key]) + total

#===================================
bitvavo = Bitvavo({'APIKEY': APIKEY, 'APISECRET': APISECRET})
# response = bitvavo.balance({})

# if type(response) == dict:
#   print(response.keys())

# for item in response:
#   print(item)
#   if item == 'errorCode':
#     print(response['errorCode'])

#   if item == 'error':
#     print(response['error'])

target_list = HEADERS
response = bitvavo.ordersOpen({})
print(response)
#newlist = sorted(list_to_be_sorted, key=lambda d: d['name'])
table = sorted(response, key=lambda d: d['market'])
target_table_buy = []
target_table_sell = []
total_buy = 0
total_sell = 0
if type(response) == list:
  target_table = []
  for table_row in table:
    d = FilterKeys(table_row, HEADERS) #{}
    #target_table_buy.append(d) if (table_row['side'] == 'buy') else target_table_sell.append(d)
    if table_row['side'] == 'buy':
      target_table_buy.append(d)
      total_buy = GetSubTotal(d, 'onHold', total_buy)
    elif table_row['side'] == 'sell':
      target_table_sell.append(d)
      total_sell = GetSubTotal(d, 'onHold', total_sell)

target_dict = {'limit:buy': target_table_buy, 'limit:sell': target_table_sell}
print(bcolors.OKGREEN)
print(tabulate(target_table_buy, headers="keys"))
print("Total: " + str(total_buy))
print(bcolors.FAIL)
print(tabulate(target_table_sell, headers="keys"))
print("Total: " + str(total_sell))

#close with setting color back to normal (HEADERS?)
print(bcolors.ENDC)

print(target_dict)
