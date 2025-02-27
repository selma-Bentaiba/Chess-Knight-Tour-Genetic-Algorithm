from chromosome import Chromosome
import random

moves={
        1:(1,-2),
        2:(2,-1),
        3:(2,1),
        4:(1,2),
        5:(-1,2),
        6:(-2,1),
        7:(-2,-1),
        8:(-1,-2)
        }


def valid(path,pos):
    if pos[0]<0 or pos[1]<0 or pos[0]>7 or pos[1]>7:
        return False
    

    elif path.count(pos)>1:
        return False
    else:
        return True

def cycle_list(direction,index):
    l=[]
    if direction==0:
        for i in range(index+1,9):
            l.append(i)
            
        for i in range(1,index):
            l.append(i)
        
    else:
        for i in range(index-1,0,-1):
            l.append(i)
        
        for i in range(8,index,-1):
            l.append(i)
    return(l)

class Knight:
    def __init__(self,chromosome=None):
        #position tkon tuple (x,y)
        self.position=(0,0)
        if chromosome==None:
            self.chromosome=Chromosome()
        else:
            self.chromosome=chromosome
        self.path=[self.position]
        self.fitness=0

    def move_forward(self,direction):
        move=moves[direction]
        position=self.position

        self.position= (position[0]+move[0],position[1]+move[1])
        p=self.position
        self.path.append(p)

        
    

    def move_backward(self):
        if len(self.path) > 1:
            self.path.pop()
            self.position = self.path[-1]


    def cycle(self,direction,e,index):
        l=cycle_list(direction,e)
        for i in l:
            self.move_forward(i)
            if(valid(self.path,self.position)):
                self.chromosome.genes[index]=i
                return
            self.move_backward()
        self.move_forward(e)

    


    def check_moves(self):
        cycling_dir=random.randint(0,1)
 
        

        
        for i,e in enumerate(self.chromosome.genes):
            self.move_forward(e)
            
            if valid(self.path,self.position)==False:
                
                self.move_backward()
                self.cycle(cycling_dir,e,i)
            #print('after')
            #print(self.path)
            


    
    
    
    def evaluate_fitness(self):
        f=0
        exist= []
        for pos in self.path:
            exist.append(pos)
            if valid(exist,pos):
                f=f+1
            else:
                break
            
        return f


                


