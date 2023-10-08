"""
 在python中使用C/C++扩展
 参考：https://www.zhihu.com/question/369166918/answer/2464030553
"""


from setuptools import setup
from setuptools import Extension

setup(
    name="hello-lib",
    version="0.0.1",
    ext_modules=[Extension("_hello", ['hello.cpp'])]
)
