import string

class CS21:

    alphanumeric_alphabet = list(string.ascii_uppercase) + ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    def __init__(self, alphanumeric=""):
        self.alphanumeric = alphanumeric.upper()

    def decode_alphanumeric(self):
        # Transforms alphanumeric string into list
        alpha_list = list(self.alphanumeric)
        alpha_dict = {}
        # Creates a dictionary that has number/index values for each character in the alphanumeric alphabet
        for i in range(len(self.alphanumeric_alphabet)):
            alpha_dict[self.alphanumeric_alphabet[i]] = i
        # Loops through each character in the alphanumeric alphabet using i as the current key
        for i in range(len(self.alphanumeric_alphabet)):
            current_decoded = []
            # Decodes each character in the encoded alphanumeric text
            for j in range(len(alpha_list)):
                # Checks to see if the character is apart of the alphanumeric alphabet
                #   If not, that character does not get decoded
                if alpha_list[j] in alpha_dict:
                    # Subtracts the key value from the character value
                    x = (alpha_dict[alpha_list[j]]) - i
                    # If x is less than 0 it wraps around to the beginning of the alphabet
                    if x < 0:
                        x = (len(self.alphanumeric_alphabet) - 1) + x
                    current_decoded.append(self.alphanumeric_alphabet[x])
                else:
                    current_decoded.append(alpha_list[j])
            print("Key is {}, Decoded Text: {}".format(self.alphanumeric_alphabet[i], "".join(current_decoded)))



if __name__ == '__main__':
    my_encrypted = CS21("9QXX P1ZQ TQ4Q’5 G 21UZ65")
    my_encrypted.decode_alphanumeric()