class KeyboardService:
    """A keyboard service inteface."""
    def is_key_down(self, key):
        """detects if the given key is being pressed"""
        raise NotImplementedError

    def is_key_pressed(self, key):
        raise NotImplementedError

    def is_key_released(self, key):
        raise NotImplementedError

    def is_key_up(self, key):
        raise NotImplementedError
        

    