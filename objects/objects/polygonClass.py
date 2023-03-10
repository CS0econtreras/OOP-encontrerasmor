from typing import List, Tuple
class convex_polygon(object):
    '''Class that calculates the area of a convex polygon'''
    def __init__(self) -> None:
        self._vertices_amount:int = 0
        self._vertex_pairs:List[Tuple[int,int]] = []
        self.n1: float = 0.0
        self.n2: float = 0.0
        self.n3: float = 0.0

    def set_area(self, vert_count: int, vert_pairs:List[Tuple[int,int]]) -> None:
        '''Calculates the area of the polygon'''
        self._vertex_pairs = vert_pairs
        self._vertices_amount = vert_count

        j = self._vertices_amount - 1
        for i in range(0, self._vertices_amount):
            self.n1 = (self._vertex_pairs[j][0] + self._vertex_pairs[i][0])
            self.n2 = (self._vertex_pairs[j][1] - self._vertex_pairs[i][1])
            self.n3 += (self.n1 * self.n2)
            j = i
        self.n3 = abs(self.n3 / 2)

    def get_area(self) -> float:
        '''Returns the area of the polygon'''
        return self.n3