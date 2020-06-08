def start_game():

    #playerone_marker = input("Player One, choose your marker.. 'X or O': ")
    #playertwo_marker = input("Player Two, choose your marker.. 'X or O': ")



    #MARKER ONE
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