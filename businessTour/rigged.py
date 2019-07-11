"""
to generate the data, play a game with NB_PLAYERS bots then find the output_log.txt
file and run the command : grep "on cell" output_log.txt > rigged.txt
"""
import seaborn as sns
import matplotlib.pyplot as plt

DATA_PATH = "./rigged3.txt"
NB_PLAYERS = 4

city_list = ["START", "GRANADA", "SEVILLE", "MADRID", "BALI", "HONG KONG", "BEIJING",
             "SHANGHAI", "LOST ISLAND", "VENICE", "MILAN", "ROME", "CHANCE1", "HAMBURG",
             "CYPRUS", "BERLIN", "WORLD CHAMPIONSHIPS", "LONDON", "DUBAI", "SYDNEY",
             "CHANCE2", "CHICAGO", "LAS     VEGAS", "NEW     YORK", "WORLD TOUR", "NICE",
             "LYON", "PARIS", "CHANCE3", "OSAKA", "TAX", "TOKYO"]
values = [i for i in range(32)]
city_dic = dict(zip(city_list, values))

class Player(object):

    def __init__(self, name):
        self.name = name
        self.last_case = "START"
        self.current_case = "START"
        print("New player succesfully created.")
    def dice(self):
        current = city_dic[self.current_case]
        last = city_dic[self.last_case]
        dice_roll = abs(current-last)
        if not (dice_roll < 13 and dice_roll > 1):
            dice_roll = abs(current - last + 32)
        return dice_roll


def main():
    name_1, name_2, name_3, name_4 = get_players_names()
    player_1, player_2, player_3, player_4 = Player(name_1), Player(name_2), Player(name_3), Player(name_4)
    dice_dict = play(player_1, player_2, player_3, player_4)
    plot_results(dice_dict)
    plot_real()
    chi_sqrd = compute_chi_squared(dice_dict)
    print(chi_sqrd)
    #The chi squared is higher than the critical value. We reject the null hypothesis.
    #Conclusion: the game is rigged.
    #However, more data is needed and more tests will be done soon

def compute_chi_squared(dice_dict):
    vals = [dice_dict[i] for i in range(2, 13)]
    real_vals = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
    chi_sqrd = 0
    for val, real_val in zip(vals, real_vals):
        real_val = real_val / 36
        val = val / len(vals)
        chi_sqrd += (val-real_val)**2/real_val
    return chi_sqrd

def plot_real():
    vals = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
    x_vals = [i for i in range(2, 13)]
    sns.set()
    plt.bar(x_vals, vals)
    plt.show()

def plot_results(dice_dict):
    vals = [dice_dict[i] for i in range(2, 13)]
    x_vals = [i for i in range(2, 13)]
    sns.set()
    plt.bar(x_vals, vals)
    plt.show()

def play(player_1, player_2, player_3, player_4):
    players_list = [player_1, player_2, player_3, player_4]
    ids_list = [player_1.name, player_2.name, player_3.name, player_4.name]
    dice_dict = {}
    with open(DATA_PATH) as input_file:
        for line in input_file:
            player_id = line.split("Player")[-1].split(" ")[0]
            player = players_list[ids_list.index(player_id)]
            current_case = line.split("on cell")[-1].split(":")[0].strip()
            player.last_case = player.current_case.upper()
            player.current_case = current_case.upper()
            if player.last_case != player.current_case: #not the first round infos
                #we don't take chances into consideration because there are 3 of them
                #and have unfortunately the same name. After a world tour no die is thrown.
                if (player.last_case != "CHANCE" and player.current_case != "CHANCE") and (player.last_case != "WORLD TOUR"):
                    dice = player.dice()
                    if dice in dice_dict:
                        dice_dict[dice] += 1
                    else:
                        dice_dict[dice] = 1

    return dice_dict


def get_players_names():
    ids_set = set()
    with open(DATA_PATH) as input_file:
        for line in input_file:
            player_id = line.split("Player")[-1].split(" ")[0]
            ids_set.add(player_id)
            if(len(ids_set) == NB_PLAYERS):
                return ids_set
    return None

if __name__ == "__main__":
    main()
