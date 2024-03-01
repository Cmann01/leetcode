class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        altitude = [0]  # Initialize with starting altitude 0
        current_altitude = 0

        # Calculate altitudes using prefix sum
        for gain_value in gain:
            current_altitude += gain_value
            altitude.append(current_altitude)

        # Return the maximum altitude
        return max(altitude)
