class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 依位置由大到小排序，配對 (位置, 速度)
        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
        prev_time = -1.0
        for pos, spd in cars:
            time = (target - pos) / spd
            if time > prev_time:   # 追不上前車，形成新車隊
                fleets += 1
                prev_time = time
            # 否則併入前面車隊（time <= prev_time）
        return fleets

