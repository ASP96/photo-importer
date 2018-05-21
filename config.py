#!/usr/bin/python3

import configparser
import os


class Config(object):
    DEFAULT_CONFIG_FILE = os.path.expanduser('~/.photo-importer.cfg')
    DEFAULTS = {
        'main': {
            'out_time_format': '%%Y-%%m-%%d_%%H-%%M-%%S',
            'out_date_format': '%%Y-%%m-%%d',
            'out_subdir_image': 'Foto',
            'out_subdir_video': 'Video',
            'out_subdir_audio': 'Audio',
            'time_src_image': 'exif,name',
            'time_src_video': 'exif,name,attr',
            'time_src_audio': 'exif,name,attr',
            'remove_garbage': 1,
            'remove_empty_dirs': 1,
            'move_mode': 0,
            'threads_count': 2,
        }
    }

    def __init__(self, filename=None, create=False):
        if filename is None:
            filename = self.DEFAULT_CONFIG_FILE

        self.__config = configparser.ConfigParser()
        self.__config.read_dict(self.DEFAULTS)
        self.__config.read([filename, ])

        if create:
            self.__create_if_not_exists()

    def __create_if_not_exists(self):
        if os.path.exists(self.DEFAULT_CONFIG_FILE):
            return

        with open(self.DEFAULT_CONFIG_FILE, 'w') as conffile:
            self.__config.write(conffile)

    def __getitem__(self, sect):
        return self.__config[sect]


if __name__ == "__main__":
    Config(create=True)
