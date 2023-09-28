import random
import glob
import os
import namelists
import math

# AS OF TODAY SCRIPT IS WORKING UNDER THE ASSUMPTION THAT INPUT CHARACTER IS A LORD REIGNING DURING RR BOOKMARK


# Main Globals
detailed_backgenerations = 3
cutoff_year_back = 7897 # Earliest allowed bookmark
cutoff_year_front = 8300 # Furthest allowed bookmark
backancestors_after_cutoff = 2 # Amount of extra lordly ancestors after earliest allowed bookmark
assumed_year_for_root = 8282 # Year of the bookmark in which RootCharacter is a lord
MaxLifeExpectancy = 70 # Max age characters are allowed to live
FemaleRulerChance = 10 # Chance for lordly parent to be a woman
Ceil_SiblingNum = 4 # Maximum amount of non-lordly siblings
Knightify = 1
DornishLaw = False
GenderDistribution = 50 # Chance for a female character to be created

class CHARACTER:
    def __init__(self,ID,name,dynasty,isfemale,culture,religion,BirthDate,DeathDate):
        self.ID = ID
        self.Name = name
        self.Female = isfemale
        self.Dynasty = dynasty
        # Basic Data Block
        self.Religion = religion
        self.Culture = culture
        # Birth-Death Data
        self.BirthDate = BirthDate
        self.DeathDate = DeathDate
        self.IsALord = 0

    def PrintCharacterBlock(self):
        print(self.ID + " = { ")
        # Character Base Data
        print("\tname = " + self.Name + " # a lord" * self.IsALord)
        print("\tdynasty = " + self.Dynasty)
        if self.Female == True:
            print("\tfemale = yes")
        print(" ")
        # Character Origin Data
        print("\treligion = " + self.Religion)
        print("\tculture = " + self.Culture)
        if hasattr(self,"Father") or hasattr(self,"Mother"):
            print(" ")
            if hasattr(self,"Father"):
                print("\tfather = " + self.Father)
            if hasattr(self,"Mother"):
                print("\tmother = " + self.Mother)
        # Character Birth-Death Data
        print(" ")
        if hasattr(self,"Twin"):
            print("\ttrait = twin\n")
        print("\t" + self.BirthDate + " = { birth = yes }")
        if Knightify == 1 and self.Female == False:
            knightification_date = int(self.BirthDate[0:4])+16
            if knightification_date < int(self.DeathDate[0:4]) and knightification_date < cutoff_year_front:
                print("\t" + str(knightification_date) + ".1.1 = { trait = knight }")
        if hasattr(self,"RandomSpouse"):
            if self.Female == False:
                print("\t" + str(self.RandomSpouse) + ".1.1 = { add_spouse = " + RandomSpousifyID(self.ID) + " } ")
            else:
                print("\t" + str(self.RandomSpouse) + ".1.1 = { add_matrilineal_spouse = " + RandomSpousifyID(self.ID) + " } ")
        if self.DeathDate != "9999.1.1":
            print("\t" + self.DeathDate + " = { death = yes }")
        print("}")
        if hasattr(self,"RandomSpouse"):
            print(RandomSpousifyID(self.ID) + " = {")
            if self.Female == False:
                print("\tname = " + namelists.get_random_name(self.Culture,1))
                print("\tfemale = yes")
            else:
                print("\tname = " + namelists.get_random_name(self.Culture,0))
            print("")
            print("\treligion = " + self.Religion)
            print("\tculture = " + self.Culture)
            print("")
            print("\t" + self.BirthDate + " = { birth = yes }")
            if Knightify == 1 and self.Female == True:
                knightification_date = int(self.BirthDate[0:4])+16
                if knightification_date < int(self.DeathDate[0:4]) and knightification_date < cutoff_year_front:
                    print("\t" + str(knightification_date) + ".1.1 = { trait = knight }")
            if self.DeathDate != "9999.1.1":
                print("\t" + self.DeathDate + " = { death = yes }")
            print("}")

    def CreateLordlyParent(self):
        # Character is assumed to be a parent between being 16 and 32 years old
        NewBirthDate = int(self.BirthDate[0:4]) - random.randrange(16,32)
        # Character is assumed to be alive when root-char is born but dead by the time of RR
        DeathDatesCalc = [
            random.randrange(int(self.BirthDate[0:4]),min(assumed_year_for_root,NewBirthDate+MaxLifeExpectancy)),
            random.randrange(int(self.BirthDate[0:4]),min(assumed_year_for_root,NewBirthDate+MaxLifeExpectancy)),
            random.randrange(int(self.BirthDate[0:4]),min(assumed_year_for_root,NewBirthDate+MaxLifeExpectancy))
        ]
        NewDeathDate = max(DeathDatesCalc)
        # Turn them into dates again
        NewBirthDate = str(NewBirthDate) + ".1.1"
        NewDeathDate = str(NewDeathDate) + ".1.1"
        NewIsFemale = False
        if DornishLaw == True and random.randrange(1,100) <= GenderDistribution:
            NewIsFemale = True
        elif random.randrange(1,100) <= FemaleRulerChance:
            NewIsFemale = True
        NewName = namelists.get_random_name(self.Culture,int(NewIsFemale))
        NewID = FindSuitableID() # TEMP, add mechanic to get ID pool
        new_char = CHARACTER(NewID, NewName, self.Dynasty, NewIsFemale, self.Culture, self.Religion, NewBirthDate, NewDeathDate)
        if NewIsFemale == True:
            self.Mother = NewID
        else:
            self.Father = NewID
        family_list.append(new_char)

    def CreateLordlySiblings(self):
        # Ensure there is room for new character
        for x in family_list: # Finding common parent
            if (hasattr(self,"Father") and x.ID == self.Father) or (hasattr(self,"Mother") and x.ID == self.Mother):
                ProcessedDeathDate = x.DeathDate
                x.SkipKids = True
                x.RandomSpouse = int(self.BirthDate[0:4]) - 1
                ProcessedParent = x
                if x.Female == True:
                    self.Father = RandomSpousifyID(x.ID)
                else:
                    self.Mother = RandomSpousifyID(x.ID)
        time_for_kids = int(ProcessedDeathDate[0:4]) - int(self.BirthDate[0:4])
        ceil_kids = math.ceil(min(time_for_kids/2,Ceil_SiblingNum))
        if ceil_kids != 0:
            ceil_kids = random.randrange(0,ceil_kids)
        #LatestBirthdate = int(self.BirthDate[0:4]) + 1
        LatestIndex = family_list.index(self)
        ## Newest Code
        LatestBirthdate = int(ProcessedParent.BirthDate[0:4]) + 17
        ## New Code
        # elif self.Female == True: # Character is ruler and woman, the only siblings may be younger sisters
        #     LatestBirthdate = int(self.BirthDate[0:4]) + 1
        # else:
        #     LatestBirthdate = int(ProcessedParent.BirthDate[0:4]) + 17
        ## Old Code
        for i in range(ceil_kids):
            # Character is assumed to be younger than Root
            if LatestBirthdate < int(ProcessedDeathDate[0:4]):
                NewIsFemale = False
                if random.randrange(1,100) <= GenderDistribution:
                    NewIsFemale = True
                # if self.Female == True:
                    # NewIsFemale = True
                NewBirthDate = random.randrange(LatestBirthdate, min(int(ProcessedDeathDate[0:4]),LatestBirthdate+10))
                LatestBirthdate = NewBirthDate+1
                if NewBirthDate <= ProcessedParent.RandomSpouse: # Ensure it's after parent married
                    ProcessedParent.RandomSpouse = NewBirthDate - 1
                DeathDatesCalc = [
                    random.randrange(int(NewBirthDate) + 1, NewBirthDate + MaxLifeExpectancy),
                    random.randrange(int(NewBirthDate) + 1, NewBirthDate + MaxLifeExpectancy),
                    random.randrange(int(NewBirthDate) + 1, NewBirthDate + MaxLifeExpectancy)
                ]
                NewDeathDate = max(DeathDatesCalc)
                # Char can't be allowed to live as Root is now lord
                if NewBirthDate < int(self.BirthDate[0:4]):
                    if DornishLaw == True:
                        NewDeathDate = random.randrange(NewBirthDate,int(ProcessedParent.DeathDate[0:4]))
                    elif NewIsFemale == True and self.Female == False: # Elder kid is girl and Root is boy - she can stay
                        pass
                    else:
                        NewDeathDate = random.randrange(NewBirthDate,int(ProcessedParent.DeathDate[0:4]))
                if NewDeathDate >= cutoff_year_front:
                    NewDeathDate = 9999
                # Turn them into dates again
                NewBirthDate = str(NewBirthDate) + ".1.1"
                NewDeathDate = str(NewDeathDate) + ".1.1"
                NewName = namelists.get_random_name(self.Culture,int(NewIsFemale))
                NewID = FindSuitableID()
                new_char = CHARACTER(NewID, NewName, self.Dynasty, NewIsFemale, self.Culture, self.Religion, NewBirthDate, NewDeathDate)
                new_char.Father = self.Father
                new_char.Mother = self.Mother

                if int(new_char.BirthDate[0:4]) < int(self.BirthDate[0:4]):
                    if DornishLaw == True:
                        new_char.SkipKids = True
                    elif NewIsFemale == True and self.Female == False: # Elder kid is girl and Root is boy - she can stay
                        pass
                    else:
                        new_char.SkipKids = True
                if int(self.BirthDate[0:4]) == int(new_char.BirthDate[0:4]):
                    new_char.Twin = True
                    self.Twin = True
                if int(self.BirthDate[0:4]) > int(new_char.BirthDate[0:4]):
                    family_list.insert(LatestIndex+1,new_char)
                else:
                    family_list.insert(LatestIndex,new_char)
                    LatestIndex = family_list.index(new_char)

    def SpawnSomeKids(self):
        if int(self.DeathDate[0:4]) - 16 < int(self.BirthDate[0:4]):
            return # Character too young to have kiddos
        else:
            ceil_kids = int(self.DeathDate[0:4]) - int(self.BirthDate[0:4]) - 16
        ceil_kids = random.randrange(min(math.ceil(ceil_kids/4),(Ceil_SiblingNum-1)),Ceil_SiblingNum)
        LatestBirthdate = int(self.BirthDate[0:4]) + random.randrange(17, 32)
        MarriageDate = LatestBirthdate
        for i in range(ceil_kids):
            # Character is assumed to be younger than Root
            if LatestBirthdate < min(int(self.DeathDate[0:4]),cutoff_year_front):
                self.RandomSpouse = MarriageDate # Moved here, so it catches characters that actually got some kiddos
                NewIsFemale = False
                if random.randrange(1, 100) <= GenderDistribution:
                    NewIsFemale = True
                NewBirthDate = random.randrange(LatestBirthdate, min(int(self.DeathDate[0:4]),LatestBirthdate+10,cutoff_year_front))
                LatestBirthdate = NewBirthDate + 1
                if NewBirthDate > cutoff_year_front - 2:
                    NewDeathDate = 9999
                else:
                    DeathDatesCalc = [
                        random.randrange(int(NewBirthDate) + 1, NewBirthDate + MaxLifeExpectancy),
                        random.randrange(int(NewBirthDate) + 1, NewBirthDate + MaxLifeExpectancy),
                        random.randrange(int(NewBirthDate) + 1, NewBirthDate + MaxLifeExpectancy)
                    ]
                    NewDeathDate = max(DeathDatesCalc)
                if NewDeathDate >= 8300:
                    NewDeathDate = 9999
                # Turn them into dates again
                NewBirthDate = str(NewBirthDate) + ".1.1"
                NewDeathDate = str(NewDeathDate) + ".1.1"
                NewName = namelists.get_random_name(self.Culture, int(NewIsFemale))
                NewID = FindSuitableID()
                new_char = CHARACTER(NewID, NewName, self.Dynasty, NewIsFemale, self.Culture, self.Religion,
                                     NewBirthDate, NewDeathDate)
                if self.Female == True:
                    new_char.Mother = self.ID
                    new_char.Father = RandomSpousifyID(self.ID)
                else:
                    new_char.Father = self.ID
                    new_char.Mother = RandomSpousifyID(self.ID)
                if new_char.Female == False and int(new_char.BirthDate[0:4]) < cutoff_year_front + 20:
                    chars_to_kidify_even_further.append(new_char)
                family_list.insert(0, new_char)

    def DoesCharHaveKids(self):
        for x in family_list:
            if x.Father == self.ID:
                return True
        return False

    def GetDynastiedParent(self):
        for x in family_list:
            if x.ID == self.Father:
                return x
            elif x.ID == self.Mother:
                return x
        return False

    def NumOfKids(self):
        counter = 0
        for x in family_list:
            if hasattr(x,"Father") and x.Father == self.ID:
                counter += 1
            elif hasattr(x,"Mother") and x.Mother == self.ID:
                counter += 1
        return counter

def TakeLastWordOfLine(line_processed):
        line_processed = line_processed.split("#")[0]
        line_processed = line_processed.split(" ")
        line_processed = [x for x in line_processed if x != '']
        line_processed = line_processed[-1].strip()
        return line_processed

def TakeFirstWordOfLine(line_processed):
        line_processed = line_processed.split("#")[0]
        line_processed = line_processed.split(" ")[0].strip()
        return line_processed

def FindSuitableID(RandomSpouse=0):
    ID_Number = 2 # Assume that root-character of entirely new house gets the one
    while True:
        IDtoReturn = RootID[0] + str(ID_Number)
        if IDtoReturn not in used_ID:
            used_ID.append(IDtoReturn)
            return IDtoReturn
        else:
            ID_Number += 1

def RandomSpousifyID(ID):
    ID = ID.split("_")
    ID[0] = '_'.join(ID[:-1])
    return ID[0] + "_rs_" + ID[-1]

def IsAllowedToHaveKids(Char):
    if hasattr(x, "SkipKids"):
        return False
    elif DornishLaw == True:
        if random.randrange(1,100) < 66:
            return True
    elif x.Female == False:
        return True
    return False

######################################## START PROCESSING DATA
with open('input.txt') as f:
    lines = f.readlines()

list_of_tags = []
lines_pressed = [[]]
lines = [y.split('#', 1)[0] for y in lines]
lines = [y.split('\n', 1)[0] for y in lines]

for line in lines:
    if line.isspace():
        lines.remove(line)

index = 0
ID = "EMPTY"
Name = "EMPTY"
Dynasty = "EMPTY"
IsFemale = False
Culture = "EMPTY"
Religion = "EMPTY"
BirthDate = "9999.1.1"
MarriageDate = "9999.1.1"
DeathDate = "9999.1.1"

for line in lines:
    if not "\t" in line and "{" in line:
        ID = TakeFirstWordOfLine(line)
    elif "name" in line:
        Name = TakeLastWordOfLine(line)
    elif "dynasty" in line:
        Dynasty = TakeLastWordOfLine(line)
    elif "female" in line:
        IsFemale = True
    elif "culture" in line:
        Culture = TakeLastWordOfLine(line)
    elif "religion" in line:
        Religion = TakeLastWordOfLine(line)
    elif "birth" in line:
        BirthDate = TakeFirstWordOfLine(line)
    elif "death" in line:
        DeathDate = TakeFirstWordOfLine(line)

root_character = CHARACTER(ID, Name, Dynasty, IsFemale, Culture, Religion, BirthDate, DeathDate)
root_character.IsALord = 1

family_list = [root_character]

# Prepwork:
# Find earliest available ID
RootID = root_character.ID
RootID = RootID.split("_")
RootID[0] = '_'.join(RootID[:-1])
RootID[0] += "_"

file_list = glob.glob(os.path.join(os.getcwd(), "characters", "*.txt"))

corpus = []
used_ID = []

for file_path in file_list:
    with open(file_path) as f_input:
        corpus.append(f_input.read())

corpus = [y.split('\n') for y in corpus]

for file in corpus:
    for x in file:
        if not "\t" in x and RootID[0] in x:
            used_ID.append(x.split(" ")[0])

###

while int(family_list[-1].DeathDate[0:4]) > cutoff_year_back:
    family_list[-1].CreateLordlyParent()
for i in range(backancestors_after_cutoff):
    family_list[-1].CreateLordlyParent()

### THIS IS THE POINT WHEN THE LIST IS FULLY #LORDLY#
# So let's get title block now

print("\n\n\n### TITLE HISTORY BLOCK \n\n\n")

for item in reversed(family_list):
    if not hasattr(item,"Father") and not hasattr(item,"Mother"): # First char
        current_date = str(int(item.DeathDate[0:4]) - random.randrange(1,10)) + ".1.1"
        print("\t" + current_date + " = { ")
        print("\t\tholder = " + item.ID + " # " + item.Name)
        print("\t}")
        current_date = item.DeathDate
        item.IsALord = 1
    elif int(current_date[0:3]) < int(item.DeathDate[0:3]):
        print("\t" + current_date + " = { ")
        print("\t\tholder = " + item.ID + " # " + item.Name)
        print("\t}")
        current_date = item.DeathDate
        item.IsALord = 1

print("\n\n\n### CHARACTER HISTORY BLOCK \n\n\n")

# Now to expand existing families
# Cache detailed generations
cached = family_list[0:min(detailed_backgenerations,len(family_list)-1)]
first_non_complex = family_list[min(detailed_backgenerations+1,len(family_list)-1)]

for x in cached:
    x.CreateLordlySiblings()

cached = family_list[0:family_list.index(first_non_complex)]

chars_to_kidify_even_further = []

for x in cached:
    if x.ID == root_character.ID:
        x.SpawnSomeKids()
    elif IsAllowedToHaveKids(x) == True:
        x.SpawnSomeKids()

for x in chars_to_kidify_even_further:
    x.SpawnSomeKids()

for x in family_list:
    if x.NumOfKids() == 0 and IsAllowedToHaveKids(x):
        x.SpawnSomeKids()

### Print Characters
print("###### HOUSE " + RootID[0][:-1].upper() + " (id = " + root_character.Dynasty + ")")
print("############################")
print("###")
print("###")
print("###### HOUSE " + RootID[0][:-1].upper() + " (id = " + root_character.Dynasty + ")")
print("############################")
print("###")
print("###")
for item in reversed(family_list):
    item.PrintCharacterBlock()

counter = 0
for item in family_list:
    if int(item.BirthDate[0:4]) <= assumed_year_for_root and int(item.DeathDate[0:4]) >= assumed_year_for_root:
        counter += 1
print("\n\nAlive at Root Scenario: " + str(counter))

