class Solution:
    def alienOrder(self,words):
        #chars用于获取字母集合
        chars=set(''.join(words))
        print(chars)
        #用于存储入度
        degrees={x:0 for x in chars}
        from collections import defaultdict
        #用于存储优先级
        graph=defaultdict(list)
        #pair是从上到下两两匹对
        for pair in zip(words,words[1:]):
            print(pair)
            #x,y依次取出匹对的字母
            for x,y in zip(*pair):
                print(x,y)
                if x!=y:
                    #建立优先级关系
                    graph[x].append(y)
                    #入度增加1
                    degrees[y]+=1
                    break
        print(degrees)
        print(graph)
        queue=[]
        for i in chars:
            if degrees[i] == 0:
                queue.append(i)
        res=""
        while queue:
            x=queue.pop(0)
            res+=x
            for i in graph[x]:
                degrees[i]-=1
                if degrees[i]==0:
                    queue.append(i)
        return res*(set(res)==chars)

s=Solution()
print(s.alienOrder([
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]))


#### 深度优先

class Solution:
    def alienOrder(self,words):
        #chars用于获取字母集合
        chars=set(''.join(words))
        print(chars)
        #用于存储入度
        degrees={x:0 for x in chars}
        from collections import defaultdict
        #用于存储优先级
        graph=defaultdict(list)
        #pair是从上到下两两匹对
        for pair in zip(words,words[1:]):
            print(pair)
            #x,y依次取出匹对的字母
            for x,y in zip(*pair):
                print(x,y)
                if x!=y:
                    #建立优先级关系
                    graph[x].append(y)
                    #入度增加1
                    degrees[y]+=1
                    break
        print(degrees)
        print(graph)
        lis=[]
        for i in chars:
            if degrees[i] == 0:
                lis.append(i)
        res=""
        while lis:
            tmp=[]
            for ch in lis:
                res+=ch
                for c in graph[ch]:
                    degrees[c]-=1
                    if degrees[c]==0:
                        tmp.append(c)
                del graph[ch]
            lis=tmp
        return res if len(res)==len(chars) else ""

s=Solution()
print(s.alienOrder([
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]))