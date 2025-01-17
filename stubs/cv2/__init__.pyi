"""
Type stubs for cv2.
Note that stubs are only written for the parts that we use.
"""
from typing import List, Optional, Tuple, Union

from numpy.typing import NDArray

CAP_PROP_BUFFERSIZE: int
CAP_PROP_FPS: int
CAP_PROP_FRAME_WIDTH: int
CAP_PROP_FRAME_HEIGHT: int
CAP_PROP_FRAME_COUNT: int

FILE_STORAGE_READ: int

BORDER_CONSTANT: int

class aruco_DetectorParameters:
    pass

class FileNode:
    def mat(self) -> NDArray: ...
    def at(self, position: int) -> FileNode: ...
    def real(self) -> float: ...

class FileStorage:
    def __init__(self, path: str, mode: int) -> None: ...
    def getNode(self, nodename: str) -> FileNode: ...
    def release(self) -> None: ...
    def write(self, nodename: str, data: NDArray) -> None: ...

class VideoCapture:
    def __init__(self, camera_id: Union[int, str]) -> None: ...
    def isOpened(self) -> bool: ...
    def read(self) -> Tuple[bool, NDArray]: ...
    def release(self) -> None: ...
    def set(self, property: int, value: int) -> None: ...
    def get(self, property: int) -> float: ...

class VideoWriter_fourcc:
    def __init__(self, c1: str, c2: str, c3: str, c4: str): ...

class VideoWriter:
    def __init__(
        self,
        filename: str,
        fourcc: VideoWriter_fourcc,
        fps: float,
        frameSize: List[int],
    ): ...
    def write(self, frame: NDArray) -> None: ...
    def release(self) -> None: ...

class aruco_Dictionary:
    bytesList: NDArray
    markerSize: int

def imread(path: str) -> NDArray: ...
def copyMakeBorder(
    src: NDArray,
    top: int,
    bottom: int,
    left: int,
    right: int,
    borderType: int,
    value: Optional[List[int]],
) -> NDArray: ...
def imshow(winname: str, mat: NDArray) -> None: ...
def imwrite(filename: str, mat: NDArray) -> None: ...
def waitKey(delay: int) -> int: ...

# Note that this is not the only signature of Rodrigues, but it is the only one we use.
def Rodrigues(vector: Tuple[float, float, float]) -> Tuple[NDArray, NDArray]: ...

class error(Exception): ...
