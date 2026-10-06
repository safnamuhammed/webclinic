class PlayfairCipher:
    def __init__(self, keyword):
        self.keyword = ''.join(filter(str.isalpha, keyword.upper()))
        if not self.keyword:
            raise ValueError("Keyword must contain letters")
        self.matrix = self._generate_matrix()
    
    def _generate_matrix(self):
        chars = []
        for char in self.keyword:
            if char not in chars and char != 'J':
                chars.append(char)
            elif char == 'J' and 'I' not in chars:
                chars.append('I')
        
        alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
        for char in alphabet:
            if char not in chars:
                chars.append(char)
        
        return [chars[i:i+5] for i in range(0, 25, 5)]
    
    def _find_pos(self, char):
        if char == 'J':
            char = 'I'
        for i in range(5):
            for j in range(5):
                if self.matrix[i][j] == char:
                    return (i, j)
        return None
    
    def _prepare(self, text):
        text = ''.join(filter(str.isalpha, text.upper())).replace('J', 'I')
        digraphs = []
        i = 0
        while i < len(text):
            if i + 1 >= len(text):
                digraphs.append(text[i] + 'X')
                break
            if text[i] == text[i+1]:
                digraphs.append(text[i] + 'X')
                i += 1
            else:
                digraphs.append(text[i] + text[i+1])
                i += 2
        return digraphs
    
    def _encrypt_pair(self, pair):
        r1, c1 = self._find_pos(pair[0])
        r2, c2 = self._find_pos(pair[1])
        if r1 == r2:
            return self.matrix[r1][(c1+1)%5] + self.matrix[r2][(c2+1)%5]
        elif c1 == c2:
            return self.matrix[(r1+1)%5][c1] + self.matrix[(r2+1)%5][c2]
        else:
            return self.matrix[r1][c2] + self.matrix[r2][c1]
    
    def _decrypt_pair(self, pair):
        r1, c1 = self._find_pos(pair[0])
        r2, c2 = self._find_pos(pair[1])
        if r1 == r2:
            return self.matrix[r1][(c1-1)%5] + self.matrix[r2][(c2-1)%5]
        elif c1 == c2:
            return self.matrix[(r1-1)%5][c1] + self.matrix[(r2-1)%5][c2]
        else:
            return self.matrix[r1][c2] + self.matrix[r2][c1]
    
    def encrypt(self, text):
        digraphs = self._prepare(text)
        return ' '.join(self._encrypt_pair(d) for d in digraphs)
    
    def decrypt(self, text):
        text = ''.join(text.split())
        pairs = [text[i:i+2] for i in range(0, len(text), 2)]
        return ''.join(self._decrypt_pair(p) for p in pairs)


print("PLAYFAIR CIPHER - Encrypt & Decrypt")


keyword = input("\nEnter keyword: ").strip()
while not keyword:
    keyword = input("Keyword cannot be empty. Enter keyword: ").strip()

message = input("Enter message to encrypt: ").strip()
while not message:
    message = input("Message cannot be empty. Enter message: ").strip()

cipher = PlayfairCipher(keyword)

print("\n Playfair Matrix:")
print("-" * 25)
for row in cipher.matrix:
    print("| " + " | ".join(row) + " |")
print("-" * 25)

encrypted = cipher.encrypt(message)
print(f"\n Encrypted: {encrypted}")
decrypted = cipher.decrypt(encrypted)
print(f" Decrypted: {decrypted}")


original_clean = ''.join(filter(str.isalpha, message.upper())).replace('J', 'I')
print("\n" )
print("VERIFICATION")

if original_clean == decrypted:
    print(" Success! Decryption matches the original message!")
else:
    print(f"  Note: Decrypted '{decrypted}' differs from '{original_clean}'")
    print("   (This is normal due to 'X' insertion and J/I replacement)")
