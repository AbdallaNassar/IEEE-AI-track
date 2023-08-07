'''
Download this file and write a program to read the file and store the
users in the dictionary with the following structure:
{'id' : {'name','score','birthday','sex'}}
then write a program to answer the following questions :
a. Do no store a user with no registered score ? # [ N/A ]
b. What is the ID of the oldest user ?
c. What is the average score ?
d. What is the sex of the user with the highest score ?

'''
users = {}
oldest_user_id = 0
oldest_user_birthday = 9999
highest_score = -9999
highest_score_sex = None
score_sum = 0
score_count = 0
with open('database.txt', 'r') as f:
    for line in f:
        fields = line.strip().split(' ')
        id = fields[0]
        name = fields[1]
        score = fields[2]
        birthday = fields[4]
        sex = fields[6]
        if score == 'N/A':
            continue
        users[id] = {'name': name, 'score': int(score), 'birthday': int(birthday), 'sex': sex}
        if int(birthday) < oldest_user_birthday:
            oldest_user_id = id
            oldest_user_birthday = int(birthday)
        if int(score) > highest_score:
            highest_score = int(score)
            highest_score_sex = sex
        score_sum += int(score)
        score_count += 1
average_score = score_sum / score_count
print( "Users:>> " ,users)
print("Oldest user ID:", oldest_user_id)
print("Average score:", average_score)
print("Sex of user with highest score:", highest_score_sex)