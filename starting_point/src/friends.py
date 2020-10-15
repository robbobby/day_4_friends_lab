import pdb
# 1. For a given person, return their name

def get_name(list):
    return list["name"]

# 2. For a given person, return their favourite tv show

def get_favourite_tv_show(list):
    return list["favourites"]["tv_show"]

# 3. For a given person, check if they like a particular food

def likes_to_eat(person, food_to_check):
    for food in person["favourites"]["snacks"]:
        if food == food_to_check:
            return True
    
    return False

# 4. For a given person, add a new name to their list of friends
# (e.g. the function add_friend(self.person2, "Scrappy-Doo") should add Scrappy-Doo to the friends.)
# (hint: This function should not return anything. After the function call, check for the length of the friends array to test it!)


    # self.person2 = {
    #   "name": "Velma",
    #   "age": 15,
    #   "monies": 2,
    #   "friends": ["Fred"],
    #   "favourites": {
    #     "tv_show": "Baywatch",
    #     "snacks": ["soup","bread"]
    #   }
    # }

def add_friend(person, new_friend_to_add):
    person["friends"].append(new_friend_to_add)

# 5. For a given person, remove a specific name from their list of friends
# (hint: Same as above, testing for the length of the array should be sufficient)

def remove_friend(person, remove_friend_name):
    person["friends"].remove(remove_friend_name)

# 6. Find the total of everyone's money
# (hint: use the self.people array, remember how we checked the total number of eggs yesterday?)

def total_money(people):
    sum_of_money = 0
    for person in people:
        sum_of_money += person["monies"]
    return sum_of_money

# 7. For two given people, allow the first person to loan a given value of money to the other
# (hint: our function will probably need 3 arguments passed to it... the ler, the lee, and the amount for this function)
# (hint2: You should test if both the ler's and the lee's money have changed, maybe two assertions?)

def l_money(person1, person2, loan_amount):
    # take money off person 1
    person1["monies"] -= loan_amount
    # add money to person 2
    person2["monies"] += loan_amount


# 8. Find the set of everyone's favourite food joined together
# (hint: concatenate the favourites/snack arrays together)

def all_favourite_foods(people):
    all_food = []

    for person in people:
        for item in person["favourites"]["snacks"]:
            all_food.append(item)

    return all_food

    # self.person2 = {
    #   "name": "Velma",
    #   "age": 15,
    #   "monies": 2,
    #   "friends": ["Fred"],
    #   "favourites": {
    #     "tv_show": "Baywatch",
    #     "snacks": ["soup","bread"]
    #   }
    # }



# our list 
# ['charcuterie', 'soup', 'bread', 'Scooby s[41 chars]ach'] != [['charcuterie'], ['soup', 'bread'], ['Sco[51 chars]ch']]

#expected
# "charcuterie", "soup", "bread", "Scooby snacks", "spaghetti", "ratatouille", "spinach"]


# 9. Find people with no friends
# (hint: return an list, there might be more people in the future with no friends!)

#define a func that takes in people
# make a empty list of people without friends 
#loop through people
# second loop through person's friends
#check if friend's list is empty
# if empty, add to list
# return a list of people without friends

def find_no_friendends(people):
    no_friends = []

    for person in people:
        for friend in person["friends"]:
            if not friend:
                pdb.set_trace()
                no_friends.append(person)
    return no_friends