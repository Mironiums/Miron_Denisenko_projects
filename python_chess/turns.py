
def turn(color,field,tie,notation,mate,w_king_looker,b_king_looker,white_ch,black_ch,field2):
    from checks import check
    keys={"a":0,        #keys to convert letter notation into numbers
      "b":1,
      "c":2,
      "d":3,
      "e":4,
      "f":5,
      "g":6,
      "h":7}
    m=False                             #just a variable that repeats the loop


    while m==False:
        try:

                                                    #taking input and preparing it for the checking


            if check(field2)==(True, False):
                white_ch=True
                print("check to white")
            elif check(field2)==(False, True):
                black_ch=True
                print("check to black")
            elif check(field2)==(False, False):
                white_ch=False
                black_ch=False

            real_turn=input("{}'s turn: ".format(color)).lower()

            if len(real_turn)==6 and real_turn[3]=="-":

                turn_list=[real_turn[0],int(real_turn[2])-1,keys[real_turn[1]],int(real_turn[5])-1,keys[real_turn[4]]]
                promotion=""





                go, promotion=way(turn_list,field,color,promotion)
                if color+" "+turn_list[0]==field[turn_list[1]][turn_list[2]] and go:


                    if promotion=="":
                        field2[turn_list[3]][turn_list[4]]=field2[turn_list[1]][turn_list[2]]
                    else:
                        field2[turn_list[3]][turn_list[4]]=color+" "+promotion

                    if (turn_list[1]+turn_list[2])%2==0:
                        field2[turn_list[1]][turn_list[2]]=" "
                    else:
                        field2[turn_list[1]][turn_list[2]]="█"


                    if white_ch==True and check(field2)==(True,False):
                        print("\nPay attention on check")
                        continue
                    elif black_ch==True and check(field2)==(False,True):
                        print("\nPay attention on check")
                        continue


                    if promotion=="":
                        field[turn_list[3]][turn_list[4]]=field[turn_list[1]][turn_list[2]]
                    else:
                        field[turn_list[3]][turn_list[4]]=color+" "+promotion

                    if (turn_list[1]+turn_list[2])%2==0:
                        field[turn_list[1]][turn_list[2]]=" "
                    else:
                        field[turn_list[1]][turn_list[2]]="█"


                                                            #keeping notation
                    if color=="black":
                        notation.append("   :   ")
                        notation.append(real_turn)
                        notation.append("\n")
                    elif color=="white":
                        notation.append(real_turn)
                    m=True
                else:
                    print("somewhere is an error")


                                                    #checking for tie
            elif real_turn=="tie?":
                answer=input("(yes/no) ")
                if answer=="yes":
                    m=True
                    tie=True
                else:
                    print("game continuous")
                                                    #checking for resinging
            elif real_turn=="resign":
                m=True
                mate=True
                if color=="white":
                    w_king_looker-=1
                else:
                    b_king_looker-=1

                                                        #two cases for wrong answers. better to be safe
            else:
                print("Incorrect input. Plese try again")
                continue
        except:
            print("Incorrect input. Plese try again")
            continue
    return tie,mate,w_king_looker,b_king_looker

                                                #the function that checks for moves' possibilities
                                               #the function that checks for moves' possibilities
def way_r(turn,field,color,x):
    if (turn[4]==turn[2] or turn[3]==turn[1]) and field[turn[3]][turn[4]][0]!=color[0]:
        if turn[4]>turn[2] and turn[3]==turn[1]:
            for i in range(turn[2]+1-turn[4]):
                if field[turn[1]][turn[2]+i]==" " or field[turn[1]][turn[2]+i]=="█":
                    x+=0
                else:
                    x+=1
        elif turn[4]<turn[2] and turn[3]==turn[1]:
            for i in range(turn[4]+1-turn[2]):
                if field[turn[1]][turn[4]+i]==" " or field[turn[1]][turn[4]+i]=="█":
                    x+=0
                else:
                    x+=1
        elif turn[4]==turn[2] and turn[3]<turn[1]:
            for i in range(turn[3]+1-turn[1]):
               if field[turn[3]+i][turn[2]]==" " or field[turn[3]+i][turn[2]]=="█":
                   x+=0
               else:
                   x+=1
        elif turn[4]==turn[2] and turn[3]>turn[1]:
            for i in range(turn[1]+1-turn[3]):
                if field[turn[1]+i][turn[2]]==" " or field[turn[1]+i][turn[2]]=="█":
                    x+=0
                else:
                    x+=1
    else:
        x+=1


                                                    # check if bishop can move if player uses bishop
def way_b(turn,field,color,x):
    if (turn[2]-turn[4]==turn[1]-turn[3] or turn[2]-turn[4]==turn[3]-turn[1]) and field[turn[3]][turn[4]][0]!=color[0]:
        if turn[2]<turn[4] and turn[1]<turn[3]:
            for i in range(1,turn[4]-turn[2]):
                if field[turn[1]+i][turn[2]+i]==" " or field[turn[1]+i][turn[2]+i]=="█":
                    x+=0
                else:
                    x+=1
        elif turn[2]>turn[4] and turn[1]<turn[3]:
            for i in range(1,turn[2]-turn[4]):
                if field[turn[1]+i][turn[2]-i]==" " or field[turn[1]+i][turn[2]-i]=="█":
                    x+=0
                else:
                    x+=1
        elif turn[2]<turn[4] and turn[1]>turn[3]:
            for i in range(1,turn[4]-turn[2]):
                if field[turn[1]-i][turn[2]+i]==" " or field[turn[1]-i][turn[2]+i]=="█":
                    x+=0
                else:
                    x+=1
        elif turn[2]>turn[4] and turn[1]>turn[3]:
            for i in range(1,turn[2]-turn[4]):
                if field[turn[1]-i][turn[2]-i]==" " or field[turn[1]-i][turn[2]-i]=="█":
                    x+=0
                else:
                    x+=1
    else:
        x+=1

    if x==0:                                # my own type of returns. I know they aren't good, but they work
        return True
    else:
        return False



                                                                        # check if pawn can move if player uses pawn
def way_p(turn,field,color,x,new):
                #white pawn
    if color=="white":
        if turn[1]==1:
            if turn[2]==turn[4] and (turn[1]==turn[3]-1 or turn[1]==turn[3]-2):
                if turn[1]==turn[3]-1 and (field[turn[3]][turn[4]]==" " or field[turn[3]][turn[4]]=="█"):
                    x+=0

                elif turn[1]==turn[3]-2 and ((field[turn[3]-1][turn[4]]==" " or field[turn[3]-1][turn[4]]=="█") and (field[turn[3]][turn[4]]==" " or field[turn[3]][turn[4]]=="█")):
                    x+=0

                else:
                    x+=1

            elif turn[1]==turn[3]-1 and (turn[2]==turn[4]-1 or turn[2]==turn[4]+1):
                if field[turn[3]][turn[4]]==" " or field[turn[3]][turn[4]]=="█":
                    x+=0
                else:
                    x+=1
            else:
                x+=1


        else:
            if turn[2]==turn[4] and turn[1]==turn[3]-1:
                if turn[1]==turn[3]-1 and (field[turn[3]][turn[2]]==" " or field[turn[3]][turn[2]]=="█"):
                    x+=0
                else:
                    x+=1
            elif turn[1]==turn[3]-1 and (turn[2]==turn[4]-1 or turn[2]==turn[4]+1):
                if field[turn[3]][turn[4]]==" " or field[turn[3]][turn[4]]=="█":
                    x+=1
            else:
                x+=1

        if x==0 and turn[3]==7:
            new+=input("Promotes to\n")[0].lower()
            if new=="k":
                new="n"




                                            #black pawn
    else:
        if turn[1]==6:
            if turn[2]==turn[4] and (turn[1]==turn[3]+1 or turn[1]==turn[3]+2):
                if turn[1]==turn[3]+1 and (field[turn[3]][turn[4]]==" " or field[turn[3]][turn[4]]=="█"):
                    x+=0

                elif turn[1]==turn[3]+2 and ((field[turn[3]+1][turn[4]]==" " or field[turn[3]+1][turn[4]]=="█") and (field[turn[3]][turn[4]]==" " or field[turn[3]][turn[4]]=="█")):
                    x+=0
                else:
                    x+=1

            elif turn[1]==turn[3]+1 and (turn[2]==turn[4]-1 or turn[2]==turn[4]+1):
                if field[turn[3]][turn[4]]==" " or field[turn[3]][turn[4]]=="█":
                    x+=0
                else:
                    x+=1
            else:
                x+=1

        elif turn[3]==0:


            if turn[2]==turn[4] and turn[1]==turn[3]+1:
                if turn[1]==turn[3]+1 and (field[turn[3]][turn[2]]==" " or field[turn[3]][turn[2]]=="█"):
                    x+=0
                else:
                    x+=1
            elif turn[1]==turn[3]+1 and (turn[2]==turn[4]-1 or turn[2]==turn[4]+1):
                if field[turn[3]][turn[4]]==" " or field[turn[3]][turn[4]]=="█":
                    x+=1
            else:
                x+=1
        if x==0 and turn[3]==0:
            new+=input("Promotes to\n")[0].lower()
            if new=="k":
                new="n"


    if x==0:                                # my own type of returns. I know they aren't good, but they work
        return True, new

    else:
        return False, new
                                                        #knight moves check

def way_n(turn,field,color,x):
    if color=="white":
        if ((turn[4]==turn[2]-1 and turn[3]==turn[1]+2) or (turn[4]==turn[2]+2 and turn[3]==turn[1]-1) or (turn[4]==turn[2]+2 and turn[3]==turn[1]+1) or (turn[4]==turn[2]+1 and turn[3]==turn[1]+2) or (turn[4]==turn[2]+1 and turn[3]==turn[1]-2) or (turn[4]==turn[2]-2 and turn[3]==turn[1]+1) or (turn[4]==turn[2]-2 and turn[3]==turn[1]-1) or (turn[4]==turn[2]-1 and turn[3]==turn[1]-2) or (turn[4]==turn[2]+1 and turn[3]==turn[1]-2)) and field[turn[3]][turn[4]][0]!="w":
            x+=0
        else:
            x+=1
    elif color=="black":
        if ((turn[4]==turn[2]-1 and turn[3]==turn[1]+2) or (turn[4]==turn[2]+2 and turn[3]==turn[1]-1) or (turn[4]==turn[2]+2 and turn[3]==turn[1]+1) or (turn[4]==turn[2]+1 and turn[3]==turn[1]+2) or (turn[4]==turn[2]+1 and turn[3]==turn[1]-2) or (turn[4]==turn[2]-2 and turn[3]==turn[1]+1) or (turn[4]==turn[2]-2 and turn[3]==turn[1]-1) or (turn[4]==turn[2]-1 and turn[3]==turn[1]-2) or (turn[4]==turn[2]+1 and turn[3]==turn[1]-2)) and field[turn[3]][turn[4]][0]!="b":
            x+=0
        else:
            x+=1
    else:
        x+=1
    if x==0:                                # my own type of returns. I know they aren't good, but they work
        return True
    else:
        return False



                                                    #check for queen
def way_q(turn,field,color,x):

            #rook like queen's mpve

    if (turn[4]==turn[2] or turn[3]==turn[1]) and field[turn[3]][turn[4]][0]!=color[0]:
        if turn[4]>turn[2] and turn[3]==turn[1]:
            for i in range(turn[2]+1-turn[4]):
                if field[turn[1]][turn[2]+i]==" " or field[turn[1]][turn[2]+i]=="█":
                    x+=0
                else:
                    x+=1
        elif turn[4]<turn[2] and turn[3]==turn[1]:
            for i in range(turn[4]+1-turn[2]):
                if field[turn[1]][turn[4]+i]==" " or field[turn[1]][turn[4]+i]=="█":
                    x+=0
                else:
                    x+=1
        elif turn[4]==turn[2] and turn[3]<turn[1]:
            for i in range(turn[3]+1-turn[1]):
                if field[turn[3]+i][turn[2]]==" " or field[turn[3]+i][turn[2]]=="█":
                    x+=0
                else:
                    x+=1
        elif turn[4]==turn[2] and turn[3]>turn[1]:
            for i in range(turn[1]+1-turn[3]):
                if field[turn[1]+i][turn[2]]==" " or field[turn[1]+i][turn[2]]=="█":
                    x+=0
                else:
                    x+=1


            #bishop-like queen's move

    elif (turn[2]-turn[4]==turn[1]-turn[3] or turn[2]-turn[4]==turn[3]-turn[1]) and field[turn[3]][turn[4]][0]!=color[0]:
        if turn[2]<turn[4] and turn[1]<turn[3]:
            for i in range(turn[4]-turn[2]):
                if field[turn[1]+i][turn[2]+i]==" " or field[turn[1]+i][turn[2]+i]=="█":
                    continue
                else:
                    x+=1
        elif turn[2]>turn[4] and turn[1]<turn[3]:
            for i in range(1,turn[2]-turn[4]):
                if field[turn[1]+i][turn[2]-i]==" " or field[turn[1]+i][turn[2]-i]=="█":
                    x+=0
                else:
                    x+=1
        elif turn[2]<turn[4] and turn[1]>turn[3]:
            for i in range(1,turn[4]-turn[2]):
                if field[turn[1]-i][turn[2]+i]==" " or field[turn[1]-i][turn[2]+i]=="█":
                    x+=0
                else:
                    x+=1
        elif turn[2]>turn[4] and turn[1]>turn[3]:
            for i in range(1,turn[2]-turn[4]):
                if field[turn[1]-i][turn[2]-i]==" " or field[turn[1]-i][turn[2]-i]=="█":
                    x+=0
                else:
                    x+=1
    if x==0:                                # my own type of returns. I know they aren't good, but they work
        return True
    else:
        return False

                                #king movings
def way_k(turn,field,color,x):
    if ((turn[2]==turn[4] and turn[1]+1==turn[3]) or (turn[2]+1==turn[4] and turn[1]+1==turn[3]) or (turn[2]+1==turn[4] and turn[1]==turn[3]) or (turn[2]+1==turn[4] and turn[1]-1==turn[3]) or (turn[2]==turn[4] and turn[1]-1==turn[3]) or (turn[2]-1==turn[4] and turn[1]-1==turn[3]) or (turn[2]-1==turn[4] and turn[1]==turn[3]) or (turn[2]-1==turn[4] and turn[1]+1==turn[3])) and field[turn[3]][turn[4]][0]!=color[0]:
        x+=0
    else:
        x+=1
    if x==0:                                # my own type of returns. I know they aren't good, but they work
        return True
    else:
        return False


def way(turn,field,color,new):
    x=0
    if turn[0]=="p":
        ans,new=way_p(turn,field,color,x,new)
    elif turn[0]=="r":
        ans=way_r(turn,field,color,x)
    elif turn[0]=="b":
        ans=way_b(turn,field,color,x)
    elif turn[0]=="k":
        ans=way_k(turn,field,color,x)
    elif turn[0]=="n":
        ans=way_n(turn,field,color,x)
    elif turn[0]=="q":
        ans=way_q(turn,field,color,x)
    else:
        ans=False
    return ans,new
