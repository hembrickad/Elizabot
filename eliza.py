"""
 Adrienne Hembrick
 February 16, 2021

 The Eliza Program uses regular expressions in order to act as a therapist to the user and responds to the users
 responses based on which verb correleates with the listed verbs.

 The code first requests the name of the user. The user only inputs their name and once it is stored Eliza asks questions based on past responses
 given by the user in a while loop. If an answer is not understood the method confusion randomly generates a number
 to give the user a clarifying response. If the answer contains one of the detectable verbs then feeling will generate the appropriate
 response. If 'I', 'me' or 'my' is used in the statement given it will be converted into the 'you' form before converting the question
 into an answer. It admittedly has problems with changing tense accordingly.

 The word 'Bye' ends the session and Eliza says goodbye.
 
 Basic verbs that can be detected: feel, wish, have, have not, want, know, are, am, is, crave, desire   

 Examples:
    
     Input: I feel tired
     Output: "Why is that [Username]?" or "

     Input: I crave attention
     Output: "Let's talk more about why you want attention" or "Why do you want attention?"

     Input: People are just stupid
     Output: "[Username], could you clarify?" or "Elaborate, please, [Username]" or etc.

     Input: I haven't seen him lately
     Output: "Why haven't you?"

     Input: I know he stole my stuff
     Output: "Why do you believe this, [Username]?" or "How do you know he stole your stuff"

"""

import re
import random 

def feeling(phrase,name):
    phrase = phrase.lower()
    random1 = random.randint(0,3)

    #Changes the I/me to you and my to your in order to chaneg into question
    phrase = re.sub("i('m|'dv|'d)* |me", " you ", phrase)
    phrase = re.sub("my", " your ", phrase)
    print(phrase)

    #Different regular expression combinations for different responses
    patternDesire = re.compile("(wish(ed*|es*)*)|(desire(s*|d*))|(crave(s*))|(want(s*|ed*))")
    patternState = re.compile("(fe(el(s*)|lt))|a(re|m)|is")

    #Catches answers about desires
    if re.search(patternDesire, phrase):
        theList = re.split(patternDesire, phrase, 1)
        if random1 < 2:
            print("Let's talk more about why you desire" + theList[len(theList)-1] + ".")
        else:
            print("Why do you want" + theList[len(theList)-1] + "?")
    #Detects know in the statement
    elif re.search(re.compile("(kn|(ow(s*)|ew))"), phrase):
        theList = re.split(re.compile("(kn(ow(s*)|ew))"), phrase, 1)
        if random1 < 2:
            print("How do you know" + theList[len(theList)-1] + "?")
        else:
            print("Why do you believe that " + theList[len(theList)-1] + name + " ?")
    #Catches answers about feeling and state of mind
    elif re.search(patternState, phrase):
            theList = re.split(patternState, phrase, 1)
            print("Why do you feel" + theList[len(theList)-1] + " ?")
    #Detects if the user has done something or not
    elif re.search(re.compile("(ha(ve|s)(n\'t| not)*)"), phrase):
        if re.search(re.compile("(n\'t| not)"), phrase):
            print("Why haven't you?")
        else:
            confusion(random1, name)
    else:
        confusion(random1, name)
    
# Random chooses a statement if it does not know what to ask
def confusion(num, name):
    if num == 0:
        print("Please, continue.")
    elif num == 1:
        print(name + ", could you clarify?")
    elif num == 2:
        print("Elaborate, please, " + name + ".")
    elif num == 3:
        print("Try explaining it another way.")

#Eliza introduction
print("Hi, my name is Eliza. What can I call you.")

# Stores the patients name
# Does not take into account more than just a name
patientN  = input()

#Temperarily Store Patent Answers
patientA = ""

#regular expressions
#Verbs used: feel, wish, have, have not, want, know, are, am, is, crave, desire
pattern = re.compile("(FE(EL(S*)|LT))|(WISH(ED*|ES*)*)|(HA(VE|S)(N\'T| NOT)*)|(WANT(S*|ED*))|(KN|(OW(S*)|EW))|(A(RE|M))|(IS)|") 
# Introduction: Uses name, Informs the user how to end session, begins session
print("Hi, " + patientN + ". If you feel you need a break just say \'Bye\'")
print("How do you feel today?") 

while patientA != "BYE":
    #Answer from patient
    patientA = input().upper()

    #reaction to patient
    if bool(re.search(pattern, patientA)) == True:
        feeling(patientA, patientN)
    #Salutations
    elif patientA == "BYE":
        print("It has been a pleasure speaking with you " + patientN + ".") 
    # Answers given if no available    
    else:
        confusion(random.randint(0,3), patientN)

