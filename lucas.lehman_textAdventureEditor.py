import json

def main():
    game = {"start": ["default start node", "start over", "start", "quit", "quit"]}
    keepGoing = True
    
    while keepGoing:
        menuChoice = getMenuChoice()
   
        if menuChoice == "0":
            keepGoing = False
       
        elif menuChoice == "1":
            game = getDefaultGame()
    
        elif menuChoice == "2":
            game = loadGame()         
        
        elif menuChoice == "3":
            saveGame(game)
        
        elif menuChoice == "4":
            game = editNode(game)
    
        elif menuChoice == "5":
            playGame(game)
    
        else:
            print("please enter a valid menu choice (0-5)")
          
           
def getMenuChoice():
    print("0) exit \n1) load default game \n2) load a game file \n3) save the current game \n4) edit or add a node \n5) play the current game")
    menuChoice = input("What will you do? ")
    return menuChoice    

    
def getDefaultGame():
    print("\ndefault game loaded\n")
    game = {
        "start": ["default start node", "start over", "start", "quit", "quit"]
        }
    return game


def loadGame():
    inFile = open("game.json", "r")
    game = json.load(inFile)
    inFile.close()
    print("\nGame data loaded from file\n")
    return game

    
def saveGame(game):
    outFile = open("game.json", "w")
    json.dump(game, outFile, indent = 2)
    outFile.close()
    print("\nsaved game to game.json\n")
    
def playGame(game):
    currentNode = "start"
    keepGoing = True
    while keepGoing:
        currentNode = playNode(game, currentNode)
        if currentNode == "quit":
            keepGoing = False
    
    
def playNode(game, currentNode):
    nodeData = game[currentNode]
    print(f"\n{nodeData[0]}")
    print(f"1) {nodeData[1]}")
    print(f"2) {nodeData[3]}")
    choice = input("Your choice: (1 or 2)\n")
    
    if choice == "1":
        return nodeData[2]
    if choice == "2":
        return nodeData[4]
    else:
        print("please enter a valid choice")
        return currentNode
    
def editField(text, field):
    newField = input(f"{text} ({field}): ")
    if newField == "":
        return field
    else:
        return newField

    
def editNode(game):
    print("edit or add node\n")
    print("current status of game:")
    print(json.dumps(game, indent = 2))
    print("\nexisting node names:")
    
    for key in game:
        print(key)
    
    nodeName = input("\nChoose node to edit, or enter new node name: ")
    if nodeName in game:
        newNode = game[nodeName].copy()
    else:
        newNode = ["","","","",""]
        
    newNode[0] = editField("description", newNode[0])
    newNode[1] = editField("Menu A", newNode[1])
    newNode[2] = editField("Node A", newNode[2])
    newNode[3] = editField("Menu B", newNode[3])
    newNode[4] = editField("Node B", newNode[4])
    print()
    game[nodeName] = newNode
    return game
                 

main()