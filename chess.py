from turns import *
def main():
    field_list=[["white r","white n","white b","white q","white k","white b","white n","white r"],          #this is the game field
                ["white p","white p","white p","white p","white p","white p","white p","white p"],
                [" ","█"," ","█"," ","█"," ","█"],
                ["█"," ","█"," ","█"," ","█"," "],
                [" ","█"," ","█"," ","█"," ","█"],
                ["█"," ","█"," ","█"," ","█"," "],
                ["black p","black p","black p","black p","black p","black p","black p","black p"],
                ["black r","black n","black b","black q","black k","black b","black n","black r"]]
    second_field=[["white r","white n","white b","white q","white k","white b","white n","white r"],          #this is the game field
                 ["white p","white p","white p","white p","white p","white p","white p","white p"],
                 [" ","█"," ","█"," ","█"," ","█"],
                 ["█"," ","█"," ","█"," ","█"," "],
                 [" ","█"," ","█"," ","█"," ","█"],
                 ["█"," ","█"," ","█"," ","█"," "],
                 ["black p","black p","black p","black p","black p","black p","black p","black p"],
                ["black r","black n","black b","black q","black k","black b","black n","black r"]]

    bllack_figures={"black p":"♟",        #keys to convert text field into other symbols (i know it could be easer, but i'm too lazy to fix it)
                    "black r":"♜",
                    "black n":"♞",
                    "black b":"♝",
                    "black q":"♛",
                    "black k":"♚"}
    white_figures={"white p":"♙",
                   "white r":"♖",
                   "white n":"♘",
                   "white b":"♗",
                   "white q":"♕",
                   "white k":"♔"}


    mate=False                          #preparing
    x=1
    notation=["\n"]
    tie=False

                                                    #rule explaining

    print("Program accepts algebraic chess notation only. For example, input 'Pe2-e4' will move pawn from e2 to e4")
    print("If you want to offer tie, input 'tie?' on your turn, opponent can answer 'yes' or 'no' on his turn")
    print("If you want to resign - just input 'resign' on your turn")
    print("Game ends by taking the king")
    print("Let's start!\n")

    black_ch=False
    white_ch=False
    while mate!=True and tie!=True:
                                                       #next 12 strings make and print game field

        string_to_print=""
        for row in range(8):
            string_to_print+="\n"
            for column in range(8):
                if field_list[7-row][column][0]=="b":
                    string_to_print+=bllack_figures[field_list[7-row][column]]
                elif field_list[7-row][column][0]=="w":
                    string_to_print+=white_figures[field_list[7-row][column]]
                else:
                    string_to_print+=field_list[7-row][column]

        print(string_to_print)

                                                        #changing sides
        if x%2==1:
            turn_color="white"
        else:
            turn_color="black"

        w_king_looker=0
        b_king_looker=0
                                                    #the function that gets and processes inputs and makes turns
        tie, mate, w_king_looker,b_king_looker = turn(turn_color,field_list,tie,notation,mate,w_king_looker,b_king_looker,white_ch,black_ch,second_field)

                                        # checking if both kings are on the field
        for i in range(8):
            for m in range(8):
                if field_list[i][m]=="white k":
                    w_king_looker+=1
                elif field_list[i][m]=="black k":
                    b_king_looker+=1
        if w_king_looker==0 or b_king_looker==0:
            mate=True


        x+=1
    string_not=""                       #converting notation
    for c in range(len(notation)):
        string_not+=notation[c]
    print(string_not)
    for i in range(4):              #just a little gap
        print()
    if tie==True:                                               #summing up at the end of the game
        print("game ended with tie after",x-1,"turns")
    elif mate==True:
        print("game ended by mate after",x-1,"turns")
        if b_king_looker==0:
            print("white won")
        elif w_king_looker==0:
            print("black won")
    new_game()

                                                #function that repeats the game as long as user wants to
def new_game():
    answer=input("want to play again?(yes/no) ")
    if answer=="yes":
        main()
    else:
        print("sad, bye")
main()
