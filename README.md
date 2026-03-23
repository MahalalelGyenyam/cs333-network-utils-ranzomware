# cs333-Network-Utils-Ranzomware

This repo is a collection of network utilities

## Group Members

- Mahala Solorzano
- Eben Meyer
- Chris Shoemaker

## Quick Start


## Network Packet Structure
### Core structure
- Header: The header of a network packet is the part that contains the instructions and descriptive details of the packet. It contains information such as the length of the packet itself, the packet's number in a sequence of other packets, the destination, and the origin address. Additionally, the packet header has the protocol included to identify the type of information carried in the payload. The header size is variable depending on the amount of information, as well as what format is being used.
  
- Payload: The size of a payload can vary. The total packet size typically includes the header and payload, but it can't exceed the MTU (Maximum Transmission Unit). The max for a typical standard Ethernet is 1500 bytes. When the header is sent along with the payload, the header is stripped.
  
- Footer or Trailer: Differs from each network Type. Contains a few bits that inform the recipient device that it has reached the end of the packet, as well as a CRC (Cyclic Redundancy Check), which enables the PC to determine whether all packets were received in full. 

### Data Structure
- Writing a class as the data structure for a network packet
- Needs to match the TCP Packet Format



## Sources
- Tech Target (https://www.techtarget.com/searchnetworking/definition/packet)
- Axclusive ISP (https://www.axclusive.com.sg/what-is-packet-in-networking/)
- LiveAction (https://www.liveaction.com/resources/blog-post/what-is-a-network-packet/)
- HowStuffWorks (https://computer.howstuffworks.com/question525.htm)
