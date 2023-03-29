questions = ("1.What is a variable?",
             "2.What are the whole data types?",
             "3.What are the fractionated number data types?",
             "4.What is an if statement?",
             "5.What is the correct format of a for-loop in Java?",
             "6.What is the correct format of a while-loop in Java?",
             "7.What is the correct format of a do-while loop in Java?",
             "8.What is an Array vector?",
             "9.What is an Array List?",
             "10.What are the Types of Testing?",
             "11.What are the Testing Techniques?",
             "12.What are the Levels of Testing?",
             "13.What do we cover when we perform White-box Testing?",
             "14.What do we cover when we perform Black-box Testing?",
             "15.What is the basic unit of Object Oriented Programming?",
             "16.What is an Instance of a class?",
             "17.What is a Constructor?",
             "18.What is a Constructor used for?",
             "19.What is a Class comprised of?",
             "20.What is a Getter used for?"
             )

choices = (('a) a box which serves as a storing location', 'b) a reserved word', 'c) a statement', 'd) a type of data'), #1
           ('a) byte, float, double, char', 'b) int, short, long, and float', 'c) byte, short, int, and long', 'd) float and double'), #2
           ('a) int, short, long, and float', 'b) byte, float, double, char', 'c) float and double', 'd) byte, float, double, char'), #3
           ('a) a built in function', 'b) a conditional statement that allows you to execute a block of code if a certain condition is true', 'c) A reserved keyword for defining variables', 'd) a type of sequencing'), #4
           ('a) for i = 0; i < n; i++', 'b) for (i = 0; i < n; i++)', 'c) for (int i = 0; i < n; i++)', 'd) for i = 0; i < n; i)'), #5
           ('a) while (i <= 100) {do something}', 'b) int i = 0, while (i <= 100) {do something i++}', 'c) while i+i = 0 {do something ++i}', 'd) while i in range(n): {do something i++;}'), #6
           ('a) do {something ++i} while i>100', 'b) do {++i something} while i!=100', 'c) do {something ++i} while i<= 100', 'd) int i = 0; do {something i++} while (i<=100)'), #7
           ('a) an ordered collection of elements', 'b) a resizable vector', 'c) a list', 'd) a variable'), #8
           ('a) a list of variables', 'b) a vector', 'c) a resizable vector', 'd) an ordered collection of elements'), #9
           ('a) Experience Based Testing, Exploratory Testing, Monkey Testing, Security Testing', 'b) Functional Testing, Non-functional Testing, Static Testing, Dynamic Testing', #10
            'c) Non-functional Testing, Functional Testing, White-box Testing, Black-box Testing', 'd) White-box Testing, Black-box Testing, Experience Based Testing, Exploratory Testing'),
           ('a) White-box Testing, Black-box Testing, Experienced-based testing, Exploratory Testing, Monkey Testing','b) Unit Testing, Equivalence Class Partitioning, Boundry Value Analysis, System Testing', #11
            'c) Functional Testing, Non-functional Testing, Static Testing, Dynamic Testing', 'd) Unit Testing, Integration Testing, System Testing, Acceptance Testing'),
           ('a) Statement Coverage, Condition Coverage, Branch Coverage, Path Coverage', 'b) Statement Coverage, Class Statement, Decision Coverage, Path Coverage', #12
            'c) Static Coverage and Dynamic Coverage', 'd) Unit Testing, Integration Testing, System Testing, Acceptance Testing'),
           ('a) Equivalence Class Partitioning, Boundary Value Analysis, Decision Tables, State Transition Diagrams', 'b) Load Testing and Scalability Testing', #13
            'c) Statement Coverage, Condition Coverage, Branch Coverage, Path Coverage',
            'd) Sanity Testing, Smoke Testing, Regression Testing, Usability Testing'),
           ('a) Load Testing, System Testing', 'b) Sanity Testing, Smoke Testing, Regression Testing, Usability Testing',#14
            'c) Equivalence Class Partitioning, Boundary Value Analysis, Decision Tables, State Transition Diagrams', 'd) Component and System functional properties'),
           ('a) the class', 'b) the variable', 'c) the object', 'd) the function'), #15
           ('a) a function that initializes an element', 'b) a realization of a particular item of a class', 'c) a built in library', 'd) a realization of a function'), #16
           ('a) a constructor is a parameter that initializes the value of an object', 'b) a constructor is a special method that has the same name as the class name', #17
            'c) a constructor is a type of data', 'd) a constructor is a function'),
           ('a) for calling a method', 'b) for making the class private', 'c) for making the class public', 'd) for initializing all the member variables'),#18
           ('a) methods and functions', 'b) variables', 'c) name and behaviors', 'd) name, static attributes and dynamic behaviors'),#19
           ('a) a way to make a variable private', 'b) a function used to inherit all the attributes of another class', 'c) a way to allow other classes to read the value of a private variable', #20
            'd) a way to allow other classes to modify the value of a private variable'))

            #1  #2    #3   #4   #5  #6   #7   #8   #9   #10  #11  #12  #13  #14  #15  #16  #17  #18  #19  #20
answers = ('A', 'C', 'C', 'B', 'C', 'B', 'D', 'A', 'C', 'B', 'A', 'D', 'C', 'C', 'A', 'B', 'B', 'D', 'D', 'C')
user_answers = []
score = 0
question_index = 0

# for key, value in questions.items():
#     print(key, ": " + value['question'])
#     for choice in value['choices']:
#         print(choice)

for question in questions:
    print(question)
    for choice in choices[question_index]:
        print(choice)

    user_answer = input("Please enter A, B, C OR D: ").upper()
    user_answers.append(user_answer)
    if user_answer == answers[question_index]:
        score += 1
        print("RIGHT ANSWER!")
    else:
        print("WRONG ANSWER!")
    question_index += 1

score = int(score/len(questions) * 100)
print(f"Your score is: {score}%")


