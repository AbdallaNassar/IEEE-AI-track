'''
In a different file, import the dictionary you just created and write a
function to create a file named “busted.txt”. Save the data of dictionary
in this file without sex and score.
# lines in the file should be like this 1 Atef - 1970
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
def create_busted_file(users):
    with open('busted.txt', 'w') as f:
        for user_id, user_data in users.items():
            user_name = user_data['name']
            user_birthday = user_data['birthday']
            f.write(f"{user_id} {user_name} - {user_birthday}\n")
create_busted_file(users)