def generate_header(pkt_type, ID):
    # Initialize header as a 32-bit unsigned integer (value 0)
    header = 0

    # Set bits 4:0 to ID
    header |= (ID & 0b11111)  # Mask to ensure only 5 bits are set

    # Set bits 14:12 to pktType
    header |= (pkt_type & 0b111) << 12  # Shift pktType to position 12

    # Set bits 20:16 to -1 (all bits set to 1, 5 bits)
    header |= 0b11111 << 16

    # Set bits 27:21 to -1 (all bits set to 1, 7 bits)
    header |= 0b1111111 << 21

    # Set bit 31 based on xor_reduce of bits 30:0
    # Calculate xor of bits 30:0
    xor_reduce = 0
    for i in range(31):
        xor_reduce ^= (header >> i) & 1

    # If xor_reduce is 0, set bit 31 to 1, otherwise 0
    header |= (0 if xor_reduce else 1) << 31

    return header

# Example usage
header = generate_header(pkt_type=0, ID=1)
print(f"Generated header: {header}")  # Print as 32-bit binary 