bounty_type = str(input("Is the bounty a normal or legendary? \n"))

cash_base = 0
xp_base = 0
tier_multiplier = 0.0
target_count = 0
count_multiplier_cash = 0.0
count_multiplier_xp = 0.0
status_multiplier = 0.0
time_mutliplier = 0.0
difficulty_multiplier = 0.0

#For Calculating Normal Bounties

if bounty_type in ["normal", "Normal", "norm", "Norm", "n", "N", "small", "Small"]:
	print("Normal Bounty \n")
	
	#Set Base Values
	cash_base = 30
	xp_base = 600

	#Determine The Tier Multiplier
	multiplier_type = int(input("How many dollar signs($)? \n"))
	if (multiplier_type == 1):
		tier_multiplier = 1
	if (multiplier_type == 2):
		tier_multiplier = 1.25
	if (multiplier_type == 3):
		tier_multiplier = 1.5 

	#Determine The Count Multiplier
	target_count = int(input("How many targets are there? \n"))
	if (target_count == 1):
		count_multiplier_cash = 1
		count_multiplier_xp = 1
	if (target_count == 2):
		count_multiplier_cash = 5/3
		count_multiplier_xp = 1
	if (target_count == 3):
		count_multiplier_cash = 5/3
		count_multiplier_xp = 1
	if (target_count == 4):
		count_multiplier_cash = 2
		count_multiplier_xp = 1.2
	if (target_count == 5):
		count_multiplier_cash = 2
		count_multiplier_xp = 1.2
	if (target_count == 6):
		count_multiplier_cash = 2
		count_multiplier_xp = 1.2

	#Determine The Target Status
	target_status = input("Is the target alive or dead? \n")

	if (target_status in "alive","living","live","Alive","Living","Live","Yes","yes"):
		status_multiplier = 1
	if (target_status in "dead","Dead","no","No"):
		status_multiplier = 0.5

	#Determine The Time Multiplier
	time = int(input("How long in minutes did it take you to complete the mission? \n"))
	if (0 < time < 11):
		time_mutliplier = time * 0.05
	if (10 < time < 31):
		time_mutliplier = (0.025 * (time-10)) + 0.5

	print("Cash Multiplier is",count_multiplier_cash,"\n")
	print("XP Multiplier is",count_multiplier_xp,"\n")
	print("Tier Multiplier is",tier_multiplier,"\n")
	print("Status Multiplier is",status_multiplier,"\n")
	print("Time Multiplier is",time_mutliplier,"\n")
	final_cash = cash_base * tier_multiplier * count_multiplier_cash *status_multiplier * time_mutliplier
	final_xp = xp_base * tier_multiplier * count_multiplier_xp *status_multiplier * time_mutliplier
	print("Expected Cash Return is",final_cash,"\n")
	print("Expected XP Return is",final_xp,"\n")


#For Calculating Legendary Bounties
if bounty_type in ["legendary", "Legendary", "legend", "Legend", "l", "L", "big", "Big"]:
	print("Legendary Bounty \n")
	xp_base = 1000
	bounty_target = input("Who is the target? \n")
	if (bounty_target in "philip","Philip"):
		cash_base = 125
	if (bounty_target in "wolf","Wolf"):
		cash_base = 100
	if (bounty_target in "cecil","Cecil"):
		cash_base = 100
	if (bounty_target in "yukon","Yukon"):
		cash_base = 125
	if (bounty_target in "barb","Barb"):
		cash_base = 100
	if (bounty_target in "etta","Etta"):
		cash_base = 150
	if (bounty_target in "owlhoot","Owlhoot"):
		cash_base = 125
	if (bounty_target in "sergio","Sergio"):
		cash_base = 125
	if (bounty_target in "tobin","Tobin"):
		cash_base = 150
	if (bounty_target in "red","Red"):
		cash_base = 150
		

	#Determine The Count Multiplier
	target_count = int(input("How many targets are there? \n"))
	if (target_count == 1):
		count_multiplier_cash = 1
		count_multiplier_xp = 1
	if (target_count == 2):
		count_multiplier_cash = 5/3
		count_multiplier_xp = 1
	if (target_count == 3):
		count_multiplier_cash = 5/3
		count_multiplier_xp = 1
	if (target_count == 4):
		count_multiplier_cash = 2
		count_multiplier_xp = 1.2
	if (target_count == 5):
		count_multiplier_cash = 2
		count_multiplier_xp = 1.2
	if (target_count == 6):
		count_multiplier_cash = 2
		count_multiplier_xp = 1.2

	#Determine The Target Status
	target_status = input("Is the target alive or dead? \n")

	if (target_status in "alive","living","live","Alive","Living","Live","Yes","yes"):
		status_multiplier = 1
	if (target_status in "dead","Dead","no","No"):
		status_multiplier = 0.5

	#Determine The Time Multiplier
	time = int(input("How long in minutes did it take you to complete the mission? \n"))
	if (0 < time < 11):
		time_mutliplier = time * 0.05
	if (10 < time < 31):
		time_mutliplier = (0.025 * (time-10)) + 0.5

	#Difficulty Multiplier
	difficulty = int(input("How many stars is the bounty? \n"))
	if (difficulty == 1):
		difficulty_multiplier = 1
	if (difficulty == 2):
		difficulty_multiplier = 1.12
	if (difficulty == 3):
		difficulty_multiplier = 1.25
	if (difficulty == 4):
		difficulty_multiplier = 1.37
	if (difficulty == 5):
		difficulty_multiplier = 1.5
		
	#Payout
	print("Cash Multiplier is",count_multiplier_cash,"\n")
	print("XP Multiplier is",count_multiplier_xp,"\n")
	print("Status Multiplier is",status_multiplier,"\n")
	print("Time Multiplier is",time_mutliplier,"\n")
	print("Difficulty Multiplier is",difficulty_multiplier,"\n")
	final_cash = cash_base * count_multiplier_cash *status_multiplier * time_mutliplier * difficulty_multiplier
	final_xp = xp_base * count_multiplier_xp *status_multiplier * time_mutliplier * difficulty_multiplier
	print("Expected Cash Return is",final_cash,"\n")
	print("Expected XP Return is",final_xp,"\n")