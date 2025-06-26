# Copyright 2025 by Alon Gil-Ad
# Center for Intelligent Systems (CIS), Faculty of Computer Science
# Technion - Israel Institute of Technology
# https://github.com/AlonGil-Ad/simple_mocap

from multiprocessing import Lock

class Asset:
    _id_num: int = None
    _name: str = None
    _tracking_valid: bool = False
    _position = None
    _rotation = None
    _mutex = Lock()

    def __init__(self, id_num: int, name: str):
        self._id_num = id_num
        self._name = name

    def get_id_num(self):
        return self._id_num

    def get_name(self):
        return self._name

    def set_location(self, position: tuple, rotation: tuple):
        with self._mutex:
            self._position = position
            self._rotation = rotation
            self._tracking_valid = True

    def get_location(self) -> tuple or None:
        with self._mutex:
            if not self._tracking_valid:
                return None, None
            return self._position, self._rotation

    def set_tracking_invalid(self):
        with self._mutex:
            self._tracking_valid = False
            self._position = None
            self._rotation = None

    def is_tracking_valid(self):
        with self._mutex:
            return self._tracking_valid

    def __eq__(self, other):
        # print(f'{other} of type {type(other)}')
        if isinstance(other, Asset):
            # print(f'{other} is type(Asset)')
            if other.get_id_num() == self.get_id_num() and other.get_name() == self.get_name():
                return True
            else:
                return False
        if isinstance(other, int):
            if other == self.get_id_num():
                return True
            else:
                return False
        if isinstance(other, str):
            if other == self.get_name():
                return True
            else:
                return False
        return False

    def __str__(self):
        return (f'Name: {self.get_name()}, ' +
                f'ID: {self.get_id_num()}')
                # f'ID: {self.get_id_num()}, ' +
                # f'tracking {"is valid" if self.is_tracking_valid() else "invalid"}')


