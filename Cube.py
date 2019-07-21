import copy


GREEN = (0,255,0)
RED = (255,0,0)
YELLOW = (255,255,0)
ORANGE = (255,165,0)
WHITE = (255,255,255)
BLUE = (0,0,255)


class Cube:

    def __init__(self):
        w,h = 9,6
        self.faces = [[0 for x in range(w)] for y in range(h)]
        for i in range(0,6):
            for j in range(0,9):
                if i==0:
                    self.faces[i][j] = GREEN
                if i==1:
                    self.faces[i][j] = RED
                if i==2:
                    self.faces[i][j] = BLUE
                if i==3:
                    self.faces[i][j] = ORANGE
                if i==4:
                    self.faces[i][j] = WHITE
                if i==5:
                    self.faces[i][j] = YELLOW

        
    def move(self, move):
        for i in range(len(move)):
            reverse = False
            if i < len(move)-1:
                if move[i+1] == "'":
                    reverse = True

            # TODO: pass reverse parameter
            if move[i] == 'R':
                self.moveRightTwist()
            if move[i] == 'U':
                self.moveUpperTwist()
            if move[i] == 'F':
                self.moveFrontTwist()
            if move[i] == 'L':
                self.moveLeftTwist()
            if move[i] == 'B':
                self.moveBackTwist()
            if move[i] == 'D':
                self.moveDownTwist()

        
    def moveLeftTwist(self):
        new_faces = copy.deepcopy(self.faces)
        # red face
        new_faces[1][0] = self.faces[4][0]
        new_faces[1][3] = self.faces[4][3]
        new_faces[1][6] = self.faces[4][6]


        # white face
        new_faces[4][6] = self.faces[3][2]
        new_faces[4][3] = self.faces[3][5]
        new_faces[4][0] = self.faces[3][8]

        #orange face
        new_faces[3][2] = self.faces[5][6]
        new_faces[3][5] = self.faces[5][3]
        new_faces[3][8] = self.faces[5][0]

        #yellow face
        new_faces[5][0] = self.faces[1][0]
        new_faces[5][3] = self.faces[1][3]
        new_faces[5][6] = self.faces[1][6]


        #spinning green faces
        new_faces[0][0] = self.faces[0][6]
        new_faces[0][1] = self.faces[0][3]
        new_faces[0][2] = self.faces[0][0]
        new_faces[0][3] = self.faces[0][7]
        new_faces[0][4] = self.faces[0][4]
        new_faces[0][5] = self.faces[0][1]
        new_faces[0][6] = self.faces[0][8]
        new_faces[0][7] = self.faces[0][5]
        new_faces[0][8] = self.faces[0][2]
        
        
        self.faces = copy.deepcopy(new_faces)

        
    def moveFrontTwist(self):
        new_faces = copy.deepcopy(self.faces)

        # white face
        new_faces[4][6] = self.faces[0][8]
        new_faces[4][7] = self.faces[0][5]
        new_faces[4][8] = self.faces[0][2]

        # blue face
        new_faces[2][0] = self.faces[4][6]
        new_faces[2][3] = self.faces[4][7]
        new_faces[2][6] = self.faces[4][8]

        #yellow face
        new_faces[5][0] = self.faces[2][6]
        new_faces[5][1] = self.faces[2][3]
        new_faces[5][2] = self.faces[2][0]

        #green face
        new_faces[0][2] = self.faces[5][0]
        new_faces[0][5] = self.faces[5][1]
        new_faces[0][8] = self.faces[5][2]

        # spinning red face
        
        new_faces[1][0] = self.faces[1][6]
        new_faces[1][1] = self.faces[1][3]
        new_faces[1][2] = self.faces[1][0]
        new_faces[1][3] = self.faces[1][7]
        new_faces[1][4] = self.faces[1][4]
        new_faces[1][5] = self.faces[1][1]
        new_faces[1][6] = self.faces[1][8]
        new_faces[1][7] = self.faces[1][5]
        new_faces[1][8] = self.faces[1][2]
        
        
        self.faces = copy.deepcopy(new_faces)

    def moveUpperTwist(self):
        new_faces = copy.deepcopy(self.faces)

        # red face
        new_faces[1][0] = self.faces[2][0]
        new_faces[1][1] = self.faces[2][1]
        new_faces[1][2] = self.faces[2][2]

        #blue face
        new_faces[2][0] = self.faces[3][0]
        new_faces[2][1] = self.faces[3][1]
        new_faces[2][2] = self.faces[3][2]

        #orange face
        new_faces[3][0] = self.faces[0][0]
        new_faces[3][1] = self.faces[0][1]
        new_faces[3][2] = self.faces[0][2]

        #green face
        new_faces[0][0] = self.faces[1][0]
        new_faces[0][1] = self.faces[1][1]
        new_faces[0][2] = self.faces[1][2]

        # white face twist
        new_faces[4][0] = self.faces[4][6]
        new_faces[4][1] = self.faces[4][3]
        new_faces[4][2] = self.faces[4][0]
        new_faces[4][3] = self.faces[4][7]
        new_faces[4][4] = self.faces[4][4]
        new_faces[4][5] = self.faces[4][1]
        new_faces[4][6] = self.faces[4][8]
        new_faces[4][7] = self.faces[4][5]
        new_faces[4][8] = self.faces[4][2]
        
        
        self.faces = copy.deepcopy(new_faces)

    def moveDownTwist(self):
        new_faces = copy.deepcopy(self.faces)

        #red face
        new_faces[1][6] = self.faces[0][6]
        new_faces[1][7] = self.faces[0][7]
        new_faces[1][8] = self.faces[0][8]

        #blue face
        new_faces[2][6] = self.faces[1][6]
        new_faces[2][7] = self.faces[1][7]
        new_faces[2][8] = self.faces[1][8]

        #orange face
        new_faces[3][6] = self.faces[2][6]
        new_faces[3][7] = self.faces[2][7]
        new_faces[3][8] = self.faces[2][8]

        #green face
        new_faces[0][6] = self.faces[3][6]
        new_faces[0][7] = self.faces[3][7]
        new_faces[0][8] = self.faces[3][8]

        #yellow twist
        new_faces[5][0] = self.faces[5][6]
        new_faces[5][1] = self.faces[5][3]
        new_faces[5][2] = self.faces[5][0]
        new_faces[5][3] = self.faces[5][7]
        new_faces[5][4] = self.faces[5][4]
        new_faces[5][5] = self.faces[5][1]
        new_faces[5][6] = self.faces[5][8]
        new_faces[5][7] = self.faces[5][5]
        new_faces[5][8] = self.faces[5][2]
        
        self.faces = copy.deepcopy(new_faces)

    def moveRightTwist(self):
        new_faces = copy.deepcopy(self.faces)

        #red face
        new_faces[1][2] = self.faces[5][2]
        new_faces[1][5] = self.faces[5][5]
        new_faces[1][8] = self.faces[5][8]

        #white face
        new_faces[4][2] = self.faces[1][2]
        new_faces[4][5] = self.faces[1][5]
        new_faces[4][8] = self.faces[1][8]

        #orange face
        new_faces[3][0] = self.faces[4][8]
        new_faces[3][3] = self.faces[4][5]
        new_faces[3][6] = self.faces[4][2]

        #yellow face
        new_faces[5][2] = self.faces[3][6]
        new_faces[5][5] = self.faces[3][3]
        new_faces[5][8] = self.faces[3][0]

        #blue twist
        new_faces[2][0] = self.faces[2][6]
        new_faces[2][1] = self.faces[2][3]
        new_faces[2][2] = self.faces[2][0]
        new_faces[2][3] = self.faces[2][7]
        new_faces[2][4] = self.faces[2][4]
        new_faces[2][5] = self.faces[2][1]
        new_faces[2][6] = self.faces[2][8]
        new_faces[2][7] = self.faces[2][5]
        new_faces[2][8] = self.faces[2][2]

        self.faces = copy.deepcopy(new_faces)

    def moveBackTwist(self):
        new_faces = copy.deepcopy(self.faces)


        #white face
        new_faces[4][0] = self.faces[2][2]
        new_faces[4][1] = self.faces[2][5]
        new_faces[4][2] = self.faces[2][8]

        #blue face
        new_faces[2][2] = self.faces[5][8]
        new_faces[2][5] = self.faces[5][7]
        new_faces[2][8] = self.faces[5][6]

        #yellow face
        new_faces[5][6] = self.faces[0][0]
        new_faces[5][7] = self.faces[0][3]
        new_faces[5][8] = self.faces[0][6]

        #green face
        new_faces[0][0] = self.faces[4][2]
        new_faces[0][3] = self.faces[4][1]
        new_faces[0][6] = self.faces[4][0]


        #orange twist
        new_faces[3][0] = self.faces[3][6]
        new_faces[3][1] = self.faces[3][3]
        new_faces[3][2] = self.faces[3][0]
        new_faces[3][3] = self.faces[3][7]
        new_faces[3][4] = self.faces[3][4]
        new_faces[3][5] = self.faces[3][1]
        new_faces[3][6] = self.faces[3][8]
        new_faces[3][7] = self.faces[3][5]
        new_faces[3][8] = self.faces[3][2]
        
        
        self.faces = copy.deepcopy(new_faces)
