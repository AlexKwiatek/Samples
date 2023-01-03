import random
import include
from dialogue import AI_Output

def common_data(list1, list2):
    result = False
    for x in list1:
        for y in list2:
            #print(x + ":" + y)
            if x.lower() == y.lower():
                result = True
                return result
    return result

def puma(player,speaker):
    reponsnes = [
        "No pumy",
        "Chodzi o to czy się pumy lękasz!",
        "W moim pytaniu chodzi o to czy się boisz pumy",
        "Wiesz dobrze o którą pume mi chodzi!",
        "Odpowiedz mi czy boisz się pumy albo idź precz!"
    ]
    reponsnes_offtopic = [
        "Nie pora na czcze rozmowy, czas nas nagli! Mów prędko czy boisz się pumy albo znajdę innego śmiałka.",
        "Nie nadużywaj mojej cierpliwości dziecko i rozmawiajmy na temat. Temat brzmi: Czy lękasz się PUMY!",
        "Później odpowiem na wszystkie twoje pytania, ale teraz najważniejszym jest: Czy boisz się pumy?"
    ]
    puma_variants = [
        "puma","pumy","pumie","pumę","pume","pumą","pumo"
    ]
    AI_Output(speaker,"Powiedz wędrowcze. Czy lękasz się pumy?")
    while True:
        command = input()
        AI_Output(player,command)
        command = command.lower()
        # Response is MANY words
        if ' ' in command:
            # print("Many words detected")
            command = command.split()
            if command[-1][-1] == "?":
                command[-1] = command[-1][:-1]

            if "jakiej" in command and "pumy" in command:
                AI_Output(speaker,"Tej co ma jaja z gumy! Ha!")
                AI_Output(player,"Obudzisz się kiedyś martwy w przestrzeni leśnej.")
                return "SUCCESS"
            elif common_data(command,puma_variants) == True:
                AI_Output(speaker,random.choice(reponsnes))
            else:
                AI_Output(speaker,random.choice(reponsnes_offtopic))
        # Response is ONE word
        elif command == "":
            return
        else:
            # print("One word detected")
            if command[-1] == "?":
                command = command[:-1]
            if command in puma_variants:
                AI_Output(speaker,random.choice(reponsnes))
            elif command in include.back_set:
                return "FAILURE"
            elif command in include.no_set:
                return "NO"
            elif command in include.yes_set:
                return "YES"
            elif command in include.maybe_set:
                AI_Output(speaker,"Musisz się zdecydować czy boisz się pumy.")
            else:
                # print("Ended with final else")
                AI_Output(speaker, random.choice(reponsnes_offtopic))

