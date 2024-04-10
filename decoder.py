#rocco tammone
def decoder(password):
    decoding = []
    output = ""
    for num in password:
        decoding.append(int(num))
    for num in decoding:
        num -= 3
        output += str(num)
    return output
