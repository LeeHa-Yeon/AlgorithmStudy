'''
대소문자 구분 안함
캐시 교체 알고리즘은 LRU(Least Recently Used)를 사용한다.
hit -> 1
miss -> 5

LRU 알고리즘 :
가장 오랫동안 참조되지 않은 페이지를 교체하는 기법
=> 가장 오래동안 사용되지 않은 페이지는 앞으로도 사용할 확률이 적다는 가정 하에 사용된다.

페이지 교체 알고리즘은 페이징 기법으로 메모리를 관리하는 운영체제에서, 페이지 부재가 발생 하여 새로운 페이지를 할당하기 위해 현재 할당된 페이지 중 어느 것과 교체할지를 결정하는 방법입니다.

FIFO : 페이지가 주기억장치에 적재된 시간을 기준으로 교체될 페이지를 선정하는 기법
단점 : 중요한 페이지가 오래 있었다는 이유만으로 교체되는 불합리. 가장 오래 있었던 페이지는 앞으로 계속 사용될 가능성이 있음.

LFU : 가장 적은 횟수를 참조하는 페이지를 교체
단점 : 참조될 가능성이 많음에도 불구하고 횟수에 의한 방법이므로 최근에 사용된 프로그램을 교체시킬 가능성이 있고, 해당 횟수를 증가시키므로 오버헤드 발생

LRU : 가장 오랫동안 참조되지 않은 페이지를 교체
단점 : 프로세스가 주기억장치에 접근할 때마다 참조된 페이지에 대한 시간을 기록해야함. 큰 오버헤드가 발생

LRU 알고리즘 파이썬 예시 )
# cacheSize = 3
# reference = [4, 2, 3, 4, 5, 6, 5, 4, 7]
# cache = []
# for ref in reference:
#   if not ref in cache:
#     if len(cache) < cacheSize:
#         cache.append(ref)
#      else:
#         cache.pop(0)
#         cache.append(ref)
#   else:
#     cache.pop(cache.index(ref))
#     cache.append(ref)


캐시크기(cacheSize)	도시이름(cities)	실행시간
3	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]	50
3	["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]	21
2	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]	60
5	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]	52
2	["Jeju", "Pangyo", "NewYork", "newyork"]	16
0	["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]	25


'''

def solution(cacheSize, cities):
    cache = []
    answer = 0
    for city in cities :
        city=city.upper()
        if cacheSize == 0 :
            answer+=5
            continue
        if not city in cache :
            answer+=5
            if len(cache) < cacheSize :
                cache.append(city)
            else :
                cache.pop(0)
                cache.append(city)
        else :
            answer+=1
            cache.pop(cache.index(city))
            cache.append(city)

    return answer

print(solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))




