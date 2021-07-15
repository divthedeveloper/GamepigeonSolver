
class Map1:
    def __init__(self) -> None:
        self.map1str = '''
        + - + - + - + - +
        |   |   |   |   |
        + - + - + - + - +
        |   |   |   |   |
        + - + - + - + - +
        |   |   |   |   |
        + - + - + - + - +
        |   |   |   |   |
        + - + - + - + - +
        '''
        self.node1 = ''
        self.node2 = ''
        self.node3 = ''
        self.node4 = ''
        self.node5 = ''
        self.node6 = ''
        self.node7 = ''
        self.node8 = ''
        self.node9 = ''
        self.node10 = ''
        self.node11 = ''
        self.node12 = ''
        self.node13 = ''
        self.node14 = '' 
        self.node15 = ''
        self.node16 = ''

        self.graph = {  self.node1 : {self.node5, self.node5},
                        self.node2 : {self.node1, }
                        
                        
                        }
        




class GUI_input():

    def __init__(self) -> None:
        self.maptype = None

    def step_1(self) -> None:
        '''Asks user to select between 4 maps of the game,
        or press enter for default 4x4 map.'''
        while(True):
            self.maptype = input(  'Options:\n\t- Press [Enter] for default 4x4 Map 1' +
                        '\n\t- Press [2] for Map 2' +
                        '\n\t- Press [3] for Map 3' +
                        '\n\t- Press [4] for Map 4\n')
            
            if (self.maptype == '') or (self.maptype == '2') or (self.maptype == '3') \
                or (self.maptype == '4'):
                break

    def step_2(self) -> None:
        '''Asks user to input words into the console given maptype, undo words,
        or go back to step 1.'''
        pass



g = GUI_input()
g.step_1()
print(g.maptype)
