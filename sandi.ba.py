def encode(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ba_patterns = {alphabet[i]: "ba" * (i + 1) for i in range(26)}
    
    encoded_text = []
    for char in text:
        if char == " ":
            encoded_text.append("....")
        elif char in ba_patterns:
            encoded_text.append(ba_patterns[char] + ".")
    return "".join(encoded_text).rstrip(".")

def decode(encoded_text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ba_patterns = {"ba" * (i + 1): alphabet[i] for i in range(26)}
    
    words = encoded_text.split("....")
    decoded_text = []
    for word in words:
        decoded_word = [ba_patterns[pattern] for pattern in word.split(".") if pattern in ba_patterns]
        decoded_text.append("".join(decoded_word))
    return " ".join(decoded_text)

# Contoh penggunaan
encoded_text = "ba.baba.bababa"
decoded_text = decode(encoded_text)

print("Teks Terenkode:", encoded_text)
print("Teks Terdekode:", decoded_text)
