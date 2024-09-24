class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=sorted(zip(position,speed),reverse=True)
        fleet=0
        currTime=0
        for pos,spd in cars:
            time=(target-pos)/spd
            if time>currTime:
                fleet+=1
                currTime=time
        return fleet
