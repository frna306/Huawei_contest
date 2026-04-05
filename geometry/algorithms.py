from point import Point
from polygen import Polygon

def point_polygon_relation(point: Point, polygon: Polygon) -> int:
    """
    返回点与多边形的位置关系
    -1: 外部
     0: 边界上
     1: 内部
    """
    


def segment_intersection(p1: Point, p2: Point, p3: Point, p4: Point):
    """两条线段是否相交（含端点）"""
    # 实现跨立实验
    
def segment_distance(p1: Point, p2: Point, p: Point) -> Point:
    """点到线段的最短距离"""
    # 投影法实现

    
def is_point_on_segment(p: Point, a: Point, b: Point) -> bool:
    """点是否在线段上（含端点）"""
    # 叉积为0 + 点积范围判断


# 点到多边形的最短平移向量（关键！）
def point_to_polygon_min_vector(point: Point, polygon: Polygon) -> Point:
    """
    返回将点移出多边形的最短平移向量
    - 如果点在外部：返回 (0,0)
    - 如果点在内部/边界：返回移出边界的最短向量
    """
    relation = point_polygon_relation(point, polygon)
    if relation == -1:  # 外部
        return Point(0, 0)
    
    # 内部或边界：找到最近的边，返回垂直移出的方向
    min_dist = float('inf')
    closest_edge = None
    
    for start, end in polygon.edges:
        dist = point_segment_distance(point, start, end)
        if dist < min_dist - EPS:
            min_dist = dist
            closest_edge = (start, end)
    
    if closest_edge is None:
        return Point(0, 0)
    
    start, end = closest_edge
    # 计算垂直方向（向外）
    edge = end - start
    # 垂直向量（单位化）
    perp = Point(-edge.y, edge.x)  # 或 (edge.y, -edge.x)，需判断方向
    perp_len = math.hypot(perp.x, perp.y)
    if perp_len > EPS:
        perp = Point(perp.x / perp_len, perp.y / perp_len)
    
    # 确定向外方向（指向多边形外部）
    center = polygon_center(polygon)  # 多边形中心
    mid = Point((start.x + end.x)/2, (start.y + end.y)/2)
    outward = perp
    # 如果垂直方向指向内部，则取反
    if (mid + perp).distance_to(center) < mid.distance_to(center):
        outward = Point(-perp.x, -perp.y)
    
    # 返回平移向量 = 向外方向 * (min_dist + epsilon)
    return Point(outward.x * (min_dist + EPS), outward.y * (min_dist + EPS))
    
    