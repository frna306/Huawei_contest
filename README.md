# Huawei_contest
项目框架
project/  
├── main.py                 # 程序入口，交互控制  
├── geometry/               # 几何计算模块  
│   ├── __init__.py         # 模块导出  
│   ├── point.py            # 点/向量类  
│   ├── polygon.py          # 多边形数据结构  
│   ├── polygonB.py         # 优化版多边形B（相对坐标）  
│   ├── algorithms.py       # 几何判断算法  
│   └── nfp.py              # 临界多边形计算  
├── solver/                 # 求解模块  
│   ├── __init__.py         # 模块导出  
│   └── solve.py            # 单样本求解器  
├── tests/                  # 单元测试（待实现）  
└── utils/                  # 工具模块  
    ├── __init__.py         # 模块导出  
    ├── constants.py        # 全局常量  
    └── output.py           # 输出格式化  
