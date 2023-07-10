class MyInt(int):
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
