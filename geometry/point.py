# 支持向量运算（p1 + p2, p1 - p2, p * k 等）
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # 向量运算
    def __add__(self, other): ...
    def __sub__(self, other): ...
    def __mul__(self, k): ...
    
    # 点积、叉积（作为方法）
    def dot(self, other):
        return self.x * other.x + self.y * other.y
    
    def cross(self, other):
        return self.x * other.y - self.y * other.x
    
    # 距离
    def distance_to(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)
    
    def distance_sq(self, other):  # 避免开方，用于比较
        dx = self.x - other.x
        dy = self.y - other.y
        return dx*dx + dy*dy