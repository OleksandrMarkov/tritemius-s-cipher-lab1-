alphabet = """abcdefghijklmnopqrstuvwxyz""" + '\n'

def get_key(filename):
    st = open(filename, "r")
    content = st.read()
    st.close()
    key = content.lower()
    if key.isalpha() == True:
        return key
    else:
        print ('Wrong key!')
        raise  SystemExit

def get_message(filename):
    st = open(filename, "r")
    content = st.read()
    st.close()
    msg = content.lower()
    msg = msg.replace(' ', '')
    msg = msg.replace('.', '')
    msg = msg.replace(',', '')

    for i in msg:
        if i not in alphabet:
            break
            print ('Wrong symbol in the message: ' + i)
            raise  SystemExit
        else:
            return  msg

def get_row(key):
    row = []
    for i in key:
        if i not in row:
            row.append(i)
    for i in alphabet:
        if i not in row:
            row.append(i)
    return row

def encrypt(key, msg):
    row = get_row(key)
    cipher = []
    for i in msg:
        if row.index(i)<20:
            new_index = row.index(i) + 6
        elif row.index(i)<24:
            new_index = row.index(i)-18
        else:
            new_index = row.index(i)-24
        cipher.append(row[new_index])
    result = ""
    for i in cipher:
        result += i
    return result

def decrypt(cipher, key):
    row = get_row(key)
    result = ""
    for i in cipher:
        if row.index(i)<2:
            new_index = row.index(i) + 24
        elif row.index(i)<6:
            new_index = row.index(i) + 18
        else:
            new_index = row.index(i) - 6
        result += row[new_index]
    return  result

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


def analyze (cipher):
   # frequency = {'a': 0.0856, 'b':0.0139, 'c': 0.0279,
    #             'd': 0.0378, 'e': 0.1304, 'f':0.0289,
     #            'g': 0.0199, 'h': 0.0528, 'i': 0.0627,
      #           'j':0.0013, 'k': 0.0042, 'l':0.0339,
       #          'm':0.0249, 'n': 0.0707, 'o':0.0797,
        #         'p': 0.0199, 'q': 0.0012, 'r': 0.0677,
         #        's':0.0607, 't': 0.1045, 'u': 0.0249,
          #       'v': 0.0092, 'w':0.0149, 'x': 0.0017,
           #      'y':0.0199, 'z':0.0008}
    elements = []
    for i in cipher:
        if i not in elements:
            elements.append(i)


    print('Results of analysis:')
    print("Number of symbols: " + str(len(cipher)))
    print('Symbol`s statistics: ')
    for i in elements:
        print("Symbol \"" + i + "\" is present " + str(cipher.count(i)) +
" times. Frequency is "+ str(toFixed(cipher.count(i)/len(cipher)*100, 2)) + "%")


key = get_key("key.txt")
print(key)

message = get_message("message.txt")
print(message)

cipher = encrypt(key, message)
print ("Your cipher: " + cipher)

decryption = decrypt(cipher, key)
print ("Your decryption: " + decryption)

analyze(cipher)

a = input()