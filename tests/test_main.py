import binascii
import ctypes
import os
import unittest


def getDirPath():
    return (
        os.path.dirname(os.path.realpath(__file__)) + "/../build/main.dll"
        if os.name == "nt"
        else os.path.dirname(os.path.realpath(__file__)) + "/../build/main.so"
    )


class TestMainMethod(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestMainMethod, self).__init__(*args, **kwargs)
        self.data = b"TEST_DATA"
        self.output = b"f92eb8174577afd80849d6a026aa7d4c5d18b9d8b97dce631001001ad9dd7000164fc97a811851014ed0558212fbd8f9e1ab9b14ac414657da7fb3695db1049618857db913be1b61eff7a9e036db46ca57a927822428cce6a48887322fb5a294522435c671efa3733c393f104833ea35897ad783d4ef204af5a9a67814f7e84d78e437f627019fc270bbe9ed309291d0a5f6bf98bfae0f750538ba56646f7327032494458d1583e1d1252d8eb9620e01d7ebcd61b08d189013257352c05d2978c9328398a6c577c7cee14c37bec0c9c012d38fababbc0dd2dc6bd7a55bf27151"
        self.segment_size = 16384
        self.data_shards = 4
        self.parity_shards = 2
        self.data_rendundancy_fct = ctypes.cdll.LoadLibrary(
            getDirPath()
        ).GenerateDataRedundancy

    def test_generate_data_redundancy(self):
        c_data = ctypes.c_char_p(self.data)
        self.data_rendundancy_fct.argtypes = [
            ctypes.c_int,
            ctypes.c_int,
            ctypes.c_int,
            ctypes.c_int,
            ctypes.c_char_p,
        ]
        self.data_rendundancy_fct.restype = ctypes.c_void_p
        self.assertEqual(
            ctypes.string_at(
                self.data_rendundancy_fct(
                    self.segment_size,
                    self.data_shards,
                    self.parity_shards,
                    len(self.data),
                    c_data,
                ),
                224,
            ),
            binascii.unhexlify(self.output),
        )


if __name__ == "__main__":
    unittest.main()
