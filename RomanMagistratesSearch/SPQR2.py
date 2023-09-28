import pandas as pd
import numpy as np

FicticiousYears = [333,324,309,301]
CorrectDates = 0 # Decide whether to show dates according to modern scholarship or according to Roman tradition
UseWesternNaming = True
magistrates_list = []
parties_dict = {
    # Base + Sullan Civil War
    "O":"Optimates",
    "P":"Populares",
    # Caesar's Civil War
    "C":"Caesarian",
    "Po":"Pompeian",
    # Post-Caesar's Civil War
    "L":"Liberatores",
    "Oc":"Octavianian",
    "A":"Antonian",
}
roman_name_dict = {
    "Agr": "Agrippa", "Ap": "Appius", "A": "Aulus",
    "C": "Gaius", "Cn": "Gnaeus",
    "D": "Decimus",
    "E": "Enneas",
    "F": "Faustus",
    "H": "Hostus",
    "K": "Kaeso",
    "L": "Lucius", "Lars": "Lars",
    "M": "Marcus", "Mam": "Mamercus", "M'": "Manius",
    "N": "Numerius",
    "O": "Octavius", "Opet": "Opiter",
    "P": "Publius", "Pro": "Proculus", "Post": "Postumius",
    "Q": "Quintus",
    "Ser": "Servius", "Sex": "Sextus", "Sp": "Spurius", "St": "Statius", "Sert": "Sertor",
    "Ti": "Tiberius", "T": "Titus", "Ter": "Tertius",
    "V": "Vibius", "Vol": "Volesus", "Vop": "Vopiscus",
    "0":"-"
}


def DisplayYear(Year):
    CorrectedYear = Year
    if CorrectDates == 1:
        if Year > 333:
            CorrectedYear -= 1
        if Year > 324:
            CorrectedYear -= 1
        if Year > 309:
            CorrectedYear -= 1
        if Year > 301:
            CorrectedYear -= 1
    return CorrectedYear

def AdjustYear(Year):
    CorrectedYear = Year
    if Year > 333:
        CorrectedYear += 1
    if Year > 324:
        CorrectedYear += 1
    if Year > 309:
        CorrectedYear += 1
    if Year > 301:
        CorrectedYear += 1
    return CorrectedYear

def TurnYearsIntoInts(Data):
    # Ensure it's a list
    if " " in Data:
        Data = Data.split()
    else:
        Data = [Data]
    for x in Data:
        if isinstance(x,int):
            continue
        if ":" in x:
            a = x.split(":")
            z = int(a[0])
            while z >= int(a[1]):
                Data.append(z)
                z -= 1
            Data.remove(x)

    Data = [int(y) for y in Data]
    Data.sort(reverse=True)
    return Data

def flatten(xs):
    result = []
    if isinstance(xs, (list, tuple)):
        for x in xs:
            result.extend(flatten(x))
    else:
        result.append(xs)
    return result

SPQR_DECO = "       ςανπ αωελ δρυγ ιγωα λξιλ μαλε δζιε ξιςα νπαω ελδρ υγιγ"
class MAGISTRATE:
    def __init__(
            self, praenomen, nomen, filf, filgf, cognomen, alias, patrician, politicalparty,
            dictator, magisterequitum, triumvir,
            consul, consulsuffectus, consulartribune, decemvir,
            praetor, aedile, tribunusplebis, quaestor,
            censor, princepssenatus, pontifexmaximus, vestalismaxima, praefectusurbanus,
            sicilia, corsicaetsardinia, galliacisalpina, galliatransalpina, galliacomata, hispaniaciterior, hispaniaulterior, africa, numidia, illyricum,
            macedonia, bithyniaetpontus, asia, ciliciaetcyprus, syria, cyrenaicaetcreta, aegyptus,
            general
        ):
        self.Name = [praenomen]
        self.Name.append(nomen)
        self.FilF = filf
        self.FilGF = filgf
        if self.FilF == "0":
            self.FilF = "-"
        if self.FilGF == "0":
            self.FilGF = "-"
        if " " in cognomen:
            self.Name.extend(cognomen.split())
        elif cognomen != "0":
            self.Name.append(cognomen)
        self.Patrician = patrician
        self.Alias = alias
        self.PoliticalParty = politicalparty
        # Dictatorial Offices
        self.Dictator = TurnYearsIntoInts(dictator)
        self.MagisterEquitum = TurnYearsIntoInts(magisterequitum)
        self.Triumvir = TurnYearsIntoInts(triumvir)
        # Consular Offices
        self.Consul = TurnYearsIntoInts(consul)
        self.ConsulSuffectus = TurnYearsIntoInts(consulsuffectus)
        self.ConsularTribune = TurnYearsIntoInts(consulartribune)
        self.Decemvir = TurnYearsIntoInts(decemvir)
        # High Offices
        self.Censor = TurnYearsIntoInts(censor)
        self.PrincepsSenatus = TurnYearsIntoInts(princepssenatus)
        self.PraefectusUrbanus = TurnYearsIntoInts(praefectusurbanus)
        self.PontifexMaximus = TurnYearsIntoInts(pontifexmaximus)
        self.VestalisMaxima = TurnYearsIntoInts(vestalismaxima)
        # Low Offices
        self.Praetor = TurnYearsIntoInts(praetor)
        self.Aedile = TurnYearsIntoInts(aedile)
        self.TribunusPlebis = TurnYearsIntoInts(tribunusplebis)
        self.Quaestor = TurnYearsIntoInts(quaestor)
        # Provinces
        self.Sicilia = TurnYearsIntoInts(sicilia)
        self.CorsicaEtSardinia = TurnYearsIntoInts(corsicaetsardinia)
        self.GalliaCisalpina = TurnYearsIntoInts(galliacisalpina)
        self.GalliaTransalpina = TurnYearsIntoInts(galliatransalpina)
        self.GalliaComata = TurnYearsIntoInts(galliacomata)
        self.HispaniaCiterior = TurnYearsIntoInts(hispaniaciterior)
        self.HispaniaUlterior = TurnYearsIntoInts(hispaniaulterior)
        self.Africa = TurnYearsIntoInts(africa)
        self.Numidia = TurnYearsIntoInts(numidia)
        self.Illyricum = TurnYearsIntoInts(illyricum)
        self.Macedonia = TurnYearsIntoInts(macedonia)
        self.BithyniaEtPontus = TurnYearsIntoInts(bithyniaetpontus)
        self.Asia = TurnYearsIntoInts(asia)
        self.CiliciaEtCyprus = TurnYearsIntoInts(ciliciaetcyprus)
        self.Syria = TurnYearsIntoInts(syria)
        self.CyrenaicaEtCreta = TurnYearsIntoInts(cyrenaicaetcreta)
        self.Aegyptus = TurnYearsIntoInts(aegyptus)
        self.ArmyGeneral = TurnYearsIntoInts(general)


        self.PoliticalParty = self.PoliticalParty.split(" ")
        self.PoliticalParty = [x.split(":") for x in self.PoliticalParty]
        for x in self.PoliticalParty:
            if x[0] == "0":
                x[0] = ""
            if len(x) == 1:
                x.append(753)
            else:
                x[1] = int(x[1])

    def __str__(self):
        if not UseWesternNaming:
            StringToReturn = self.Name[0] + ". " + self.Name[1] + " " + self.FilF + ". f. " + self.FilGF + ". n."
        else:
            StringToReturn = roman_name_dict[self.Name[0]] + " " + self.Name[1]
        if len(self.Name) >= 3:
            StringToReturn +=  " " + ' '.join(self.Name[2::])
        if not UseWesternNaming:
            StringToReturn += self.GetIsPatrician()
        return StringToReturn

    def GetCharacterNameAndInfo(self,Year,Consul=False):
        ValueToReturn = "     " + str(self)
        if Consul == True:
            ValueToReturn += self.GetConsulshipNumber(Year)
        ValueToReturn += "; " + self.GetCurrentPoliticalLeaning(Year) + " "

        x = 70 - len(ValueToReturn)
        ValueToReturn += " " * x

        ValueToReturn += self.GetAlias()
        return ValueToReturn

    def GetAlias(self):
        if self.Alias != "0":
            return " --- " + self.Alias
        else:
            return ""

    def GetIsPatrician(self):
        if self.Patrician == "TRUE":
            return " Pat. "
        else:
            return ""

    def PrintFullNameAndTitles(self):
        if len(self.Name) >= 3:
            print("### - " + self.Name[0] + ". " + self.Name[1] + " " + self.FilF + ". f. " + self.FilGF + ". n. " + ' '.join(self.Name[2::]) + self.GetIsPatrician() + " ")
        else:
            print("### - " + self.Name[0] + ". " + self.Name[1] + " " + self.FilF + ". f. " + self.FilGF + ". n. " + self.GetIsPatrician() + " ")
        dictatorstring = self.Dictator
        consulstring = self.Consul
        consulstring.extend(self.ConsulSuffectus)
        consulartribstring = self.ConsularTribune
        consulstring.sort(reverse=True)
        if 0 in dictatorstring:
            dictatorstring.remove(0)
        if 0 in consulstring:
            consulstring.remove(0)
        if 0 in consulartribstring:
            consulartribstring.remove(0)
        if len(dictatorstring) > 0:
            print("Dictator of " + ', '.join([str(y) for y in dictatorstring]))
        if len(consulstring) > 0:
            print("Consul of " + ', '.join([str(y) for y in consulstring]))
        if len(consulartribstring) > 0:
            print("Consular Tribune of " + ' '.join([str(y) for y in consulartribstring]))


    def GetPotentialFather(self):
        print("Potential fathers of " + str(self))
        for x in magistrates_list:
            if x.Name[1] == self.Name[1] and x.Name[0] == self.FilF and x.FilF == self.FilGF:
                # Filiations matched!
                ValuesFrom = [ y for y in flatten(list(self.__dict__.values())) if type(y) == int and y != 0 and y != 753 ]
                ValuesTo = [ y for y in flatten(list(x.__dict__.values())) if type(y) == int and y != 0 and y != 753 ]
                if not max(ValuesTo) < min(ValuesFrom):
                    x.PrintFullNameAndTitles()

    def GetCurrentPoliticalLeaning(self,Year):
        CurrentPoliticalParty = ""
        for x in self.PoliticalParty:
            if x[1] >= Year:
                CurrentPoliticalParty = x[0]
        if len(CurrentPoliticalParty) > 0:
            return "[" + parties_dict[CurrentPoliticalParty] + "]"
        else:
            return CurrentPoliticalParty


    def GetConsulshipNumber(self,Year):
        Consulships = []
        for i in self.Consul:
            Consulships.append(i)
        for i in self.ConsulSuffectus:
            Consulships.append(i)
        Consulships.sort(reverse=True)
        if 0 in Consulships:
            Consulships.remove(0)
        if len(Consulships) == 1:
            return ""
        num = Consulships.index(Year) + 1
        # Storing roman values of digits from 0-9
        # when placed at different places
        m = ["", "M", "MM", "MMM"]
        c = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM "]
        x = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        i = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        # Converting to roman
        thousands = m[num // 1000]
        hundreds = c[(num % 1000) // 100]
        tens = x[(num % 100) // 10]
        ones = i[num % 10]

        ans = (thousands + hundreds + tens + ones)

        return " " + ans


df = pd.read_excel(r'Magistrates.xlsx', dtype=str)
df = df.replace(np.nan, "0")
excelmagistrates = df.values.tolist()
for x in excelmagistrates:
    magistrates_list.append(MAGISTRATE(*x))

class YEAR:
    def __init__(self):
        self.Dictator = []
        self.MagisterEquitum = []
        self.Triumvir = []
        self.Consul = []
        self.ConsulSuffectus = []
        self.ConsularTribune = []
        self.Decemvir = []
        self.Censor = []
        self.PrincepsSenatus = []
        self.PraefectusUrbanus = []
        self.VestalisMaxima = []
        self.PontifexMaximus = []
        self.Praetor = []
        self.Aedile = []
        self.TribunusPlebis = []
        self.Quaestor = []
        # Provinces
        self.Sicilia = []
        self.CorsicaEtSardinia = []
        self.GalliaCisalpina = []
        self.GalliaTransalpina = []
        self.GalliaComata = []
        self.HispaniaCiterior = []
        self.HispaniaUlterior = []
        self.Africa = []
        self.Numidia = []
        self.Illyricum = []
        self.Macedonia = []
        self.BithyniaEtPontus = []
        self.Asia = []
        self.CiliciaEtCyprus = []
        self.Syria = []
        self.CyrenaicaEtCreta = []
        self.Aegyptus = []
        self.ArmyGeneral = []

def PrintYear(Year,Year2 = -1):
    if Year2 == -1:
        Year2 = Year
    #if CorrectDates == 1:
    #    Year = AdjustYear(Year)
    #    Year2 = AdjustYear(Year2)
    debug_log = ""
    consul_count = 950
    while True:
        if Year in FicticiousYears:
            if Year > Year2:
                Year -= 1
            elif Year < Year2:
                Year += 1
            else:
                break
            continue
        processed_year = YEAR()
        for x in magistrates_list:
            # Dictatorial Offices
            if Year in x.Dictator:
                processed_year.Dictator.append(x)
            if Year in x.MagisterEquitum:
                processed_year.MagisterEquitum.append(x)
            if Year in x.Triumvir:
                processed_year.Triumvir.append(x)
            # Consular Offices
            if Year in x.Consul:
                processed_year.Consul.append(x)
            if Year in x.ConsulSuffectus:
                processed_year.ConsulSuffectus.append(x)
            if Year in x.ConsularTribune:
                processed_year.ConsularTribune.append(x)
            if Year in x.Decemvir:
                processed_year.Decemvir.append(x)
            # High Offices
            if Year in x.Censor:
                processed_year.Censor.append(x)
            if Year in x.PrincepsSenatus:
                processed_year.PrincepsSenatus.append(x)
            if Year in x.PraefectusUrbanus:
                processed_year.PraefectusUrbanus.append(x)
            if Year in x.PontifexMaximus:
                processed_year.PontifexMaximus.append(x)
            if Year in x.VestalisMaxima:
                processed_year.VestalisMaxima.append(x)
            # Low Offices
            if Year in x.Praetor:
                processed_year.Praetor.append(x)
            if Year in x.Aedile:
                processed_year.Aedile.append(x)
            if Year in x.TribunusPlebis:
                processed_year.TribunusPlebis.append(x)
            if Year in x.Quaestor:
                processed_year.Quaestor.append(x)
            # Provinces
            if Year in x.Sicilia:
                processed_year.Sicilia.append(x)
            if Year in x.CorsicaEtSardinia:
                processed_year.CorsicaEtSardinia.append(x)
            if Year in x.GalliaCisalpina:
                processed_year.GalliaCisalpina.append(x)
            if Year in x.GalliaTransalpina:
                processed_year.GalliaTransalpina.append(x)
            if Year in x.GalliaComata:
                processed_year.GalliaComata.append(x)
            if Year in x.HispaniaCiterior:
                processed_year.HispaniaCiterior.append(x)
            if Year in x.HispaniaUlterior:
                processed_year.HispaniaUlterior.append(x)
            if Year in x.Africa:
                processed_year.Africa.append(x)
            if Year in x.Numidia:
                processed_year.Numidia.append(x)
            if Year in x.Illyricum:
                processed_year.Illyricum.append(x)
            if Year in x.Macedonia:
                processed_year.Macedonia.append(x)
            if Year in x.BithyniaEtPontus:
                processed_year.BithyniaEtPontus.append(x)
            if Year in x.Asia:
                processed_year.Asia.append(x)
            if Year in x.CiliciaEtCyprus:
                processed_year.CiliciaEtCyprus.append(x)
            if Year in x.Syria:
                processed_year.Syria.append(x)
            if Year in x.CyrenaicaEtCreta:
                processed_year.CyrenaicaEtCreta.append(x)
            if Year in x.Aegyptus:
                processed_year.Aegyptus.append(x)
            if Year in x.ArmyGeneral:
                processed_year.ArmyGeneral.append(x)

        # Now print the results
        print(SPQR_DECO)
        print("                               " + str(DisplayYear(Year)) + " BC")
        if len(processed_year.Consul) == 2:
            print("                # The Year of " + processed_year.Consul[0].Name[-1] + " and " + processed_year.Consul[1].Name[-1] + " #")
        print("                               " + str(754-DisplayYear(Year)) + " AUC")
        if len(processed_year.Dictator) > 0:
            print("DICTATOR:")
            for x in processed_year.Dictator:
                print(x.GetCharacterNameAndInfo(Year))
            if len(processed_year.MagisterEquitum) > 0:
                print("MAGISTER EQUITUM:")
                for x in processed_year.MagisterEquitum:
                    print(x.GetCharacterNameAndInfo(Year))
            print("###")
        if len(processed_year.Triumvir) > 0:
            print("TRIUMVIRATE:")
            for x in processed_year.Triumvir:
                print(x.GetCharacterNameAndInfo(Year))
            print("###")
        if len(processed_year.Consul) > 0:
            print("CONSULS:")
            for x in processed_year.Consul:
                print(x.GetCharacterNameAndInfo(Year,True))
            if len(processed_year.Consul) > 2:
                debug_log += "WARNING: MORE THAN 2 CONSULS IN YEAR " + str(Year) + "\n"
            else:
                consul_count -= len(processed_year.Consul)
        if len(processed_year.ConsulSuffectus) > 0:
            print("SUFFECT CONSUL:")
            for x in processed_year.ConsulSuffectus:
                print(x.GetCharacterNameAndInfo(Year,True))
        if len(processed_year.ConsularTribune) > 0:
            print("CONSULAR TRIBUNES:")
            for x in processed_year.ConsularTribune:
                print(x.GetCharacterNameAndInfo(Year))
        if len(processed_year.Decemvir) > 0:
            print("DECEMVIRATE:")
            for x in processed_year.Decemvir:
                print(x.GetCharacterNameAndInfo(Year))
        print("\n### High Magistrates ###")
        if len(processed_year.Censor) > 0:
            print("CENSORS:")
            for x in processed_year.Censor:
                print(x.GetCharacterNameAndInfo(Year))
        if len(processed_year.PrincepsSenatus) > 0:
            print("PRINCEPS SENATUS:")
            for x in processed_year.PrincepsSenatus:
                print(x.GetCharacterNameAndInfo(Year))
        if len(processed_year.PraefectusUrbanus) > 0:
            print("PRAEFECTUS URBANUS:")
            for x in processed_year.PraefectusUrbanus:
                print(x.GetCharacterNameAndInfo(Year))
        if len(processed_year.PontifexMaximus) > 0:
            print("PONTIFEX MAXIMUS:")
            for x in processed_year.PontifexMaximus:
                print(x.GetCharacterNameAndInfo(Year))
        if len(processed_year.VestalisMaxima) > 0:
            print("VESTALIS MAXIMA:")
            for x in processed_year.VestalisMaxima:
                print(x.GetCharacterNameAndInfo(Year))
        print("\n### Low Magistrates ###")
        if len(processed_year.Praetor) > 0:
            print("PRAETORS:")
            for x in processed_year.Praetor:
                print(x.GetCharacterNameAndInfo(Year))
        if len(processed_year.Aedile) > 0:
            print("AEDILES:")
            for x in processed_year.Aedile:
                print(x.GetCharacterNameAndInfo(Year))
        if len(processed_year.TribunusPlebis) > 0:
            print("PLEBEIAN TRIBUNES:")
            for x in processed_year.TribunusPlebis:
                print(x.GetCharacterNameAndInfo(Year))
        if len(processed_year.Quaestor) > 0:
            print("QUAESTORS:")
            for x in processed_year.Quaestor:
                print(x.GetCharacterNameAndInfo(Year))
        print("\n### Promagistrates ###")
        if len(processed_year.Sicilia) > 0:
            print("GOVERNOR OF SICILIA:")
            for x in processed_year.Sicilia:
                print(x.GetCharacterNameAndInfo(Year))
        if len(processed_year.CorsicaEtSardinia) > 0:
            print("GOVERNOR OF CORSICA ET SARDINIA:")
            for x in processed_year.CorsicaEtSardinia:
                print(x.GetCharacterNameAndInfo(Year))
        if len(processed_year.GalliaCisalpina) > 0:
            print("GOVERNOR OF GALLIA CISALPINA:")
            for x in processed_year.GalliaCisalpina:
                print(x.GetCharacterNameAndInfo(Year))
        if len(processed_year.GalliaTransalpina) > 0:
            print("GOVERNOR OF GALLIA TRANSALPINA:")
            for x in processed_year.GalliaTransalpina:
                print(x.GetCharacterNameAndInfo(Year))
        if len(processed_year.GalliaComata) > 0:
            print("GOVERNOR OF GALLIA COMATA:")
            for x in processed_year.GalliaComata:
                print(x.GetCharacterNameAndInfo(Year))
        if len(processed_year.HispaniaCiterior) > 0:
            print("GOVERNOR OF HISPANIA CITERIOR:")
            for x in processed_year.HispaniaCiterior:
                print(x.GetCharacterNameAndInfo(Year))
        if len(processed_year.HispaniaUlterior) > 0:
            print("GOVERNOR OF HISPANIA ULTERIOR:")
            for x in processed_year.HispaniaUlterior:
                print(x.GetCharacterNameAndInfo(Year))
        if len(processed_year.Africa) > 0:
            print("GOVERNOR OF AFRICA:")
            for x in processed_year.Africa:
                print(x.GetCharacterNameAndInfo(Year))
        if len(processed_year.Numidia) > 0:
            print("GOVERNOR OF NUMIDIA:")
            for x in processed_year.Numidia:
                print(x.GetCharacterNameAndInfo(Year))
        if len(processed_year.Illyricum) > 0:
            print("GOVERNOR OF ILLYRICUM:")
            for x in processed_year.Illyricum:
                print(x.GetCharacterNameAndInfo(Year))
        if len(processed_year.Macedonia) > 0:
            print("GOVERNOR OF MACEDONIA:")
            for x in processed_year.Macedonia:
                print(x.GetCharacterNameAndInfo(Year))
        if len(processed_year.BithyniaEtPontus) > 0:
            print("GOVERNOR OF BITHYNIA ET PONTUS:")
            for x in processed_year.BithyniaEtPontus:
                print(x.GetCharacterNameAndInfo(Year))
        if len(processed_year.Asia) > 0:
            print("GOVERNOR OF ASIA:")
            for x in processed_year.Asia:
                print(x.GetCharacterNameAndInfo(Year))
        if len(processed_year.CiliciaEtCyprus) > 0:
            print("GOVERNOR OF CILICIA ET CYPRUS:")
            for x in processed_year.CiliciaEtCyprus:
                print(x.GetCharacterNameAndInfo(Year))
        if len(processed_year.Syria) > 0:
            print("GOVERNOR OF SYRIA:")
            for x in processed_year.Syria:
                print(x.GetCharacterNameAndInfo(Year))
        if len(processed_year.CyrenaicaEtCreta) > 0:
            print("GOVERNOR OF CYRENAICA ET CRETA:")
            for x in processed_year.CyrenaicaEtCreta:
                print(x.GetCharacterNameAndInfo(Year))
        if len(processed_year.Aegyptus) > 0:
            print("GOVERNOR OF AEGYPTUS:")
            for x in processed_year.Aegyptus:
                print(x.GetCharacterNameAndInfo(Year))
        if len(processed_year.ArmyGeneral) > 0:
            print("ARMY GENERALS:")
            for x in processed_year.ArmyGeneral:
                print(x.GetCharacterNameAndInfo(Year))


        print("\n" + SPQR_DECO + "\n\n\n")

        if Year > Year2:
            Year -= 1
        elif Year < Year2:
            Year += 1
        else:
            break
    print(debug_log)
    print("Still missing " + str(consul_count) + " Consuls")
PrintYear(509,31)