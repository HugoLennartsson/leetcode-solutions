class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        largest_altitude = 0
        current_altitude = 0

        if not gain:
            return 0
        
        for alt_gain in gain:
            current_altitude += alt_gain
            if current_altitude > largest_altitude:
                largest_altitude = current_altitude
        
        return largest_altitude