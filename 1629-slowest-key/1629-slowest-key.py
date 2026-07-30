class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        result = keysPressed[0]
        max_dur = releaseTimes[0]
        for i in range(1, len(releaseTimes)):
            dur = releaseTimes[i] - releaseTimes[i-1]
            if dur > max_dur or (dur == max_dur and keysPressed[i] > result):
                max_dur = dur
                result = keysPressed[i]
        return result