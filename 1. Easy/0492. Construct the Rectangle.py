class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for largo in range(int(area**0.5), 0, -1):            
            if area % largo == 0: 
                return [area // largo, largo]
