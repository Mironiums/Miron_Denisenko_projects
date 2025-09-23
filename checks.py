def check(field):
    x=0
    king_lock=0
    for i in range(8):
        try:
            king_pos2=field[i].index("white k")
            king_lock+=1
            king_pos=[i,king_pos2]
        except:
            king_lock+=0
    if king_lock>0:

                                                            #rook and queen
        for i in range(1,king_pos[0]+1):
            if (field[king_pos[0]-i][king_pos[1]]=="black r" or field[king_pos[0]-i][king_pos[1]]=="black q") and king_pos[0]-i>=0:                        #it may count king as a figure
                x+=1
                break
            elif not (field[king_pos[0]-i][king_pos[1]]==" " or field[king_pos[0]-i][king_pos[1]]=="█"):

                break


        for i in range(1,7-king_pos[0]):
            if (field[king_pos[0]+i][king_pos[1]]=="black r" or field[king_pos[0]+i][king_pos[1]]=="black q") and king_pos[0]+i<8:
                x+=1
                break
            elif not (field[king_pos[0]+i][king_pos[1]]==" " or field[king_pos[0]+i][king_pos[1]]=="█"):
                break


        for i in range(1,king_pos[1]+1):
            if (field[king_pos[0]][king_pos[1]-i]=="black r" or field[king_pos[0]][king_pos[1]-i]=="black q") and king_pos[1]-i>=0:
                x+=1
                break
            elif not (field[king_pos[0]][king_pos[1]-i]==" " or field[king_pos[0]][king_pos[1]-i]=="█"):
                break

        for i in range(1,7-king_pos[1]):
            if (field[king_pos[0]][king_pos[1]+i]=="black r" or field[king_pos[0]][king_pos[1]+i]=="black q") and king_pos[1]+i<8:
                x+=1
                break
            elif not (field[king_pos[0]][king_pos[1]+i]==" " or field[king_pos[0]][king_pos[1]+i]=="█"):
                break

                                                        #bishop and queen

        for i in range(1,7):
                try:
                    if (field[king_pos[0]+i][king_pos[1]+i]=="black b" or field[king_pos[0]+i][king_pos[1]+i]=="black q") and (king_pos[0]+i<8 and king_pos[0]+i>=0) and (king_pos[1]+i<8 and king_pos[1]+i>=0):
                        x+=1
                        break
                    elif not (field[king_pos[0]+i][king_pos[1]+i]==" " or field[king_pos[0]+i][king_pos[1]+i]=="█"):
                        break
                except:
                    break
        for i in range(1,7):
            try:
                if (field[king_pos[0]+i][king_pos[1]-i]=="black b" or field[king_pos[0]+i][king_pos[1]-i]=="black q")  and (king_pos[0]+i<8 and king_pos[0]+i>=0) and (king_pos[1]-i<8 and king_pos[1]-i>=0):
                    x+=1
                    break
                elif not (field[king_pos[0]+i][king_pos[1]-i]==" " or field[king_pos[0]+i][king_pos[1]-i]=="█"):
                    break
            except:
                break
        for i in range(1,7):
            try:
                if (field[king_pos[0]-i][king_pos[1]+i]=="black b" or field[king_pos[0]-i][king_pos[1]+i]=="black q")  and (king_pos[0]-i<8 and king_pos[0]-i>=0) and (king_pos[1]+i<8 and king_pos[1]+i>=0):
                    x+=1
                    break
                elif not (field[king_pos[0]-i][king_pos[1]+i]==" " or field[king_pos[0]-i][king_pos[1]+i]=="█"):
                    break
            except:
                break
        for i in range(1,7):
            try:
                if (field[king_pos[0]-i][king_pos[1]-i]=="black b" or field[king_pos[0]-i][king_pos[1]-i]=="black q") and (king_pos[0]-i<8 and king_pos[0]-i>=0) and (king_pos[1]-i<8 and king_pos[1]-i>=0):
                    x+=1
                    break
                elif not (field[king_pos[0]-i][king_pos[1]-i]==" " or field[king_pos[0]-i][king_pos[1]-i]=="█"):
                    break
            except:
                break





        try:
            if field[king_pos[0]+2][king_pos[1]+1]=="black n" and king_pos[0]+2<8 and king_pos[1]+1<8:
                x+=1
        except:
            x+=0

        try:
            if field[king_pos[0]+2][king_pos[1]-1]=="black n" and king_pos[1]-1>=0 and king_pos[0]+2<8:
                x+=1
        except:
            x+=0

        try:
            if field[king_pos[0]-2][king_pos[1]+1]=="black n" and king_pos[0]-2>=0 and king_pos[1]+1<8:
                x+=1
        except:
            x+=0

        try:
            if field[king_pos[0]-2][king_pos[1]-1]=="black n" and king_pos[0]-2>=0 and king_pos[1]-1>=0:
                x+=1
        except:
            x+=0

        try:
            if field[king_pos[0]+1][king_pos[1]+2]=="black n" and king_pos[1]+2<8 and king_pos[0]+1<8:
                x+=1
        except:
            x+=0

        try:
            if field[king_pos[0]+1][king_pos[1]-2]=="black n" and king_pos[0]+1<8 and king_pos[1]-2>=0:
                x+=1
        except:
            x+=0

        try:
            if field[king_pos[0]-1][king_pos[1]+2]=="black n" and king_pos[1]+2<8 and king_pos[0]-1>=0:
                x+=1
        except:
            x+=0

        try:
            if field[king_pos[0]-1][king_pos[1]-2]=="black n" and king_pos[0]-1>=0 and king_pos[1]-2:
                x+=1
        except:
            x+=0

        try:
            if field[king_pos[0]+1][king_pos[1]+1]=="black p" or field[king_pos[0]+1][king_pos[1]-1]=="black p":
                x+=1
        except:
            x+=0


    if x==0:
        way1=False
    else:
        way1=True






                            # just copied and pasted. Yes, i'm lazy
    x=0
    king_lock=0
    for i in range(8):
        try:
            king_pos2=field[i].index("black k")
            king_lock+=1
            king_pos=[i,king_pos2]
        except:
            king_lock+=0
    if king_lock>0:


                                                            #rook and queen
        for i in range(1,king_pos[0]+1):
            if (field[king_pos[0]-i][king_pos[1]]=="white r" or field[king_pos[0]-i][king_pos[1]]=="white q") and king_pos[0]-i>=0:                        #it may count king as a figure
                x+=1
                break
            elif not (field[king_pos[0]-i][king_pos[1]]==" " or field[king_pos[0]-i][king_pos[1]]=="█"):


                break




        for i in range(1,7-king_pos[0]):
            if (field[king_pos[0]+i][king_pos[1]]=="white r" or field[king_pos[0]+i][king_pos[1]]=="white q") and king_pos[0]+i<8:
                x+=1
                break
            elif not (field[king_pos[0]+i][king_pos[1]]==" " or field[king_pos[0]+i][king_pos[1]]=="█"):
                break




        for i in range(1,king_pos[1]+1):
            if (field[king_pos[0]][king_pos[1]-i]=="white r" or field[king_pos[0]][king_pos[1]-i]=="white q") and king_pos[1]-i>=0:
                x+=1
                break
            elif not (field[king_pos[0]][king_pos[1]-i]==" " or field[king_pos[0]][king_pos[1]-i]=="█"):
                break


        for i in range(1,7-king_pos[1]):
            if (field[king_pos[0]][king_pos[1]+i]=="white r" or field[king_pos[0]][king_pos[1]+i]=="white q") and king_pos[1]+i<8:
                x+=1
                break
            elif not (field[king_pos[0]][king_pos[1]+i]==" " or field[king_pos[0]][king_pos[1]+i]=="█"):
                break


                                                        #bishop and queen


        for i in range(1,7):
                try:
                    if (field[king_pos[0]+i][king_pos[1]+i]=="white b" or field[king_pos[0]+i][king_pos[1]+i]=="white q") and (king_pos[0]+i<8 and king_pos[0]+i>=0) and (king_pos[1]+i<8 and king_pos[1]+i>=0):
                        x+=1
                        break
                    elif not (field[king_pos[0]+i][king_pos[1]+i]==" " or field[king_pos[0]+i][king_pos[1]+i]=="█"):
                        break
                except:
                    break
        for i in range(1,7):
            try:
                if (field[king_pos[0]+i][king_pos[1]-i]=="white b" or field[king_pos[0]+i][king_pos[1]-i]=="white q")  and (king_pos[0]+i<8 and king_pos[0]+i>=0) and (king_pos[1]-i<8 and king_pos[1]-i>=0):
                    x+=1
                    break
                elif not (field[king_pos[0]+i][king_pos[1]-i]==" " or field[king_pos[0]+i][king_pos[1]-i]=="█"):
                    break
            except:
                break
        for i in range(1,7):
            try:
                if (field[king_pos[0]-i][king_pos[1]+i]=="white b" or field[king_pos[0]-i][king_pos[1]+i]=="white q")  and (king_pos[0]-i<8 and king_pos[0]-i>=0) and (king_pos[1]+i<8 and king_pos[1]+i>=0):
                    x+=1
                    break
                elif not (field[king_pos[0]-i][king_pos[1]+i]==" " or field[king_pos[0]-i][king_pos[1]+i]=="█"):
                    break
            except:
                break
        for i in range(1,7):
            try:
                if (field[king_pos[0]-i][king_pos[1]-i]=="white b" or field[king_pos[0]-i][king_pos[1]-i]=="white q") and (king_pos[0]-i<8 and king_pos[0]-i>=0) and (king_pos[1]-i<8 and king_pos[1]-i>=0):
                    x+=1
                    break
                elif not (field[king_pos[0]-i][king_pos[1]-i]==" " or field[king_pos[0]-i][king_pos[1]-i]=="█"):
                    break
            except:
                break







        try:
            if field[king_pos[0]+2][king_pos[1]+1]=="white n" and king_pos[0]+2<8 and king_pos[1]+1<8:
                x+=1
        except:
            x+=0


        try:
            if field[king_pos[0]+2][king_pos[1]-1]=="white n" and king_pos[1]-1>=0 and king_pos[0]+2<8:
                x+=1
        except:
            x+=0


        try:
            if field[king_pos[0]-2][king_pos[1]+1]=="white n" and king_pos[0]-2>=0 and king_pos[1]+1<8:
                x+=1
        except:
            x+=0


        try:
            if field[king_pos[0]-2][king_pos[1]-1]=="white n" and king_pos[0]-2>=0 and king_pos[1]-1>=0:
                x+=1
        except:
            x+=0


        try:
            if field[king_pos[0]+1][king_pos[1]+2]=="white n" and king_pos[1]+2<8 and king_pos[0]+1<8:
                x+=1
        except:
            x+=0


        try:
            if field[king_pos[0]+1][king_pos[1]-2]=="white n" and king_pos[0]+1<8 and king_pos[1]-2>=0:
                x+=1
        except:
            x+=0


        try:
            if field[king_pos[0]-1][king_pos[1]+2]=="white n" and king_pos[1]+2<8 and king_pos[0]-1>=0:
                x+=1
        except:
            x+=0


        try:
            if field[king_pos[0]-1][king_pos[1]-2]=="white n" and king_pos[0]-1>=0 and king_pos[1]-2:
                x+=1
        except:
            x+=0


        try:
            if field[king_pos[0]+1][king_pos[1]+1]=="white p" or field[king_pos[0]+1][king_pos[1]-1]=="white p":
                x+=1
        except:
            x+=0




    if x==0:
        way2=False
    else:
        way2=True



    return way1,way2

