# Context manager : quan ly tai nguyen

# normal
# f = open("sample.txt","w")
# f.write("Hello, world!")
# f.close()
# print(f.closed)

# context manager
# with open("sample.txt", "w") as f:
#     f.write("Hello, world! python")

# print(f.closed)

from contextlib import contextmanager
class writefile():
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
    def __enter__(self):
        self.file = open(self.file_name, self.mode)
        return self.file
    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

@contextmanager
def write_file(filename, mode):
    f = open(filename, mode)
    yield f
    f.close()

with write_file("sample.text","w") as f:
    f.write("Hello")
print(f.closed)

