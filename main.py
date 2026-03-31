FILE_NAME=test.bin

# Example how to open a file and print content 
#
# f = open("demofile.txt", "r")
# print(f.read())

# "r" - Read - Default value. Opens a file for reading
# "a" - Append - Opens a file for appending, creates if doesn't exist
# "w" - Write - Opens a file for writing, creates file if doesn't exist
# "x" - Create - Creates the specified file, returns an error if file exist

# TO-DO:
# - Take string input (Use array then file)
# - Split the string into sections
# - Convert string to int
# - Convert into to bin
# - Write bin to file



# - Read bin from file
# - Convert bin to int
# - Convert int to string
def to_bin(var):
    print("Write var to disk in binary format")
    
    # Converts the int to 8-bit binary string
    binary_data = format(var, '08b')  

    f = open("demofile.txt", "a")
    print(f.read())
    
    with open ("demofile.txt", "a") as f:
        f.write(binary_data)
    
    print("Wrote to text file in binary format.")

def from_bin(file):
    print("Reading binary file to mem")

if __name__ == "__main__":
    # print("In the main file")
    # to_bin(10)
    # from_bin()
    # var = from_bin()
    # print(var)
    
    
    # This is how it'd look like if we were to read from a file and print the content
    to_bin(10)
    var = from_bin("demofile.txt")
    print(var)

class Packet:
    def __init__(self, source_ip, dest_ip, payload):
        self.source_ip = source_ip
        self.dest_ip = dest_ip
        self.payload = payload

    def __str__(self):
        return f"Packet from {self.source_ip} to {self.dest_ip} with payload: {self.payload}"
