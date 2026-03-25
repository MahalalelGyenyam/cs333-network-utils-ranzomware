def main():
    print("Hello from cs333-network-utils-ranzomware!")


if __name__ == "__main__":
    main()

class Packet:
    def __init__(self, source_ip, dest_ip, payload):
        self.source_ip = source_ip
        self.dest_ip = dest_ip
        self.payload = payload

    def __str__(self):
        return f"Packet from {self.source_ip} to {self.dest_ip} with payload: {self.payload}"
