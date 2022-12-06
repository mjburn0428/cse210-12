class VideoService:
    """A video service inteface."""

    def clear_buffer(self):
        raise NotImplementedError
    
    def draw_image(self, image, position):
        raise NotImplementedError

    def draw_rectangle(self, size, position, color):
        raise NotImplementedError

    def draw_text(self, text, position):
        raise NotImplementedError

    def flush_buffer(self):
        raise NotImplementedError

    def initialize(self):
        raise NotImplementedError

    def is_window_open(self):
        raise NotImplementedError

    def load_fonts(self, directory):
        raise NotImplementedError

    def load_images(self, directory):
        raise NotImplementedError

    def release(self):
        raise NotImplementedError
    
    def unload_fonts(self):
        raise NotImplementedError

    def unload_images(self):
        raise NotImplementedError