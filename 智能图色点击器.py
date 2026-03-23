
import importlib.metadata
import subprocess



#通过环境变量 设置 源 
import os
import sys
if 'PIP_INDEX_URL' not in os.environ:os.environ['PIP_INDEX_URL'] = 'https://pypi.mirrors.ustc.edu.cn/simple/'
三方库 = [
    'numpy',
    'pillow',
    'pygame',
    # 'Nuitka'
    ]
for i in 三方库:
    try:
        importlib.metadata.version(i)
    except importlib.metadata.PackageNotFoundError:
        print(f"缺少{i}库, 正在自动安装...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', i])


exit()





import time
import ctypes
from ctypes import wintypes
import _thread
import struct
import traceback
import os
import sys
import atexit
import weakref
from functools import wraps


import subprocess
try:
    import numpy as np # type: ignore
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--index-url', 'https://mirrors.aliyun.com/pypi/simple/', 'numpy'])
    import numpy as np # type: ignore






import numpy as np
from PIL import Image
import pygame
import sys













import numpy as np
from PIL import Image
import pygame
import Nuitka






class 脚本工具():
    def __init__(self):
        pass
    class _方法增强:
        def __init__(self, 方法):
            self.方法 = 方法
            self.实例缓存 = weakref.WeakKeyDictionary()
            @wraps(方法)
            def 类包装函数(*参数, **关键字参数):
                return self.方法(self.类, 类包装函数, self.方法, *参数, **关键字参数)
            类包装函数.__原函__ = self.方法
            self.类包装函数 = 类包装函数
            self.锁 = _thread.allocate_lock()
        def __get__(self, 实例, 类) -> callable:
            with self.锁:
                if 实例 is not None:
                    if 实例 not in self.实例缓存:
                        @wraps(self.方法)
                        def 实例包装函数(*参数, **关键字参数):
                            return self.方法(实例, 实例包装函数,self.方法, *参数, **关键字参数)
                        实例包装函数.__原函__ = self.方法
                        self.实例缓存[实例] = 实例包装函数
                    return self.实例缓存[实例]
                self.类 = 类
                return self.类包装函数
    @_方法增强
    def _动态属性化(主体, 包函, 原函, 类型, **属性):
        class 动态属性化(类型):
            def __new__(cls, *args, **kwargs):
                对象 = super().__new__(cls, *args, **kwargs)
                对象.__dict__.update(属性)
                return 对象
            def __setattr__(self, name, value):
                self.__dict__[name] = value
            def __getattr__(self, name):
                return self.__dict__[name]
            def __delattr__(self, name):
                del self.__dict__[name]
        return 动态属性化
    @_方法增强
    def _DPI感知(主体, 包函, 原函, 感知级别=2):

        if not hasattr(原函, '_DPI感知级别') or 原函._DPI感知级别!= 感知级别:
            if not hasattr(原函, '锁'):原函.锁 = _thread.allocate_lock()
            with 原函.锁:
                原函._DPI感知级别 = 感知级别
                返回值 = ctypes.windll.shcore.SetProcessDpiAwareness(感知级别)
                if 返回值 < 0:
                    错误码 = ctypes.get_last_error()
                    del 原函._DPI感知级别
                    raise ctypes.WinError(错误码, f"SetProcessDpiAwareness API调用失败, 返回值{返回值}, 错误码{错误码}")

        return 原函._DPI感知级别
    


    @_方法增强
    def 窗口矩形(主体, 包函, 原函, 窗口句柄: int)->tuple[int:'窗口矩形.left', int:'窗口矩形.top', int:'窗口矩形.right', int:'窗口矩形.bottom']:
        主体._DPI感知()
        # if not hasattr(cls, '_工作区宽度'):cls._工作区宽度 = ctypes.windll.user32.GetSystemMetrics(16)
        # if not hasattr(cls, '_工作区高度'):cls._工作区高度 = ctypes.windll.user32.GetSystemMetrics(17)
        # if not hasattr(cls, '_屏幕宽度'):cls._屏幕宽度 = ctypes.windll.user32.GetSystemMetrics(0)
        # if not hasattr(cls, '_屏幕高度'):cls._屏幕高度 = ctypes.windll.user32.GetSystemMetrics(1)
        if not hasattr(原函, '_GetWindowRect'): 
            原函._GetWindowRect = ctypes.windll.user32.GetWindowRect
            原函._GetWindowRect.argtypes = [wintypes.HWND, ctypes.POINTER(wintypes.RECT)]
            原函._GetWindowRect.restype = wintypes.BOOL
        窗口矩形 = wintypes.RECT()
        返回值 = 原函._GetWindowRect(窗口句柄, ctypes.byref(窗口矩形))
        if 返回值 != 0:
            return (窗口矩形.left, 窗口矩形.top, 窗口矩形.right, 窗口矩形.bottom)
        else:
            错误码 = ctypes.get_last_error()
            raise ctypes.WinError(错误码, f"GetWindowRect API调用失败, 窗口句柄{窗口句柄}, 返回值{返回值}, 错误码{错误码}")
    @classmethod
    def 窗口类名(cls, 窗口句柄: int):
        if not hasattr(cls, '_GetClassName'): 
            cls._GetClassName = ctypes.windll.user32.GetClassNameW
            cls._GetClassName.argtypes = [wintypes.HWND, wintypes.LPWSTR, wintypes.INT]
            cls._GetClassName.restype = wintypes.INT
        类名 = ctypes.create_unicode_buffer(257)#类名最多为256个字符, 加1个null结尾
        返回值 = cls._GetClassName(窗口句柄, 类名, 257)
        if 返回值 != 0 :
            return 类名.value
        else:
            错误码 = ctypes.get_last_error()
            raise ctypes.WinError(错误码, f"GetClassName API调用失败, 窗口句柄{窗口句柄}, 返回值{返回值}, 错误码{错误码}")
    @classmethod
    def 窗口标题(cls, 窗口句柄: int):
        if not hasattr(cls, '_GetWindowText'): 
            cls._GetWindowText = ctypes.windll.user32.GetWindowTextW
            cls._GetWindowText.argtypes = [wintypes.HWND, wintypes.LPWSTR, wintypes.INT]    
            cls._GetWindowText.restype = wintypes.INT
        标题 = ctypes.create_unicode_buffer(256)
        返回值 = cls._GetWindowText(窗口句柄, 标题, 256)
        if 返回值:
            return 标题.value
        else:
            错误码 = ctypes.get_last_error()
            if 错误码 == 0:
                return None
            raise ctypes.WinError(错误码, f"GetWindowText API调用失败, 窗口句柄{窗口句柄}, 返回值{返回值}, 错误码{错误码}")
    @classmethod
    def 坐标查找窗口(cls, 屏幕坐标):
        cls._DPI感知()
        if not hasattr(cls, '_WindowFromPoint'): 
            cls._WindowFromPoint = ctypes.windll.user32.WindowFromPoint
            cls._WindowFromPoint.argtypes = [wintypes.POINT]
            cls._WindowFromPoint.restype = wintypes.HWND
        if not hasattr(cls, '_GetAncestor'): 
            cls._GetAncestor = ctypes.windll.user32.GetAncestor
            cls._GetAncestor.argtypes = [wintypes.HWND, wintypes.UINT]
            cls._GetAncestor.restype = wintypes.HWND
        _POINT = wintypes.POINT(屏幕坐标[0],屏幕坐标[1])
        窗口句柄 = cls._WindowFromPoint(_POINT)
        if 窗口句柄:
            窗口句柄 = cls._GetAncestor(窗口句柄, 2)
            if 窗口句柄:
                return 窗口句柄
            else:
                错误码 = ctypes.get_last_error()
                raise ctypes.WinError(错误码, f"GetAncestor API调用失败, 窗口句柄{窗口句柄}, 返回值{窗口句柄}, 错误码{错误码}")
        else:
            错误码 = ctypes.get_last_error()
            raise ctypes.WinError(错误码, f"WindowFromPoint API调用失败, 屏幕坐标{屏幕坐标}, 返回值{窗口句柄}, 错误码{错误码}")
    @classmethod
    def 进程标识符(cls, 窗口句柄: int):
        if not hasattr(cls, '_GetWindowThreadProcessId'): 
            cls._GetWindowThreadProcessId = ctypes.windll.user32.GetWindowThreadProcessId
            cls._GetWindowThreadProcessId.argtypes = [wintypes.HWND, ctypes.POINTER(wintypes.DWORD)]
            cls._GetWindowThreadProcessId.restype = wintypes.DWORD
        进程ID = wintypes.DWORD()
        返回值 = cls._GetWindowThreadProcessId(窗口句柄, ctypes.byref(进程ID))
        if 返回值 != 0:
            return 进程ID.value
        else:
            错误码 = ctypes.get_last_error()
            raise ctypes.WinError(错误码, f"GetWindowThreadProcessId API调用失败, 窗口句柄{窗口句柄}, 返回值{返回值}, 错误码{错误码}")
    @classmethod
    def 进程路径(cls, 进程PID: int):
        if not hasattr(cls, '_OpenProcess'): 
            cls._OpenProcess = ctypes.windll.kernel32.OpenProcess
            cls._OpenProcess.argtypes = [wintypes.DWORD, wintypes.BOOL, wintypes.DWORD]
            cls._OpenProcess.restype = wintypes.HANDLE
        if not hasattr(cls, '_QueryFullProcessImageName'): 
            cls._QueryFullProcessImageName = ctypes.windll.kernel32.QueryFullProcessImageNameW
            cls._QueryFullProcessImageName.argtypes = [wintypes.HANDLE, wintypes.DWORD, wintypes.LPWSTR, ctypes.POINTER(wintypes.DWORD)]
            cls._QueryFullProcessImageName.restype = wintypes.BOOL
        进程句柄 = cls._OpenProcess(0x1000, False, 进程PID)
        if 进程句柄:
            初始长度 = 260
            路径 = ctypes.create_unicode_buffer(初始长度)
            路径长度 = wintypes.DWORD(初始长度)
            返回值 = cls._QueryFullProcessImageName(进程句柄, 0, 路径, ctypes.byref(路径长度))
            if 返回值 == 0:
                错误码 = ctypes.get_last_error()
                if 错误码 == 122:  # ERROR_INSUFFICIENT_BUFFER
                    实际所需长度 = 路径长度.value
                    路径 = ctypes.create_unicode_buffer(实际所需长度)
                    路径长度 = wintypes.DWORD(实际所需长度)
                    返回值 = cls._QueryFullProcessImageName(进程句柄, 0, 路径, ctypes.byref(路径长度))
                    if 返回值:
                        return 路径.value
                raise ctypes.WinError(错误码, f"QueryFullProcessImageName失败, 进程PID{进程PID}")
            return 路径.value
        else:
            错误码 = ctypes.get_last_error()
            raise ctypes.WinError(错误码, f"OpenProcess失败, 进程PID{进程PID}")
    @classmethod
    def 鼠标位置(cls):
        cls._DPI感知()
        if not hasattr(cls, '_GetCursorPos'): 
            cls._GetCursorPos = ctypes.windll.user32.GetCursorPos
            cls._GetCursorPos.argtypes = [ctypes.POINTER(wintypes.POINT)]
            cls._GetCursorPos.restype = wintypes.BOOL
        _POINT = ctypes.wintypes.POINT()
        返回值 = cls._GetCursorPos(ctypes.byref(_POINT))#获取光标/鼠标位置
        if 返回值 != 0:
            return (_POINT.x, _POINT.y)
        else:
            错误码 = ctypes.get_last_error()
            raise ctypes.WinError(错误码, f"GetCursorPos API调用失败, 返回值{返回值}, 错误码{错误码}")


    @_方法增强
    def 线程池(主体, 包函, 原函, 线程函数, *线程参数, **线程选项) -> dict['线程状态':bool, '异常信息':str, '返回值':object, '线程函数':callable, '线程参数':tuple, '线程标识符':int]:
        if not hasattr(原函, '_线程池'): 原函._线程池 = {}
        线程信息 = {'线程状态':True, '异常信息':None, '返回值':None, '线程函数':线程函数, '线程参数':(线程参数,线程选项), '线程标识符':None}
        def _线程(线程函数,线程参数,线程选项):
            # 线程标识符 = _thread.get_ident()
            # 线程信息['线程标识符'] = 线程标识符
            原函._线程池[线程标识符] = 线程信息
            try:
                返回值 = 线程函数(*线程参数,**线程选项)
                线程信息['线程状态'] = False
                线程信息['返回值'] = 返回值
            except BaseException:
                线程信息['异常信息'] = traceback.format_exc()
                线程信息['线程状态'] = False
                raise
            finally:
                del 原函._线程池[线程标识符]
        线程标识符 = _thread.start_new_thread(_线程, (线程函数,线程参数,线程选项))
        线程信息['线程标识符'] = 线程标识符
        return 线程信息
    class 双端队列():
        def __init__(self):
            self.左队列 = []
            self.右队列 = []
            self.左指针 = -1
            self.右指针 = -1
            self.双端队列长度 = 0
            self.锁 = _thread.allocate_lock()
        def __len__(self):
            return self.双端队列长度
        def __repr__(self):
            队列 = []
            with self.锁:
                for i in range(len(self.左队列)-self.左指针-1):
                    队列.append(self.左队列[-i-1])
                for i in range(len(self.右队列)-self.右指针-1):
                    队列.append(self.右队列[i])
            return str(队列)
        def __getitem__(self, 索引):
            def 索引转化(索引):
                with self.锁:
                    左队列有效元素 = len(self.左队列) - self.左指针 - 1
                    右队列有效元素 = len(self.右队列) - self.右指针 - 1
                    if 0 <= 索引 < 左队列有效元素:
                        元素 = self.左队列[-索引-1]
                        return 元素
                    elif 左队列有效元素 <= 索引 <= self.双端队列长度:
                        元素 = self.右队列[索引-左队列有效元素]
                        return 元素
                    elif -右队列有效元素 <= 索引 < 0:
                        元素 = self.右队列[索引]
                        return 元素
                    elif -self.双端队列长度 <= 索引 < -右队列有效元素:
                        元素 = self.左队列[-右队列有效元素-索引-1]
                        return 元素
                    else:
                        raise IndexError("索引超出范围")
            if isinstance(索引, int):
                返回值 = 索引转化(索引)
                return 返回值
            elif isinstance(索引, slice):
                队列 = []
                步长 = 1 if 索引.step is None else 索引.step
                双端队列长度 = self.双端队列长度
                开始 = (0 if 步长 > 0 else 双端队列长度-1) if 索引.start is None else (双端队列长度+索引.start if 索引.start < 0 else 索引.start)
                结束 = (双端队列长度 if 步长 > 0 else -1) if 索引.stop is None else (双端队列长度+索引.stop if 索引.stop < 0 else 索引.stop)
                for i in range(开始, 结束, 步长):
                    队列.append(索引转化(i))
                返回值 = 队列
                return 返回值
            else:
                raise TypeError("索引必须是整数或切片")
        def 左入队(self, 元素):
            with self.锁:
                self.双端队列长度 += 1
                self.左队列.append(元素)
        def 右入队(self, 元素):
            with self.锁:
                self.双端队列长度 += 1
                self.右队列.append(元素)
        def 左出队(self):
            with self.锁:
                if self.左指针+1 < len(self.左队列):
                    self.双端队列长度 -= 1
                    元素 = self.左队列.pop()
                    return 元素
                elif self.右指针+1 < len(self.右队列):
                    self.双端队列长度 -= 1
                    self.右指针 += 1
                    if self.右指针 > 99:
                        self.右队列 = self.右队列[self.右指针:]
                        self.右指针 = 0
                    元素 =  self.右队列[self.右指针]
                    return 元素
            while self.双端队列长度 == 0:
                time.sleep(0.1)
            else:
                return self.左出队()
        def 右出队(self):
            with self.锁:
                if self.右指针+1 < len(self.右队列):
                    self.双端队列长度 -= 1
                    元素 = self.右队列.pop()
                    return 元素
                elif self.左指针+1 < len(self.左队列):
                    self.双端队列长度 -= 1
                    self.左指针 += 1
                    if self.左指针 > 99:
                        self.左队列 = self.左队列[self.左指针:]
                        self.左指针 = 0
                    元素 =  self.左队列[self.左指针]
                    return 元素
            while self.双端队列长度 == 0:
                time.sleep(0.1)
            else:
                return self.右出队()
    @_方法增强
    def _RGBQUAD类型(主体, 包函, 原函):
        if not hasattr(原函, '_RGBQUAD类型'): 
            class RGBQUAD(ctypes.Structure):
                _fields_ = [
                    ("rgbBlue", wintypes.BYTE),      # 蓝色的强度
                    ("rgbGreen", wintypes.BYTE),     # 绿色的强度  
                    ("rgbRed", wintypes.BYTE),       # 红色的强度
                    ("rgbReserved", wintypes.BYTE),  # 保留成员, 必须为零
                ]
            原函._RGBQUAD类型 = RGBQUAD
        return 原函._RGBQUAD类型
    @_方法增强
    def _BITMAPINFOHEADER类型(主体, 包函, 原函):
        if not hasattr(原函, '_BITMAPINFOHEADER类型'): 
            class BITMAPINFOHEADER(ctypes.Structure):
                _fields_ = [
                    ("biSize", wintypes.DWORD),           # 结构大小
                    ("biWidth", wintypes.LONG),            # 位图宽度(像素)
                    ("biHeight", wintypes.LONG),           # 位图高度(像素)
                    ("biPlanes", wintypes.WORD),         # 目标设备平面数, 必须为1
                    ("biBitCount", wintypes.WORD),       # 每像素位数(bpp)
                    ("biCompression", wintypes.DWORD),    # 压缩方式
                    ("biSizeImage", wintypes.DWORD),      # 图像大小(字节)
                    ("biXPelsPerMeter", wintypes.LONG),    # 水平分辨率(像素/米)
                    ("biYPelsPerMeter", wintypes.LONG),    # 垂直分辨率(像素/米)
                    ("biClrUsed", wintypes.DWORD),        # 实际使用的颜色索引数
                    ("biClrImportant", wintypes.DWORD),   # 重要颜色索引数
                ]
            原函._BITMAPINFOHEADER类型 = BITMAPINFOHEADER
        return 原函._BITMAPINFOHEADER类型
    @_方法增强
    def _BITMAPINFO类型(主体, 包函, 原函):
        if not hasattr(原函, '_BITMAPINFO类型'): 
            class BITMAPINFO(ctypes.Structure):
                _fields_ = [
                    ("bmiHeader", 主体._BITMAPINFOHEADER类型()),  # 位图信息头
                    ("bmiColors", 主体._RGBQUAD类型() * 1),       # 颜色表(柔性数组, 这里定义为1个元素)
                ]
            原函._BITMAPINFO类型 = BITMAPINFO
        return 原函._BITMAPINFO类型
    @_方法增强
    def _BITMAPINFO对象(主体, 包函, 原函):
        _BITMAPINFO对象 = 主体._BITMAPINFO类型()()
        _BITMAPINFO对象.bmiHeader.biSize = ctypes.sizeof(主体._BITMAPINFOHEADER类型())
        _BITMAPINFO对象.bmiHeader.biPlanes = 1
        _BITMAPINFO对象.bmiHeader.biBitCount = 32
        _BITMAPINFO对象.bmiHeader.biCompression = 0
        _BITMAPINFO对象.bmiHeader.biSizeImage = 0
        _BITMAPINFO对象.bmiHeader.biXPelsPerMeter = 0
        _BITMAPINFO对象.bmiHeader.biYPelsPerMeter = 0
        _BITMAPINFO对象.bmiHeader.biClrUsed = 0
        _BITMAPINFO对象.bmiHeader.biClrImportant = 0
        return _BITMAPINFO对象
    @_方法增强
    def _CreateDIBSection函数(主体, 包函, 原函, hdc:'wintypes.HDC', pbmi:'ctypes.POINTER(BITMAPINFO)', usage:'wintypes.UINT', ppvBits:'ctypes.POINTER(ctypes.c_void_p)', hSection:'wintypes.HANDLE', offset:'wintypes.DWORD'): # type: ignore
        if not hasattr(原函, '_CreateDIBSection'): 
            原函._CreateDIBSection = ctypes.windll.gdi32.CreateDIBSection
            原函._CreateDIBSection.argtypes = [
                wintypes.HDC,
                ctypes.POINTER(主体._BITMAPINFO类型()),
                wintypes.UINT,
                ctypes.POINTER(ctypes.c_void_p),
                wintypes.HANDLE,
                wintypes.DWORD
            ]
            原函._CreateDIBSection.restype = wintypes.HBITMAP
        返回值 = 原函._CreateDIBSection(hdc, pbmi, usage, ppvBits, hSection, offset)
        if 返回值 == 0:
            错误码 = ctypes.get_last_error()
            raise ctypes.WinError(错误码, f"CreateDIBSection API调用失败, 返回值{返回值}, 错误码{错误码}")
        return 返回值
    @_方法增强
    def _PrintWindow函数(主体, 包函, 原函, hwnd:'wintypes.HWND', hdcBlt:'wintypes.HDC', nFlags:'wintypes.UINT'):
        if not hasattr(原函, '_PrintWindow'): 
            原函._PrintWindow = ctypes.windll.user32.PrintWindow
            原函._PrintWindow.argtypes = [
                wintypes.HWND,
                wintypes.HDC,
                wintypes.UINT
            ]
            原函._PrintWindow.restype = wintypes.BOOL
        返回值 = 原函._PrintWindow(hwnd, hdcBlt, nFlags)
        if 返回值 == 0:
            错误码 = ctypes.get_last_error()
            raise ctypes.WinError(错误码, f"PrintWindow API调用失败, 返回值{返回值}, 错误码{错误码}")
        return 返回值
    @_方法增强
    def _BitBlt函数(主体, 包函, 原函, hdc:'wintypes.HDC', x:'wintypes.INT', y:'wintypes.INT', cx:'wintypes.INT', cy:'wintypes.INT', hdcSrc:'wintypes.HDC', x1:'wintypes.INT', y1:'wintypes.INT', rop:'wintypes.DWORD'):
        if not hasattr(原函, '_BitBlt'): 
            原函._BitBlt = ctypes.windll.gdi32.BitBlt
            原函._BitBlt.argtypes = [
                wintypes.HDC,
                wintypes.INT,
                wintypes.INT,
                wintypes.INT,
                wintypes.INT,
                wintypes.HDC,
                wintypes.INT,
                wintypes.INT,
                wintypes.DWORD
            ]
            原函._BitBlt.restype = wintypes.BOOL
        返回值 = 原函._BitBlt(hdc, x, y, cx, cy, hdcSrc, x1, y1, rop)
        if 返回值 == 0:
            错误码 = ctypes.get_last_error()
            raise ctypes.WinError(错误码, f"BitBlt API调用失败, 返回值{返回值}, 错误码{错误码}")
        return 返回值


    @_方法增强
    def _StretchBlt函数(主体, 包函, 原函, hdcDest:'wintypes.HDC', xDest:'wintypes.INT', yDest:'wintypes.INT', wDest:'wintypes.INT', hDest:'wintypes.INT', hdcSrc:'wintypes.HDC', xSrc:'wintypes.INT', ySrc:'wintypes.INT', wSrc:'wintypes.INT', hSrc:'wintypes.INT', rop:'wintypes.DWORD'):
        if not hasattr(原函, '_StretchBlt'): 
            原函._StretchBlt = ctypes.windll.gdi32.StretchBlt
            原函._StretchBlt.argtypes = [
                wintypes.HDC,
                wintypes.INT,
                wintypes.INT,
                wintypes.INT,
                wintypes.INT,
                wintypes.HDC,
                wintypes.INT,
                wintypes.INT,
                wintypes.INT,
                wintypes.INT,
                wintypes.DWORD
            ]
            原函._StretchBlt.restype = wintypes.BOOL
        返回值 = 原函._StretchBlt(hdcDest, xDest, yDest, wDest, hDest, hdcSrc, xSrc, ySrc, wSrc, hSrc, rop)
        if 返回值 == 0:
            错误码 = ctypes.get_last_error()
            raise ctypes.WinError(错误码, f"StretchBlt API调用失败, 返回值{返回值}, 错误码{错误码}")
        return 返回值



    @_方法增强
    def _SelectObject函数(主体, 包函, 原函, hdc:'wintypes.HDC', h:'wintypes.HGDIOBJ'):
        if not hasattr(原函, '_SelectObject'): 
            原函._SelectObject = ctypes.windll.gdi32.SelectObject
            原函._SelectObject.argtypes = [
                wintypes.HDC,
                wintypes.HGDIOBJ
            ]
            原函._SelectObject.restype = wintypes.HGDIOBJ
        返回值 = 原函._SelectObject(hdc, h)
        if 返回值 == 0 or 返回值 == 0xFFFFFFFF:
            错误码 = ctypes.get_last_error()
            raise ctypes.WinError(错误码, f"SelectObject API调用失败, 返回值{返回值}, 错误码{错误码}")
        return 返回值
    @_方法增强
    def _DeleteObject函数(主体, 包函, 原函, ho:'wintypes.HGDIOBJ'):
        if not hasattr(原函, '_DeleteObject'): 
            原函._DeleteObject = ctypes.windll.gdi32.DeleteObject
            原函._DeleteObject.argtypes = [wintypes.HGDIOBJ]
            原函._DeleteObject.restype = wintypes.BOOL
        返回值 = 原函._DeleteObject(ho)
        if 返回值 == 0:
            错误码 = ctypes.get_last_error()
            raise ctypes.WinError(错误码, f"DeleteObject API调用失败, 返回值{返回值}, 错误码{错误码}")
        return 返回值

    @_方法增强
    def BitBlt截图(主体, 包函, 原函, 窗口句柄: int, 相对截图区域: tuple[int:'x', int:'y', int:'width', int:'height'] = None):
        try:
            主体._DPI感知()
            窗口设备上下文句柄 = ctypes.windll.user32.GetWindowDC(窗口句柄)
            内存设备上下文句柄 = ctypes.windll.gdi32.CreateCompatibleDC(窗口设备上下文句柄)
            _BITMAPINFO结构体 = 主体._BITMAPINFO对象()
            if 相对截图区域 is None:lx,ty,rx, by = 主体.窗口矩形(窗口句柄);x,y,w, h = 0,0,rx-lx, by-ty
            else:x,y,w,h = 相对截图区域
            _BITMAPINFO结构体.bmiHeader.biWidth = w
            _BITMAPINFO结构体.bmiHeader.biHeight = -h # 负值表示自上而下更符合现代编程习惯
            _BITMAPINFO结构体.bmiHeader.biBitCount = 4 * 8

            像素数据指针 = wintypes.LPVOID()
            位图句柄 = 主体._CreateDIBSection函数(内存设备上下文句柄, ctypes.byref(_BITMAPINFO结构体), 0, ctypes.byref(像素数据指针), None, 0)
            原对象句柄 = 主体._SelectObject函数(内存设备上下文句柄, 位图句柄)
            BitBlt操作结果 = 主体._BitBlt函数(内存设备上下文句柄, 0, 0, w, h, 窗口设备上下文句柄, x, y, 0x00CC0020)

            总字节数 = int(w * h * 4)

            图像缓冲区 = 主体._动态属性化(bytearray, 窗口句柄=窗口句柄, x=x, y=y, w=w, h=h)(总字节数)
            ctypes.memmove((ctypes.c_ubyte * 总字节数).from_buffer(图像缓冲区), 像素数据指针.value, 总字节数)

            return 图像缓冲区

        finally:
            if '原对象句柄' in locals():主体._SelectObject函数(内存设备上下文句柄, 原对象句柄)
            if '位图句柄' in locals():主体._DeleteObject函数(位图句柄)
            if '内存设备上下文句柄' in locals():ctypes.windll.gdi32.DeleteDC(内存设备上下文句柄)
            if '窗口设备上下文句柄' in locals():ctypes.windll.user32.ReleaseDC(窗口句柄, 窗口设备上下文句柄)

    @_方法增强
    def PrintWindow截图(主体, 包函, 原函, 窗口句柄: int, 相对截图区域: tuple[int:'x', int:'y', int:'width', int:'height'] = None):
        try:
            主体._DPI感知()
            窗口设备上下文句柄 = ctypes.windll.user32.GetWindowDC(窗口句柄)
            内存设备上下文句柄 = ctypes.windll.gdi32.CreateCompatibleDC(窗口设备上下文句柄)
            _BITMAPINFO结构体 = 主体._BITMAPINFO对象()
            lx,ty,rx, by = 主体.窗口矩形(窗口句柄)
            biWidth = rx - lx
            biHeight = by - ty
            _BITMAPINFO结构体.bmiHeader.biWidth = biWidth
            _BITMAPINFO结构体.bmiHeader.biHeight = -biHeight # 负值表示自上而下更符合现代编程习惯
            _BITMAPINFO结构体.bmiHeader.biBitCount = 4 * 8

            像素数据指针 = wintypes.LPVOID()


            位图句柄 = 主体._CreateDIBSection函数(内存设备上下文句柄, ctypes.byref(_BITMAPINFO结构体), 0, ctypes.byref(像素数据指针), None, 0)
            原对象句柄 = 主体._SelectObject函数(内存设备上下文句柄, 位图句柄)
            PrintWindow操作结果 = 主体._PrintWindow函数(窗口句柄, 内存设备上下文句柄, 0x00000002)


            if 相对截图区域 is None:
                x,y,w,h = 0,0,biWidth,biHeight
                总字节数 = int(w * h * 4)
                图像缓冲区 = 主体._动态属性化(bytearray, 窗口句柄=窗口句柄, x=x, y=y, w=w, h=h)(总字节数)
                ctypes.memmove((ctypes.c_ubyte * 总字节数).from_buffer(图像缓冲区), 像素数据指针.value, 总字节数)
            else:
                x,y,w,h = 相对截图区域
                总字节数 = w * h * 4
                图像缓冲区 = 主体._动态属性化(bytearray, 窗口句柄=窗口句柄, x=x, y=y, w=w, h=h)(总字节数)
                # 进行偏移计算
                源偏移 = y * 4 * biWidth + x * 4
                目标偏移 = 0
                源行字节数 = 4 * biWidth
                目标行字节数 = w * 4
                for i in range(h):
                    ctypes.memmove((ctypes.c_ubyte * 目标行字节数).from_buffer(图像缓冲区, 目标偏移), 像素数据指针.value + 源偏移, 目标行字节数)
                    源偏移 += 源行字节数
                    目标偏移 += 目标行字节数
            return 图像缓冲区
        finally:
            if '原对象句柄' in locals():主体._SelectObject函数(内存设备上下文句柄, 原对象句柄)
            if '位图句柄' in locals():主体._DeleteObject函数(位图句柄)
            if '内存设备上下文句柄' in locals():ctypes.windll.gdi32.DeleteDC(内存设备上下文句柄)
            if '窗口设备上下文句柄' in locals():ctypes.windll.user32.ReleaseDC(窗口句柄, 窗口设备上下文句柄)

    @_方法增强
    def 窗口截图(主体, 包函, 原函, 窗口句柄: int, 相对截图区域: tuple[int:'x', int:'y', int:'width', int:'height'] = None):
        主体._DPI感知()
        if not hasattr(原函, '_API字典'):原函._API字典 = {}
        if 窗口句柄 in 原函._API字典:
            if 原函._API字典[窗口句柄] == 'BitBlt':
                像素数据 = 主体.BitBlt截图(窗口句柄, 相对截图区域)
            elif 原函._API字典[窗口句柄] == 'PrintWindow':
                像素数据 = 主体.PrintWindow截图(窗口句柄, 相对截图区域)
        else:
            try:
                像素数据 = 主体.BitBlt截图(窗口句柄, 相对截图区域)
                for i in 像素数据[:12] + 像素数据[len(像素数据)//5-12:len(像素数据)//5+12] + 像素数据[2 * len(像素数据)//5-12:2 * len(像素数据)//5+12] + 像素数据[3 * len(像素数据)//5-12:3 * len(像素数据)//5+12] + 像素数据[4 * len(像素数据)//5-12:4 * len(像素数据)//5+12] + 像素数据[-12:]:
                    if i != 0 and i != 255:
                        原函._API字典[窗口句柄] = 'BitBlt'
                        break
                else:
                    raise ctypes.WinError(0, "窗口截图数据全部为0或255")
            except WindowsError as e:
                像素数据 = 主体.PrintWindow截图(窗口句柄, 相对截图区域)
                for i in 像素数据[:12] + 像素数据[len(像素数据)//5-12:len(像素数据)//5+12] + 像素数据[2 * len(像素数据)//5-12:2 * len(像素数据)//5+12] + 像素数据[3 * len(像素数据)//5-12:3 * len(像素数据)//5+12] + 像素数据[4 * len(像素数据)//5-12:4 * len(像素数据)//5+12] + 像素数据[-12:]:
                    if i != 0 and i != 255:
                        原函._API字典[窗口句柄] = 'PrintWindow'
                        break
                else:
                    lx,ty,rx, by = 主体.窗口矩形(窗口句柄)
                    相对截图区域 = lx,ty,rx-lx, by-ty
                    像素数据 = 主体.BitBlt截图(ctypes.windll.user32.GetDesktopWindow(), 相对截图区域)
        return 像素数据



    @_方法增强
    def 像素矩阵(主体, 包函, 原函, 图像数据:'RGBA | RGB', 宽度: int, 高度: int): # type: ignore

        填充数量 = (4 - (宽度 * 3 % 4)) % 4
        颜色字节 = int((len(图像数据))/(宽度*高度))
        assert 宽度 * 高度 * 4 == len(图像数据) or 宽度 * 高度 * 3 + 填充数量 * 高度 == len(图像数据), "图像数据格式错误"

        像素矩阵 = np.frombuffer(图像数据, dtype=np.uint8).reshape((高度, 宽度, 颜色字节))
        return 像素矩阵


    @_方法增强
    def RGBA转RGB(主体, 包函, 原函, 像素数据: 'RGBA', 宽度: int, 高度: int): # type: ignore
        assert len(像素数据) % 4 == 0, "位图数据格式错误"
        类型 = type(像素数据)

        矩阵 = np.frombuffer(像素数据, dtype=np.uint8).reshape((高度, 宽度, 4))
        矩阵 = 矩阵[:, :, :3]

        矩阵 = 矩阵.reshape((高度, 宽度 * 3))

        对齐填充 = (4 - (宽度 * 3 % 4)) % 4
        矩阵 = np.pad(矩阵, ((0, 0), (0, 对齐填充)), 'constant', constant_values=0)

        像素数据 = 类型(矩阵.flatten())
        return 像素数据

    @_方法增强
    def RGB转RGBA(主体, 包函, 原函, 像素数据: 'RGB', 宽度: int, 高度: int): # type: ignore
        assert len(像素数据) % 3 == 0, "位图数据格式错误"
        类型 = type(像素数据)

        矩阵 = np.frombuffer(像素数据, dtype=np.uint8).reshape((高度, -1))

        对齐填充 = (4 - (宽度 * 3 % 4)) % 4

        if 对齐填充 != 0:矩阵 = 矩阵[:, :-对齐填充]

        矩阵 = 矩阵.reshape((高度, 宽度, 3))
        矩阵 = np.pad(矩阵, ((0, 0), (0, 0), (0, 1)), 'constant', constant_values=255)

        像素数据 = 类型(矩阵.flatten())
        return 像素数据


    @_方法增强
    def 保存位图(主体, 包函, 原函, 位图数据, 宽度, 高度, 文件名):


        颜色字节 = int((len(位图数据))/(宽度*高度))
        assert 宽度 * 高度 * 4 == len(位图数据) or 宽度 * 高度 * 3 + (4 - (宽度 * 3 % 4)) % 4 * 高度 == len(位图数据), "位图数据格式错误"



        # 创建BMP文件头
        文件头 = struct.pack('<2sIHHI', b'BM', 54 + len(位图数据), 0, 0, 54)
        # 创建BMP信息头
        信息头 = struct.pack('<iiiHHIIIIII', 40, 宽度, -高度, 1, 颜色字节*8, 0, len(位图数据), 0, 0, 0, 0)

        os.makedirs(os.path.dirname(os.path.abspath(文件名)), exist_ok=True)
        # 写入文件(BMP要求数据从下到上存储)
        with open( fr'\\?\{os.path.abspath(文件名)}', 'wb') as 文件:
            文件.write(文件头 + 信息头 + 位图数据)

    @_方法增强
    def 读取位图(主体, 包函, 原函, 文件名):
        with open(fr'\\?\{os.path.abspath(文件名)}', 'rb') as 文件:
            文件头 = struct.unpack('<2sIHHI', 文件.read(14))
            assert 文件头[0] == b'BM', "文件头错误"
            信息头长度 = struct.unpack('<i', 文件.read(4))[0]
            文件.seek(14)
            信息头 = struct.unpack('<iiiHHIIIIII', 文件.read(信息头长度))
            宽度 = abs(信息头[1])
            高度 = abs(信息头[2])
            颜色字节 = int(信息头[4] / 8)
            数据大小 = abs(信息头[6])
            数据起始 = 文件头[4]
            文件.seek(数据起始)
            位图数据 = 文件.read(数据大小)
            主体._动态属性化(bytearray, w=宽度, h=高度)(位图数据)
            return 位图数据


    @classmethod
    def _SendInput函数(cls, pInputs):
        '''
        功能: 
            发送输入事件到系统
        参数:
            - pInputs: 输入事件结构体列表
        返回值: 无
        异常:
            - 当SendInput API调用失败时抛出ctypes.WinError
        说明:
            - 内部使用windll.user32.SendInput
            - 自动处理DPI感知
            - 首次调用时会初始化SendInput函数
        '''
        cls._DPI感知()
        if not hasattr(cls, '_INPUT结构体'):
            class MOUSEINPUT(ctypes.Structure):
                _fields_ = [
                    ("dx", wintypes.LONG),
                    ("dy", wintypes.LONG),
                    ("mouseData", wintypes.DWORD),
                    ("dwFlags", wintypes.DWORD),
                    ("time", wintypes.DWORD),
                    ("dwExtraInfo", ctypes.c_ulonglong),
                ]
            class KEYBDINPUT(ctypes.Structure):
                _fields_ = [
                    ("wVk", wintypes.WORD),
                    ("wScan", wintypes.WORD),
                    ("dwFlags", wintypes.DWORD),
                    ("time", wintypes.DWORD),
                    ("dwExtraInfo", ctypes.c_ulonglong),
                ]
            class HARDWAREINPUT(ctypes.Structure):
                _fields_ = [
                    ("uMsg", wintypes.DWORD),
                    ("wParamL", wintypes.WORD),
                    ("wParamH", wintypes.WORD),
                ]
            class INPUT_UNION(ctypes.Union):
                _fields_ = [
                    ("mi", MOUSEINPUT),
                    ("ki", KEYBDINPUT),
                    ("hi", HARDWAREINPUT),
                ]
            class INPUT(ctypes.Structure):
                _fields_ = [
                    ("type", wintypes.DWORD),
                    ("union", INPUT_UNION),
                ]
            cls._INPUT结构体 = INPUT
        if not hasattr(cls, '_SendInput'):
            SendInput = ctypes.windll.user32.SendInput
            SendInput.argtypes = [
                wintypes.UINT,
                ctypes.POINTER(cls._INPUT结构体),
                wintypes.INT
            ]
            SendInput.restype = wintypes.UINT
            cls._SendInput = SendInput
        # cInputs = 1
        # pInputs = (cls._INPUT结构体 * 1)()
        # pInputs[0] = INPUT结构体
        cInputs = len(pInputs)
        cbSize = ctypes.sizeof(cls._INPUT结构体)
        返回值 = cls._SendInput(cInputs, pInputs, cbSize)
        if 返回值 != cInputs:
            错误码 = ctypes.get_last_error()
            raise ctypes.WinError(f"SendInput API调用失败, 错误码：{错误码}")
    @classmethod
    def _鼠标INPUT结构体(cls, dx: int, dy: int, mouseData: int, dwFlags: int, time: int, dwExtraInfo: int):
        '''
        功能: 
            创建并返回一个鼠标输入事件的结构体对象
        参数:
            - dx: 鼠标的绝对位置, 或自上次生成鼠标事件以来的运动量, 具体取决于 dwFlags 成员的值。(LONG)
            - dy: 鼠标的绝对位置, 或自上次生成鼠标事件以来的运动量, 具体取决于 dwFlags 成员的值。(LONG)
            - mouseData: 鼠标数据(DWORD),主要用于鼠标滚轮事件
            - dwFlags: 鼠标事件标志(DWORD)
            - time: 时间戳(DWORD)
            - dwExtraInfo: 额外信息(ULONG_PTR)
        返回值: 
            返回配置好的鼠标输入结构体 _INPUT结构体 对象
        说明:
            - 此方法仅创建和配置输入结构体, 不实际发送输入事件
            - 结构体可用于后续的_SendInput函数调用,注意_SendInput函数的参数pInputs为C数组类型：
                pInputs = (type(_INPUT结构体) * 1)(_INPUT结构体)
        '''
        if not hasattr(cls, '_INPUT结构体'):
            class MOUSEINPUT(ctypes.Structure):
                _fields_ = [
                    ("dx", wintypes.LONG),
                    ("dy", wintypes.LONG),
                    ("mouseData", wintypes.DWORD),
                    ("dwFlags", wintypes.DWORD),
                    ("time", wintypes.DWORD),
                    ("dwExtraInfo", ctypes.c_ulonglong),
                ]
            class KEYBDINPUT(ctypes.Structure):
                _fields_ = [
                    ("wVk", wintypes.WORD),
                    ("wScan", wintypes.WORD),
                    ("dwFlags", wintypes.DWORD),
                    ("time", wintypes.DWORD),
                    ("dwExtraInfo", ctypes.c_ulonglong),
                ]
            class HARDWAREINPUT(ctypes.Structure):
                _fields_ = [
                    ("uMsg", wintypes.DWORD),
                    ("wParamL", wintypes.WORD),
                    ("wParamH", wintypes.WORD),
                ]
            class INPUT_UNION(ctypes.Union):
                _fields_ = [
                    ("mi", MOUSEINPUT),
                    ("ki", KEYBDINPUT),
                    ("hi", HARDWAREINPUT),
                ]
            class INPUT(ctypes.Structure):
                _fields_ = [
                    ("type", wintypes.DWORD),
                    ("union", INPUT_UNION),
                ]
            cls._INPUT结构体 = INPUT
        _INPUT结构体 = cls._INPUT结构体()
        _INPUT结构体.type = 0
        mi = _INPUT结构体.union.mi
        mi.dx = dx
        mi.dy = dy
        mi.mouseData = mouseData
        mi.dwFlags = dwFlags
        mi.time = time
        mi.dwExtraInfo = dwExtraInfo
        return _INPUT结构体
    @classmethod
    def _键盘INPUT结构体(cls, wVk: int, wScan: int, dwFlags: int, time: int, dwExtraInfo: int):
        '''
        功能: 
            创建并返回一个键盘输入事件的结构体对象
        参数:
            - wVk: 虚拟键码(WORD)
            - wScan: 扫描码(WORD)
            - dwFlags: 键盘事件标志(DWORD)
            - time: 时间戳(DWORD)
            - dwExtraInfo: 额外信息(ULONG_PTR)
        返回值: 
            返回配置好的键盘输入结构体 _INPUT结构体 对象
        说明:
            - 此方法仅创建和配置输入结构体, 不实际发送输入事件
            - 结构体可用于后续的_SendInput函数调用,注意_SendInput函数的参数pInputs为C数组类型：
                pInputs = (type(_INPUT结构体) * 1)(_INPUT结构体)
        '''
        if not hasattr(cls, '_INPUT结构体'):
            class MOUSEINPUT(ctypes.Structure):
                _fields_ = [
                    ("dx", wintypes.LONG),
                    ("dy", wintypes.LONG),
                    ("mouseData", wintypes.DWORD),
                    ("dwFlags", wintypes.DWORD),
                    ("time", wintypes.DWORD),
                    ("dwExtraInfo", ctypes.c_ulonglong),
                ]
            class KEYBDINPUT(ctypes.Structure):
                _fields_ = [
                    ("wVk", wintypes.WORD),
                    ("wScan", wintypes.WORD),
                    ("dwFlags", wintypes.DWORD),
                    ("time", wintypes.DWORD),
                    ("dwExtraInfo", ctypes.c_ulonglong),
                ]
            class HARDWAREINPUT(ctypes.Structure):
                _fields_ = [
                    ("uMsg", wintypes.DWORD),
                    ("wParamL", wintypes.WORD),
                    ("wParamH", wintypes.WORD),
                ]
            class INPUT_UNION(ctypes.Union):
                _fields_ = [
                    ("mi", MOUSEINPUT),
                    ("ki", KEYBDINPUT),
                    ("hi", HARDWAREINPUT),
                ]
            class INPUT(ctypes.Structure):
                _fields_ = [
                    ("type", wintypes.DWORD),
                    ("union", INPUT_UNION),
                ]
            cls._INPUT结构体 = INPUT
        _INPUT结构体 = cls._INPUT结构体()
        _INPUT结构体.type = 1
        ki = _INPUT结构体.union.ki
        ki.wVk = wVk
        ki.wScan = wScan
        ki.dwFlags = dwFlags
        ki.time = time
        ki.dwExtraInfo = dwExtraInfo
        return _INPUT结构体
    @classmethod
    def _硬件INPUT结构体(cls, uMsg: int, wParamL: int, wParamH: int):
        '''
        功能: 
            创建并返回一个硬件输入事件的结构体对象
        参数:
            - uMsg: 消息(DWORD)
            - wParamL: 参数1(WORD)
            - wParamH: 参数2(WORD)
        返回值: 
            返回配置好的硬件输入结构体 _INPUT结构体 对象
        说明:
            - 此方法仅创建和配置输入结构体, 不实际发送输入事件
            - 结构体可用于后续的_SendInput函数调用,注意_SendInput函数的参数pInputs为C数组类型：
                pInputs = (type(_INPUT结构体) * 1)(_INPUT结构体)
        '''
        if not hasattr(cls, '_INPUT结构体'):
            class MOUSEINPUT(ctypes.Structure):
                _fields_ = [
                    ("dx", wintypes.LONG),
                    ("dy", wintypes.LONG),
                    ("mouseData", wintypes.DWORD),
                    ("dwFlags", wintypes.DWORD),
                    ("time", wintypes.DWORD),
                    ("dwExtraInfo", ctypes.c_ulonglong),
                ]
            class KEYBDINPUT(ctypes.Structure):
                _fields_ = [
                    ("wVk", wintypes.WORD),
                    ("wScan", wintypes.WORD),
                    ("dwFlags", wintypes.DWORD),
                    ("time", wintypes.DWORD),
                    ("dwExtraInfo", ctypes.c_ulonglong),
                ]
            class HARDWAREINPUT(ctypes.Structure):
                _fields_ = [
                    ("uMsg", wintypes.DWORD),
                    ("wParamL", wintypes.WORD),
                    ("wParamH", wintypes.WORD),
                ]
            class INPUT_UNION(ctypes.Union):
                _fields_ = [
                    ("mi", MOUSEINPUT),
                    ("ki", KEYBDINPUT),
                    ("hi", HARDWAREINPUT),
                ]
            class INPUT(ctypes.Structure):
                _fields_ = [
                    ("type", wintypes.DWORD),
                    ("union", INPUT_UNION),
                ]
            cls._INPUT结构体 = INPUT
        _INPUT结构体 = cls._INPUT结构体()
        _INPUT结构体.type = 2
        hi = _INPUT结构体.union.hi
        hi.uMsg = uMsg
        hi.wParamL = wParamL
        hi.wParamH = wParamH
        return _INPUT结构体
    @classmethod
    def 鼠标操作(cls, dx: int, dy: int, mouseData: int, dwFlags: int, time: int, dwExtraInfo: int):
        INPUT结构体 = cls._鼠标INPUT结构体(dx, dy, mouseData, dwFlags, time, dwExtraInfo)
        pInputs = (type(INPUT结构体) * 1)(INPUT结构体)
        cls._SendInput函数(pInputs)
    @classmethod
    def 键盘操作(cls, wVk: int, wScan: int, dwFlags: int, time: int, dwExtraInfo: int):
        INPUT结构体 = cls._键盘INPUT结构体(wVk, wScan, dwFlags, time, dwExtraInfo)
        pInputs = (type(INPUT结构体) * 1)(INPUT结构体)
        cls._SendInput函数(pInputs)
    @classmethod
    def 硬件操作(cls, uMsg: int, wParamL: int, wParamH: int):
        INPUT结构体 = cls._硬件INPUT结构体(uMsg, wParamL, wParamH)
        pInputs = (type(INPUT结构体) * 1)(INPUT结构体)
        cls._SendInput函数(pInputs)
    @classmethod
    def 标题类名查找窗口(cls,  类名: str=None, 标题: str=None,):
        if not hasattr(cls, '_FindWindowW'):
            cls._FindWindow = ctypes.windll.user32.FindWindowW
            cls._FindWindow.argtypes = [wintypes.LPCWSTR, wintypes.LPCWSTR]
            cls._FindWindow.restype = wintypes.HWND
        返回值 = cls._FindWindow(类名, 标题)
        if 返回值 == 0:
            错误码 = ctypes.get_last_error()
            raise ctypes.WinError(f"FindWindow API调用失败, 错误码：{错误码}")
        return 返回值
    class 键码:
        if True:#键码
            VK_LBUTTON = 0x01
            VK_RBUTTON = 0x02
            VK_CANCEL = 0x03
            VK_MBUTTON = 0x04
            VK_XBUTTON1 = 0x05
            VK_XBUTTON2 = 0x06
            VK_BACK = 0x08
            VK_TAB = 0x09
            VK_CLEAR = 0x0C
            VK_RETURN = 0x0D
            VK_SHIFT = 0x10
            VK_CONTROL = 0x11
            VK_MENU = 0x12
            VK_PAUSE = 0x13
            VK_CAPITAL = 0x14
            VK_KANA = 0x15
            VK_HANGUL = 0x15
            VK_IME_ON = 0x16
            VK_JUNJA = 0x17
            VK_FINAL = 0x18
            VK_HANJA = 0x19
            VK_KANJI = 0x19
            VK_IME_OFF = 0x1A
            VK_ESCAPE = 0x1B
            VK_CONVERT = 0x1C
            VK_NONCONVERT = 0x1D
            VK_ACCEPT = 0x1E
            VK_MODECHANGE = 0x1F
            VK_SPACE = 0x20
            VK_PRIOR = 0x21
            VK_NEXT = 0x22
            VK_END = 0x23
            VK_HOME = 0x24
            VK_LEFT = 0x25
            VK_UP = 0x26
            VK_RIGHT = 0x27
            VK_DOWN = 0x28
            VK_SELECT = 0x29
            VK_PRINT = 0x2A
            VK_EXECUTE = 0x2B
            VK_SNAPSHOT = 0x2C
            VK_INSERT = 0x2D
            VK_DELETE = 0x2E
            VK_HELP = 0x2F
            VK_0 = 0x30
            VK_1 = 0x31
            VK_2 = 0x32
            VK_3 = 0x33
            VK_4 = 0x34
            VK_5 = 0x35
            VK_6 = 0x36
            VK_7 = 0x37
            VK_8 = 0x38
            VK_9 = 0x39
            VK_A = 0x41
            VK_B = 0x42
            VK_C = 0x43
            VK_D = 0x44
            VK_E = 0x45
            VK_F = 0x46
            VK_G = 0x47
            VK_H = 0x48
            VK_I = 0x49
            VK_J = 0x4A
            VK_K = 0x4B
            VK_L = 0x4C
            VK_M = 0x4D
            VK_N = 0x4E
            VK_O = 0x4F
            VK_P = 0x50
            VK_Q = 0x51
            VK_R = 0x52
            VK_S = 0x53
            VK_T = 0x54
            VK_U = 0x55
            VK_V = 0x56
            VK_W = 0x57
            VK_X = 0x58
            VK_Y = 0x59
            VK_Z = 0x5A
            VK_LWIN = 0x5B
            VK_RWIN = 0x5C
            VK_APPS = 0x5D
            VK_SLEEP = 0x5F
            VK_NUMPAD0 = 0x60
            VK_NUMPAD1 = 0x61
            VK_NUMPAD2 = 0x62
            VK_NUMPAD3 = 0x63
            VK_NUMPAD4 = 0x64
            VK_NUMPAD5 = 0x65
            VK_NUMPAD6 = 0x66
            VK_NUMPAD7 = 0x67
            VK_NUMPAD8 = 0x68
            VK_NUMPAD9 = 0x69
            VK_MULTIPLY = 0x6A
            VK_ADD = 0x6B
            VK_SEPARATOR = 0x6C
            VK_SUBTRACT = 0x6D
            VK_DECIMAL = 0x6E
            VK_DIVIDE = 0x6F
            VK_F1 = 0x70
            VK_F2 = 0x71
            VK_F3 = 0x72
            VK_F4 = 0x73
            VK_F5 = 0x74
            VK_F6 = 0x75
            VK_F7 = 0x76
            VK_F8 = 0x77
            VK_F9 = 0x78
            VK_F10 = 0x79
            VK_F11 = 0x7A
            VK_F12 = 0x7B
            VK_F13 = 0x7C
            VK_F14 = 0x7D
            VK_F15 = 0x7E
            VK_F16 = 0x7F
            VK_F17 = 0x80
            VK_F18 = 0x81
            VK_F19 = 0x82
            VK_F20 = 0x83
            VK_F21 = 0x84
            VK_F22 = 0x85
            VK_F23 = 0x86
            VK_F24 = 0x87
            VK_NUMLOCK = 0x90
            VK_SCROLL = 0x91
            VK_LSHIFT = 0xA0
            VK_RSHIFT = 0xA1
            VK_LCONTROL = 0xA2
            VK_RCONTROL = 0xA3
            VK_LMENU = 0xA4
            VK_RMENU = 0xA5
            VK_BROWSER_BACK = 0xA6
            VK_BROWSER_FORWARD = 0xA7
            VK_BROWSER_REFRESH = 0xA8
            VK_BROWSER_STOP = 0xA9
            VK_BROWSER_SEARCH = 0xAA
            VK_BROWSER_FAVORITES = 0xAB
            VK_BROWSER_HOME = 0xAC
            VK_VOLUME_MUTE = 0xAD
            VK_VOLUME_DOWN = 0xAE
            VK_VOLUME_UP = 0xAF
            VK_MEDIA_NEXT_TRACK = 0xB0
            VK_MEDIA_PREV_TRACK = 0xB1
            VK_MEDIA_STOP = 0xB2
            VK_MEDIA_PLAY_PAUSE = 0xB3
            VK_LAUNCH_MAIL = 0xB4
            VK_LAUNCH_MEDIA_SELECT = 0xB5
            VK_LAUNCH_APP1 = 0xB6
            VK_LAUNCH_APP2 = 0xB7
            VK_OEM_1 = 0xBA
            VK_OEM_PLUS = 0xBB
            VK_OEM_COMMA = 0xBC
            VK_OEM_MINUS = 0xBD
            VK_OEM_PERIOD = 0xBE
            VK_OEM_2 = 0xBF
            VK_OEM_3 = 0xC0
            VK_GAMEPAD_A = 0xC3
            VK_GAMEPAD_B = 0xC4
            VK_GAMEPAD_X = 0xC5
            VK_GAMEPAD_Y = 0xC6
            VK_GAMEPAD_RIGHT_SHOULDER = 0xC7
            VK_GAMEPAD_LEFT_SHOULDER = 0xC8
            VK_GAMEPAD_LEFT_TRIGGER = 0xC9
            VK_GAMEPAD_RIGHT_TRIGGER = 0xCA
            VK_GAMEPAD_DPAD_UP = 0xCB
            VK_GAMEPAD_DPAD_DOWN = 0xCC
            VK_GAMEPAD_DPAD_LEFT = 0xCD
            VK_GAMEPAD_DPAD_RIGHT = 0xCE
            VK_GAMEPAD_MENU = 0xCF
            VK_GAMEPAD_VIEW = 0xD0
            VK_GAMEPAD_LEFT_THUMBSTICK_BUTTON = 0xD1
            VK_GAMEPAD_RIGHT_THUMBSTICK_BUTTON = 0xD2
            VK_GAMEPAD_LEFT_THUMBSTICK_UP = 0xD3
            VK_GAMEPAD_LEFT_THUMBSTICK_DOWN = 0xD4
            VK_GAMEPAD_LEFT_THUMBSTICK_RIGHT = 0xD5
            VK_GAMEPAD_LEFT_THUMBSTICK_LEFT = 0xD6
            VK_GAMEPAD_RIGHT_THUMBSTICK_UP = 0xD7
            VK_GAMEPAD_RIGHT_THUMBSTICK_DOWN = 0xD8
            VK_GAMEPAD_RIGHT_THUMBSTICK_RIGHT = 0xD9
            VK_GAMEPAD_RIGHT_THUMBSTICK_LEFT = 0xDA
            VK_OEM_4 = 0xDB
            VK_OEM_5 = 0xDC
            VK_OEM_6 = 0xDD
            VK_OEM_7 = 0xDE
            VK_OEM_8 = 0xDF
            VK_OEM_102 = 0xE2
            VK_PROCESSKEY = 0xE5
            VK_PACKET = 0xE7
            VK_ATTN = 0xF6
            VK_CRSEL = 0xF7
            VK_EXSEL = 0xF8
            VK_EREOF = 0xF9
            VK_PLAY = 0xFA
            VK_ZOOM = 0xFB
            VK_NONAME = 0xFC
            VK_PA1 = 0xFD
            VK_OEM_CLEAR = 0xFE
    @classmethod
    def 调整窗口位置(cls, 大小位置: tuple[int, int, int, int], 窗口句柄: int = ctypes.windll.user32.GetForegroundWindow(), Z序句柄: int = 0,uFlags = 0x4000|0x0020|0x0400|0x0040):
        cls._DPI感知()
        if not hasattr(cls, '_SetWindowPos'): 
            SetWindowPos = ctypes.windll.user32.SetWindowPos
            SetWindowPos.argtypes = [
                wintypes.HWND,  # hWnd
                wintypes.HWND,  # hWndInsertAfter
                wintypes.INT,   # X
                wintypes.INT,   # Y
                wintypes.INT,   # cx
                wintypes.INT,   # cy
                wintypes.UINT   # uFlags
            ]
            SetWindowPos.restype = wintypes.BOOL
            cls._SetWindowPos = SetWindowPos
        左边, 上边, 宽度, 高度 = 大小位置
        if Z序句柄 == 0 and not uFlags & 0x0004:
            if 窗口句柄 != ctypes.windll.user32.GetForegroundWindow() or ctypes.windll.user32.IsZoomed(窗口句柄) or ctypes.windll.user32.IsIconic(窗口句柄):
                ctypes.windll.user32.ShowWindow(窗口句柄, 6)
                ctypes.windll.user32.ShowWindow(窗口句柄, 1)
        返回值 = cls._SetWindowPos(
            窗口句柄,  # 窗口的句柄。
            Z序句柄,    # 窗口的句柄, 用于在 Z 顺序中定位的窗口之前。 此参数必须是窗口句柄或1(底部)、0(顶部)、-1(置顶)、-2(取消置顶)之一。
            左边,   # 新X坐标
            上边,   # 新Y坐标
            宽度,   # 新宽度
            高度,   # 新高度
            uFlags  
        )
        if 返回值 == 0:
            错误码 = ctypes.get_last_error()
            print(f"SetWindowPos API调用失败, 错误码：{错误码}")
    @classmethod
    def _PostMessage函数(cls, hWnd: int, Msg: int, wParam: int, lParam: int):
        cls._DPI感知()
        if not hasattr(cls, '_PostMessage'):
            PostMessage = ctypes.windll.user32.PostMessageW
            PostMessage.argtypes = [wintypes.HWND, wintypes.UINT, wintypes.WPARAM, wintypes.LPARAM]
            PostMessage.restype = wintypes.BOOL
            cls._PostMessage = PostMessage
        返回值 = cls._PostMessage(hWnd, Msg, wParam, lParam)
        if 返回值 == 0:
            错误码 = ctypes.get_last_error()
            raise ctypes.WinError(f"PostMessage API调用失败, 错误码：{错误码}")
        return 返回值
    @classmethod
    def _SendMessage函数(cls, hWnd: int, Msg: int, wParam: int, lParam: int):
        cls._DPI感知()
        if not hasattr(cls, '_SendMessage'):
            SendMessage = ctypes.windll.user32.SendMessageW
            SendMessage.argtypes = [wintypes.HWND, wintypes.UINT, wintypes.WPARAM, wintypes.LPARAM]
            SendMessage.restype = ctypes.c_long
            cls._SendMessage = SendMessage
        返回值 = cls._SendMessage(hWnd, Msg, wParam, lParam)
        # if 返回值 == 0:
        #     错误码 = ctypes.get_last_error()
        #     raise ctypes.WinError(f"SendMessage API调用失败, 错误码：{错误码}")
        return 返回值
    @classmethod
    def 鼠标左键单击(cls,位置:tuple[int, int], 窗口句柄:int=None):
        cls._DPI感知()
        if not hasattr(cls, '_屏幕宽度'):cls._屏幕宽度 = ctypes.windll.user32.GetSystemMetrics(0)
        if not hasattr(cls, '_屏幕高度'):cls._屏幕高度 = ctypes.windll.user32.GetSystemMetrics(1)
        if 窗口句柄 is None:
            位置 = (位置[0] * 65535 // cls._屏幕宽度, 位置[1] * 65535 // cls._屏幕高度)
            INPUT1 = cls._鼠标INPUT结构体(位置[0],位置[1],0,0x8000|0x0002|0x0001,0,0)
            INPUT2 = cls._鼠标INPUT结构体(位置[0],位置[1],0,0x8000|0x0004|0x0001,0,0)
            pInputs = (type(INPUT1) * 2)(INPUT1, INPUT2)
            cls._SendInput函数(pInputs)
        else:
            if not hasattr(cls, '_ClientToScreen'):
                ClientToScreen = ctypes.windll.user32.ClientToScreen
                ClientToScreen.argtypes = [wintypes.HWND, ctypes.POINTER(wintypes.POINT)]
                ClientToScreen.restype = wintypes.BOOL
                cls._ClientToScreen = ClientToScreen
            if not hasattr(cls, '_ScreenToClient'):
                ScreenToClient = ctypes.windll.user32.ScreenToClient
                ScreenToClient.argtypes = [wintypes.HWND, ctypes.POINTER(wintypes.POINT)]
                ScreenToClient.restype = wintypes.BOOL
                cls._ScreenToClient = ScreenToClient
            _位置 = wintypes.POINT()
            _位置.x, _位置.y = 位置[0],位置[1]
            返回值 = cls._ScreenToClient(窗口句柄, ctypes.byref(_位置))
            if 返回值 == 0:
                错误码 = ctypes.get_last_error()
                raise ctypes.WinError(f"ClientToScreen API调用失败, 错误码：{错误码}")
            else:
                x,y = _位置.x, _位置.y
                lParam = y << 16 | x
                wParam = 0x0001
                WM_LBUTTONDOWN = 0x0201
                返回值1 = cls._SendMessage函数(窗口句柄, WM_LBUTTONDOWN, wParam, lParam)
                WM_LBUTTONUP = 0x0202
                wParam = 0
                返回值2 = cls._SendMessage函数(窗口句柄, WM_LBUTTONUP, wParam, lParam)
                # print(返回值1, 返回值2)
    @_方法增强
    def _SetConsoleCtrlHandler函数(主体, 包函, 原函, HandlerRoutine, Add):
        if not hasattr(原函, '_SetConsoleCtrlHandler'):
            SetConsoleCtrlHandler = ctypes.windll.kernel32.SetConsoleCtrlHandler
            SetConsoleCtrlHandler.argtypes = [ctypes.c_void_p, wintypes.BOOL]
            SetConsoleCtrlHandler.restype = wintypes.BOOL
            原函._SetConsoleCtrlHandler = SetConsoleCtrlHandler
        返回值 = 原函._SetConsoleCtrlHandler(HandlerRoutine, Add)
        if 返回值 == 0:
            错误码 = ctypes.get_last_error()
            raise ctypes.WinError(f"SetConsoleCtrlHandler API调用失败, 错误码：{错误码}")
        return 返回值
    @_方法增强
    def 退出清理(主体, 包函, 原函, 清理函数,*位置参数,**关键字参数):
        def 回调函数(dwCtrlType=None):
            if dwCtrlType == 0:# CTRL_C_EVENT 0	已从键盘输入或 GenerateConsoleCtrlEvent 函数生成的信号中接收 CTRL+C 信号。
                return
            elif dwCtrlType == 1:# CTRL_BREAK_EVENT 1	已从键盘输入或 GenerateConsoleCtrlEvent 函数生成的信号中接收 CTRL+BREAK 信号。
                pass
            elif dwCtrlType == 2:# CTRL_CLOSE_EVENT 2	当用户关闭控制台时，系统向附加到控制台的所有进程发送的信号（单击控制台窗口的窗口菜单上的关闭或单击任务管理器中的结束任务按钮命令）。
                pass
            elif dwCtrlType == 5:# CTRL_LOGOFF_EVENT 5	系统在用户退出登录时发送到所有控制台进程的信号。 此信号不指示哪个用户正在退出登录，因此无法做出任何假设。
                pass
            elif dwCtrlType == 6:# CTRL_SHUTDOWN_EVENT 6	当系统关闭时发送的信号。 当系统发送此信号时，交互式应用程序不存在，因此这种情况下只能由服务接收它。 服务也有自己的关闭事件通知机制。 有关详细信息，请参阅处理程序。
                pass
            清理函数(*位置参数, **关键字参数)
        atexit.register(回调函数)
        PHANDLER_ROUTINE = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.c_uint)
        HandlerRoutine = PHANDLER_ROUTINE(回调函数)
        主体._SetConsoleCtrlHandler函数(HandlerRoutine, True)
        if not hasattr(原函, '_退出清理列表'):原函._退出清理列表 = ['HandlerRoutine','清理函数','位置参数','关键字参数']
        原函._退出清理列表.append([HandlerRoutine,清理函数,位置参数,关键字参数])#阻止被垃圾回收器回收导致失效
        return 原函._退出清理列表
    @_方法增强
    def _SetWindowsHookEx函数(主体, 包函, 原函, idHook: wintypes.INT, lpfn: ctypes.WINFUNCTYPE, hmod: wintypes.HINSTANCE, dwThreadId: wintypes.DWORD):
        主体._DPI感知()
        if not hasattr(原函, '_SetWindowsHookEx'):
            SetWindowsHookEx = ctypes.windll.user32.SetWindowsHookExW
            SetWindowsHookEx.argtypes = [wintypes.INT, ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int, wintypes.WPARAM, wintypes.LPARAM), wintypes.HINSTANCE, wintypes.DWORD]
            SetWindowsHookEx.restype = wintypes.HHOOK
            原函._SetWindowsHookEx = SetWindowsHookEx
        返回值 = 原函._SetWindowsHookEx(idHook, lpfn, hmod, dwThreadId)
        if 返回值 == 0:
            错误码 = ctypes.get_last_error()
            raise ctypes.WinError(f"SetWindowsHookEx API调用失败, 错误码：{错误码}")
        return 返回值

    @_方法增强
    def _安装鼠标钩子(主体, 包函, 原函, 钩子回调函数):
        主体._DPI感知()
        idHook = WH_MOUSE_LL = 14
        HOOKPROC = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int, wintypes.WPARAM, wintypes.LPARAM)
        原函.lpfn = HOOKPROC(钩子回调函数)
        鼠标钩子句柄 = 主体._SetWindowsHookEx函数(idHook, 原函.lpfn, hmod = 0, dwThreadId = 0)
        return 鼠标钩子句柄
    @_方法增强
    def _安装键盘钩子(主体, 包函, 原函, 钩子回调函数) -> int:
        主体._DPI感知()
        # cls._安装键盘钩子.lpfn = None
        idHook = WH_KEYBOARD_LL = 13
        HOOKPROC = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int, wintypes.WPARAM, wintypes.LPARAM)
        原函.lpfn = HOOKPROC(钩子回调函数)
        键盘钩子句柄 = 主体._SetWindowsHookEx函数(idHook, 原函.lpfn, hmod = 0, dwThreadId = 0)
        return 键盘钩子句柄

    @_方法增强
    def 后台安装鼠键钩子(主体, 包函, 原函, 钩子回调函数:'callable[int:"wParam", object:"KBDLLHOOKSTRUCT|MSLLHOOKSTRUCT"]') -> dict["线程状态":bool, "异常信息":str, "返回值":object, "线程函数":callable, "线程参数":tuple, "线程标识符":int,"鼠标钩子句柄":int,"键盘钩子句柄":int,"任务链":list[callable:"钩子回调函数"]]:
        主体._DPI感知()
        if not hasattr(原函, '_任务链'):原函._任务链 = []
        原函._任务链.append(钩子回调函数)
        if not hasattr(原函, '_线程信息'):
            if not hasattr(原函, '_MSLLHOOKSTRUCT结构体'):
                class MSLLHOOKSTRUCT(ctypes.Structure):
                    _fields_ = [
                        ("pt", wintypes.POINT),
                        ("mouseData", wintypes.DWORD),
                        ("flags", wintypes.DWORD),
                        ("time", wintypes.DWORD),
                        ("dwExtraInfo", ctypes.c_void_p)
                    ]
                原函._MSLLHOOKSTRUCT结构体 = MSLLHOOKSTRUCT
            if not hasattr(原函, '_KBDLLHOOKSTRUCT结构体'):
                class KBDLLHOOKSTRUCT(ctypes.Structure):
                    _fields_ = [
                        ("vkCode", wintypes.DWORD),
                        ("scanCode", wintypes.DWORD),
                        ("flags", wintypes.DWORD),
                        ("time", wintypes.DWORD),
                        ("dwExtraInfo", ctypes.c_void_p)
                    ]
                原函._KBDLLHOOKSTRUCT结构体 = KBDLLHOOKSTRUCT
            if not hasattr(原函, '_CallNextHookEx'):
                CallNextHookEx = ctypes.windll.user32.CallNextHookEx
                CallNextHookEx.argtypes = [wintypes.HHOOK, ctypes.c_int, wintypes.WPARAM, wintypes.LPARAM]
                CallNextHookEx.restype = ctypes.c_int
                原函._CallNextHookEx = CallNextHookEx
            def _键盘回调函数(nCode, wParam, lParam):
                if nCode == 0:
                    KBDLLHOOKSTRUCT = 原函._KBDLLHOOKSTRUCT结构体.from_address(lParam)
                    for 钩子回调函数 in reversed(原函._任务链):
                        if 钩子回调函数(wParam, KBDLLHOOKSTRUCT):return 1
                return 原函._CallNextHookEx(原函._键盘钩子句柄, nCode, wParam, lParam)
            def _鼠标回调函数(nCode, wParam, lParam):
                if nCode == 0:
                    MSLLHOOKSTRUCT = 原函._MSLLHOOKSTRUCT结构体.from_address(lParam)
                    for 钩子回调函数 in reversed(原函._任务链):
                        if 钩子回调函数(wParam, MSLLHOOKSTRUCT):return 1
                return 原函._CallNextHookEx(原函._鼠标钩子句柄, nCode, wParam, lParam)
            def _后台线程():
                原函._鼠标钩子句柄 = 主体._安装鼠标钩子(_鼠标回调函数)
                原函._键盘钩子句柄 = 主体._安装键盘钩子(_键盘回调函数)
                原函._线程信息['鼠标钩子句柄'] = 原函._鼠标钩子句柄
                原函._线程信息['键盘钩子句柄'] = 原函._键盘钩子句柄
                原函._线程信息['任务链'] = 原函._任务链
                原函._消息结构 = wintypes.MSG()
                # while True:
                #     返回值 = 主体._PeekMessage函数(ctypes.byref(原函._消息结构), None, 0, 0, 0x0000)
                #     print(原函._消息结构.message,原函._消息结构.wParam,原函._消息结构.lParam)
                while 主体._GetMessage函数(ctypes.byref(原函._消息结构), None, 0, 0) != 0:
                    pass
            原函._线程信息 = 主体.线程池(_后台线程)
        return 原函._线程信息
    @classmethod
    def 按键监听脚本录制器(cls, 键码: int = 键码.VK_F10,撤回键:int = 键码.VK_DELETE,录制区域大小=(16,16)):#默认键码F10
        cls._DPI感知()
        if not hasattr(cls, '_脚本数据'): cls._脚本数据 = {}
        def _按键监听脚本录制器(键码):
            获取异步按键状态=ctypes.windll.user32.GetAsyncKeyState
            线程标识符 = _thread.get_ident()
            while cls._线程池[线程标识符]['线程信息']['线程状态']:
                if 获取异步按键状态(键码) & 0b1000000000000000:#F10按下时
                    当前鼠标位置 = cls.鼠标位置()
                    窗口句柄 = cls.坐标查找窗口(当前鼠标位置)
                    lx,ty,rx, by = cls.窗口矩形(窗口句柄)
                    相对图色区域 = 当前鼠标位置[0]-录制区域大小[0]//2 - lx, 当前鼠标位置[1]-录制区域大小[1]//2 - ty, 录制区域大小[0], 录制区域大小[1]
                    窗口标题 = cls.窗口标题(窗口句柄)
                    if 窗口标题 not in cls._脚本数据:cls._脚本数据[窗口标题] = []
                    if ctypes.windll.user32.IsZoomed(窗口句柄):窗口大小 = '最大化'
                    else:窗口大小 = rx-lx, by-ty
                    图色数据 = cls.窗口截图(相对图色区域,窗口句柄)
                    dx , dy = 录制区域大小[0]*2,录制区域大小[1]*2
                    while 获取异步按键状态(键码) & 0b1000000000000000:#F10持续时
                        _dx, _dy = abs(cls.鼠标位置()[0] - 当前鼠标位置[0]), abs(cls.鼠标位置()[1] - 当前鼠标位置[1])
                        if _dx + _dy > dx + dy:
                            dx, dy = _dx, _dy
                            图色数据 = cls.窗口截图(相对图色区域,窗口句柄)
                        time.sleep(0.01)
                    数据 = {'窗口大小':窗口大小, '相对图色区域':相对图色区域, '图色数据':图色数据}
                    当前鼠标位置 = cls.鼠标位置()
                    相对鼠标位置 = 当前鼠标位置[0] - lx, 当前鼠标位置[1] - ty
                    数据['相对鼠标位置'] = 相对鼠标位置
                    cls._脚本数据[窗口标题].append(数据)
                    位图文件名称 = fr'图色数据'+os.sep+fr'{窗口标题}'.encode('utf-8').hex()+os.sep+fr'{窗口大小}_{相对图色区域}_{相对鼠标位置}'.encode('utf-8').hex()
                    cls.保存位图(图色数据,相对图色区域[2],相对图色区域[3],os.path.abspath(fr'{位图文件名称}.bmp'))
                elif 获取异步按键状态(撤回键) & 0b1000000000000000:
                    if len(cls._脚本数据) > 0:
                        窗口标题 = next(reversed(cls._脚本数据))
                        if len(cls._脚本数据[窗口标题]) > 0:
                            窗口大小,相对图色区域,图色数据,相对鼠标位置 = cls._脚本数据[窗口标题][-1]['窗口大小'],cls._脚本数据[窗口标题][-1]['相对图色区域'],cls._脚本数据[窗口标题][-1]['图色数据'],cls._脚本数据[窗口标题][-1]['相对鼠标位置']
                            位图文件名称 = fr'图色数据'+os.sep+fr'{窗口标题}'.encode('utf-8').hex()+os.sep+fr'{窗口大小}_{相对图色区域}_{相对鼠标位置}'.encode('utf-8').hex()
                            os.remove(os.path.abspath(fr'{位图文件名称}.bmp'))
                            cls._脚本数据[窗口标题].pop()
                        if len(cls._脚本数据[窗口标题]) == 0:
                            del cls._脚本数据[窗口标题]
                    while 获取异步按键状态(撤回键) & 0b1000000000000000:
                        time.sleep(0.01)
                time.sleep(0.01)
        线程信息 = cls.线程池(_按键监听脚本录制器, 键码)
        return cls._脚本数据, 线程信息
    @classmethod
    def 脚本执行(cls, 脚本数据=None,误差=16,识别级别=0):
        cls._DPI感知()
        if not hasattr(cls, '_EnumWindows') or not hasattr(cls, '_lpEnumFunc'):
            cls._lpEnumFunc = ctypes.WINFUNCTYPE(ctypes.c_bool, wintypes.HWND, wintypes.LPARAM)
            cls._EnumWindows = ctypes.windll.user32.EnumWindows
            cls._EnumWindows.argtypes = [cls._lpEnumFunc, wintypes.LPARAM]
            cls._EnumWindows.restype = wintypes.BOOL
        def 识别操作(图色数据,对比图色数据,鼠标位置,窗口句柄=None):
            if 图色数据 is None:图色数据=[0]
            if 对比图色数据 is None:对比图色数据=[0]
            容错 = 误差*len(图色数据)//256
            for i,j in zip(图色数据, 对比图色数据):
                if abs(i-j) > 误差:
                    容错 -= 1
                    if 容错 < 0:
                        break
            else:
                cls.鼠标左键单击(鼠标位置,窗口句柄)
        def 窗口位置调整(窗口句柄,窗口大小,z序不变=True,显露区域=None):
            if z序不变:
                if 窗口大小 == '最大化':
                    if not ctypes.windll.user32.IsZoomed(窗口句柄):
                        ctypes.windll.user32.ShowWindow(窗口句柄, 3)
                else:
                    if not hasattr(cls, '_屏幕宽度'):cls._屏幕宽度 = ctypes.windll.user32.GetSystemMetrics(0)
                    if not hasattr(cls, '_屏幕高度'):cls._屏幕高度 = ctypes.windll.user32.GetSystemMetrics(1)
                    # if not hasattr(cls, '_工作区宽度'):cls._工作区宽度 = ctypes.windll.user32.GetSystemMetrics(16)
                    # if not hasattr(cls, '_工作区高度'):cls._工作区高度 = ctypes.windll.user32.GetSystemMetrics(17)
                    lx,ty,rx, by = cls.窗口矩形(窗口句柄)
                    if lx < 0 or ty < 0 or rx > cls._屏幕宽度 or by > cls._屏幕高度:
                        cls.调整窗口位置((0,0,窗口大小[0],窗口大小[1]),窗口句柄,1,uFlags=0x0004)
                    elif 窗口大小[0] != rx-lx or 窗口大小[1] != by-ty :
                        cls.调整窗口位置((lx,ty,窗口大小[0],窗口大小[1]),窗口句柄,1,uFlags=0x0002|0x0004)
            else:
                if 窗口大小 == '最大化':
                    if 窗口句柄 != ctypes.windll.user32.GetForegroundWindow():
                        ctypes.windll.user32.ShowWindow(窗口句柄, 6)
                        ctypes.windll.user32.ShowWindow(窗口句柄, 3)
                    elif not ctypes.windll.user32.IsZoomed(窗口句柄):
                        ctypes.windll.user32.ShowWindow(窗口句柄, 3)
                else:
                    if not hasattr(cls, '_屏幕宽度'):cls._屏幕宽度 = ctypes.windll.user32.GetSystemMetrics(0)
                    if not hasattr(cls, '_屏幕高度'):cls._屏幕高度 = ctypes.windll.user32.GetSystemMetrics(1)
                    lx,ty,rx, by = cls.窗口矩形(窗口句柄)
                    if 窗口大小[0] != rx-lx or 窗口大小[1] != by-ty or lx < 0 or ty < 0 or rx > cls._屏幕宽度 or by > cls._屏幕高度:
                        cls.调整窗口位置((0,0,窗口大小[0],窗口大小[1]),窗口句柄)
                    elif 窗口句柄 != ctypes.windll.user32.GetForegroundWindow():
                        if 窗口句柄 != cls.坐标查找窗口((显露区域[0]+lx+显露区域[2]//2,显露区域[1]+ty+显露区域[3]//2)):
                            ctypes.windll.user32.ShowWindow(窗口句柄, 6)
                            ctypes.windll.user32.ShowWindow(窗口句柄, 1)
                            句柄 = cls.坐标查找窗口((显露区域[0]+lx+显露区域[2]//2,显露区域[1]+ty+显露区域[3]//2))
                            while 窗口句柄 != 句柄:
                                ctypes.windll.user32.ShowWindow(句柄, 6)
                                句柄 = cls.坐标查找窗口((显露区域[0]+lx+显露区域[2]//2,显露区域[1]+ty+显露区域[3]//2))
        def _窗口枚举回调(窗口句柄, lParam):
            窗口标题 = cls.窗口标题(窗口句柄)
            if 窗口标题 in 脚本数据:
                数据列表 = 脚本数据[窗口标题]
                for 数据 in 数据列表:
                    窗口大小 = 数据['窗口大小']
                    相对图色区域 = 数据['相对图色区域']
                    图色数据 = 数据['图色数据']
                    相对鼠标位置 = 数据['相对鼠标位置']
                    if 识别级别 == 0:#只识别和点击前台窗口
                        if not ctypes.windll.user32.IsIconic(窗口句柄):
                            lx,ty,rx, by = cls.窗口矩形(窗口句柄)
                            鼠标位置 = lx + 相对鼠标位置[0], ty + 相对鼠标位置[1]
                            if 窗口句柄 == cls.坐标查找窗口((相对图色区域[0]+lx+相对图色区域[2]//2,相对图色区域[1]+ty+相对图色区域[3]//2)) == cls.坐标查找窗口(鼠标位置):
                                识别操作(图色数据,cls.窗口截图(相对图色区域,窗口句柄),鼠标位置)
                    elif 识别级别 == 1:#只识别和点击前台窗口, 但对于最大化、最小化、屏幕外、大小不匹配的窗口, 会尝试调整窗口为录制时的大小和状态。
                        窗口位置调整(窗口句柄,窗口大小)
                        lx,ty,rx, by = cls.窗口矩形(窗口句柄)
                        鼠标位置 = lx + 相对鼠标位置[0], ty + 相对鼠标位置[1]
                        if 窗口句柄 == cls.坐标查找窗口((相对图色区域[0]+lx+相对图色区域[2]//2,相对图色区域[1]+ty+相对图色区域[3]//2)) == cls.坐标查找窗口(鼠标位置):
                            识别操作(图色数据,cls.窗口截图(相对图色区域,窗口句柄),鼠标位置)
                    elif 识别级别 == 2:#对所有窗口进行后台识别和后台点击(可能对某些窗口失效), 对于最大化、最小化、屏幕外、大小不匹配的窗口, 会尝试调整窗口为录制时的大小和状态。
                        窗口位置调整(窗口句柄,窗口大小)
                        lx,ty,rx, by = cls.窗口矩形(窗口句柄)
                        鼠标位置 = lx + 相对鼠标位置[0], ty + 相对鼠标位置[1]
                        识别操作(图色数据,cls.窗口截图(相对图色区域,窗口句柄),鼠标位置,窗口句柄)
                    elif 识别级别 == 3:#对所有窗口强制激活到前台进行前台识别和前台点击, 对于最大化、最小化、屏幕外、大小不匹配的窗口, 会尝试调整窗口为录制时的大小和状态。
                        窗口位置调整(窗口句柄,窗口大小,False,相对图色区域)
                        lx,ty,rx, by = cls.窗口矩形(窗口句柄)
                        鼠标位置 = lx + 相对鼠标位置[0], ty + 相对鼠标位置[1]
                        识别操作(图色数据,cls.窗口截图(相对图色区域,窗口句柄),鼠标位置)
            return True # 返回True继续枚举, 返回False中止枚举
        if 脚本数据 is None:脚本数据=cls._脚本数据
        def _脚本执行():
            cls._EnumWindows(cls._lpEnumFunc(_窗口枚举回调), 0)
        线程信息 = cls.线程池(_脚本执行)
        return 线程信息



    @_方法增强
    def _GetMessage函数(主体, 包函, 原函, lpMsg: ctypes.POINTER(wintypes.MSG), hWnd: wintypes.HWND, wMsgFilterMin: wintypes.UINT, wMsgFilterMax: wintypes.UINT): # type: ignore
        if not hasattr(原函, '_GetMessage'):
            GetMessage = ctypes.windll.user32.GetMessageW
            GetMessage.argtypes = [ctypes.POINTER(wintypes.MSG), wintypes.HWND, wintypes.UINT, wintypes.UINT]
            GetMessage.restype = wintypes.BOOL
            原函._GetMessage = GetMessage
        返回值 = 原函._GetMessage(lpMsg, hWnd, wMsgFilterMin, wMsgFilterMax)
        if 返回值 == -1:
            错误码 = ctypes.get_last_error()
            raise ctypes.WinError(f"GetMessage API调用失败, 错误码：{错误码},返回值：{返回值}")
        return 返回值
    @_方法增强
    def _PeekMessage函数(主体, 包函, 原函, lpMsg: ctypes.POINTER(wintypes.MSG), hWnd: wintypes.HWND, wMsgFilterMin: wintypes.UINT, wMsgFilterMax: wintypes.UINT, wRemoveMsg: wintypes.UINT): # type: ignore
        if not hasattr(原函, '_PeekMessage'):
            PeekMessage = ctypes.windll.user32.PeekMessageW
            PeekMessage.argtypes = [ctypes.POINTER(wintypes.MSG), wintypes.HWND, wintypes.UINT, wintypes.UINT, wintypes.UINT]
            PeekMessage.restype = wintypes.BOOL
            原函._PeekMessage = PeekMessage
        返回值 = 原函._PeekMessage(lpMsg, hWnd, wMsgFilterMin, wMsgFilterMax, wRemoveMsg)
        return 返回值


    @_方法增强
    def _WNDPROC类型函数(主体, 包函, 原函):
        if not hasattr(原函, '_WNDPROC'):
            # WNDPROC Wndproc;
            # LRESULT Wndproc(
            # HWND unnamedParam1,
            # UINT unnamedParam2,
            # WPARAM unnamedParam3,
            # LPARAM unnamedParam4
            # )
            # {...}


            # typedef LRESULT (CALLBACK* WNDPROC)(HWND, UINT, WPARAM, LPARAM);unnamedParam1unnamedParam4

            WNDPROC = ctypes.WINFUNCTYPE(
                wintypes.LPARAM,  # 返回值
                wintypes.HWND,      # hwnd  
                wintypes.UINT,      # msg   
                wintypes.WPARAM,    # wParam
                wintypes.LPARAM     # lParam
            )
            原函._WNDPROC = WNDPROC
        return 原函._WNDPROC
    
    @_方法增强
    def _WNDCLASSEXW类型函数(主体, 包函, 原函):
        
        if not hasattr(原函, '_WNDCLASSEXW类型'):
            # typedef struct tagWNDCLASSEXW {
            #   UINT      cbSize;
            #   UINT      style;
            #   WNDPROC   lpfnWndProc;
            #   int       cbClsExtra;
            #   int       cbWndExtra;
            #   HINSTANCE hInstance;
            #   HICON     hIcon;
            #   HCURSOR   hCursor;
            #   HBRUSH    hbrBackground;
            #   LPCWSTR   lpszMenuName;
            #   LPCWSTR   lpszClassName;
            #   HICON     hIconSm;
            # } WNDCLASSEXW, *PWNDCLASSEXW, *NPWNDCLASSEXW, *LPWNDCLASSEXW;

            class WNDCLASSEXW(ctypes.Structure):
                _fields_ = [
                    ("cbSize", wintypes.UINT),
                    ("style", wintypes.UINT),
                    ("lpfnWndProc", 主体._WNDPROC类型函数()),
                    ("cbClsExtra", wintypes.INT),
                    ("cbWndExtra", wintypes.INT),
                    ("hInstance", wintypes.HINSTANCE),
                    ("hIcon", wintypes.HICON),
                    ("hCursor", wintypes.HANDLE),
                    ("hbrBackground", wintypes.HBRUSH),
                    ("lpszMenuName", wintypes.LPCWSTR),
                    ("lpszClassName", wintypes.LPCWSTR),
                    ("hIconSm", wintypes.HICON),
                ]
            原函._WNDCLASSEXW类型 = WNDCLASSEXW
        return 原函._WNDCLASSEXW类型

    @_方法增强
    def _WNDCLASSEXW对象函数(主体, 包函, 原函, 过程函数:callable, style:int=0x0002|0x0001, cbClsExtra:int=0, cbWndExtra:int=0, hInstance:int=ctypes.windll.kernel32.GetModuleHandleW(None), hIcon:int=0, hCursor:int=ctypes.windll.user32.LoadCursorW(0, 32512), hbrBackground:int=ctypes.windll.gdi32.GetStockObject(0), lpszMenuName:int=0, lpszClassName:str='默认窗口', hIconSm:int=0)->int:
    # def _WNDCLASSEXW对象函数(主体, 包函, 原函, 过程函数:callable):
        _WNDCLASSEXW类型 = 主体._WNDCLASSEXW类型函数()
        _WNDCLASSEXW对象 = _WNDCLASSEXW类型()
        _WNDCLASSEXW对象.cbSize = ctypes.sizeof(_WNDCLASSEXW类型)
        _WNDCLASSEXW对象.style = style
        _WNDCLASSEXW对象.lpfnWndProc = 主体._WNDPROC类型函数()(过程函数)
        _WNDCLASSEXW对象.cbClsExtra = cbClsExtra
        _WNDCLASSEXW对象.cbWndExtra = cbWndExtra
        _WNDCLASSEXW对象.hInstance = hInstance
        _WNDCLASSEXW对象.hIcon = hIcon
        _WNDCLASSEXW对象.hCursor = hCursor
        _WNDCLASSEXW对象.hbrBackground = hbrBackground
        _WNDCLASSEXW对象.lpszMenuName = lpszMenuName
        _WNDCLASSEXW对象.lpszClassName = lpszClassName
        _WNDCLASSEXW对象.hIconSm = hIconSm


        return _WNDCLASSEXW对象
    
    @_方法增强
    def _DefWindowProc函数(主体, 包函, 原函, hWnd: wintypes.HWND, Msg: wintypes.UINT, wParam: wintypes.WPARAM, lParam: wintypes.LPARAM)->wintypes.LPARAM:
        if not hasattr(原函, '_DefWindowProc'):
            # LRESULT DefWindowProcW(
            # [in] HWND   hWnd,
            # [in] UINT   Msg,
            # [in] WPARAM wParam,
            # [in] LPARAM lParam
            # );
            
            DefWindowProcW = ctypes.windll.user32.DefWindowProcW
            DefWindowProcW.argtypes = [wintypes.HWND, wintypes.UINT, wintypes.WPARAM, wintypes.LPARAM]
            DefWindowProcW.restype = wintypes.LPARAM
            原函._DefWindowProc = DefWindowProcW
        return 原函._DefWindowProc(hWnd, Msg, wParam, lParam)

    @_方法增强
    def _RegisterClassEx函数(主体, 包函, 原函, unnamedParam1):

        if not hasattr(原函, '_RegisterClassEx'):

            # ATOM RegisterClassExW(
            # [in] const WNDCLASSEXW *unnamedParam1
            # );

            RegisterClassEx = ctypes.windll.user32.RegisterClassExW
            RegisterClassEx.argtypes = [ctypes.POINTER(主体._WNDCLASSEXW类型函数())]
            RegisterClassEx.restype = wintypes.ATOM
            原函._RegisterClassEx = RegisterClassEx

        返回值 = 原函._RegisterClassEx(unnamedParam1)
        if 返回值 == 0:
            raise Exception(fr"注册窗口类失败, 错误码：{ctypes.get_last_error()}")
        return 返回值

    @_方法增强
    def _CreateWindowEx函数(主体, 包函, 原函, dwExStyle:int=0, lpClassName:str='默认窗口', lpWindowName:str='默认窗口', dwStyle:int=0x10000000|0x00000000 | 0x00C00000 | 0x00080000 | 0x00040000 | 0x00020000 | 0x00010000, X:int=0x80000000, Y:int=0x80000000, nWidth:int=0x80000000, nHeight:int=0x80000000, hWndParent:int=0, hMenu:int=0, hInstance:int=ctypes.windll.kernel32.GetModuleHandleW(None), lpParam:int=0)->int:
        if not hasattr(原函, '_CreateWindowEx'):
            # HWND CreateWindowExW(
            # [in]           DWORD     dwExStyle,
            # [in, optional] LPCWSTR   lpClassName,
            # [in, optional] LPCWSTR   lpWindowName,
            # [in]           DWORD     dwStyle,
            # [in]           int       X,
            # [in]           int       Y,
            # [in]           int       nWidth,
            # [in]           int       nHeight,
            # [in, optional] HWND      hWndParent,
            # [in, optional] HMENU     hMenu,
            # [in, optional] HINSTANCE hInstance,
            # [in, optional] LPVOID    lpParam
            # );

            CreateWindowEx = ctypes.windll.user32.CreateWindowExW
            CreateWindowEx.argtypes = [wintypes.DWORD, wintypes.LPCWSTR, wintypes.LPCWSTR, wintypes.DWORD, wintypes.INT, wintypes.INT, wintypes.INT, wintypes.INT, wintypes.HWND, wintypes.HMENU, wintypes.HINSTANCE, wintypes.LPVOID]
            CreateWindowEx.restype = wintypes.HWND
            原函._CreateWindowEx = CreateWindowEx

        # 创建窗口
        _hwnd = 原函._CreateWindowEx(dwExStyle, lpClassName, lpWindowName, dwStyle, X, Y, nWidth, nHeight, hWndParent, hMenu, hInstance, lpParam)
        if not _hwnd:
            raise Exception("创建窗口失败")
        return _hwnd

    @_方法增强
    def _GetMessage循环(主体, 包函, 原函):
        msg = wintypes.MSG()
        pMsg = ctypes.byref(msg)
        while ctypes.windll.user32.GetMessageW(pMsg, 0, 0, 0) > 0:
            ctypes.windll.user32.TranslateMessage(pMsg)
            ctypes.windll.user32.DispatchMessageW(pMsg)



    class 窗口类:
        def __init__(self, dwExStyle:int=0, lpClassName:str='默认窗口', lpWindowName:str='默认窗口', dwStyle:int=0x10000000|0x00000000 | 0x00C00000 | 0x00080000 | 0x00040000 | 0x00020000 | 0x00010000, X:int=0x80000000, Y:int=0x80000000, nWidth:int=0x80000000, nHeight:int=0x80000000, hWndParent:int=0, hMenu:int=0, hInstance:int=ctypes.windll.kernel32.GetModuleHandleW(None), lpParam:int=0):

            # 注册窗口类
            self.注册窗口类(过程函数=self.窗口过程函数,lpszClassName=lpClassName)

            # 创建窗口，返回窗口的句柄 hwnd
            self._hwnd = 脚本工具._CreateWindowEx函数(dwExStyle, lpClassName, lpWindowName, dwStyle, X, Y, nWidth, nHeight, hWndParent, hMenu, hInstance, lpParam)

            # 消息循环
            脚本工具._GetMessage循环()

        def 注册窗口类(self, 过程函数:callable, style:int=0x0002|0x0001, cbClsExtra:int=0, cbWndExtra:int=0, hInstance:int=ctypes.windll.kernel32.GetModuleHandleW(None), hIcon:int=0, hCursor:int=ctypes.windll.user32.LoadCursorW(0, 32512), hbrBackground:int=ctypes.windll.gdi32.GetStockObject(0), lpszMenuName:int=0, lpszClassName:str='默认窗口', hIconSm:int=0):
            if not hasattr(self, '_窗口类字典'):self._窗口类字典 = {}
            if not lpszClassName in self._窗口类字典:
                self._窗口类字典[lpszClassName] = 脚本工具._WNDCLASSEXW对象函数(过程函数, style, cbClsExtra, cbWndExtra, hInstance, hIcon, hCursor, hbrBackground, lpszMenuName, lpszClassName, hIconSm)
                脚本工具._RegisterClassEx函数(unnamedParam1 = ctypes.byref(self._窗口类字典[lpszClassName]))
            return self._窗口类字典

        def 创建窗口(self, dwExStyle:int=0, lpClassName:str='默认窗口', lpWindowName:str='默认窗口', dwStyle:int=0x10000000|0x00000000 | 0x00C00000 | 0x00080000 | 0x00040000 | 0x00020000 | 0x00010000, X:int=0x80000000, Y:int=0x80000000, nWidth:int=0x80000000, nHeight:int=0x80000000, hWndParent:int=0, hMenu:int=0, hInstance:int=ctypes.windll.kernel32.GetModuleHandleW(None), lpParam:int=0):
            return 脚本工具._CreateWindowEx函数(dwExStyle, lpClassName, lpWindowName, dwStyle, X, Y, nWidth, nHeight, hWndParent, hMenu, hInstance, lpParam)

        def 窗口过程函数(self, hwnd, msg, wParam, lParam):


            if msg == 0x0002:
                ctypes.windll.user32.PostQuitMessage(0)
                return 0
            if msg == 0x000F:# WM_PAINT, 绘制窗口
                self.绘制窗口()
                return 0
            else:
                return 脚本工具._DefWindowProc函数(hwnd, msg, wParam, lParam)
            
        def 绘制窗口(self):
            pass

        def 设置背景图片(self,hwnd,RGBA数据:bytes,宽:int,高:int):

            assert len(RGBA数据) == 宽 * 高 * 4, "RGBA数据格式错误"

            窗口设备上下文句柄 = ctypes.windll.user32.GetWindowDC(hwnd)
            内存设备上下文句柄 = ctypes.windll.gdi32.CreateCompatibleDC(窗口设备上下文句柄)
            _BITMAPINFO结构体 = 脚本工具._BITMAPINFO对象()
            lx,ty,rx, by = 脚本工具.窗口矩形(hwnd);x,y,w, h = 0,0,rx-lx, by-ty

            _BITMAPINFO结构体.bmiHeader.biWidth = 宽
            _BITMAPINFO结构体.bmiHeader.biHeight = -高 # 负值表示自上而下更符合现代编程习惯
            _BITMAPINFO结构体.bmiHeader.biBitCount = 4 * 8

            像素数据指针 = wintypes.LPVOID()
            位图句柄 = 脚本工具._CreateDIBSection函数(内存设备上下文句柄, ctypes.byref(_BITMAPINFO结构体), 0, ctypes.byref(像素数据指针), None, 0)

            ctypes.memmove(像素数据指针.value, (ctypes.c_ubyte * (宽 * 高 * 4)).from_buffer(RGBA数据), (宽 * 高 * 4))

            原对象句柄 = 脚本工具._SelectObject函数(内存设备上下文句柄, 位图句柄)

            StretchBlt操作结果 = 脚本工具._StretchBlt函数(窗口设备上下文句柄, 0, 0, w, h, 内存设备上下文句柄, 0, 0, 宽, 高, 0xCC0020)


from PIL import Image



窗口 = 脚本工具.窗口类(
    dwStyle=0x01000000|0x80000000|0x10000000,
)



