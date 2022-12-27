import redis

r = redis.Redis(host='192.168.1.129', port=7001)

print(r.hget("order:10", "amount"))
print(r.exists("order:0"))
print(r.exists("order:1"))
print(r.hkeys("order:1"))
print(r.keys())
for key in r.keys():
    print(r.hvals(key))

d = {'market': 'ADA-EUR', 'orderType': 'limit', 'amount': '270', 'price': '0.55', 'onHold': '270'}
r.hset("order", 'market', d['market'])
