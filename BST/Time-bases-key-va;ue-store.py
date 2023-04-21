class TimeMap:

    def __init__(self):
        self.ddict = {} # key: [[val, timestamp], [val, timestamp]...] 

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.ddict:
            self.ddict[key] = []
        self.ddict[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.ddict.get(key, [])
        l, r = 0, len(values)-1

        while l<=r:
            m = (l+r)//2
            if values[m][1] <= timestamp:
                res = values[m][0] # Doing this also for lesser than case, because we want to return the closest `prev_timestamp` in case if exact match of timestamp is not found. This will also store result in case match is found
                l = m+1
            else:
                r = m-1
        return res

# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
key,value,timestamp = "love","high",10
obj.set(key,value,timestamp)

key,value,timestamp = "love","low",20
obj.set(key,value,timestamp)

print(obj.get("love",5))
print(obj.get("love",10))
print(obj.get("love",15))
print(obj.get("love",20))
print(obj.get("love",25))

