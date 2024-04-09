

# file_descriptors=[]
# for i in range(10000000):
#     file_descriptors.append(open('test.txt', 'w'))


class ContxtManager():
    def __init__(self):
        print('init')

    def __enter__(self):
        print('enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')
        return True


class FileManager():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return True
    

for i in range(1000):
    with FileManager('test.txt', 'w') as f:
        f.write('Hello, World!')    