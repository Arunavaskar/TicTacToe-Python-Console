import player_input,updated_board

while True:
        playerone_marker = input("Player One, choose your marker.. 'X or O': ")


        if playerone_marker.lower() == "x":
            #print(marker)
            break

        elif  playerone_marker.lower() == "o":
            #print(marker)
            break
        #elif marker == "quite":
            #print("quited!")
            #break
        else:
            print("You need to choose between X or O, Try Again!")
            continue

    #MARKER TWO
    playertwo_marker = ""
    if playerone_marker == "x":
        playertwo_marker = "o"
    elif playerone_marker == "o":
        playertwo_marker = "x"
    print("So Player Two, your marker is ",playertwo_marker)


    board = """
            1           |2           |3
                        |            |    
                        |            |
            ------------|------------|------------
            4           |5           |6
                        |            |    
                        |            |
            ------------|------------|------------
            7           |8           |9
                        |            |    
                        |            |

    """

    print("\nHere is the Classic Tic-Tac-Toe board\n", board)
        
#POSITION
while True:
    
    playerone_position = int(input("Player One, enter the position you want, from 1 to 9: "))
    if playerone_position in range(1,10):
        break
    else:
        print("You need to choose from 1 to 9, Try Again!")
        continue
        

while True:
    
    playertwo_position = int(input("Player Two, enter the position you want, from 1 to 9: "))
    if playertwo_position in range(1,10):
        break
    else:
        print("You need to choose from 1 to 9, Try Again!")
        continue
player_input(playerone_marker,playertwo_marker,playerone_position,playertwo_position)
#player_two_input(playerone_marker,playertwo_marker,playerone_position,playertwo_position)        
#updated_board(blank_B)
