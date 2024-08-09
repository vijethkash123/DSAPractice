from collections import defaultdict, deque
from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        reversed_adj=defaultdict(list)
        terminal_leaves =set()  # set of nodes in ans 
        n =len(graph)
        outdegree=defaultdict(int)
        for i in range(n):
            c = 0
            for j in graph[i]:
                c += 1
                reversed_adj[j].append(i)  # reversing the direction of the edge , to find from which edges we can reach to a particular edge 
            outdegree[i] = c
            if c == 0:  # if the node is a terminal node 
                terminal_leaves.add(i)

        print(reversed_adj)
        print(outdegree)

        q = deque(terminal_leaves)
        while q:
            node = q.popleft()
            for nei in reversed_adj[node]:
                outdegree[nei] -= 1
                if outdegree[nei] == 0:
                    terminal_leaves.add(nei)
                    q.append(nei)
        
        
        return sorted(list(terminal_leaves))



print(Solution().eventualSafeNodes([[1,2],[2,3],[5,4],[0],[5],[],[]]))



# DFS Approach:
from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        terminal_nodes = set()
        visited = set()
        
        def dfs(node):
            nonlocal visited
            if node in terminal_nodes:  # safe node
                return 1
            if node in visited:  # cycle detected
                return 0
            visited.add(node)
            for nei in graph[node]:
                if not dfs(nei):
                    return 0
            visited.remove(node)
            terminal_nodes.add(node)
            return 1  
        
        res = []
        for i in range(len(graph)):
            if dfs(i):
                res.append(i)
        
        return sorted(list(set(res)))


print(Solution().eventualSafeNodes(graph = [[0,3],[4],[5,6,7,8],[0,4,6,8,9],[1],[1,6],[7,8,9],[8,9],[2,9],[]]))
print(Solution().eventualSafeNodes(graph = [[],[0,2,3,4],[3],[4],[]]))
print(Solution().eventualSafeNodes(graph = [[3,10],[5,6,14,16],[],[6,10,14,16,19],[16],[9,11,16,17],[8],[16,19],[10,13,16,17,18,19],[],[],[2,12,13,16],[],[1,14,16,17,18],[0,15,16,18,19],[17,19],[17,18,19],[18,19],[7,19],[]]))
print(Solution().eventualSafeNodes(graph = [[217,307,327,336,429],[],[105,241,309,461],[243,408,482],[185,263],[92,124,211,236,259],[42,199,239,284,298,322],[],[128],[24,369,499],[90],[228,269,363,384,401],[364],[108,142,407,428,466],[62,198,224,315],[175,218,252,395,456],[62,383],[100,150,211,290,296,373],[169],[122,150,250],[253],[37],[28,113,325],[122,376],[202,362],[],[37,199,228,350,432],[61,265],[145,279,459,469],[38,496],[217,219,241,266],[149,233,350],[67,105,138,238,457,471],[],[102],[124,330],[25],[355,387,480],[105,194,202,359],[292],[147,175,203,290,422,436],[288,356,497],[175,210,307,386],[34,182,186],[75,155,229,333],[371],[21,144,291,437,443],[239,366],[121,471],[143,250,265,421],[101,123,244,414],[20],[],[55,204,316,395,426,436],[133,180,251,405],[56,60,118,293,295,339],[169,209,210,256,277],[31,150],[369,424,429,438],[157,303,330,340],[226,243,268,342,408,432],[68,72,227,230,244,361],[131,193,234,341,376,443],[],[71,259,331,373,491],[105,224,261,297,324,472],[83],[],[308],[184,188,265,269,327],[205,413],[156,298,348,394],[91,102,214,332],[109,175,234,258],[],[98,315,328,494],[236,237,351],[],[],[155,342,453,470,485,494],[124,145,203,322,405,465],[75,275,310,474,484,493],[128,138,178,297,326,476],[162,490],[110,292],[105,272],[369,452],[105,198],[129,389,429,462,471],[482,491],[235,263,281,294,473],[301,418,419],[101,191,222],[94],[146,354,466,469,489],[261,335,377,404,498],[],[143,177,318,369,471],[],[149],[404,418],[347],[123,238,256,434],[155,170,310,489],[169,267,302],[304,330,464,476,491],[327,468],[151,313,497],[189,368,414,427],[154,259,281,282,283,441],[194,318,353,419],[401],[126,136,229,249,388],[121,132,458,459],[189,220,265,388,405],[217,264,286,313,412],[227,491],[492],[130,266,281,370],[315,369,374,392,483],[88,175,479,486],[305,368,465],[98,165],[219,268,292,484],[138,173,232,272,358,395],[146,210,338],[364,436,498],[196,252,307,490,498],[403],[160,203,247,303,459],[216,217,237,289,325],[],[140,292,320,342],[142,145,147,342],[],[153,189,194,256,268],[240],[181,184,236,422,444],[179,183,192,213,371,428],[187],[144,229,240,251,292,460],[277,477],[191,215,231,319,355],[181,274,333,372,375],[169,352,372,447,448,495],[321,352,366],[190,271,316],[166,355,390,454],[420,490],[181,340],[334,403,408,431,439,466],[60,180,181,375],[235,307,387],[304,326,404,420,491,496],[242,443],[196,252],[163,430],[159,360,484,491,499],[477],[318,362,417],[389,425,470],[219,222,301,421,454],[392],[171,228,279,318,416],[404],[],[203,264,320,483],[235,263],[185,275],[239,245],[208,308,358,394,401,484],[219,222,263,448],[185,432,449,463,470],[193,252,308,370],[77,294,298,388,441],[261],[207,468],[417,441],[211],[261,313,323,359,434,456],[267,352,451,459],[246,391,464,467,493],[],[282,410,415,486],[196,251,279,289,473,482],[],[493],[219,445],[134,254,291,360,362,408],[265,456],[116,434],[264,292,459,472],[318,466],[196,228,270,320,435,449],[252,309,361,390,399,426],[390,398,488,491],[363],[362,451],[312,315,421,448],[447],[218,285,435],[224],[352,431],[206,212,213,267,306,403],[260,390,461,465,470],[],[339,416],[235,249,307,488],[379,429,436],[225,231,320],[242,300,314,361,441,463],[292],[],[289,319,369,498],[266],[249,300,367,426,447,479],[232,257,297,412],[243,382,410,446],[313,429],[345,348,403,480,491],[333,415,428,444],[],[356,469],[224,243,332,477,487],[24,476],[302,471],[249,276,455],[471],[248,369,495],[413,448,472],[292,298,329,377,434],[341,361,406,407,490,495],[288,383,466],[],[287,349,497],[],[353,407,419,462],[238],[279,404],[302,338,340,346],[277,335,377,407,443,497],[255,257,412,413,451],[340,346,388,478,494],[259],[276,286,382,492],[254,305,351,394,416,492],[295,341,433],[],[490],[283,456,467,472,490],[167,433],[420,447,452,477],[277,349,403,426],[290,407],[331,340,345,355,435,491],[298,335,376,460,477],[279,356,389,407,410,486],[268,308,458,498],[264,313,442,464,488],[361,467,496],[311,372,406,423],[],[295,420,490],[431],[381,388,462],[396],[408],[378,458],[],[403,474],[288,315,351,353,359,408],[328],[333,342,465],[281,287,408,454],[321,330,399,407,426,459],[321,390,489,499],[340,401,456,463,472,488],[281,367],[280,286,327,392,441,496],[281,287,365,414,425,438],[304,375,386,410,430,447],[298],[322,392,442,490],[],[336,338,376,431],[314,386,418,493],[303,306,334,436],[311,495],[100,348,477,479],[],[320],[7,382],[303,358],[343,388],[324,350,357,372,480],[],[499],[326,428,451],[369,403,455],[357,390,494],[330,336,361,415,418,428],[321,368,414],[328,441],[351,483],[345,378,432,480,487,498],[366],[309,410],[313,339,370,422,486,494],[365,389,454,479],[0,403,478],[347,388,456],[],[353,400,474,492],[],[404,467],[386],[363,494],[349],[431,468],[],[400],[458],[377,419,487],[351],[330,348,376,423,452],[344,346,432,488],[383,427],[379,394,399,406,456,495],[394,399,422,429],[342],[345,474],[402,439,471,486],[494],[357,360,403,442,461,496],[374],[352,393,406,442,471],[356,364,407,412,434,478],[354,371,394,409,435,438],[339,439,467],[369,386,400],[342,376,380,422,448,453],[359,360],[374],[391,459,469,480,494],[450,477],[362,386,427,446,482],[370,384,386,397,482],[459],[411,498],[],[414],[367,404,431,461,483,484],[371,381,419,437,444,473],[357,419,422,426,461],[375,388],[448],[],[365,380],[376,385,386],[405],[375,455,464,469,484],[401,497],[],[381,417,469,489],[477],[384,392,426,449,454],[370,413,456],[410,465],[364,389,433,450,491],[],[306,379,400,410,435,436,479],[381,390,484],[377,402,441,484,493],[388,395,421,489],[107,413,434,470,495],[377,399,422],[430,437],[386,399,402,468,495],[410,422,430,481,499],[403,414,472,488,493],[435,462,464,474,476],[396,419,432,449,474,476],[415,426,434,454,494],[],[225],[423,434,454,455,465,477],[392,421],[391,400,407,425],[],[395,418,439,454,458,495],[420,430,479,485],[],[395,409,441,451,463,480],[407,496],[410,412,423,453],[402,456,462,472],[428,457,464,471],[432,438,454,485],[],[437,490,496],[436,439,444,459,478],[444,449,450,491],[374,405,407,428,472,487,499],[307,434,450,494],[405,407,459,467],[416,443,468,480,484],[410,471,486],[],[],[413,414,424,454,457,483],[],[423,433,492],[487],[445,447,458,497],[480],[],[436,466,489],[419,437,495],[497],[435,458,470],[438,469,475],[427,431,471],[436,437,463,464],[428,444,445,460,465,496],[],[450,453,480],[449,460,462],[431,435,440,459,464,465],[475,480,483,489,498],[],[433,466,479],[],[362,464,476],[449,468,486,498],[],[449,483,493,497],[],[467],[442,466,472,482],[448,453,460,465,468,493],[490],[463,465,468,491,493,497],[447,452,463,466],[470,481],[445,458,465,472,482,499],[479],[465,476,482,491,494],[458,469],[454,459,478],[466,469,482,484],[458,466,469,470,497],[461,470,478,480,483,497],[478,487,490,496],[461,480,495,496],[462,480,494],[462,473,475,477,484,497],[469,490],[],[485,486,491,497],[472,480,481],[24,461,463,466,474,490],[486],[476,479,485,492,493],[465,475,477,478],[477],[],[473,485,491,492,494,498],[472,485,499],[479,491],[498],[471,481,482,485,494,499],[476,478,499],[475],[476,477,495],[478,484,491,494],[478],[482,486],[479,485,490,494,496,497],[490],[481,482,494,495,496,499],[484,489,490,492,495,496],[483,488,494],[483,486,490,492,495,498],[484,487,489,492,493,497],[499],[492,493,496],[494,495,496],[488,489,491,494,496,499],[493,495],[490,492,493,494,498],[493,496,497,498],[492,493,494,495,497,498],[494,495,496,497,498],[494,495,496,497,498,499],[495,496,497,498,499],[496,497,498,499],[],[498,499],[499],[]]))