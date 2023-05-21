from abc import ABC, abstractmethod


class InvalidOperationException(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.open = False

    def open(self):
        if self.open:
            raise InvalidOperationException("Stream is already open")
        self.open = True

    def close(self):
        if not self.open:
            raise InvalidOperationException("Stream is already closed")
        self.open = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from file...")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from network...")


class MemoryStream(Stream):
    def read(self):
        print("Reading data from memory...")
