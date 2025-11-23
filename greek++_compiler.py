#Python version 3.11

import string
import sys
from typing import List, Union
from abc import ABC, abstractmethod

global character_pointer
global pointer_to_next_character
global line_counter
global function_names
global character_counter
global white_characters
global greek_lowercase_letters_set
global greek_uppercase_letters_set
global keywords
global content
global read_characters_counter
global generated_intermidiate_code
global file_to_compile

white_characters = {"\n", " ", "\t"}

greek_lowercase_letters_set = {'α', 'β', 'γ', 'δ', 'ε', 'ζ', 'η', 'θ', 'ι', 'κ', 'λ', 'μ', 'ν', 'ξ', 'ο', 'π', 'ρ', 'σ', 'τ', 'υ', 'φ', 'χ', 'ψ', 'ω', 'ά', 'έ', 'ή', 'ί', 'ό',
'ύ', 'ώ', 'ς'}

greek_uppercase_letters_set = {'Α', 'Β', 'Γ', 'Δ', 'Ε', 'Ζ', 'Η', 'Θ', 'Ι', 'Κ', 'Λ', 'Μ', 'Ν', 'Ξ', 'Ο', 'Π', 'Ρ', 'Σ', 'Τ', 'Υ', 'Φ', 'Χ', 'Ψ', 'Ω', 'Ά', 'Έ', 'Ή', 'Ί', 'Ό',
'Ύ', 'Ώ', '_'}

keywords = {"πρόγραμμα", "αρχή_προγράμματος", "τέλος_προγράμματος", "δήλωση", "συνάρτηση", "διαδικασία", "διαπροσωπεία",
                "αρχή_συνάρτησης", "τέλος_συνάρτησης", "αρχή_διαδικασίας", "τέλος_διαδικασίας", "είσοδος", "έξοδος", "εάν", "τότε", "εάν_τέλος", "αλλιώς",
                "όσο", "επανάλαβε", "όσο_τέλος", "μέχρι", "για", "έως", "για_τέλος", "με_βήμα", "γράψε", "διάβασε", "εκτέλεσε"}


class Token:
#properties: recognizedString, family, lineNumber
    recognizedString: str
    family: str
    lineNumber: int
    
    def __init__(self, recognizedString, family, lineNumber):
        self.recognizedString = recognizedString
        self.family = family
        self.lineNumber = lineNumber

    def __str__(self):
        return f'Token(recognizedString={self.recognizedString}, family={self.family}, line={self.lineNumber})'


# Lexical Analyzer
class Lex:
    currentLine: int
    fileName: str
    token: Token
    intermidiateStates: dict
    finalStates: set
    inputSymbols: dict
    transitionDiagram: list
    EOF: bool
    
    def __init__(self, currentLine, fileName, token):
        self.currentLine = currentLine
        self.fileName = fileName
        self.token = token
        self.EOF = False
        self.intermidiateStates = {"begin" : 0, "reading_number" : 1, "reading_id_or_operator_or_keyword" : 2, "reading_id" : 3, "possible_less" : 4,
        "possible_greater" : 5, "reading_comment" : 6, "possible_assignment" : 7}

        self.finalStates = {"number_found", "keyword_found", "id_found", "smaller_found","smaller_or_equal_found", "greater_found", "greater_or_equal_found",
        "semicolon_found", "comma_found","opening_parenthesis_found", "closing_parenthesis_found", "opening_bracket_found", "closing_bracket_found", 
        "pass_by_address_char_found", "assignment_found","different_found", "and_operator_found", "or_operator_found", "not_operator_found", "mul_operator_found", 
        "div_operator_found", "minus_found", "plus_found", "equal_found", "EOF_found", "check_if_keyword_or_operator_or_id", "plus_or_positive_number_or_id_found"}

        self.inputSymbols = {"white_character" : 0, "digit" : 1, "letter" : 2, "opening_parenthesis": 3, "closing_parenthesis": 4, "opening_comment_char": 5, 
                            "closing_comment_char" : 6, "equals" : 7, "assignment_char" : 8, "EOF" : 9, "plus" : 10, "minus" : 11, "greater_char" : 12, "less_char": 13, 
                            "other" : 14, "comma": 15, "mul_op" : 16, "div_op" : 17, "opening_bracket" : 18, "closing_bracket" : 19, "pass_by_address_char" : 20, "semicolon" : 21}

        self.transitionDiagram = [["begin", "reading_number", "reading_id_or_operator_or_keyword", "opening_parenthesis_found", "closing_parenthesis_found", "reading_comment", "error20", "equal_found", "possible_assignment", "EOF_found", "plus_found", "minus_found", "possible_greater", "possible_less", "error40", "comma_found", "mul_operator_found", "div_operator_found", "opening_bracket_found", "closing_bracket_found", "pass_by_address_char_found", "semicolon_found"],
                                    ["number_found", "reading_number", "error3", "number_found", "number_found", "error10", "error20", "number_found", "error21", "error30", "number_found", "number_found", "number_found", "number_found", "error40", "number_found", "number_found", "number_found", "number_found", "number_found", "number_found", "number_found"],
                                    ["check_if_keyword_or_operator_or_id", "reading_id", "reading_id_or_operator_or_keyword", "check_if_keyword_or_operator_or_id", "check_if_keyword_or_operator_or_id", "error10", "error20", "check_if_keyword_or_operator_or_id", "check_if_keyword_or_operator_or_id", "error30", "check_if_keyword_or_operator_or_id", "check_if_keyword_or_operator_or_id", "check_if_keyword_or_operator_or_id", "check_if_keyword_or_operator_or_id", "error40", "check_if_keyword_or_operator_or_id", "check_if_keyword_or_operator_or_id", "check_if_keyword_or_operator_or_id", "check_if_keyword_or_operator_or_id", "check_if_keyword_or_operator_or_id", "check_if_keyword_or_operator_or_id", "check_if_keyword_or_operator_or_id"],
                                    ["id_found", "reading_id", "reading_id", "id_found", "id_found", "error10", "error20", "id_found", "id_found", "error30", "id_found", "id_found", "id_found", "id_found", "error40", "if_found", "id_found", "id_found", "id_found", "if_found", "id_found", "id_found"],
                                    ["smaller_found", "smaller_found", "smaller_found", "smaller_found", "error6", "error10", "error20", "smaller_or_equal_found", "error22", "error30", "smaller_found", "smaller_found", "different_found", "error35", "error40", "smaller_found", "smaller_found", "smaller_found", "smaller_found", "smaller_found", "smaller_found", "smaller_found"],
                                    ["greater_found", "greater_found", "greater_found", "greater_found", "error7", "error10", "error20", "greater_or_equal_found", "error23", "error30", "greater_found", "greater_found", "error33", "error36", "error40", "greater_found", "greater_found", "greater_found", "greater_found", "greater_found", "greater_found", "greater_found"],
                                    ["reading_comment", "reading_comment", "reading_comment", "reading_comment", "reading_comment", "reading_comment", "begin", "reading_comment", "reading_comment", "error30", "reading_comment", "reading_comment", "reading_comment", "reading_comment", "reading_comment", "reading_comment", "reading_comment", "reading_comment", "reading_comment", "reading_comment", "reading_comment", "reading_comment"],
                                    ["error1", "error1", "error1", "error1", "error1", "error10", "error20", "assignment_found", "error1", "error30", "error1", "error1", "error1", "error1", "error40", "error1", "error1", "error1", "error1", "error1", "error1", "error1"]]
                                    
    def handleError(self, state, readCharacters): # Χειριστής λαθών. Με βάση τη κατάσταση τυπώνει το σωστό σφάλμα
        global line_counter
        print(readCharacters)
        if len(readCharacters) == 0:
            print("Too few characters have been read. The file is possible too small.")
            sys.exit(99)
        if state == "error1":
            print(f"Error: At line {line_counter} there was '{readCharacters[-2]}{readCharacters[-1]}' found. There is no legal character like that. Did you mean to write ':='?")
        if state == "error3":
            print(f"Error: At line {line_counter} there is the letter '{readCharacters[-1]}'. It is illegal to have variable names starting with numbers.")
        if state == "error6":
            print(f"Error: At line {line_counter} there was a closing parenthesis found '{readCharacters[-1]}' after '<'. There is no way to write something like that legally.")
        if state == "error7":
            print(f"Error: At line {line_counter} there is opening parenthesis '{readCharacters[-1]}' after '>'. There is no way to write something like that legally.") 
        if state == "error10":
            print(f"Error: At line {line_counter} there is opening comment '{readCharacters[-1]}' next to '{readCharacters[-2]}'. There must be a white character before opening comment.")
        if state == "error20":
            print(f"Error: At line {line_counter} there is closing_comment_character '{readCharacters[-1]}' while there is no open comment before it.")
        if state == "error21":
            print(f"Error: At line {line_counter} there is ':'  while before there is a number written. Numbers cannot be assigned values.")
        if state == "error22" or state == "state23":
            print(f"Error: At line {line_counter} there is '{readCharacters[-1]}' immediately after comparison character '{readCharacters[-2]}'.")
        if state == "error30":
            print(f"Error: At line {line_counter} character found after end of file.")
        if state == "error33":
            print(f"Error: At line {line_counter} there was '>>' found. There is no legal character like that. Did you mean to write '>='?")
        if state == "error35":
            print(f"Error: At line {line_counter} there was '<<' found. There is no legal character like that. Did you mean to write '>='?")
        if state == "error36":
            print(f"Error: At line {line_counter} there was '{readCharacters[-2]}{readCharacters[-1]}' found. The inequality character is '<>'.")
        if state == "error40":
            print(f"Error: At line {line_counter} there was {readCharacters[-1]} found which is an illegal character.")
        sys.exit(100)

    def isLetter(self, character): # Επιστρέφει αν ο χαρακτήρας είναι γράμμα
        global greek_uppercase_letters_set
        global greek_lowercase_letters_set
        if character in greek_uppercase_letters_set:
            return True
        if character in greek_lowercase_letters_set:
            return True
        for letter in string.ascii_letters:
            if (character == letter): return True
        return False

    def isDigit(self, character): # Επιστρέφει αν ο χαρακτήρας είνα αριθμός
        for digit in string.digits:
            if (digit == character): return True
        return False

    def nextToken(self): # Επιστρέφει το επόμενο token
        global character_pointer
        global content
        global character_counter
        global line_counter
        global white_characters
        readCharacters = ""
        state = "begin"
        if not self.EOF:
            character_pointer = content[character_counter]
            while True:
                newCharacter = character_pointer[0]
                newCharacterType = self.decideInputSymbol(newCharacter)
                state = self.transitionDiagram[self.intermidiateStates.get(state)][newCharacterType]
                if (newCharacter != ""):
                    character_counter += 1
                if ((newCharacter == "\n") and (state not in self.finalStates)):
                        line_counter += 1  
                if (state[0:5] == "error" or (state in self.finalStates)):
                    character_counter -= 1
                    if (state[0:5] == "error"):
                        self.handleError(state, (readCharacters+""+newCharacter))
                    if ((readCharacters == "" or readCharacters == ":")):
                            readCharacters = readCharacters + "" + newCharacter
                            character_counter += 1
                    elif(readCharacters == ">" or readCharacters == "<"):
                        if (newCharacterType == 7 or newCharacterType==12):
                            readCharacters = readCharacters + "" + newCharacter
                            character_counter += 1
                    break
                if ((newCharacter not in white_characters and state != "reading_comment") and newCharacter != "}"):
                    readCharacters = readCharacters + "" + newCharacter
                try :
                    character_pointer = content[character_counter]
                except: 
                    self.EOF = True
                    break
            if (state[0:5] == "error"):
                return self.handleError(state,readCharacters)
            return self.generateToken(state, readCharacters)
        else:
            return self.generateToken("EOF_found", readCharacters)
        
    def generateToken(self, state, readCharacters): #Παράγει το επόμενο token
        global line_counter
        global keywords
        global character_counter
        if (state == "number_found"):
            if (int(readCharacters) > 32767):
                print(f"Too big or too small number was found at line '{line_counter}'. Maximun acceptable number is of absoulute value equal to 32767.")
                sys.exit(1)
            return Token(readCharacters, "Number", line_counter)
        if (state == "id_found"):
            if (len(readCharacters) > 30):
                print(f"ID at line '{line_counter}' is too long. Any ID must have at most 30 characters.")
                sys.exit(30)
            return Token(readCharacters, "ID" ,line_counter)
        if (state == "check_if_keyword_or_operator_or_id"):
            if (readCharacters in keywords):
                return Token(readCharacters, "Keyword", line_counter)
            if (readCharacters == "όχι"):
                return Token(readCharacters, "Singular Operator", line_counter)
            if (readCharacters == "ή" or readCharacters == "και"):
                return Token(readCharacters, "Logical Operator", line_counter)
            if (len(readCharacters) > 30):
                print(f"ID at line '{line_counter}' is too long. Any ID must have at most 30 characters.")
                sys.exit(30)
            if (readCharacters[0] == "_"):
                print(f"Error at line {line_counter}. An ID cannot start with '_'.")
            return Token(readCharacters, "ID" ,line_counter)
        if (state == "smaller_found" or state == "smaller_or_equal_found" or state == "greater_found" or state == "greater_or_equal_found"
             or state == "different_found" or state == "equal_found"):
                return Token(readCharacters, "Relational Operand", line_counter)
        if (state == "assignment_found"):
            return Token(readCharacters, "Assignment", line_counter)
        if (state == "semicolon_found"):
            return Token(readCharacters, "Semicolon", line_counter)
        if (state == "comma_found"):
            return Token(readCharacters, "Comma", line_counter)
        if (state == "opening_parenthesis_found"):
            return Token(readCharacters, "Opening Par", line_counter)
        if (state == "closing_parenthesis_found"):
            return Token(readCharacters, "Closing Par", line_counter)
        if (state == "opening_bracket_found"):
            return Token(readCharacters, "Opening Bracket", line_counter)
        if (state == "closing_bracket_found"):
            return Token(readCharacters, "Closing Bracket", line_counter)
        if (state == "pass_by_address_char_found"):
            return Token(readCharacters, "Pass By Addr", line_counter)
        if (state == "mul_operator_found" or state == "div_operator_found"):
            return Token(readCharacters, "Multiplication Operator", line_counter)
        if (state == "minus_found" or state == "plus_found"):
            return Token(readCharacters, "Addition Operator",line_counter)
        if (state == "EOF_found"):
            return Token(readCharacters, "EOF", line_counter)
        if (state == "plus_or_positive_number_or_id_found" or "minus_or_negative_number_or_id_found"):
            if (len(readCharacters) == 1):
                return Token(readCharacters,"Addition Operator", line_counter)
            isLetter = False
            for character in readCharacters[1:]:
                if self.isLetter(character):
                    isLetter = True
            if (not isLetter):
                return Token(readCharacters,"Number",line_counter)
            if (self.isDigit(readCharacters[1:])):
                print(f"Wrongly defined number or ID at line'{line_counter}'")
                sys.exit(1)
            return Token(readCharacters, "ID", line_counter)

    def decideInputSymbol(self, newCharacter): # Αντιστοιχίζει το σύμβολο της εισόδου με τη στήλη του πίνακα καταστάσεων
        global white_characters
        if (newCharacter in white_characters):
            return self.inputSymbols.get("white_character")
        if (self.isDigit(newCharacter)):
                return self.inputSymbols.get("digit")
        if (self.isLetter(newCharacter)):
            return self.inputSymbols.get("letter")
        if (newCharacter == "("):
            return self.inputSymbols.get("opening_parenthesis")
        if (newCharacter == ")"):
            return self.inputSymbols.get("closing_parenthesis")
        if (newCharacter == "{"):
            return self.inputSymbols.get("opening_comment_char")
        if (newCharacter == "}"):
            return self.inputSymbols.get("closing_comment_char")
        if (newCharacter == "="):
            return self.inputSymbols.get("equals")
        if (newCharacter == ":"):
            return self.inputSymbols.get("assignment_char")
        if (newCharacter == ''):
            return self.inputSymbols.get("EOF")
        if (newCharacter == "+"):
            return self.inputSymbols.get("plus")
        if (newCharacter == "-"):
            return self.inputSymbols.get("minus")
        if (newCharacter == ">"):
            return self.inputSymbols.get("greater_char")
        if (newCharacter == "<"):
            return self.inputSymbols.get("less_char")
        if (newCharacter == ","):
            return self.inputSymbols.get("comma")
        if (newCharacter == "*"):
            return self.inputSymbols.get("mul_op")
        if (newCharacter == "/"):
            return self.inputSymbols.get("div_op")
        if (newCharacter == "["):
            return self.inputSymbols.get("opening_bracket")
        if (newCharacter == "]"):
            return self.inputSymbols.get("closing_bracket")
        if (newCharacter == "%"):
            return self.inputSymbols.get("pass_by_address_char")
        if (newCharacter == ";"):
            return self.inputSymbols.get("semicolon")
        return self.inputSymbols.get("other")


# Quad
class Quad:
    id: int
    operator: str
    operand1: str
    operand2: str
    operand3: str
    
    def __init__(self, id ,operator, operand1, operand2, operand3):
        self.id = id
        self.operator = operator
        self.operand1 = operand1
        self.operand2 = operand2
        self.operand3 = operand3

    def setOperand1(self, operand1):
        self.operand1 = operand1

    def setOperand2(self, operand2):
        self.operand2 = operand2

    def setOperand3(self, label):
        self.operand3 = label

    def __str__(self):
        return f'Quad: {self.id} : {self.operator}, {self.operand1}, {self.operand2}, {self.operand3}'
    

#QuadList
class QuadList:
    programList: list #Λίστα των παραγόμενων τετράδων του ενδιάμεσου κώδικα
    quadCounter: int #Μετράει το πλήθος των παραχθέντων τετράδων
    
    def __init__(self):
        self.programList = []
        self.quadCounter = 1

    def __str__(self):
        counter = 0
        for quad in self.programList:
            counter += 1
        return f'The quad counter is {self.quadCounter}'
    
    def backpatch(self, quadPointers, label):
        for i in range(len(quadPointers.labelList)):
            current_label = quadPointers.labelList[i]
            for j in range(len(self.programList)):
                current_quad = self.programList[j]
                if (current_label == current_quad.id):
                    current_quad.setOperand3(label)
                    break

    def nextQuad(self):
        return self.quadCounter

    def genQuadAndIncreaseCounter(self, label, operator, operand1, operand2, operand3):
        self.programList.append(Quad(label, operator,operand1, operand2, operand3))
        self.quadCounter += 1


#QuadPointerList
class QuadPointerList:    #is a list of pointers to quads and has 1 to 1 correlation with Parser
    labelList: List[int] 

    def __init__(self, label):
        self.labelList = [label]

    def mergeList(self, list1, list2):
        self.labelList.extend(list2.labelList)
    
    def __str__(self):
        return ', '.join(str(label) for label in self.labelList)


# Symbol 
class Symbol(ABC):
    name:str

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def __str__(self):
        pass
    
    
# Variable
class Variable(Symbol):
    datatype:str
    offset:int

    def __init__(self, name, datatype):
        super().__init__(name)
        self.datatype = datatype
    
    def setOffset(self, offset):
        self.offset = offset

    def __str__(self):
        return f"Variable {self.name} Datatype {self.datatype} Offset {self.offset}"


# Temporary Variable
class TemporaryVariable(Variable):
    name:str
    datatype:str
    offset:int
    
    def __init__(self, name, datatype):
        super().__init__(name, datatype)

    def __str__(self):
        return f"TemporaryVariable {self.name} Datatype {self.datatype} Offset {self.offset}"


# Formal Parameter
class FormalParameter(Symbol):
    name:str
    datatype:str
    mode:str

    def __init__(self, name, datatype, mode):
        super().__init__(name)
        self.datatype = datatype
        self.mode = mode

    def setFormalParameterMode(self, mode):
        if self.mode != None: #Έλεγξε αν η τυπική παράμετρος έχει ήδη δηλωμένο τρόπο περάσματος
            return -1
        self.mode = mode

    def __str__(self):
        return f"Formal parameter {self.name}, {self.datatype}, {self.mode}"


# Parameter
class Parameter(FormalParameter, Variable):
    name:str
    datatype:str
    mode:str
    offset:int

    def __init__(self, name, datatype, mode):
        self.name = name
        self.datatype = datatype
        self.mode = mode

    def __str__(self):
        return f"Parameter {self.name} Type {self.datatype} Pass {self.mode} Offset {self.offset} "
        

# Procedure
class Procedure(Symbol):
    name:str
    startingQuad:int
    framelength:int
    formalParameters:List[FormalParameter]
    
    def __init__(self, name):
        super().__init__(name)
        self.framelength = 0
        self.startingQuad = 0
        self.formalParameters = []

    def setStartingQuad(self, startingQuad):
        self.startingQuad = startingQuad

    def setFramelength(self, framelength):
        self.framelength = framelength

    def addFormalParameter(self, formalParameter):
        self.formalParameters.append(formalParameter)

    def setFormalParameterMode(self, name ,mode, line):
        for fp in self.formalParameters:
            if name==fp.name:
                result = fp.setFormalParameterMode(mode)
                if result == -1:
                    print(f"Error: At Procedure or Function {name} parameter {fp.name} at line {line} has already been set with pass method {fp.mode}")
                    sys.exit(-1)
    
    def getFormalParametersLength(self):
        return len(self.formalParameters)
    
    def getFormalParameterPosition(self, formalParameter):
        if not self.formalParameters:
            return None

    def __str__(self):
        generatedFormalParameters = ',\n#'.join(str(fp) for fp in self.formalParameters)
        return (f"Procedure {self.name}, startingQuad {self.startingQuad}, Framelength {self.framelength}, Formal parameters:\n#{generatedFormalParameters}")
    

# Function
class Function(Procedure):
    name:str
    startingQuad:int
    framelength:int
    formalParameters:List[FormalParameter]
    datatype:str

    def __init__(self, name, datatype):
        super().__init__(name)
        self.framelength = 0
        self.startingQuad = 0
        self.datatype = datatype

    def __str__(self):
        generatedFormalParameters = ',\n#'.join(str(fp) for fp in self.formalParameters)
        return (f"Function {self.name}, startingQuad {self.startingQuad}, Framelength {self.framelength}, Formal parameters:\n#{generatedFormalParameters}")

        
# Scope 
class Scope:
    nestingLevel:int
    entityList: List[Symbol]
    offset: int

    def __init__(self, nestingLevel):
        self.nestingLevel = nestingLevel
        self.offset = 0
        self.entityList = []


# Symbol Table
class SymbolTable:
    table: List[Scope] # Ο πίνακας
    depth:int # Το βάθος του πίνακα
    symTableOutput: List[str] # Η έξοδος του πίνακα συμβόλων η οποία χρησιμοποιείται για το τύπωμα αρχείων
    symbolTablePrintCounter: int # Μετρητής για το πόσες φορές έχουμε τυπώσει τον πίνακα συμβόλων
    deletedScope: Scope # Το scope το οποίο έχει διαγραφεί

    def __init__(self):
        self.table = []
        self.depth = -1
        self.symTableOutput = []
        self.symbolTablePrintCounter = 0
        self.deletedScope = None

    def addEntity(self, name, symbol_type, datatype, mode, line=0):
        entity = None
        match symbol_type:
            case "Function":
                entity = Function(name, datatype)
            case "Procedure":
                entity = Procedure(name)
            case "Variable":
                entity = Variable(name, datatype)
            case "TemporaryVariable":
                entity = TemporaryVariable(name, datatype)
            case "Parameter":
                entity = Parameter(name, datatype, mode)
            case "FormalParameter":
                entity = FormalParameter(name, datatype, mode)
        #Έλεγξε αν υπάρχει άλλη οντότητα σε αυτό το επίπεδο με το ίδιο όνομα
        if symbol_type != "FormalParameter":
            for x in self.table[self.depth].entityList:
                if x.name == entity.name:
                    print(f"{x.name} at line {line} cannot be defined as there is something else defined with this name in the scope.") #Αν υπάρχει κάτι με το ίδιο όνομα σε αυτό το επίπεδο τύπωσε μύνημα λάθους
                    sys.exit(1)
        if symbol_type in ["Variable", "TemporaryVariable", "Parameter"] and self.table[self.depth].offset != 0:
            entity.setOffset(self.table[self.depth].offset)
            self.table[self.depth].offset += 4
            self.table[self.depth].entityList.append(entity)
        elif symbol_type == "Function" or symbol_type == "Procedure":
            self.table[self.depth].entityList.append(entity)
            self.addScope()
            self.table[-1].offset = 12
        elif (symbol_type == "FormalParameter"):
            newFormalParameter = FormalParameter(name, "int", None) #Εδώ δημιουργούμε μία τυπική παράμετρο και μία απλή παράμετρο
            self.table[self.depth-1].entityList[-1].addFormalParameter(newFormalParameter)
            self.addEntity(name, "Parameter", "int", mode, line)
        return entity

    def addScope(self):
        self.depth += 1
        new_scope = Scope(self.depth)
        self.table.append(new_scope)

    def deleteScope(self):
        if self.depth >= 0:
            if self.table[self.depth-1].entityList[-1].__class__ is Function or self.table[self.depth-1].entityList[-1].__class__ is Procedure:
                if self.table[self.depth-1].entityList[-1].framelength == 0:
                    self.table[self.depth-1].entityList[-1].setFramelength(self.table[self.depth].offset) #Προτού διαγράψεις το επίπεδο προσδιόρισε το framelength της συνάρτησης ή της διαδικασίας
            self.deletedScope = self.table.pop()
            self.depth -= 1

    def searchForProcedure(self, name, line):
        for scope in reversed(self.table):
                symbolPlace = 0
                for symbol in scope.entityList:
                    if symbol.name == name and (symbol.__class__ is Procedure):
                        return True
        return False
    
    def searchForFunctionOrProcedure(self, name):
        for scope in reversed(self.table):
                symbolPlace = 0
                for symbol in scope.entityList:
                    if symbol.name == name and (symbol.__class__ is Function):
                        return scope, symbolPlace
                    symbolPlace += 1
        for scope in reversed(self.table):
                symbolPlace = 0
                for symbol in scope.entityList:
                    if symbol.name == name and (symbol.__class__ is Procedure):
                        return scope, symbolPlace
                    symbolPlace += 1
        return None, None
    
    def searchSymbolByName(self,name):
        for scope in reversed(self.table):
                symbolPlace = 0
                for symbol in scope.entityList:
                    if symbol.name == name:
                        return scope, symbolPlace
                    symbolPlace += 1

    def searchSymbol(self, name, classType, line=0, ifProcedureReturns=False):
        if not ifProcedureReturns: #Αν δεν υπάρχει περίπτωση το σύμβολο το οποίο ψάχνουμε να είναι διαδικασία η οποία επιστρέφει τιμή
            for scope in reversed(self.table):
                symbolPlace = 0
                for symbol in scope.entityList:
                    if symbol.name == name and (symbol.__class__ is classType):
                        return scope, symbolPlace
                    symbolPlace += 1
            if classType is Variable: #Αν δεν έχει βρεθεί μεταβλητή με αυτό το όνομα ψάξε να δεις αν υπάρχει παράμετρος
                for scope in reversed(self.table):
                    symbolPlace = 0
                    for symbol in scope.entityList:
                        if symbol.name == name and (symbol.__class__ is Parameter):
                            return scope, symbolPlace
                        symbolPlace += 1
                #Αν δεν έχει βρεθεί ούτε παράμετρος με αυτό το όνομα ψάξε να δεις αν υπάρχει προσωρινή μεταβλητή
                for scope in reversed(self.table):
                    symbolPlace = 0
                    for symbol in scope.entityList:
                        if symbol.name == name and (symbol.__class__ is TemporaryVariable):
                            return scope, symbolPlace
                        symbolPlace += 1
                self.printUndefinedSymbol(name, classType, line)
        else: #Σε περίπτωση που αυτό το οποίο βλέπουμε μπορεί να είναι διαδικασία η οποία επιστρέφει τιμή
            for scope in reversed(self.table):
                symbolPlace = 0
                for symbol in scope.entityList:
                    if symbol.name == name and (symbol.__class__ is classType):
                        return scope, symbolPlace
                    symbolPlace += 1
            if classType is Variable: #Αν δεν έχει βρεθεί μεταβλητή με αυτό το όνομα ψάξε να δεις αν υπάρχει παράμετρος
                for scope in reversed(self.table):
                    symbolPlace = 0
                    for symbol in scope.entityList:
                        if symbol.name == name and (symbol.__class__ is Parameter):
                            return scope, symbolPlace
                        symbolPlace += 1
                if self.searchForProcedure(name, line) == True:  #Αν δεν έχει βρεθεί ούτε παράμετρος ούτε μεταβλητή ελέγχει να δει αν είναι διαδικασία
                    print(f"Error: At line {line}, procedure returns a value and procedures cannot return a value!")
                    sys.exit(81)
                else:
                    self.printUndefinedSymbol(name, classType, line)
                
    def printLastLevel(self):
            output = ""
            output += "\n#======================================================\n"
            output += f"#Nesting level: {self.table[-1].nestingLevel} "
            output += f"#Scope offset:{self.table[-1].offset}\n#"
            for symbol in self.table[-1].entityList:
                output += str(symbol) + " | "
            output = output[:-3]
            output += "\n#"
            output += "======================================================\n"
            return output

    def printUndefinedSymbol(self, name, classType, line):
        if classType is Function:
            print(f"Not defined function called at line {line} with name {name}.")
        if classType is Procedure:
            print(f"Not defined procedure called at line {line} with name {name}.")
        if classType is Parameter:
            print(f"Not defined parameter at line {line} with name {name}.")
        if classType is Variable:
            print(f"Not defined variable at line {line} with name {name}.")
        sys.exit(11)

    def setStartingQuad(self, startingQuad):
        self.table[self.depth-1].entityList[-1].setStartingQuad(startingQuad)
        return self.table[self.depth-1].entityList[-1] #Επίστρεψε την υπορουτίνα στην οποία θέτουμε την αρχική τετράδα

    def setFormalParameterMode(self, name, mode, line):
        scope, symbol = self.searchSymbol(name, Parameter, line) #Στον πίνακα συμβόλων έχουμε μία παράμετρο η οποία βασίζεται στην τυπική παράμετρο της συνάρτησης ή της διαδικασίας
        self.table[self.depth-1].entityList[-1].setFormalParameterMode(name, mode, line) #Καλεί τη setFormalParamterMode της διαδικασίας ή της συνάρτησης
        self.setParameterMode(name, mode, line) #Ορίζει τον τρόπο με τον οποίο περνιέται η παράμετρος ο οποίος ταυτίζεται με αυτόν της τυπικής παραμέτρου

    def setParameterMode(self, name, mode, line):
        scope, symbolPlace = self.searchSymbol(name, Parameter, line)
        self.table[scope.nestingLevel].entityList[symbolPlace].setFormalParameterMode(mode) #Καλεί τη συνάρτηση την οποία κληρονομεί η Parameter από τη FormalParameter

    def checkIfPassedRight(self, classType, subroutineName, counter, passType, parameterName , line):
        scope, symbol = self.searchSymbol(subroutineName, classType, line)
        if (self.table[scope.nestingLevel].entityList[symbol].formalParameters[counter].mode != passType):
            if classType is Function:
                print(f"Error: At line {line} when function {subroutineName} is called parameter {parameterName} is passed incorrectly.")
            else:
                print(f"Error: At line {line} when procedure {subroutineName} is called parameter {parameterName} is passed incorrectly.")
            sys.exit(4)

    def checkNumberOfElements(self , classType, subroutineName, elementsPassed, lineNumber):
        scope, symbolPlace = self.searchSymbol(subroutineName, classType, lineNumber)
        numberOfFormalParameters = self.table[scope.nestingLevel].entityList[symbolPlace].getFormalParametersLength()
        if numberOfFormalParameters > elementsPassed:
            if classType is Procedure:
                print(f"Error: At line {lineNumber}. When procedure {subroutineName} is called too few arguments are passed.")
                sys.exit(7)
            print(f"Error: At line {lineNumber}. When function {subroutineName} is called too few arguments are passed.")
            sys.exit(7)
        elif numberOfFormalParameters < elementsPassed:
            if classType is Procedure:
                print(f"Error: At line {lineNumber}. Procedure {subroutineName} is called with too many arguments.")
                sys.exit(7)
            print(f"Error: At line {lineNumber}. Function {subroutineName} is called with too many arguments.")
            sys.exit(7)

    def checkIfFormalParametersAreSet(self, classType ,subroutineName, definitionLine):
        scope, symbolPlace = self.searchSymbol(subroutineName, classType, definitionLine)
        for formalParameter in self.table[scope.nestingLevel].entityList[symbolPlace].formalParameters:
            if formalParameter.mode is None:
                if classType is Function:
                    print(f"Error: Parameter {formalParameter.name} of function {subroutineName} defined at line {definitionLine} has undefined call mode!")
                else:
                    print(f"Error: Parameter {formalParameter.name} of  procedure {subroutineName} defined at line {definitionLine} has undefined call mode!")
                sys.exit(99)

    def generateSymbolTable(self):
        output = ""
        for scope in self.table:
            output += "======================================================\n\n"
            output += f"Nesting level: {scope.nestingLevel} "
            output += f"Scope offset:{scope.offset}\n\n\n"
            for symbol in scope.entityList:
                output += str(symbol) + " | "
            output = output[:-3]
            output += "\n"
        output += "======================================================\n\n"
        if self.deletedScope is not None:
            output += f"Nesting level: {self.deletedScope.nestingLevel} "
            output += f"Scope offset:{self.deletedScope.offset}\n\n\n"
            for symbol in self.deletedScope.entityList:
                output += str(symbol) + " | "
            output = output[:-3]
            output += "\n"
        self.symTableOutput.append(output)
        self.symbolTablePrintCounter += 1

    def writeSymbolTable(self):
        self.symTableOutput = []
        fname = sys.argv[1][:-3] + str(self.symbolTablePrintCounter) + ".sym"
        self.generateSymbolTable()
        with open(fname, "w", encoding="utf-8") as f:
            for line in self.symTableOutput:
                f.write(line)


# Final Code Generator
class FinalCodeGenerator:
    filename: str
    quadCounter: int #Μετρά το πλήθος των τετράδων που έχουμε διαβάσει, για να ξέρουμε το από ποια πρέπει να συνεχίσουμε
    beginBlockCounter: int #Μετράει το πόσα διαδοχικά begin_block έχουν διαβαστεί
    startOfSubroutineSet: bool #Δείχνει αν έχει καθοριστεί η αρχή της υπορουτίνας που διαβάζεται
    subroutinesToSetStart: List[str] #Βοηθητική δομή αποθήκευσης του ονόματος μίας υπορουτίνας
    framelengthsOfDefinedSubroutines: List[List] #Αποθηκεύει τα ονόματα και τα μήκη των εγγραφημάτων δραστηριοποίησης των υπορουτινών
    callingASubroutine: bool #Καλείται υπορουτίνα;
    indexOfPassingParameter: int #Δείχνει το πού πρέπει να αποθηκευτεί στο νέο εγγράφημα δραστηριοποίησης μία παράμετρος
    definedSubroutinesAndStartingLineCode : List[List] # Αποθηκεύει τα ονόματα των υπορουτινών και σε ποια ετικέτα ξεκινά ο κώδικας της καθεμιάς
    subroutinesUnderDefinition: List[str] #Λειτουργεί σαν μία στοίβα στην οποία αποθηκεύουμε υπορουτίνες των οποίων διαβάζουμε τις τετράδες.
    #Βοηθά με την αναγνώριση αναδρομικών υπορουτίων.

    def __init__(self, filename):
        self.filename = sys.argv[1][:-3] + ".asm"
        with open(self.filename, "w") as f:
            f.write("")
        self.generateChangeLine()
        self.quadCounter = 0
        self.beginBlockCounter = 0
        self.startOfSubroutineSet = False
        self.subroutinesToSetStart = list()
        self.framelengthsOfDefinedSubroutines = list()
        self.callingASubroutine = False
        self.indexOfPassingParameter = 0
        self.definedSubroutinesAndStartingLineCode = []

    def generateChangeLine(self):
        self.writeToAssemblyFile(".data")
        self.writeToAssemblyFile("str_nl:.asciz \"\\n\"\n")
        self.writeToAssemblyFile(".text\n")

    def changeLine(self): #Άλλαξε γραμμή
        self.writeToAssemblyFile("la a0, str_nl") #Φόρτωσε στον a0 τον χαρακτήρα αλλαγής γραμμής
        self.writeToAssemblyFile("li a7, 4") #Φόρτωσε στον a7 την τιμή 1
        self.writeToAssemblyFile("ecall") #Κάλεσε το Λειτουργικό Σύστημα

    def generateFinalCode(self, generatedProgram, symbolTable, mainFunctionStarts=False):
        tempCounter = 0
        for quad in generatedProgram.programList:
            if tempCounter >= self.quadCounter:
                self.writeToAssemblyFile(symbolTable.printLastLevel())
                self.writeToAssemblyFile(f"#{quad}")
                if not mainFunctionStarts:
                    self.writeToAssemblyFile(("L" + str(quad.id) + ": "))
                    self.processIntermidiateCodeLine(quad.operator, quad.operand1, quad.operand2, quad.operand3, symbolTable, generatedProgram)
                else:
                    self.mainBegins(symbolTable)
                    mainFunctionStarts = False
                tempCounter += 1
                self.quadCounter += 1
            else:
                tempCounter += 1
            
    def processIntermidiateCodeLine(self, operator, operand1, operand2, operand3, symbolTable, generatedProgram):
        if operator == ":=":
            self.checkAndSetStartOfSubroutine()
            self.loadvr(operand1, "t1", symbolTable)
            self.storevr(operand3, "t1", symbolTable)
        elif operator in {"=", "<", "<=", ">", ">=", "<>"}:
            self.checkAndSetStartOfSubroutine()
            self.loadvr(operand1, "t1", symbolTable)
            self.loadvr(operand2, "t2", symbolTable)
            branchOperator = {"=": "beq", "<" : "blt", "<=":  "ble" , ">": "bgt", ">=": "bge", "<>": "bne"}
            self.writeToAssemblyFile(f"{branchOperator[operator]} t1, t2, L{operand3}")
        elif operator in {"+", "-", "*", "/"}:
            numericalOperator = {"+" : "add", "-" : "sub", "*" : "mul", "/" : "div"}
            self.checkAndSetStartOfSubroutine()
            self.loadvr(operand1, "t1", symbolTable)
            self.loadvr(operand2, "t2", symbolTable)
            self.writeToAssemblyFile(f"{numericalOperator[operator]} t1, t1, t2")
            self.storevr(operand3, "t1", symbolTable)
        elif operator == "jump":
            self.checkAndSetStartOfSubroutine()
            self.writeToAssemblyFile(f"j L{operand3}")
        elif operator == "par":
            self.checkAndSetStartOfSubroutine()
            if operand2 != "RET": # Αν αυτή η παράμετρος δεν είναι η προσωρινή μεταβλητή στην οποία μία συνάρτηση επιστρέφει τιμή
                if not self.callingASubroutine:
                    tempCounter = 0
                    self.indexOfPassingParameter = 12 #Η πρώτη παράμετρος περνιέται στα κελιά με αριθμό -12 εώς -15 σε σχέση με την αρχή του εγγραφήματος δραστηριοποίησης
                    for quad in generatedProgram.programList: # Βρες το σε ποια υπορουτίνα περνιέται αυτή η μεταβλητή ως παράμετρος
                        if quad.operator == "call" and tempCounter >= self.quadCounter:
                            self.moveFP(quad.operand1, symbolTable) # Μετάφερε τον fp στην αρχή της κληθείσας συνάρτησης
                            self.callingASubroutine = True #Περνάμε παραμέτρους σε μία κληθείσα υπορουτίνα
                            break
                        tempCounter+=1
                self.loadvr(operand1, "t0", symbolTable, passMode=operand2,isPassingParameter=True)
                self.writeToAssemblyFile(f"sw t0, -{self.indexOfPassingParameter}(fp)") # Φόρτωσε στο εγγράφημα δραστηριοποίησης της κληθείσας υπορουτίνας τη κατάλληλη τιμή
                self.indexOfPassingParameter += 4
            else: # Διαφορετικά είναι η προσωρινή μεταβλητή στην οποία μία συνάρτηση επιστρέφει τιμή
                if not self.callingASubroutine:
                        callQuad = generatedProgram.programList[(self.quadCounter+1)] # Βρες το σε ποια υπορουτίνα περνιέται αυτή η μεταβλητή ως παράμετρος
                        self.moveFP(callQuad.operand1, symbolTable) # Μετάφερε τον fp στην αρχή της κληθείσας συνάρτησης
                scope, symbolPlace =  symbolTable.searchSymbol(operand1, TemporaryVariable)
                offset = symbolTable.table[scope.nestingLevel].entityList[symbolPlace].offset
                self.writeToAssemblyFile(f"addi t0, sp, -{offset}") # Φόρτωσε στον t0 την διεύθυνση της προσωρινής μεταβλητής στην οποία η συνάρτηση επιστρέφει τιμή
                self.writeToAssemblyFile("sw t0, -8(fp)") # Αποθήκευσε αυτή την διεύθυνση στην τρίτη θέση του εγγραφήματος δραστηριοποίησης της κληθείσας συνάρτησης
        elif operator == "retv":
            self.checkAndSetStartOfSubroutine()
            self.loadvr(operand1, "t1", symbolTable) #Φόρτωσε στον t1 τη τιμή
            self.writeToAssemblyFile("lw t0, -8(sp)") #Φόρτωσε στον t0 την διεύθυνση της μεταβλητής στην οποία επιστρέφει τιμή η συνάρτηση
            self.writeToAssemblyFile("sw t1, 0(t0)") #Φόρτωσε στη κατάλληλη θέση μνήμης την τιμή που επιστρέφει η συνάρτηση
        elif operator == "call":
            self.checkAndSetStartOfSubroutine()
            if not self.callingASubroutine: # Σε περίπτωση που καλούμε μία υπορουτίνα η οποία δε παίρνει παραμέτρους πρέπει να μετακινήσουμε πάλι κατάλληλα τον fp
                self.moveFP(operand1, symbolTable)
            scope, symbolPlace = symbolTable.searchForFunctionOrProcedure(operand1) #Με αυτό μαθαίνουμε το επίπεδο της κλειθήσας υπορουτίνας
            if (symbolTable.depth-1 == scope.nestingLevel): #Αν η κληθείσα είναι στο προτελευταίο επίπεδο τότε καλείται από τον εαυτό της ή από αδερφό της
                self.writeToAssemblyFile("lw t0, -4(sp)")
                self.writeToAssemblyFile("sw t0, -4(fp)")
            else: #Αν η κληθείσα είναι σε κατώτερο από το προτελευταίο επίπεδο τότε καλείται από τον γονέα της
                self.writeToAssemblyFile("sw sp, -4(fp)")
            self.moveSP(scope, symbolPlace, symbolTable)
            for subroutine in self.definedSubroutinesAndStartingLineCode: # Βρες το ποια ετικέτα αντιστοιχεί στην υπορουτίνα που καλείται
                if subroutine[0] == operand1:
                    self.writeToAssemblyFile(f"jal L{subroutine[1]}") #Κάνε άλμα στην υπορουτίνα και αποθήκευσε στο ra την διεύθυνση επιστροφής
                    self.moveSP(scope, symbolPlace, symbolTable, negative=True)
                    break
            self.callingASubroutine = False #Δε καλείται πια μία υπορουτίνα
        elif operator == "out":
            self.checkAndSetStartOfSubroutine()
            self.loadvr(operand1, "t1", symbolTable) #Φόρτωσε στον t1 την τιμή που θέλουμε να τυπώσουμε
            self.writeToAssemblyFile("mv  a0, t1") #Μετακίνησε την τιμή που θέλουμε να τυπώσουμε στον a0
            self.loadvr("1", "a7", symbolTable) #Φόρτωσε την τιμή 1 στον a7
            self.writeToAssemblyFile("ecall") #Κάλεσε το Λειτουργικό Σύστημα
            self.changeLine()
        elif operator == "in":
            self.checkAndSetStartOfSubroutine()
            self.writeToAssemblyFile("li a7, 5") #Πάρε είσοδο από το πληκτρολόγιο
            self.writeToAssemblyFile("ecall") #Δώσε τον έλεγχο πίσω στο Λειτουργικό
            self.writeToAssemblyFile("mv t0, a0") #Μετάφερε την είσοδο στον t0
            self.storevr(operand1, "t0", symbolTable) #Αποθήκευσε την είσοδο στη μνήμη
            self.changeLine() #Άλλαξε γραμμή
        elif operator == "begin_block":
            self.beginBlockCounter += 1 # Αύξησε το πλήθος των begin block που είναι εν αναμονή εξυπηρέτησης κατά ένα
            self.definedSubroutinesAndStartingLineCode.append([operand1, 0]) # Πέρνα το όνομα της υπορουτίνας σε μία λίστα στην οποία μετά θα το αντιστοιχίσουμε με τη πρώτη γραμμή της στον τελικό κώδικα
            self.subroutinesToSetStart.append(operand1) # Πέρνα το όνομα της υπορουτίνας στις υπορουτίνες για τις οποίες δε ξέρουμε το πότε ξεκινά η εκτέλεσή τους 
        elif operator == "end_block":
            self.checkAndSetStartOfSubroutine()
            self.beginBlockCounter -= 1 # Μείωσε το πλήθος των begin block που είναι εν αναμονή εξυπηρέτησης κατά ένα
            self.startOfSubroutineSet = False # Μόλις τελειώσαμε με τον ορισμό μίας υπορουτίνας και άρα είναι αδύνατον να έχουμε ορίσει την αρχή της επόμενης
            self.subroutinesToSetStart.pop() # Αφού ορίστηκε αυτή η υπορουτίνα ξέρουμε σίγουρα το ποια είναι η πρώτη γραμμή εκτέλεσής της
            scope, symbolPlace = symbolTable.searchForFunctionOrProcedure(operand1) # Βρες το που είναι στον πίνακα συμβόλων η ορίζουσα υπορουτίνα
            self.writeToAssemblyFile("lw ra, 0(sp)") #Φόρτωσε στον ra τη σωστή διεύθυνση επιστροφής
            self.writeToAssemblyFile("jr ra") #Επέστρεψε πίσω σε αυτόν που κάλεσε την υπορουτίνα

    def findFrameLength(self, name): # Βρίσκει το μήκος του εγγραφήματος δραστηριοποίησης μίας υπορουτίνας
        for subroutine in self.framelengthsOfDefinedSubroutines:
            if name == subroutine[0]:
                return subroutine[1]
    
    def moveSP(self, scope, symbolPlace, symbolTable, negative=False):
        framelength = symbolTable.table[scope.nestingLevel].entityList[symbolPlace].framelength
        scopeOffset = symbolTable.table[-1].offset # Το offset του scope του τελευταίου επιπέδου
        if (negative):
            framelength *= -1
            scopeOffset *= -1
        if  framelength!= 0:
            self.writeToAssemblyFile(f"addi sp, sp, {framelength}") #Μετακίνησε τον sp στην αρχή του εγγραφήματος δραστηριοποίησης της κληθείσας
        else: # Η συνάρτηση καλεί τον εαυτό της
            self.writeToAssemblyFile(f"addi sp, sp, {scopeOffset}") #Μετακίνησε τον sp στην αρχή του εγγραφήματος δραστηριοποίησης της κληθείσας
    
    def moveFP(self, name, symbolTable):
        scope, symbolPlace = symbolTable.searchForFunctionOrProcedure(name) # Επίστρεψε την θέση της υπορουτίνας στον πίνακα συμβόλων
        subroutineFound = symbolTable.table[scope.nestingLevel].entityList[symbolPlace]# Πάρε το μήκος του εγγραφήματος δραστηριοποίησης της συνάρτησης
        if subroutineFound.framelength != 0:
            self.writeToAssemblyFile(f"addi fp, sp, {symbolTable.table[scope.nestingLevel].entityList[symbolPlace].framelength}") #Μετάφερε τον frame pointer στην αρχή της κληθείσας υπορουτίνας
        else:
            self.writeToAssemblyFile(f"addi fp, sp, {symbolTable.table[-1].offset}") # Αν δεν έχει οριστεί το offset της υπορουτίνας τότε καλεί τον εαυτό της

    def checkAndSetStartOfSubroutine(self): # Θέτει την αρχική γραμμή του τελικού κώδικα για μία υπορουτίνα
        if self.beginBlockCounter > 0 and not self.startOfSubroutineSet: # Πρέπει για τουλάχιστον μία υπορουτίνα να βρούμε τη πρώτη γραμμή εκτέλεσής της
            counter = 0
            for subroutine in self.definedSubroutinesAndStartingLineCode: # Βρες την υπορουτίνα για την οποία μόλις τώρα βρήκαμε τη πρώτη τετράδα εκτέλεσής της
                if subroutine[0] == self.subroutinesToSetStart[-1]:
                    self.definedSubroutinesAndStartingLineCode[counter][1] = self.quadCounter+1 # Θέσε την τιμή της ετικέτας της πρώτης γραμμής του τελικού κώδικα για αυτή την ευρεθείσα υπορουτίνα
                    break
                counter += 1
            self.writeToAssemblyFile("sw ra, 0(sp)") # Φόρτωσε στην αρχή του εγγραφήματος δραστηριοποίησης της υπορουτίνας την διεύθυνση επιστροφής
            self.startOfSubroutineSet = True
            
    def gnlvcode(self, scope, symbolPlace, currentDepth, offsetOfWantedVariable): # Η gnlvcode μεταφέρει στον καταχωρητή t0 την διεύθυνση μίας μη τοπικής μεταβλητής
        variableLevel = scope.nestingLevel #Επίπεδο της μεταβλητής ή της παραμέτρου
        currentLevel = currentDepth #Επίπεδο στο οποίο χρειαζόμαστε τη μεταβλητή ή τη παράμετρο
        reachLevels = currentLevel - variableLevel #Η διαφορά των επιπέδων στον πίνακα συμβόλων μεταξύ του προγόνου και της κλειθήσας υπορουτίνας
        self.writeToAssemblyFile("lw t0, -4(sp)")
        for i in range(reachLevels - 1):
            self.writeToAssemblyFile("lw t0, -0(t0)")
        self.writeToAssemblyFile(f"addi t0, t0, -{offsetOfWantedVariable}")

    def loadvr(self, sourceVariable, targetRegister, symbolTable, passMode=None, isPassingParameter=False): #Χρησιμοποιείται για να φορτώσουμε σε έναν καταχωρητή της επιλογής μας την τιμή μίας μεταβλητής
        if sourceVariable.isdigit(): #Έλεξγε αν είναι αριθμός
            self.writeToAssemblyFile(f"li {targetRegister}, {sourceVariable}")
        else: # Αν δε μας δίνεται αριθμητική σταθερά να φορτώσουμε σε έναν καταχωρητή
            scope, symbolPlace =  symbolTable.searchSymbolByName(sourceVariable)
            symbolFound = symbolTable.table[scope.nestingLevel].entityList[symbolPlace]
            offset = symbolTable.table[scope.nestingLevel].entityList[symbolPlace].offset
            isParameter = isinstance(symbolFound, Parameter) #Έλεγξε αν αυτό το οποίο ψάχνουμε είναι παράμετρος
            if scope.nestingLevel == symbolTable.depth: #Αν η μεταβλητή βρίσκεται στο τελευταίο επίπεδο του Πίνακα Συμβόλων τότε είναι τοπική
                if isPassingParameter and not isParameter: # Έλεγξε αν περνάμε παράμετρο και αυτό το οποίο περνάμε είναι μεταβλητή
                    if passMode == "CV": #Έλεγξε αν η παράμετρος περνιέται με τιμή
                        self.writeToAssemblyFile(f"lw {targetRegister}, -{offset}(sp)")
                    else: #Διαφορετικά η παράμετρος έχει περαστεί με αναφορά
                        self.writeToAssemblyFile(f"addi t0, sp, -{offset}")
                        self.writeToAssemblyFile(f"mv {targetRegister}, t0")
                elif isPassingParameter and isParameter: # Περνάμε παράμτετρο η οποία είναι παράμετρος στην τρέχουσα υπορουτίνα
                    if symbolFound.mode == "CV" and passMode == "CV": #Αν περνάμε παράμετρο με τιμή η οποία είναι ήδη παράμετρος περασμένη με τιμή
                        self.writeToAssemblyFile(f"lw {targetRegister}, -{offset}(sp)")
                    elif symbolFound.mode == "REF" and passMode == "CV": # Αν είναι παράμετρος που έχουμε περάσει με αναφορά και τη περνάμε με τιμή
                        self.writeToAssemblyFile(f"lw t1, -{offset}(sp)") # Φόρτωσε στον t1 την διεύθυνση της μεταβλητής
                        self.writeToAssemblyFile(f"lw {targetRegister}, 0(t1)") #Με βάση την διεύθυνση στον t1 φόρτωσε τη σωστή τιμή στον targetRegister
                    elif symbolFound.mode == "REF" and passMode == "REF":
                        self.writeToAssemblyFile(f"lw {targetRegister}, -{offset}(sp)") #Φόρτωσε στον targetRegister την διεύθυνση της παραμέτρου που έχει περαστεί με αναφορά
                    else: #Περνάμε παράμετρο με αναφορά η οποία είχε περαστεί στην τωρινή υπορουτίνα με τιμή
                        self.writeToAssemblyFile(f"addi {targetRegister}, sp, -{offset}") # Περνάμε στον targetRegister την διεύθυνση της παρμέτρου
                elif not isPassingParameter and isParameter: #Αν δε περνάμε παράμετρο σε υπορουτίνα, αλλά διαχειριζόμαστε τοπική παράμετρο
                    if isParameter and symbolFound.mode == "CV":
                        self.writeToAssemblyFile(f"lw {targetRegister}, -{offset}(sp)")
                    elif isParameter and symbolFound.mode == "REF": # Αν είναι παράμετρος που έχουμε περάσει με αναφορά
                        self.writeToAssemblyFile(f"lw t1, -{offset}(sp)") # Φόρτωσε στον t1 την διεύθυνση της μεταβλητής
                        self.writeToAssemblyFile(f"lw {targetRegister}, 0(t1)") #Με βάση την διεύθυνση στον t1 φόρτωσε τη σωστή τιμή στον targetRegister
                else: #Αν δε περνάμε παράμετρο ούτε έχουμε να διαχειριστούμε παράμετρο, αλλά έχουμε τοπική μεταβλητή ή προσωρινή μεταβλητή
                    self.writeToAssemblyFile(f"lw {targetRegister}, -{offset}(sp)")
            else: #Αν η μεταβλητή δεν είναι τοπική είναι είτε καθολική είτε ορίζεται σε κάποιον πρόγονο της υπορουτίνας που τη χρειάζεται
                if scope.nestingLevel == 0: #Αυτό το οποίο ψάχνουμε είναι μία μεταβλητή με καθολική εμβέλεια
                    if isPassingParameter: # Αν περνάμε παράμετρο
                        if passMode == "CV": # Αν περνάμε παγκόσμια μεταβλητή με τιμή
                            self.writeToAssemblyFile(f"lw {targetRegister}, -{offset}(gp)")
                        else: # Αν περνάμε παγκόσμια μεταβλητή με αναφορά
                            self.writeToAssemblyFile(f"addi t2, gp, {symbolFound.offset}") # Φόρτωσε στον t2 την διεύθυνση της καθολικής μεταβλητής
                            self.writeToAssemblyFile(f"mv {targetRegister}, t2") # Μετάφερε στον targetRegister την διεύθυνση από τον t2 
                    else: # Αν χρειαζόμαστε την τιμή μίας παγκόσμιας μεταβλητής και δε τη περνάμε ως παράμετρο
                        self.writeToAssemblyFile(f"lw {targetRegister}, -{offset}(gp)") #Μετέφερε στον targetRegister την τιμή της καθολικής μεταβλητής 
                else: #Η μεταβλητή ορίζεται σε κάποιον πρόγονο
                    self.gnlvcode(scope, symbolPlace, symbolTable.depth, symbolFound.offset) #Αποθηκεύουμε στον t0 την διεύθυνση της μεταβλητής του προγόνου
                    if isPassingParameter and passMode == "CV" and not isParameter:  #Έλεγξε αν περνάμε μεταβλητή με τιμή
                        self.writeToAssemblyFile(f"lw {targetRegister}, 0(t0)")
                    elif isPassingParameter and passMode == "REF" and not isParameter: #Έλεγξε αν περνάμε μεταβλητή με αναφορά
                        self.writeToAssemblyFile(f"mv {targetRegister}, t0")
                    elif isPassingParameter and passMode == "REF" and isParameter:#Έλεγξε αν περνάμε παράμετρο προγόνου η οποία έχει ήδη περαστεί με αναφορά
                        self.writeToAssemblyFile(f"lw {targetRegister}, 0(t0)") #Ο t0 έχει την διεύθυνση της παραμέτρου και όχι την διεύθυνση αυτού του οποίου περάσαμε.
                        #Με βάση αυτή τη διεύθυνση πάρε την διεύθυνση που είχε περαστεί αρχικά
                    elif isPassingParameter and passMode == "CV" and isParameter: #Μετάφερε την τιμή από
                        self.writeToAssemblyFile(f"lw {targetRegister}, 0(t0)")
                    elif not isPassingParameter and not isParameter: #Είνα μία μεταβλητή της οποίας η διεύθυνση είναι φορτωμένη στον t0
                        self.writeToAssemblyFile(f"lw {targetRegister}, 0(t0)")
                    elif not isPassingParameter and isParameter and symbolFound.mode == "REF": #Είναι παράμετρος η οποία έχει περαστεί με αναφορά
                        self.writeToAssemblyFile(f"lw t1, 0(t0)") #Μεταφέρουμε στον t1 την αρχική διεύθυνση
                        self.writeToAssemblyFile(f"lw {targetRegister}, 0(t1)") #Μεταφέρουμε στον targetResgister τη σωστή τιμή της παραμέτρου
                    elif not isPassingParameter and isParameter and symbolFound.mode == "CV": # Είναι παράμετρος η οποία έχει περαστεί με τιμή
                        self.writeToAssemblyFile(f"lw {targetRegister}, 0(t0)") #Μεταφέρουμε στον targetRegister τη σωστή τιμή

    def storevr(self, targetVariable, sourceRegister, symbolTable):
        if targetVariable.isdigit(): #Έλεξγε αν είνα αριθμός
            self.loadvr(targetVariable, sourceRegister)
            self.writeToAssemblyFile(f"li {sourceRegister}, {targetVariable}")
        else:
            scope, symbolPlace =  symbolTable.searchSymbolByName(targetVariable)
            symbolFound = symbolTable.table[scope.nestingLevel].entityList[symbolPlace]
            offset = symbolFound.offset
            isParameter = isinstance(symbolFound, Parameter) #Έλεγξε αν αυτό το οποίο ψάχνουμε είναι παράμετρος
            if scope.nestingLevel == symbolTable.depth: #Αν η μεταβλητή βρίσκεται στο τελευταίο επίπεδο του Πίνακα Συμβόλων τότε είναι τοπική
                if isParameter: # Έλεγξε αν είναι παράμετρος
                    if symbolTable.table[scope.nestingLevel].entityList[symbolPlace].mode == "CV": #Έλεγξε αν η παράμετρος περνιέται με τιμή
                        self.writeToAssemblyFile(f"sw {sourceRegister}, -{offset}(sp)")
                    else: #Διαφορετικά η παράμετρος έχει περαστεί με αναφορά
                        self.writeToAssemblyFile(f"lw t0, -{offset}(sp)")
                        self.writeToAssemblyFile(f"sw {sourceRegister}, 0(t0)")
                else: #Αν η είσοδος δεν είναι παράμετρος τότε είναι μεταβλητή ή προσωρινή μεταβλητή
                    self.writeToAssemblyFile(f"sw {sourceRegister}, -{offset}(sp)")
            else: #Αν η μεταβλητή δεν είναι τοπική είναι είτε παγκόσμια είτε ορίζεται σε κάποιον πρόγονο της υπορουτίνας που τη χρειάζεται
                if scope.nestingLevel == 0: #Αυτό το οποίο ψάχνουμε είναι μία μεταβλητή με καθολική εμβέλεια
                    self.writeToAssemblyFile(f"sw {sourceRegister}, -{offset}(gp)")
                else: #Η μεταβλητή ορίζεται σε κάποιον πρόγονο
                    self.gnlvcode(scope, symbolPlace, symbolTable.depth, offset) # Φορτώνουμε στον t0 την διεύθυνση της μεταβλητής που θέλουμε
                    if isParameter and symbolFound.mode == "CV":  #Έλεγξε αν είναι παράμετρος και περνιέται με τιμή
                        self.writeToAssemblyFile(f"sw {sourceRegister}, 0(t0)") # Με βάση την διεύθυνση στον t0 φόρτωσε στη μνήμη την τιμή του sourceRegister
                    elif isParameter and symbolFound.mode == "REF":  #Έλεγξε αν είναι παράμετρος και περνιέται με αναφορά
                        self.writeToAssemblyFile(f"lw t0, 0(t0)")
                        self.writeToAssemblyFile(f"sw {sourceRegister}, 0(t0)")
                    else: #Είναι τοπική μεταβλητή ορισμένη σε πρόγονο
                        self.writeToAssemblyFile(f"sw {sourceRegister}, 0(t0)")

    def subroutineCalled(self,  subroutineType, subroutineName, symbolTable): #Βρες την υπορουτίνα και γράψε εντολή assembly που μετακινεί κατάλληλα τον fp
        scope, symbolPlace =  symbolTable.searchSymbol(subroutineName, subroutineType)

    def mainBegins(self, symbolTable):
        self.writeToAssemblyFile("Lmain:\n") #Δημιούργησε ετικέτα για το κυρίως πρόγραμμα
        self.writeToAssemblyFile(f"addi sp, sp, {symbolTable.table[0].offset}") #Μετακίνησε τον stack pointer στο τέλος της κύριας συνάρτησης
        self.writeToAssemblyFile("mv gp, sp") #Θέσε στη σωστή θέση τον global pointer

    def terminateProgram(self): # Δώσε τον έλεγχο πίσω στο Λειτουργικό σύστημα
        self.writeToAssemblyFile(f"L{(self.quadCounter+1)}:")
        self.writeToAssemblyFile("li a0, 0") 
        self.writeToAssemblyFile("li a7, 93")
        self.writeToAssemblyFile("ecall") 

    def writeToAssemblyFile(self, stringToWrite):
        with open(self.filename, "a", encoding="utf-8") as f:
            if stringToWrite[0] == "L" or stringToWrite[0] == ".":
                f.write(stringToWrite + "\n")
            else:
                f.write("   "+ stringToWrite + "\n")  
        

# Syntax Analyzer           
class Parser:
    lexicalAnalyzer: Lex # Ο Λεκτικός Αναλυτής
    token: Token #Το τωρινό token
    compilation: bool # Boolean μεταβλητή η οποία γίνεται αληθής αν δεν έχουν προκύψει προβλήματα κατά τη μεταγλώττιση του προγράμματος
    generatedProgram: QuadList #Εδώ αποθηκεύονται οι τετράδες του ενδιάμεσου κώδικα
    listOfQuadPointerList: List[QuadPointerList]
    operand3: int #Ο μετρητής για τη δημιουργία προσωρινών μεταβλητών
    operand3TempCounter: str #Η παραγόμενη προσωρινή μεταβλητή
    programID: str # Το όνομα του προγράμματος
    symbolTable: SymbolTable #Ο πίνακας συμβόλων
    functionIDs: List[List] #List : [List [ functionID : str, returnCounter : int ]] Αποθηκεύει το όνομα μίας συνάρτησης και το πόσες φορές επιστρέφει στοιχεία
    calledSubroutineNamesAndCurrentPositions: List[List] # List : [List : [type: Function | Procedure, name : str, counter : int]] Αποθηκεύει μία υπορουτίνα και το ποιο στοιχείο ελέγχουμε από αυτά που περνάμε
    forStatIDs: List[str] #Λίστα η οποία αποθηκεύει τις τοπικές παραμέτρους που καθορίζονται στις αρχέ των βρόγχων για να ελεγχθούν αν τροποποιούνται εντός του βρόγχου
    finalCodeGenerator: FinalCodeGenerator # Ο παραγωγός τελικού κώδικα

    def checkToSetStartingQuad(self, isFirstExecutableQuadOfProcedureOrFunction):
         if isFirstExecutableQuadOfProcedureOrFunction:
                subroutine = self.symbolTable.setStartingQuad(self.generatedProgram.nextQuad())
                return False
         return isFirstExecutableQuadOfProcedureOrFunction
    
    def checkIfForID(self, name, line):
        counter = 0
        for id in reversed(self.forStatIDs):
            if name == id:
                if counter != 1:
                    print(f"Error: At line {line} variable {name}, which is defined in header of for loop {counter} levels outside of current one, is changed.")
                else:
                    print(f"Error: At line {line} variable {name}, which is defined in header of for loop {counter} level outside of current one, is changed.")
                sys.exit(90)
            counter+=1

    def __init__(self, currentLine, fileName, token=""):
        self.lexicalAnalyzer = Lex(currentLine, fileName, token)
        self.token = None
        self.compilation = False
        self.operand3 = 0
        self.generatedProgram = QuadList()
        self.listOfQuadPointerList = List[QuadPointerList]
        self.symbolTable = SymbolTable()
        self.functionIDs = []
        self.calledSubroutineNamesAndCurrentPositions = []
        self.forStatIDs = []
        self.finalCodeGenerator = FinalCodeGenerator(fileName)

    def syntax_analyzer(self):
        self.program()
        if (self.compilation):
            global file_to_compile
            file_to_save = sys.argv[1][:-2]
            file_to_save = file_to_save + "int"
            with open(file_to_save, "w", encoding="UTF-8") as f:
                for quad in self.generatedProgram.programList:
                    f.write(str(quad.id) + " : " + str(quad.operator) + " , " + str(quad.operand1) + " , " + str(quad.operand2) + " , " + str(quad.operand3) + "\n")

    def getToken(self):
        token = self.lexicalAnalyzer.nextToken()
        return token
    
    def newTemp(self): #Χρησιμοποιείται για τη παραγωγή μοναδικών μοναδικών προσωρινών μεταβλητών
        self.operand3TempCounter = "T" + "@" + str(self.operand3)
        self.symbolTable.addEntity(self.operand3TempCounter, "TemporaryVariable", "int", None)
        self.operand3 += 1
        return self.operand3TempCounter


# Grammatiki tis greek++
    def program(self):
        self.token = self.getToken()    
        if self.token.recognizedString == "πρόγραμμα":
            self.token = self.getToken()
            if self.token.family == "ID":
                self.programID =  self.token.recognizedString
                self.symbolTable.addScope()
                self.finalCodeGenerator.writeToAssemblyFile("L0: j Lmain") #Γράφουμε το πρόγραμμα να κάνει άλμα στη κυρίως συνάρτηση
                self.symbolTable.table[0].offset = 12 #Δημιουργούμε το πρώτο επίπεδο του πίνακα συμβόλων
                self.token = self.getToken()
                self.programblock()
            else:
                print(f"Error: At line {self.token.lineNumber} expected ID after 'πρόγραμμα'.")
                print(f"Instead token found is {self.token.recognizedString}")
        else:
            print(f"Error: At line {self.token.lineNumber} expected 'πρόγραμμα'.")
            print(f"Instead token found is {self.token.recognizedString}")

    def programblock(self):
        self.declarations()
        self.subprograms()
        if (self.token.recognizedString == "αρχή_προγράμματος"):
            self.token = self.getToken()
            self.generatedProgram.genQuadAndIncreaseCounter(self.generatedProgram.quadCounter,"begin_block", self.programID, "_", "_")
            self.sequence(isFirstExecutableQuadOfProcedureOrFunction = False)
        else:
            print(f"Error: At line {self.token.lineNumber} every main program sequence must start with 'αρχή_προγράμματος'.")
            print(f"Instead token found is {self.token.recognizedString}")
        if (self.token.recognizedString == "τέλος_προγράμματος"):
            self.compilation = True
            self.finalCodeGenerator.generateFinalCode(self.generatedProgram, self.symbolTable, mainFunctionStarts=True)
            if self.symbolTable.deletedScope is not None:
                self.symbolTable.deleteScope()
            self.symbolTable.writeSymbolTable()
            self.generatedProgram.genQuadAndIncreaseCounter(self.generatedProgram.quadCounter, "halt", "_", "_", "_")
            self.generatedProgram.genQuadAndIncreaseCounter(self.generatedProgram.quadCounter, "end_block", self.programID, "_", "_")
            self.finalCodeGenerator.terminateProgram()
        else:
            print(f"Error: At line {self.token.lineNumber}: every program must close with 'τέλος_προγράμματος'.")
            print(f"Instead token found is {self.token.recognizedString}")

    def declarations(self):
        while (self.token.recognizedString == "δήλωση"):
                self.token = self.getToken()
                self.varlist("Variable", False, None)

    def varlist(self, type, set, mode):
        if (self.token.family=="ID"):
            if (type == "Variable"):
                self.symbolTable.addEntity(self.token.recognizedString, "Variable", "int", None, self.token.lineNumber)
            elif (type == "FormalParameter" and not set):
                self.symbolTable.addEntity(self.token.recognizedString, "FormalParameter", "int", None, self.token.lineNumber)
            elif (type == "FormalParameter" and set):
                self.symbolTable.setFormalParameterMode(self.token.recognizedString, mode, self.token.lineNumber)
            self.token = self.getToken()
            stop = False
            while (not stop):
                if (self.token.family == "Comma"):
                    self.token = self.getToken()
                    if (self.token.family == "ID"):
                        if (type == "Variable"):
                            self.symbolTable.addEntity(self.token.recognizedString, "Variable", "int", None, self.token.lineNumber)
                        elif (type == "FormalParameter" and not set):
                            self.symbolTable.addEntity(self.token.recognizedString, "FormalParameter", "int", None, self.token.lineNumber)
                        elif (type == "FormalParameter" and set):
                            self.symbolTable.setFormalParameterMode(self.token.recognizedString, mode, self.token.lineNumber)
                        self.token = self.getToken()
                    else:
                        print(f"Error: At line '{self.token.line_counter}' at a list of variables there is a comma wtih no parameter after it.")
                        print(f"Token found is {self.token.recognizedString}.")
                else:
                    stop = True
        else:
            print(f"Error: At line {self.token.lineNumber} there is missing an ID.")
            print(f"Token found is {self.token.recognizedString}")

    def subprograms(self):
        if (self.token.recognizedString == "συνάρτηση"):
            while (self.token.recognizedString == "συνάρτηση"):
                self.token = self.getToken()
                self.func()
        if (self.token.recognizedString == "διαδικασία"):
            while (self.token.recognizedString == "διαδικασία"):
                self.token = self.getToken()
                self.proc()

    def func(self):     
        functionID = self.token.recognizedString
        functionLine = self.token.lineNumber
        if (self.token.family == "ID"):
            entity = self.symbolTable.addEntity(functionID, "Function", "int", None, self.token.lineNumber)
            self.generatedProgram.genQuadAndIncreaseCounter(self.generatedProgram.quadCounter,"begin_block", functionID, "_", "_")
            self.functionIDs.append([functionID, 0])
            self.token = self.getToken()
            if (self.token.family == "Opening Par"):
                self.token = self.getToken()
                self.formalparlist()
            else:
                print(f"Error: At line {self.token.lineNumber} there is missing one '('")
                print(f"Token found is {self.token.recognizedString}")
            if (self.token.family == "Closing Par"):
                self.token = self.getToken()
                self.funcblock(functionID, functionLine)
                if self.functionIDs[-1][1] == 0: #Αν ο μετρητής είναι μηδέν η συνάρτηση δεν επιστρέφει τίποτα
                    print(f"Error: Function {functionID} startting at line {functionLine} does not return a value.")
                    sys.exit(1)
                self.functionIDs.pop() #Αφαίρεσε τη συνάρτηση από τις συναρτήσεις που πρέπει να ελεγχθούν αν επιστρέφουν τίποτα
                self.generatedProgram.genQuadAndIncreaseCounter(self.generatedProgram.quadCounter,"end_block", functionID, "_", "_")
                self.finalCodeGenerator.generateFinalCode(self.generatedProgram, self.symbolTable)
                self.symbolTable.deleteScope()
                self.symbolTable.writeSymbolTable()
            else:
                print(f"Error: At line {self.token.lineNumber} there is missing one ')'")
                print(f"Token found is {self.token.recognizedString}")
        else:
            print(f"Error: At line {self.token.lineNumber} there is no function ID")
            print(f"Token found is {self.token.recognizedString} of family {self.token.family}")

    def proc(self):
        tempID = self.token.recognizedString
        procedureLine = self.token.lineNumber
        if (self.token.family == "ID"):
            self.symbolTable.addEntity(tempID, "Procedure", None, None, self.token.lineNumber)
            self.generatedProgram.genQuadAndIncreaseCounter(self.generatedProgram.quadCounter,"begin_block", tempID, "_", "_")
            self.token = self.getToken()
            if (self.token.family == "Opening Par"):
                self.token = self.getToken()
                self.formalparlist()
            else:
                print(f"Error: At line {self.token.lineNumber} there is missing one '('")
                print(f"Token found is {self.token.recognizedString}")
            if (self.token.family == "Closing Par"):
                self.token = self.getToken()
                self.procblock(tempID, procedureLine)
                self.generatedProgram.genQuadAndIncreaseCounter(self.generatedProgram.quadCounter, "end_block", tempID, "_", "_")
                self.finalCodeGenerator.generateFinalCode(self.generatedProgram, self.symbolTable)
                self.symbolTable.deleteScope()
                self.symbolTable.writeSymbolTable()
            else:
                print(f"Error: At line {self.token.lineNumber} there is missing one ')'")
                print(f"Token found is {self.token.recognizedString}")
        else:
            print(f"Error: At line {self.token.lineNumber} there is no procedure ID")
            print(f"Token found is {self.token.recognizedString}")
            
    def formalparlist(self):
        if self.token.family != "Closing Par":
            self.varlist("FormalParameter", False, None)

    def funcblock(self, functionID, functionLine):
        if (self.token.recognizedString == "διαπροσωπεία"):
            self.token = self.getToken()
            self.funcinput()
            self.funcoutput()
            self.symbolTable.checkIfFormalParametersAreSet(Function, functionID, functionLine) #Έλεγξε ότι όλες οι παράμετροι έχουν καθορισμένο τρόπο περάσματος
            self.declarations()
            self.subprograms()
        else:
            print(f"Error: At line {self.token.lineNumber} there is word 'διαπροσωπεία' missing.")
            print(f"Instead token found is {self.token.recognizedString}")
        if (self.token.recognizedString == "αρχή_συνάρτησης"):
            self.token = self.getToken()
            isFirstExecutableQuadOfProcedureOrFunction = True
            self.sequence(isFirstExecutableQuadOfProcedureOrFunction)
            if (self.token.recognizedString == "τέλος_συνάρτησης"):
                self.token = self.getToken()
            else:
                print(f"Error: At line {self.token.lineNumber} there must be 'τέλος_συνάρτησης'.")
                print(f"Instead token found is {self.token.recognizedString}")
        else:
            print(f"Error: At line {self.token.lineNumber} there must be 'αρχή_συνάρτησης'.")
            print(f"Instead token found is {self.token.recognizedString}")

    def procblock(self, procedureID, procedureLine):
        if (self.token.recognizedString == "διαπροσωπεία"):
            self.token = self.getToken()
            self.funcinput()
            self.funcoutput()
            self.symbolTable.checkIfFormalParametersAreSet(Procedure, procedureID, procedureLine) #Έλεγξε ότι όλες οι παράμετροι έχουν καθορισμένο τρόπο περάσματος
            self.declarations()
            self.subprograms()
        else:
            print(f"Error: At line {self.token.lineNumber} there is word 'διαπροσωπεία' missing.")
            print(f"Instead token found is {self.token.recognizedString}")
        if (self.token.recognizedString == "αρχή_διαδικασίας"):
            self.token = self.getToken()
            isFirstExecutableQuadOfProcedureOrFunction = True
            self.sequence(isFirstExecutableQuadOfProcedureOrFunction)
            if (self.token.recognizedString == "τέλος_διαδικασίας"):
                self.token = self.getToken()
            else:
                print(f"Error: At line {self.token.lineNumber} there must be 'τέλος_διαδικασίας'.")
                print(f"Instead token found is {self.token.recognizedString}")
        else:
            print(f"Error: At line {self.token.lineNumber} there must be 'αρχή_διαδικασίας'.")
            print(f"Instead token found is {self.token.recognizedString}")

    def funcinput(self):
        if self.token.recognizedString == "είσοδος":
            self.token = self.getToken()
            self.varlist("FormalParameter", True, "CV")

    def funcoutput(self):
        if self.token.recognizedString == "έξοδος":
            self.token = self.getToken()
            self.varlist("FormalParameter", True, "REF")
            
    def sequence(self, isFirstExecutableQuadOfProcedureOrFunction):
        isFirstExecutableQuadOfProcedureOrFunction = self.statement(isFirstExecutableQuadOfProcedureOrFunction)
        while (self.token.family == "Semicolon"):
            self.token = self.getToken()
            if isFirstExecutableQuadOfProcedureOrFunction:
                isFirstExecutableQuadOfProcedureOrFunction = False
            self.statement(isFirstExecutableQuadOfProcedureOrFunction)
        return isFirstExecutableQuadOfProcedureOrFunction
            
    def statement(self, isFirstExecutableQuadOfProcedureOrFunction):
        if self.token.family == "ID":
            id = self.token.recognizedString
            self.checkIfForID(self.token.recognizedString, self.token.lineNumber) #Έλεγξε αν η μεταβλητή καθορίζεται στην αρχή ενός βρόχου για
            if id == self.programID: #Έλεγξε αν το κυρίως πρόγραμμα επιστρέφει τιμή
                    print(f"Error: At line {self.token.lineNumber}, main function returns a value and main cannot return a value!")
                    sys.exit(80)
            if (len(self.functionIDs) != 0):
                if self.functionIDs[-1][0] != id: #Κάθε id που βρίσκει στο αριστερό μέλος μίας ανάθεσης να βλέπει αν είναι μία συνάρτηση
                    self.symbolTable.searchSymbol(id, Variable, self.token.lineNumber, ifProcedureReturns=True) #Αν δεν είναι μία συνάρτηση, να ελέγχει αν είναι μία ορισμένη μεταβλητή
            else:                                                                                               #Αν δεν είναι ορισμένη μεταβλητή, τότε να ελέγχει αν είναι ορισμένη διαδικασία
                self.symbolTable.searchSymbol(id, Variable, self.token.lineNumber, ifProcedureReturns=True)
            self.token = self.getToken()                                                                    
            isFirstExecutableQuadOfProcedureOrFunction = self.assignment_stat(id, isFirstExecutableQuadOfProcedureOrFunction)
        elif self.token.recognizedString == "εάν":
            self.token = self.getToken()
            isFirstExecutableQuadOfProcedureOrFunction = self.if_stat(isFirstExecutableQuadOfProcedureOrFunction)
        elif self.token.recognizedString == "όσο":
            self.token = self.getToken()
            isFirstExecutableQuadOfProcedureOrFunction = self.while_stat(isFirstExecutableQuadOfProcedureOrFunction)
        elif self.token.recognizedString == "επανάλαβε":
            self.token = self.getToken()
            isFirstExecutableQuadOfProcedureOrFunction = self.do_stat(isFirstExecutableQuadOfProcedureOrFunction)
        elif self.token.recognizedString == "για":
            self.token = self.getToken()
            isFirstExecutableQuadOfProcedureOrFunction = self.for_stat(isFirstExecutableQuadOfProcedureOrFunction)
        elif self.token.recognizedString == "γράψε":
            self.token = self.getToken()
            isFirstExecutableQuadOfProcedureOrFunction = self.print_stat(isFirstExecutableQuadOfProcedureOrFunction)
        elif self.token.recognizedString == "διάβασε":
            self.token = self.getToken()
            isFirstExecutableQuadOfProcedureOrFunction = self.input_stat(isFirstExecutableQuadOfProcedureOrFunction)
        elif self.token.recognizedString == "εκτέλεσε":
            self.token = self.getToken()
            isFirstExecutableQuadOfProcedureOrFunction = self.call_stat(isFirstExecutableQuadOfProcedureOrFunction)
            
    def assignment_stat(self, id, isFirstExecutableQuadOfProcedureOrFunction):
        if self.token.recognizedString == ":=":
            assignment_symbol = self.token.recognizedString
            self.token = self.getToken()
            E_place, isFirstExecutableQuadOfProcedureOrFunction, functionCalled = self.expression(isFirstExecutableQuadOfProcedureOrFunction)
            isFirstExecutableQuadOfProcedureOrFunction = self.checkToSetStartingQuad(isFirstExecutableQuadOfProcedureOrFunction)
            if len(self.functionIDs) != 0 and self.functionIDs[-1][0] == id: #Έλεγξε αν υπάρχει συνάρτηση η οποία επιστρέφει τιμή
                if E_place != self.functionIDs[-1][0]:
                    self.generatedProgram.genQuadAndIncreaseCounter(self.generatedProgram.quadCounter, "retv", E_place, "_", "_") #Γράψε την τετράδα επιστροφής τιμής από μία συνάρτηση
                else:
                    functionReturn = self.newTemp()
                    self.generatedProgram.genQuadAndIncreaseCounter(self.generatedProgram.quadCounter, "retv", functionReturn, "_", "_") #Γράψε την τετράδα επιστροφής τιμής από μία συνάρτηση
                self.functionIDs[-1][1] += 1
            else:
                if not functionCalled:
                    self.generatedProgram.genQuadAndIncreaseCounter(self.generatedProgram.quadCounter, assignment_symbol, E_place, "_", id)
                else:
                    w = self.newTemp()
                    self.generatedProgram.genQuadAndIncreaseCounter(self.generatedProgram.quadCounter, "par", w, "RET", "_") #Πάραξε προσωρινή μεταβλητή στην οποία αποθηκεύεται η επιστρεφόμενη τιμή μίας κληθείσας συνάρτησης
                    self.generatedProgram.genQuadAndIncreaseCounter(self.generatedProgram.quadCounter, "call" ,E_place, "_", "_") #Κάλεσε τη συνάρτηση
                    self.generatedProgram.genQuadAndIncreaseCounter(self.generatedProgram.quadCounter, ":=", w, "_", id) #Αποθήκευσε το αποτέλεσμα της κληθείσας συνάρτησης σε μία μεταβλητή
        else:
            print(f"Error: Assignment character was expected at line {self.token.lineNumber}")
            print(f"Instead token found is {self.token.recognizedString}")
        return isFirstExecutableQuadOfProcedureOrFunction
         
    def if_stat(self, isFirstExecutableQuadOfProcedureOrFunction):
        B_true, B_false, isFirstExecutableQuadOfProcedureOrFunction = self.condition(isFirstExecutableQuadOfProcedureOrFunction) #Αποθήκευσε τις επιστρεφόμενες λίστες του condition. Μία για αληθή συνθήκη και μία για ψευδή συνθήκη
        if self.token.recognizedString == "τότε":  
            self.token = self.getToken()
            self.generatedProgram.backpatch(B_true, self.generatedProgram.nextQuad()) #P1
            self.sequence(isFirstExecutableQuadOfProcedureOrFunction)
            ifList = QuadPointerList(self.generatedProgram.nextQuad()) #P2
            self.generatedProgram.genQuadAndIncreaseCounter(self.generatedProgram.quadCounter, "jump","_", "_", "_" ) #P2
            self.generatedProgram.backpatch(B_false, self.generatedProgram.nextQuad())  #P2
            self.elsepart()
            self.generatedProgram.backpatch(ifList, self.generatedProgram.nextQuad()) #P3
            if (self.token.recognizedString == "εάν_τέλος"):
                self.token = self.getToken()
            else:
                print(f"Error: At line {self.token.lineNumber} there is missing a 'εάν_τέλος'")
                print(f"Token found is {self.token.recognizedString}")
            return isFirstExecutableQuadOfProcedureOrFunction
        
    def elsepart(self):
        if self.token.recognizedString == "αλλιώς":
            self.token = self.getToken()
            self.sequence(isFirstExecutableQuadOfProcedureOrFunction=False)
            
    def while_stat(self, isFirstExecutableQuadOfProcedureOrFunction):
        Bquad = self.generatedProgram.nextQuad() #P1
        B_true, B_false, isFirstExecutableQuadOfProcedureOrFunction = self.condition(isFirstExecutableQuadOfProcedureOrFunction) #Η self.condition επιστρέφει δύο λίστες οι οποίες γίνονται backpatch
        if self.token.recognizedString == "επανάλαβε":
            self.generatedProgram.backpatch(B_true, self.generatedProgram.nextQuad()) #P2
            self.token = self.getToken()
            self.sequence(isFirstExecutableQuadOfProcedureOrFunction=False)
            self.generatedProgram.genQuadAndIncreaseCounter(self.generatedProgram.quadCounter, "jump", "_", "_", str(Bquad)) #P3
            self.generatedProgram.backpatch(B_false, self.generatedProgram.nextQuad()) #P3
            if self.token.recognizedString == "όσο_τέλος":
                self.token = self.getToken()
            else:
                print(f"Error: At line {self.token.lineNumber} 'όσο' block must end with 'όσο_τέλος' in while loop.")
                print(f"Instead there is {self.token.recognizedString}.")
        else:
            print(f"Error: At line {self.token.lineNumber} expected 'επανάλαβε' after condition in 'όσο' statement.")
            print(f"Instead token found was {self.token.recognizedString}")
        return isFirstExecutableQuadOfProcedureOrFunction
                   
    def do_stat(self, isFirstExecutableQuadOfProcedureOrFunction):
        sQuad = self.generatedProgram.nextQuad() #P1
        isFirstExecutableQuadOfProcedureOrFunction = self.sequence(isFirstExecutableQuadOfProcedureOrFunction)
        if self.token.recognizedString == "μέχρι":
            self.token = self.getToken()
            cond_true, cond_false, isFirstExecutableQuadOfProcedureOrFunction = self.condition(isFirstExecutableQuadOfProcedureOrFunction) #Here condition returns two lists which later are backpatched
            self.generatedProgram.backpatch(cond_false, sQuad) #P2
            self.generatedProgram.backpatch(cond_true, self.generatedProgram.nextQuad()) #P2
        else:
            print(f"Error: At line {self.token.lineNumber} expected 'μέχρι' after sequence in do loop.")
            print(f"Instead token found was {self.token.recognizedString}")
        return isFirstExecutableQuadOfProcedureOrFunction
            
    def for_stat(self, isFirstExecutableQuadOfProcedureOrFunction):
        tempID = self.token.recognizedString
        self.forStatIDs.append(tempID)
        if self.token.family == "ID":
            self.token = self.getToken()
            if self.token.recognizedString == ":=":
                self.token = self.getToken()
                E_place, isFirstExecutableQuadOfProcedureOrFunction, functionCalled = self.expression(isFirstExecutableQuadOfProcedureOrFunction)
                isFirstExecutableQuadOfProcedureOrFunction = self.checkToSetStartingQuad(isFirstExecutableQuadOfProcedureOrFunction)
                self.generatedProgram.genQuadAndIncreaseCounter(self.generatedProgram.quadCounter,":=", E_place, "_", tempID) #P1 Θέσε το ID ίσο με μία τιμή
                flag = self.newTemp() # Πάραξε μία προσωρινή μεταβλητή η οποία θα κρατάει το αν το ID είναι μικρότερο από τον στόχο στην αρχή ή όχι
                self.generatedProgram.genQuadAndIncreaseCounter(self.generatedProgram.quadCounter, ":=", "1", "_", flag) #P1 Θέσε το flag 1 υποθέτοντας ότι το ID μικρότερο από τον στόχο
                if self.token.recognizedString == "έως":
                    self.token = self.getToken()
                    exp, isFirstExecutableQuadOfProcedureOrFunction, functionCalled = self.expression(isFirstExecutableQuadOfProcedureOrFunction)
                    setFlagFalseList = QuadPointerList(self.generatedProgram.nextQuad())
                    self.generatedProgram.genQuadAndIncreaseCounter(self.generatedProgram.quadCounter, ">", tempID, exp, "_") # P2 Έλεγξε αν το ID είναι μεγαλύτερο από τον στόχο και αν είναι κάνε άλμα, για να τεθεί false
                    NotChangedFlagList = QuadPointerList(self.generatedProgram.nextQuad())
                    self.generatedProgram.genQuadAndIncreaseCounter(self.generatedProgram.quadCounter, "jump", "_", "_", "_") # Αν πιο πριν αποφασίσαμε ότι η αρχική μας υπόθεση για το flag ήταν σωστή κάνε άλμα πιο κάτω
                    changeFlagQuad = self.generatedProgram.nextQuad()
                    self.generatedProgram.genQuadAndIncreaseCounter(self.generatedProgram.quadCounter, ":=", "0", "_", flag) # Θέσε το flag μηδέν, δηλαδή false, αφού η αρχική υπόθεση ότι το ID είναι μικρότερο από τον στόχο είναι λάθος
                    self.generatedProgram.backpatch(setFlagFalseList, changeFlagQuad)
                    self.generatedProgram.backpatch(NotChangedFlagList, self.generatedProgram.nextQuad())
                    FlagIsTrueList = QuadPointerList(self.generatedProgram.nextQuad()) # Φτιάξε μία λίστα που περιέχει το που θα πηγαίνει η ροή του προγράμματος όταν το flag ισχύει
                    self.generatedProgram.genQuadAndIncreaseCounter(self.generatedProgram.quadCounter, "=", flag, "1", "_") # Δες αν το flag ισούται με 1, δηλαδή είναι true, και αν είναι κάνε άλμα, για να κάνεις τη σύγκριση 
                    FlagIsFalseList = QuadPointerList(self.generatedProgram.nextQuad())
                    self.generatedProgram.genQuadAndIncreaseCounter(self.generatedProgram.quadCounter, "=", flag, "0", "_") # Δες αν το flag ισούται με 0 και αν είναι κάνε άλμα
                    forContinuesForSmallerInitialValueList = QuadPointerList(self.generatedProgram.nextQuad()) # Δημιουργούμε τον κώδικα σύγκρισης του ID με τον στόχο για το flag είναι 1, δηλαδή αν το ID ήταν εξαρχής μικρότερο του στόχου
                    FlagIsTrueQuad = self.generatedProgram.nextQuad()
                    self.generatedProgram.backpatch(FlagIsTrueList, FlagIsTrueQuad) # Αν το flag είναι true δες αν το ID έχει γίνει μικρότερο από τον στόχο όταν κάνεις σύγκριση
                    self.generatedProgram.genQuadAndIncreaseCounter(self.generatedProgram.quadCounter, "<" , tempID, exp, "_") # Κάνε άλμα πίσω στην αρχή, αφού το ID είναι ακόμη μικρότερο του στόχου
                    ListOfFalseConditionWhenSmaller = QuadPointerList(self.generatedProgram.nextQuad()) 
                    self.generatedProgram.genQuadAndIncreaseCounter(self.generatedProgram.quadCounter, "jump", "_", "_", "_") # Αν το ID έχει γίνει μεγαλύτερο από τον στόχο σταμάτα την εκτέλεση του βρόγχου
                    FlagIsFalseQuad = self.generatedProgram.nextQuad()
                    self.generatedProgram.backpatch(FlagIsFalseList, FlagIsFalseQuad) # Αν το flag είναι false τότε κάνε την ακόλουθη σύγκριση
                    forContinuesForBiggerInitialValueList = QuadPointerList(self.generatedProgram.nextQuad()) # 
                    self.generatedProgram.genQuadAndIncreaseCounter(self.generatedProgram.quadCounter, ">" , tempID, exp, "_") # Δες αν το flag είναι μεγαλυτερο του στόχου και αν είναι συνέχισε να εκτελείς τον βρόγχο
                    ListOfFalseConditionWhenBigger = QuadPointerList(self.generatedProgram.nextQuad())
                    self.generatedProgram.genQuadAndIncreaseCounter(self.generatedProgram.quadCounter, "jump", "_", "_", "_") # Αν δεν είναι πια μεγαλύτερο το ID από τον στόχο τότε τερμάτισε την εκτέλεση του βρόγχου
                    forContinuesForSmallerInitialValueList.mergeList(forContinuesForSmallerInitialValueList, forContinuesForBiggerInitialValueList) # Συνδύασε τις λίστες των τετράδων που κάνουν άλμα πίσω στην αρχή ενώ το flag είναι αληθές, αφού συνεχίζει να ισχύει η συνθήκη
                    self.generatedProgram.backpatch(forContinuesForSmallerInitialValueList, self.generatedProgram.nextQuad()) # Κάνε backpacth την τετράδα στην αρχή με τις  λίστες
                    E_place = self.step()
                    temp = self.newTemp()
                    self.generatedProgram.genQuadAndIncreaseCounter(self.generatedProgram.quadCounter,":=", E_place, "_", temp) # Υπολόγισε το βήμα
                    if self.token.recognizedString == "επανάλαβε":
                        self.token = self.getToken()
                        self.sequence(isFirstExecutableQuadOfProcedureOrFunction)
                        self.generatedProgram.genQuadAndIncreaseCounter(self.generatedProgram.quadCounter,"+", temp, tempID, tempID) # Αύξησε το ID σύμφωνα με το βήμα
                        self.generatedProgram.genQuadAndIncreaseCounter(self.generatedProgram.quadCounter, "=" , flag, "1", FlagIsTrueQuad) # Αν το flag είναι true τότε κάνε άλμα για να κάνεις τη σύγκριση ID < στόχος
                        self.generatedProgram.genQuadAndIncreaseCounter(self.generatedProgram.quadCounter, "jump", "_", "_", FlagIsFalseQuad) # Διαφορετικά το flag είνα 0 και πρέπει να γίνει η σύγκριση ID > στόχος 
                        ListOfFalseConditionWhenSmaller.mergeList(ListOfFalseConditionWhenSmaller ,ListOfFalseConditionWhenBigger) # Συνδύασε τις λίστες των τετράδων για το πού κάνει άλμα το πρόγραμμα όταν δεν ισχύει πια η συνθήκη
                        self.generatedProgram.backpatch(ListOfFalseConditionWhenSmaller, self.generatedProgram.nextQuad()) # Κάνε backpatch τη λίστα με τις ταυτότητες των τετράδων οι οποίες είναι υπεύθυνες για τον τερματισμό του βρόγχου
                        if self.token.recognizedString == "για_τέλος":
                            self.token = self.getToken()
                            self.forStatIDs.pop()
                        else:
                            print("Error: 'για' block must end with 'για_τέλος' in for loop.")
                            print(f"Token found is {self.token.recognizedString}")
                    else:
                        print("Error: Expected 'επανάλαβε' after expression step in for loop.")
                        print(f"Instead token found is {self.token.recognizedString}")
                else:
                    print("Error: Expected 'έως' after expression in for loop.")
                    print(f"Instead token found is {self.token.recognizedString}")
            else:
                print("Error: Expected ':=' after ID in for loop.")
                print(f"Instead token found is {self.token.recognizedString}")
        else:
            print(f"Error: expected ID at line {self.token.lineNumber} after 'για'")
            print(f"Instead token found is {self.token.recognizedString}")
        return isFirstExecutableQuadOfProcedureOrFunction
            
    def step(self):
        if self.token.recognizedString == "με_βήμα":
            self.token = self.getToken()
            T1_place = self.expression(False)
            return T1_place[0]
        return str(1)
            
    def print_stat(self, isFirstExecutableQuadOfProcedureOrFunction):
        E_place, isFirstExecutableQuadOfProcedureOrFunction, functionCalled = self.expression(isFirstExecutableQuadOfProcedureOrFunction)
        isFirstExecutableQuadOfProcedureOrFunction = self.checkToSetStartingQuad(isFirstExecutableQuadOfProcedureOrFunction)
        self.generatedProgram.genQuadAndIncreaseCounter(self.generatedProgram.quadCounter, "out", E_place, "_", "_") #P1
        return isFirstExecutableQuadOfProcedureOrFunction
            
    def input_stat(self, isFirstExecutableQuadOfProcedureOrFunction):
        if self.token.family == "ID":
            scope, symbol = self.symbolTable.searchSymbol(self.token.recognizedString, Variable, self.token.lineNumber)
            self.checkIfForID(self.token.recognizedString, self.token.lineNumber) #Έλεγξε αν η μεταβλητή καθορίζεται στην αρχή ενός βρόχου για
            self.generatedProgram.genQuadAndIncreaseCounter(self.generatedProgram.quadCounter ,"in", self.token.recognizedString, "_", "_") #P1
            self.token = self.getToken()
        else:
            print(f"Error: Expected 'ID' after 'διάβασε' at line {self.token.lineNumber}.")
            print(f"Instead token found is {self.token.recognizedString}")
        return isFirstExecutableQuadOfProcedureOrFunction
    
    def call_stat(self, isFirstExecutableQuadOfProcedureOrFunction):
        if self.token.family == "ID":
            tempID = self.token.recognizedString
            self.calledSubroutineNamesAndCurrentPositions.append([Procedure ,tempID, 0]) #Αποθήκευσε την διαδικασία σε μία στοίβα καλούμενων υπορουτίνων
            self.symbolTable.searchSymbol(tempID, Procedure, self.token.lineNumber)
            self.token = self.getToken()
            isFirstExecutableQuadOfProcedureOrFunction, functionCalled = self.idtail(isFirstExecutableQuadOfProcedureOrFunction)
            isFirstExecutableQuadOfProcedureOrFunction = self.checkToSetStartingQuad(isFirstExecutableQuadOfProcedureOrFunction)
            self.generatedProgram.genQuadAndIncreaseCounter(self.generatedProgram.quadCounter, "call", tempID, "_", "_") #P1
        else:
            print(f"Error: At line {self.token.lineNumber} expected 'ID' after 'εκτέλεσε'.")
            print(f"Instead token found is {self.token.recognizedString}")
        return isFirstExecutableQuadOfProcedureOrFunction
            
    def idtail(self, isFirstExecutableQuadOfProcedureOrFunction):
        isFirstExecutableQuadOfProcedureOrFunction, functionCalled = self.actualpars(isFirstExecutableQuadOfProcedureOrFunction)
        return isFirstExecutableQuadOfProcedureOrFunction, functionCalled
        
    def actualpars(self, isFirstExecutableQuadOfProcedureOrFunction):
        functionCalled = False
        if self.token.family == "Opening Par":
            functionCalled = True
            self.token = self.getToken()
            E_place, isFirstExecutableQuadOfProcedureOrFunction = self.actualparlist(isFirstExecutableQuadOfProcedureOrFunction)
            if self.token.family == "Closing Par":
                self.symbolTable.checkNumberOfElements(self.calledSubroutineNamesAndCurrentPositions[-1][0], self.calledSubroutineNamesAndCurrentPositions[-1][1], self.calledSubroutineNamesAndCurrentPositions[-1][2], self.token.lineNumber) #Κοίτα αν έχει δωθεί σωστό πλήθος παραμέτρων
                self.token = self.getToken()
                self.calledSubroutineNamesAndCurrentPositions.pop() #Αν έχει καλεστεί συνάρτηση ή διαδικασία τότε τώρα σταματάει να καλείται και πρέπει να βγει από τη στοίβα calledSubroutineNamesAndCurrentPositions
            else:
                print(f"Error: At line {self.token.lineNumber} expected ')' at the end of actual parameters.")
                print(f"Instead token found is {self.token.recognizedString}")
        else:
            self.calledSubroutineNamesAndCurrentPositions.pop() #Αν δεν έχει καλεστεί συνάρτηση έχει προστεθεί στη στοίβα calledSubroutineNamesAndCurrentPositions μεταβλητή και πρέπει να αφαιρεθεί
        return isFirstExecutableQuadOfProcedureOrFunction, functionCalled
            
    def actualparlist(self, isFirstExecutableQuadOfProcedureOrFunction):
        E_place, isFirstExecutableQuadOfProcedureOrFunction = self.actualparitem(isFirstExecutableQuadOfProcedureOrFunction)
        while self.token.recognizedString == ',':
            self.token = self.getToken()
            self.actualparitem(isFirstExecutableQuadOfProcedureOrFunction)
        return  E_place, isFirstExecutableQuadOfProcedureOrFunction
            
    def actualparitem(self, isFirstExecutableQuadOfProcedureOrFunction): #Η actualparitem εκτελείται μόνο όταν καλείται κάποια υπορουτίνα
        if self.token.recognizedString == "%":
            self.token = self.getToken()
            if self.token.family == "ID":
                self.checkIfForID(self.token.recognizedString, self.token.lineNumber) #Έλεγξε αν η μεταβλητή καθορίζεται στην αρχή ενός βρόχου για
                self.symbolTable.checkIfPassedRight(self.calledSubroutineNamesAndCurrentPositions[-1][0], self.calledSubroutineNamesAndCurrentPositions[-1][1], self.calledSubroutineNamesAndCurrentPositions[-1][2],"REF", self.token.recognizedString, self.token.lineNumber)
                self.calledSubroutineNamesAndCurrentPositions[-1][2] += 1
                isFirstExecutableQuadOfProcedureOrFunction = self.checkToSetStartingQuad(isFirstExecutableQuadOfProcedureOrFunction)
                self.generatedProgram.genQuadAndIncreaseCounter(self.generatedProgram.quadCounter,"par", self.token.recognizedString, "REF", "_") #P2
                ID_found = self.token.recognizedString
                self.token = self.getToken()
                return ID_found, isFirstExecutableQuadOfProcedureOrFunction
            else:
                print(f"Error: At line {self.token.lineNumber} Expected 'ID' after '%'.")
                print(f"Instead token found is {self.token.recognizedString}")
        elif self.token.family != "Closing Par":
            E_place, isFirstExecutableQuadOfProcedureOrFunction, functionCalled = self.expression(isFirstExecutableQuadOfProcedureOrFunction, isVariablePassedToSubroutine=True) #Βλέπουμε αν η μεταβλητή περνιέται σε υπορουτίνα
            self.symbolTable.checkIfPassedRight(self.calledSubroutineNamesAndCurrentPositions[-1][0], self.calledSubroutineNamesAndCurrentPositions[-1][1], self.calledSubroutineNamesAndCurrentPositions[-1][2], "CV", E_place, self.token.lineNumber)
            self.calledSubroutineNamesAndCurrentPositions[-1][2] += 1
            isFirstExecutableQuadOfProcedureOrFunction = self.checkToSetStartingQuad(isFirstExecutableQuadOfProcedureOrFunction)
            self.generatedProgram.genQuadAndIncreaseCounter(self.generatedProgram.quadCounter, "par", E_place, "CV", "_") #P1
            return E_place, isFirstExecutableQuadOfProcedureOrFunction
        return None, isFirstExecutableQuadOfProcedureOrFunction
            
    def condition(self, isFirstExecutableQuadOfProcedureOrFunction): 
        B_true, B_false, isFirstExecutableQuadOfProcedureOrFunction = self.boolterm(isFirstExecutableQuadOfProcedureOrFunction) #P1
        while self.token.recognizedString == "ή":
            self.generatedProgram.backpatch(B_false, self.generatedProgram.nextQuad()) #P2
            self.token = self.getToken()
            Q2_true, Q2_false, isFirstExecutableQuadOfProcedureOrFunction = self.boolterm(isFirstExecutableQuadOfProcedureOrFunction)
            B_true.mergeList(B_true, Q2_true)
            B_false = Q2_false
        return B_true, B_false, isFirstExecutableQuadOfProcedureOrFunction
            
    def boolterm(self, isFirstExecutableQuadOfProcedureOrFunction):
        R1_true, R1_false, isFirstExecutableQuadOfProcedureOrFunction = self.boolfactor(isFirstExecutableQuadOfProcedureOrFunction)
        Q_true, Q_false = R1_true, R1_false #P1
        while self.token.recognizedString == "και":
            self.generatedProgram.backpatch(Q_true, self.generatedProgram.nextQuad()) #P2
            self.token = self.getToken()
            R2_true, R2_false, isFirstExecutableQuadOfProcedureOrFunction = self.boolfactor(isFirstExecutableQuadOfProcedureOrFunction)
            Q_false.mergeList(Q_false, R2_false) #P3
            Q_true = R2_true #P3
        return Q_true, Q_false, isFirstExecutableQuadOfProcedureOrFunction
            
    def boolfactor(self, isFirstExecutableQuadOfProcedureOrFunction):
        R_true = R_false = []
        if self.token.recognizedString == "όχι":
            self.token = self.getToken()
            if self.token.recognizedString == "[":
                self.token = self.getToken()
                R_false, R_true, isFirstExecutableQuadOfProcedureOrFunction = self.condition(isFirstExecutableQuadOfProcedureOrFunction) #P1
                if self.token.recognizedString == "]":
                    self.token = self.getToken()
                else:
                    print(f"Error: At line {self.token.lineNumber} expected ']' after condition.")
                    print(f"Instead token found is {self.token.recognizedString}")
            else:
                print(f"Error: At line {self.token.lineNumber} expected '[' after 'όχι'.")
                print(f"Instead token found is {self.token.recognizedString}")
        elif self.token.family == "Opening Bracket":
            self.token = self.getToken()
            R_true, R_false, isFirstExecutableQuadOfProcedureOrFunction = self.condition(isFirstExecutableQuadOfProcedureOrFunction) #P2
            if self.token.family == "Closing Bracket":
                self.token = self.getToken()
            else:
                print(f"Error: Expected ']' at line {self.token.lineNumber} after condition.")
                print(f"Instead token found is {self.token.recognizedString}")
        else:
            E1_place, isFirstExecutableQuadOfProcedureOrFunction, functionCalled = self.expression(isFirstExecutableQuadOfProcedureOrFunction)
            tempRelationalOper = self.relational_oper()
            E2_place, isFirstExecutableQuadOfProcedureOrFunction, functionCalled = self.expression(isFirstExecutableQuadOfProcedureOrFunction)
            R_true = QuadPointerList(self.generatedProgram.nextQuad()) #P3
            isFirstExecutableQuadOfProcedureOrFunction = self.checkToSetStartingQuad(isFirstExecutableQuadOfProcedureOrFunction)
            self.generatedProgram.genQuadAndIncreaseCounter(self.generatedProgram.quadCounter, tempRelationalOper , E1_place, E2_place, "_") #P3
            R_false = QuadPointerList(self.generatedProgram.nextQuad()) #P3
            self.generatedProgram.genQuadAndIncreaseCounter(self.generatedProgram.quadCounter,"jump", "_", "_", "_") #P3
        return R_true, R_false, isFirstExecutableQuadOfProcedureOrFunction

    def expression(self, isFirstExecutableQuadOfProcedureOrFunction, isVariablePassedToSubroutine=False): #Με τον όρο υπορουτίνα εννοούμε συνάρτηση ή διαδικασία
        optional_sign = self.optional_sign()
        T1_place, isFirstExecutableQuadOfProcedureOrFunction, functionCalled = self.term(isFirstExecutableQuadOfProcedureOrFunction, isVariablePassedToSubroutine)
        if (optional_sign == None): #Αν δεν έχουμε αρνητικό πρόσημο
            while self.token.family == "Addition Operator":
                operator_found  = self.token.recognizedString
                self.add_oper()
                T2_place, isFirstExecutableQuadOfProcedureOrFunction, functionCalled = self.term(isFirstExecutableQuadOfProcedureOrFunction, isVariablePassedToSubroutine)
                w = self.newTemp() #P1
                isFirstExecutableQuadOfProcedureOrFunction = self.checkToSetStartingQuad(isFirstExecutableQuadOfProcedureOrFunction)
                self.generatedProgram.genQuadAndIncreaseCounter(self.generatedProgram.quadCounter, operator_found, T1_place, T2_place, w) #P1
                T1_place = w #P1
        elif (optional_sign == "-1"): #Αν έχουμε αρνητικό πρόσημο
            w = self.newTemp()
            self.generatedProgram.genQuadAndIncreaseCounter(self.generatedProgram.quadCounter, "-", "0", T1_place, w) #Αφαιρούμε τον αριθμό από το μηδέν για να τον κάνουμε αρνητικό
            T1_place = w
            while self.token.family == "Addition Operator":
                operator_found  = self.token.recognizedString
                self.add_oper()
                T2_place, isFirstExecutableQuadOfProcedureOrFunction, functionCalled = self.term(isFirstExecutableQuadOfProcedureOrFunction, isVariablePassedToSubroutine)
                w = self.newTemp() #P1
                isFirstExecutableQuadOfProcedureOrFunction = self.checkToSetStartingQuad(isFirstExecutableQuadOfProcedureOrFunction)
                self.generatedProgram.genQuadAndIncreaseCounter(self.generatedProgram.quadCounter, operator_found, T1_place, T2_place, w) #P1
                T1_place = w #P1
        return T1_place, isFirstExecutableQuadOfProcedureOrFunction, functionCalled #P2
            
    def term(self, isFirstExecutableQuadOfProcedureOrFunction, isVariablePassedToSubroutine=False):
        F1_place, isFirstExecutableQuadOfProcedureOrFunction, functionCalled = self.factor(isFirstExecutableQuadOfProcedureOrFunction, isVariablePassedToSubroutine)
        while self.token.family == "Multiplication Operator":
            mul_operator = self.mul_oper()
            F2_place, ProcedureOrFunction, functionCalled = self.factor(isFirstExecutableQuadOfProcedureOrFunction, isVariablePassedToSubroutine)
            w = self.newTemp() #P1
            isFirstExecutableQuadOfProcedureOrFunction = self.checkToSetStartingQuad(isFirstExecutableQuadOfProcedureOrFunction)
            self.generatedProgram.genQuadAndIncreaseCounter(self.generatedProgram.quadCounter, mul_operator, F1_place, F2_place, w) #P1
            F1_place = w #P1
        return F1_place, isFirstExecutableQuadOfProcedureOrFunction, functionCalled  #P2
            
    def factor(self, isFirstExecutableQuadOfProcedureOrFunction, isVariablePassedToSubroutine):
        functionCalled = False
        if self.token.family == "Number":
            number_found = self.token
            self.token = self.getToken()
            return number_found.recognizedString, isFirstExecutableQuadOfProcedureOrFunction, functionCalled
        elif self.token.family == "Opening Par":
            self.token = self.getToken()
            E_place, isFirstExecutableQuadOfProcedureOrFunction, functionCalled = self.expression(isFirstExecutableQuadOfProcedureOrFunction)
            if (self.token.family == "Closing Par"):
                self.token = self.getToken()
                return E_place, isFirstExecutableQuadOfProcedureOrFunction, functionCalled
            else:
                print(f"Error: At line {self.token.lineNumber} there is a ')' missing.")
        elif self.token.family == "ID":
            tempID = self.token.recognizedString
            line = self.token.lineNumber
            self.calledSubroutineNamesAndCurrentPositions.append([Function, tempID, 0]) #Πρόσθεσε τη συνάρτηση στη στοίβα για έλεγχο των παραμέτρων που της περνιούνται
            self.token = self.getToken()
            isFirstExecutableQuadOfProcedureOrFunction, functionCalled = self.idtail(isFirstExecutableQuadOfProcedureOrFunction)
            if functionCalled:
                scope, symbolPlace = self.symbolTable.searchSymbol(tempID, Function, line) #Έλεγξε ότι η κληθείσα συνάρτηση υπάρχει
                w = self.newTemp()
                self.generatedProgram.genQuadAndIncreaseCounter(self.generatedProgram.quadCounter, "par", w, "RET", "_") #Πάραξε προσωρινή μεταβλητή στην οποία αποθηκεύεται η επιστρεφόμενη τιμή μίας κληθείσας συνάρτησης
                self.generatedProgram.genQuadAndIncreaseCounter(self.generatedProgram.quadCounter, "call" ,tempID, "_", "_") #Κάλεσε τη συνάρτηση
                tempID = w #Επίστρεψε τη προσωρινή μεταβλητή στην οποία η συνάρτηση επιστρέφει τιμή
                functionCalled = False
            else:
                scope, symbol = self.symbolTable.searchSymbol(tempID, Variable, line)
            return tempID, isFirstExecutableQuadOfProcedureOrFunction, functionCalled
        else:
            print("Error: Invalid factor at line ", self.token.lineNumber)
            print(f"Τoken found is {self.token.recognizedString}")
        
    def relational_oper(self):
        if self.token.family == "Relational Operand":
            relational_operator = self.token.recognizedString
            self.token = self.getToken()
            return relational_operator
        else:
            print(f"Error: At line {self.token.lineNumber} there is a relational operand missing")
            print(f"Τoken found is {self.token.recognizedString}")
        
    def add_oper(self):
        if self.token.recognizedString == "+":
            addition_operator = self.token
            self.token = self.getToken()
            return None
        else:
            self.token = self.getToken()
            return str(-1)
    
    def mul_oper(self):
        if self.token.family == "Multiplication Operator":
            multiplication_operator = self.token.recognizedString
            self.token = self.getToken()
            return multiplication_operator
            
    def optional_sign(self):
        if self.token.family == "Addition Operator":
            return self.add_oper()
        return None
    

#Main runs               
def main():
    if len(sys.argv) > 2:
        print("More arguments were given than expected!", "You must enter: python <python_program>.py <file_to_compile>.gr")
        sys.exit(1)
    if len(sys.argv) < 2:
        print("Fewer arguments were given than expected!", "You must enter: python <python_program>.py <file_to_compile>.gr")
        sys.exit(1)
    if not sys.argv[0].endswith(".py"):
        print("Wrong first argument! You must enter: python <python_program>.py <file_to_compile>.gr")
    if not sys.argv[1].endswith(".gr"):
        print("Your second argument is wrong! You must enter: python <python_program>.py <file_to_compile>.gr")
    global file_to_compile
    file_to_compile = sys.argv[1]
    try:
        with open(file_to_compile, "r", encoding = "utf-8") as file_to_compile:
            global content
            content = file_to_compile.read()
            global character_pointer
            global line_counter
            global character_counter
            character_counter = 0
            character_pointer = content[character_counter]
            line_counter = 1
            parser = Parser(line_counter, file_to_compile)
            #start compiling
            parser.syntax_analyzer()
    except FileNotFoundError:
        print(f"Error: The file '{file_to_compile}' was not found.")
    
#Begin of program
if __name__ == "__main__":
    main()