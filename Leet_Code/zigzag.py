def convert( s: str, numRows: int) -> str:
        step = numRows + 1
        length = len(s) 
        converted = ''
        for i in range(length):
            converted += s[(i * step) % length]
        return converted
print(convert("PAYPALISHIRING", 3))
print(convert("PAYPALISHIRING", 4))
