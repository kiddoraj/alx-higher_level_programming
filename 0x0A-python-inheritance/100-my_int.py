#!/usr/bin/python3
""" class MyInt that inherits from int:
"""
class MyInt(int):
	""" Class """
    def __eq__(self, other):
        """
        Inverts the behavior of the == operator.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the behavior of the != operator.
        """
        return super().__eq__(other)
