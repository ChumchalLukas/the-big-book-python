""" Project inspired by Bitmap project from book The big book of small python projects."""


# Entry bitmaps - inspiration by space invaders
space_invader_1 = """
..........................
----------*----*----------
-----------*--*-----------
----------******----------
--------**-****-**--------
-------************-------
-------*-**----**-*-------
-------*-*------*-*-------
---------***--***---------
..........................
"""

space_invader_2 = """
..........................
------------**------------
-----------****-----------
---------********---------
--------**--**--**--------
--------**--**--**--------
---------********---------
--------***----***--------
--------*-**--**-*--------
..........................
"""

space_invader_3 = """
..........................
----------*----*----------
-----------*--*-----------
----------******----------
--------**-****-**--------
-------************-------
-------*-**----**-*-------
---------*-*--*-*---------
---------***--***---------
..........................
"""

space_invader_4 = """
..........................
----------*----*----------
-----------*--*-----------
------*---******---*------
------*-**-****-**-*------
------**************------
---------**----**---------
--------------------------
--------------------------
..........................
"""

space_invader_5 = """
..........................
----------*----*----------
-----------*--*-----------
------*---******---*------
------*-**-****-**-*------
------**************------
---------**----**---------
----------**--**----------
--------------------------
..........................
"""

# Pre-cleaned versions with spaces instead of '-'
invaders = {
    1: space_invader_1.replace("-", " "),
    2: space_invader_2.replace("-", " "),
    3: space_invader_3.replace("-", " "),
    4: space_invader_4.replace("-", " "),
    5: space_invader_5.replace("-", " "),
}


def main():
    # User input: message to display
    print("Enter your desired message to alien overlords:")

    while True:
        message = input(">")
        if message.strip():
            break
        else:
            print("This is not a valid option!!")

    # User input: choosing alien overlord
    print("Which of the 5 lords are you going to choose? (1-5)")

    while True:
        try:
            choosen_lord = int(input(">"))
            if choosen_lord in invaders:
                break
            else:
                print("This is not in your pantheon!! Repeat pesky human!")
        except ValueError:
            print("Enter a NUMBER between 1 and 5!")

    # Chosen overlord
    overloard = invaders[choosen_lord].splitlines()

    for line in overloard:
        for index, bit in enumerate(line):
            if bit == " ":
                print(" ", end="")
            else:
                print(message[index % len(message)], end="")
        print()


if __name__ == "__main__":
    main()
