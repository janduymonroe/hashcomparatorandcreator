import hashlib
from tkinter.filedialog import askopenfilename

print("-"*60)
print("WELCOME TO HASH COMPARATOR AND GENERATOR")
print("-"*60)

def main(select):
    if select == 1:
        hashcomparer()
    elif select == 2:
        showhash()


def hashcomparer():

    while True:
        try:
            print("Choose the first archive!")
            archive1 = askopenfilename()
            print("Choose the second archive!")
            archive2 = askopenfilename()
            hash1 = hashlib.new('SHA256')
            hash2 = hashlib.new('SHA256')

            hash1.update(open(archive1, 'rb').read())
            hash2.update(open(archive2, 'rb').read())
            break
        except:
            print("You need choose two files.\n")



    if hash1.digest() != hash2.digest():
        print(f"The archive {archive1} is different from {archive2}\n")
        print(f"The archive {archive1} 'SHA256' hash is: ", hash1.hexdigest())
        print(f"The archive {archive2} 'SHA256' hash is: ", hash2.hexdigest())
    else:
        print(f"The archive {archive1} is equal to the archive {archive2}")
        print(f"The archive {archive1} 'SHA256' hash is: ", hash1.hexdigest())
        print(f"The archive {archive2} 'SHA256' hash is: ", hash2.hexdigest())


def showhash():
    select = input(''' ### CHOOSE THE HASH ### 
        MD5
        SHA1
        SHA256
        SHA512:  ''')
    hashtypes = ['MD5', 'SHA1', 'SHA256', 'SHA512']
    if select.upper() not in hashtypes:
        print("Error: Choose a listed hash.")
        showhash()

    while True:
        try:
            print("Choose the archive!\n")
            archive1 = askopenfilename()

            hash1 = hashlib.new(select.upper())
            hash1.update(open(archive1, 'rb').read())
            break
        except:
            print("You need choose one file.")

    print(f"The archive {archive1} '{select.upper()}' hash is: \n\n", hash1.hexdigest())


if __name__ == "__main__":
    while True:
        try:
            select = int(input("Type 1 to compare hash or 2 to create hash: "))
            if select in [1, 2]:
                break
            else:
                raise Exception
        except:
            print("Type only number 1 or 2")
    main(select)