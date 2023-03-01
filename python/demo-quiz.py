# Question

class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices =choices
        self.answer = answer

    def chechkAnswer(self,answer):
        return self.answer == answer



#Quiz

class Quiz:
    def __init__(self,questions):
        self.questions=questions
        self.score =0
        self.questionIndex = 0 # soru indexini temsil ediyor.

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f"soru {self.questionIndex +1} : {question.text}")

        for q in question.choices :
            print('-'+ q)

        answer = input('cevap : ')
        self.guess(answer)
        self.loadQuestion()

        
    def guess(self,answer):
        question = self.getQuestion()

        if question.chechkAnswer(answer):
            self.score += 1
        self.questionIndex+=1

  


    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore
        else:
            self.displayProgress()
            self.displayQuestion()


    def showScore(self):
        print("score : ", self.score)


    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        if questionNumber > totalQuestion:
            print("Quiz bitti")
        else:
            print(f"Question {questionNumber} of {totalQuestion}".center(100,'*'))


q1 = Question("en iyi programlama dili hangisidir ?", ["c#","python","java","javascript"], "python")

q2 = Question("en popüler programlama dili hangisidir ?", ["c#","python","java","javascript"], "python")

q3 = Question("en çok kazandıran programlama dili hangisidir ?", ["c#","python","java","javascript"], "python")
questions= [q1,q2,q3]

quiz =Quiz(questions) # nesne oluşturduk quiz diye ve bu nesne Quiz classının nesnesi olduğunu belirttik ve Quiz classıda questions parametresini verdik

quiz.loadQuestion()