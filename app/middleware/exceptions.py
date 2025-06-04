class NotFoundException(Exception):
    def __init__(self, detail="Resource not found"):
        self.detail = detail
