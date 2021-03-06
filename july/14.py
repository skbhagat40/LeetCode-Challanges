"""
Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.
"""
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        h = hour
        m = minutes
        if (h == 12): 
            h = 0
        if (m == 60): 
            m = 0
            h += 1; 
            if(h>12): 
                   h = h-12; 
          
        # Calculate the angles moved by  
        # hour and minute hands with  
        # reference to 12:00 
        hour_angle = 0.5 * (h * 60 + m) 
        minute_angle = 6 * m 
          
        # Find the difference between two angles 
        angle = abs(hour_angle - minute_angle) 
          
        # Return the smaller angle of two  
        # possible angles 
        angle = min(360 - angle, angle) 
          
        return angle
