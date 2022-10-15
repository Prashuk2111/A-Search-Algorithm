maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0]]

#  Goal Nodes & Start Node
Start = [11,2]
Goal_Node_1 = [18,23]
Goal_Node_2 = [21,2]

# Function to check if particular point in maze is out of bounds or not
def check_next_node(Node):
    x = Node[0]
    y = Node[1]
    
    if (x < 0 or x > 24 ):
            return 0

    elif (y < 0 or y > 24):
            return 0

    elif (maze[x][y] == 1):
            return 0

    else:
        return 1


def A_star_Search():

    #  Four list are created
    # Open_Queue_1 Stores all the nodes that is presne the open_queue and each node is in form of a list having, the node itself, the gn and fn value and its parent node
    Open_Queue_1 = []
    # Open_Queue_2 Stores all the nodes that is present in the open_queue for A* 
    Open_Queue_2 = [] 
    # Closed_Queue_2 Stores all the nodes that enters into close queue and each node is in form of a list having, the node itself, the gn and fn value and its parent node
    Closed_Queue_1 = []
    # Closed_Queue_1 Stores all the nodes that enters into close queue
    Closed_Queue_2 = []

    # Start node Hn, Gn
    Gn_Start = 1
    Hn_Start =  min(abs(Start[0]-Goal_Node_1[0]) + abs(Start[1]-Goal_Node_1[1]) , abs(Start[0]-Goal_Node_2[0]) + abs(Start[1]-Goal_Node_2[1]))
    Start_Node = [Start,Gn_Start,Hn_Start]
    Closed_Queue_1.append(Start_Node)
    Closed_Queue_2.append(Start_Node[0])

    # Arbitary value assigned to Current_Node which gets updated in every iteration of the loop
    Current_Node = [0,0]
    # this cost is in terms of nodes explored
    Cost = 1
    
    #  The loop ends when the Current node is on the same point as the goal node
    while((Current_Node != Goal_Node_1) and (Current_Node != Goal_Node_2) ):
        
        # parent Node is the node that was enqueued in closed queue in the last iteration
        Parent_Node = Closed_Queue_1[-1][0]
        Parent_Gn = Closed_Queue_1[-1][1]
        Parent_X = Parent_Node[0]
        Parent_Y = Parent_Node[1]
        
        
        Up = Parent_X+1
        Down = Parent_X-1
        Left = Parent_Y - 1
        Right = Parent_Y+1
        
        #  4 possible children of parent_node
        Possible_New_Children = [[Up, Parent_Y], [Down, Parent_Y], [Parent_X, Left], [Parent_X, Right]]
        
        # Iterating through the 4 possible childeren and checking if they are present in out of bounds or are in Open or close queue, If not then add the node 
        # in the open_queue with its respective fn, gn and its parent node
        for Node in Possible_New_Children:
        
            Out_of_Bounds = check_next_node(Node)
            if (Out_of_Bounds == 0):
                continue
            if Node in Closed_Queue_2:
                continue
            if Node in Open_Queue_2:
                continue
            else:
                New_Node = Node
                New_Node_Gn = Parent_Gn+1
                New_Node_Fn = New_Node_Gn + min(abs(New_Node[0]-Goal_Node_1[0]) + abs(New_Node[1]-Goal_Node_1[1]) , abs(New_Node[0]-Goal_Node_2[0]) + abs(New_Node[1]-Goal_Node_2[1]))
                Open_Queue_1.append([New_Node,New_Node_Gn,New_Node_Fn,Parent_Node])
                Open_Queue_2.append(New_Node)


        
        #  Now it is time to pop out the node from open_queue with minimum Fn value 
        # So the current_node would be the node poped out
        #  Intitally thr arbitary value is assigned to the current node respectivily to the Fn
        Current_Node = Open_Queue_1[0]
        Minimum_Fn = Current_Node[2]

        # Now we iterate through open_queue      
        for Node in Open_Queue_1:

            if (Node[2] < Minimum_Fn):
                Current_Node = Node
                Minimum_Fn = Node[2]
            
            #  Tie breaking in case we have two nodes with same fn value, then pop the node which has less hn value
            if (Node[2] == Minimum_Fn):
                if ((Node[2]-Node[1]) < (Current_Node[2] - Current_Node[1]) ):
                    Current_Node = Node
                

        #  once the node has been detected, we pop it out from open_queue and put it in close_queue
        Open_Queue_1.remove(Current_Node)
        Open_Queue_2.remove(Current_Node[0])
        Closed_Queue_1.append(Current_Node)
        Closed_Queue_2.append(Current_Node[0])

        Cost = Cost +1
        
        # Checking again if the node is not equal to goal node, if yes then break out of the loop
        if((Current_Node[0] == Goal_Node_1) or (Current_Node[0] == Goal_Node_2)):
            break

    
    #  Its time to calculate the Path to goal node
    Path =[Current_Node[0]]
    Current_node = Current_Node[0]
    Parent_Node = []
   
    # Looping through closed_queue and extracting parent of goal node, then parent of the preveious parent node and thus so on     
    while (Current_node != Start):
        for node in Closed_Queue_1:
            if node[0] == Current_node:
                Parent_Node = node[3]
                Path.append(Parent_Node)
                Current_node = Parent_Node
                break
        
    print(f"The exit found is {Path[0]}")
    print(f"The number of nodes explored {len(Closed_Queue_1)}")
    print(f"The nodes travelled by the path is {Path}")
    print(f"The cost of the path is {len(Path)}")

    #  Printing the Path onto the Maze  P = path taken , "-" = Blocked area in maze, "*" = remaining places on maze
    for i in range(24,0,-1):
        for j in range(25):

            if [i,j] in Path:
                maze[i][j] = "P"
            elif maze[i][j] == 1:
                maze[i][j] = "-"
            else:
                maze[i][j] = "*"
        print(" ".join(maze[i]))
        

if __name__ == "__main__":
    A_star_Search()


