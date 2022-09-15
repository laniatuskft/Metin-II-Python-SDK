# ----------------------------------------------------------------------------------------
#	Copyright © 2021 - 2022 Laniatus Games Studio Inc. Software System and Partition T.F
#	This class can be used by anyone provided that the copyright notice remains intact.
#
#	This class is used to replicate the ability to pass arguments by reference in Python.
# ----------------------------------------------------------------------------------------
class RefObject:
    def __init__(self, ref_arg):
        self.arg_value = ref_arg