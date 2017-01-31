n = int(input())

i = 0
team = ''
time = 0
ques =0

while i < n:
    line_input = input().split()
    team_time = 0
    team_ques = 0
    team_name = line_input [0]
    j = 1
    while j < 9:
        try_times = int(line_input[j])
        solve_time = int(line_input[j+1])
        if solve_time > 0:
            team_ques = team_ques+1
            team_time = team_time + solve_time + 20*(try_times-1)
        j = j+2
    if (team_ques > ques) | (team_ques == ques) & (team_time < time):
        team = team_name
        ques = team_ques
        time = team_time
    i = i+1
    
    
print (team, ques, time)