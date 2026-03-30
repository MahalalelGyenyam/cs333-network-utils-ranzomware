FILE_NAME=test.bin

def to_bin(var):
    print("Write var to disk in binary format")

def from_bin(file):
    print("Reading binary file to mem")

if __name__ == "__main__":
    print("In the main file")
    to_bin(10)
    from_bin()
    var = from_bin()
    print(var)

class Packet:
    def __init__(self, source_ip, dest_ip, payload):
        self.source_ip = source_ip
        self.dest_ip = dest_ip
        self.payload = payload

    def __str__(self):
        return f"Packet from {self.source_ip} to {self.dest_ip} with payload: {self.payload}"
