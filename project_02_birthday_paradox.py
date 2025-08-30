"""
Birthday Paradox Simulation
Based on Al Sweigart's project from 'The Big Book of Small Python Projects'
Enhanced with mathematical formula and improved structure.
"""


import datetime, random, math

def getBirthdays(numberOfBirthdays):
    """Returns a list of number random date objects for birthdays."""
    birthdays = []
    for i in range(numberOfBirthdays):
        # The year is unimportant for our simulation, as long as all
        # birthdays have the same year.
        startOfYear = datetime.date(2001, 1, 1)
        # Get a random day into the year:
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays):
    """Returns the date object of a birthday that occurs more than once
    in the birthdays list."""
    if len(birthdays) == len(set(birthdays)):
        return None  # All birthdays are unique, so return None.
    # Compare each birthday to every other birthday:
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA  # Return the matching birthday.
            
def project_intro():
    print('''Birthday Paradox, by Al Sweigart al@inventwithpython.com
    The Birthday Paradox shows us that in a group of N people, the odds
    that two of them have matching birthdays is surprisingly large.
    This program does a Monte Carlo simulation (that is, repeated random
    simulations) to explore this concept.
    (It's not actually a paradox, it's just a surprising result.)
    ''')

def project_result(num_birthdays, match_birthday_count, prob):

    result = f"""

    Out of 100 000 simulations of {num_birthdays}, people, there was a matching
    birthday in that group {match_birthday_count} times. This means, that {num_birthdays}
    people have a {prob} % change of having a matching birthdays in
    their group.


            
    """

    print(result)

# Birthday problem math formula:

def birthday_problem_formula(num_people):
    Vnr = math.factorial(365) // math.factorial(365 - num_people)
    Vt = 365 ** num_people
    PA = Vnr / Vt
    return 1 - PA

            
# Utility function for spaces:

def new_row(n=1):
    print("\n" * (n-1))




def main():

    print(datetime.now())

    # Simulation start:
    project_intro()

    # Moths names:
    MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
    

    # User input:
    while True:

        print("How many birthdays shall I generate?")
        print("Possible to create up to 100.")

        user_number = input(">")

        if user_number.isdecimal() and (0 < int(user_number) <= 100):
            numBDays = int(user_number)
            break

        print("Input is not a valid number. Try it again.")

    # Generating first simulation:    
    print(f"Printing {numBDays} birthdays:")

    generated_birthday = getBirthdays(numBDays)

    for index, birthday in enumerate(generated_birthday):
        if index != 0:
            print(',', end=" ")

        monthName = MONTHS[birthday.month - 1]
        dateText = f"{monthName} {birthday.day}"
        print(dateText, end='')
    
    new_row(2)

    # Determine if there are two birthdays that match.
    match = getMatch(generated_birthday)

    # Display the results:
    print('In this simulation, ', end='')


    if match is not None:
        monthName = MONTHS[match.month - 1]
        dateText = '{} {}'.format(monthName, match.day)
        print('multiple people have a birthday on', dateText)
    else:
        print('there are no matching birthdays.')

    new_row(2)

    print(f"""

    Generating {numBDays} random birthdays 100 000 times...
    Press Enter to begin...
    Let´s run another 100 000 simulations.


    """)

    new_row(2)

    # Creating another simulation: 
    
    simMatch = 0  
    for i in range(100_000):
        
        if i % 10_000 == 0:
            print(i, 'simulations run...')
        
        birthdays = getBirthdays(numBDays)
        
        if getMatch(birthdays) != None:
            simMatch = simMatch + 1


    print('100,000 simulations run.')

    # Display simulation results:
    probability = round(simMatch / 100_000 * 100, 2)
    probability_equation = birthday_problem_formula(numBDays)

    new_row(2)


    # Simulation end:
    project_result(numBDays, simMatch, probability)

    new_row(2)

    print(f"""

    Result from birthday paradox formula was {probability_equation}.

    """)




if __name__ == "__main__":
    main()
