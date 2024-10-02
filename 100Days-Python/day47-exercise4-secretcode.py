def encode():
    st = input("Message: ")
    words = st.split(" ")
    nword = []
    for i in words:
        if len(i) >= 3:
            r1 = "apf"  # Random starting string
            r2 = "lqw"  # Random ending string
            sts = r1 + i[1:] + i[0] + r2  # Remove first letter, append at the end, add random strings
            nword.append(sts)
        else:
            nword.append(i[::-1])  # Reverse the word if less than 3 characters
    print("Encoded message:", " ".join(nword))

def decode():
    st = input("Message: ")
    words = st.split(" ")
    nword = []
    for i in words:
        if len(i) >= 3:
            sts = i[3:-3]  # Remove the 3 random characters at the start and end
            final = sts[-1] + sts[:-1]  # Move the last letter to the beginning
            nword.append(final)
        else:
            nword.append(i[::-1])  # Reverse the word if less than 3 characters
    print("Decoded message:", " ".join(nword))

while True:
    print("\n1. Encode\n2. Decode\n3. Quit\n")
    ch = int(input("Choice: "))

    if ch == 1:
        encode()
    elif ch == 2:
        decode()
    elif ch == 3:
        break
    else:
        print("Invalid (Choice between 1 - 3)\n")
