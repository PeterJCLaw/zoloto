import json
import os
from functools import lru_cache
from typing import NamedTuple

from cv2 import FILE_STORAGE_READ, FileStorage, aruco
from numpy import array

CalibrationParameters = NamedTuple(
    "CalibrationParameters",
    [("camera_matrix", array), ("distance_coefficients", array)],
)


@lru_cache()
def parse_calibration_file(calibration_file: str) -> CalibrationParameters:
    _, file_extension = os.path.splitext(calibration_file)
    if file_extension == ".json":
        with open(calibration_file) as f:
            mtx, dist = json.load(f)
            return CalibrationParameters(array(mtx), array(dist))
    if file_extension == ".xml":
        storage = FileStorage(calibration_file, FILE_STORAGE_READ)
        params = CalibrationParameters(
            storage.getNode("cameraMatrix").mat(), storage.getNode("dist_coeffs").mat()
        )
        storage.release()
        return params
    else:
        raise ValueError("Unknown calibration file format: " + calibration_file)


def save_calibrations(params: CalibrationParameters, filename: str):
    with open(filename, "w") as f:
        json.dump(
            [params.camera_matrix.tolist(), params.distance_coefficients.tolist()], f
        )


@lru_cache()
def get_fake_calibration_parameters(
    size: int, iterations: int = 15
) -> CalibrationParameters:
    """
    HACK: Generate fake calibration parameters
    """
    assert iterations >= 10
    dictionary = aruco.getPredefinedDictionary(aruco.DICT_6X6_1000)
    seen_corners = []
    seen_ids = []
    image_size = (size, size)
    board = aruco.CharucoBoard_create(6, 6, 0.025, 0.0125, dictionary)
    for i in range(iterations):
        image = board.draw(image_size)
        corners, ids, _ = aruco.detectMarkers(image, dictionary)
        _, corners, ids = aruco.interpolateCornersCharuco(corners, ids, image, board)
        seen_corners.append(corners)
        seen_ids.append(ids)
    ret, mtx, dist, _, _ = aruco.calibrateCameraCharuco(
        seen_corners, seen_ids, board, image_size, None, None
    )
    return CalibrationParameters(mtx, dist)
