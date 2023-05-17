import os

class File:

    def __init__(self, name, extension):
        self.name = name
        self.extension = extension
        self.type = extension
        self.path = self.name+'.'+self.extension
    
    def write(self, content):
        with open(self.path, 'w') as f:
            f.write(content)
    
    def read(self):
        with open(self.path, 'r') as f:
            return f.read()
    
    def clear(self):
        os.remove(self.path)


file1 = File('students-report', 'txt')
# file1.write('NAME: Almustapha Ahmad\nAGE: 21')

file2 = File('image-file', 'png')
# file2.clear()

class PDF(File):

    def send(self):
        print("You are about to send this PDF File")
        self.email = input("Enter the email to send this file to: ")
        print("File sent to "+self.email+' successfully')


file3 = PDF('example-file', 'pdf')
file3.write('Some example')
file3.clear()