
questions = [
    {'question' : "What is the capital of Japan" ,
     'options' : ['A. Seoul' ,'B. Tokyo' , 'C. Beijing' , 'D. Bagkok'],
     'answer' : 'B'},

     {'question' : "Which data type stores key-value pairs?" ,
          'options' : ['A. List' ,'B. Tuple' , 'C. Dictionary' , 'D. Set'],
          'answer' : 'C'},

    {'question' : "What does len() returns?" ,
         'options' : ['A. Length' ,'B. Data type' , 'C. Memory size' , 'D. Index'],
         'answer' : 'A'},

    {'question' : "Which keyword skips the current loop iteration?" ,
         'options' : ['A. break' ,'B. pass' , 'C. stop' , 'D. continue'],
         'answer' : 'D'},

    {'question' : "Which symbol is used for exponetiation in Pyhton" ,
         'options' : ['A. ^' ,'B. **' , 'C. //' , 'D. %'],
         'answer' : 'B'}
    
]

score = 0

for question in questions:
    print(question['question'])
    for option in question['options']:
        print(option)

    user_answer = input('Enter your answer : ').capitalize()

    if user_answer == question['answer'] :
        print('Correct')
        score += 1
    else:
        print(f'Wrong! {question["answer"]} is the correct answer.')

print(f'Score : {score} / 5')

percentage = score / len(questions) * 100

print(f'Percentage : {percentage}')



