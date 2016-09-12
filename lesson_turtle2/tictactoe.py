from math import *
class tictactoe():
    def __init__(self):
        self.val=[0,0,0,0,0,0,0,0,0]
        self.dict={'h1':[0,1,2],'h2':[3,4,5],'h3':[6,7,8],'v1':[0,3,6],'v2':[1,4,7],'v3':[2,5,8],'d1':[0,4,8],'d2':[2,4,6]}
        self.weight=[3,2,3,2,4,2,3,2,3]
        #self.result=[0,0,0,0,0,0,0,0,0]
    def eval_board(self):
        values=self.val
        any0=1
        for k in self.dict.keys():
            pos=self.dict.get(k)
            val=[values[pos[0]],values[pos[1]],values[pos[2]]]
            result=val[0]+val[1]+val[2]
            any0 *= val[0]*val[1]*val[2]
            if result==3: return 3 
            else:
                if result==-3: return -3
        if any0!=0: return 0 
        return -100  
         
    def score_pos(self,testpos): #evaluates all 8 lines
        values=self.val.copy()
        score=-999999
        if values[testpos]==0:
            score=self.weight[testpos]
            values[testpos]=1
            for k in self.dict.keys():
                pos=self.dict.get(k)
                val=[values[pos[0]],values[pos[1]],values[pos[2]]]
                sum3=val[0]+val[1]+val[2]
                score+=sum3 * pow(10,abs(sum3))
                # print(testpos," ",k," ",val," sum= ",sum3," score= ",score)
        return score 
    
    def evaluate_end_game(self):
        result=self.eval_board()
        if (result==-3): 
            print("you win,game over")
            return 1
        else:
            if result==3: 
                print("I win,game over")
                return 1 
            else:
                if result==0: 
                    print("Draw, Game over") 
                    return 1
                return 0 
    def make_move(self):
        move=self.find_best_move()
        if (move>=0): self.my_move(move)
        else: print("Game end in a Draw")           

    def find_best_move(self):
        max_pos=0
        max_score=-999999
        for i in range(0,9):
            current=self.score_pos(i)+self.weight[i] 
            if current>max_score:
                   max_pos=i
                   max_score=current
        if max_score>-999999:return max_pos
        else: return -1  

    def my_move(self,pos):
        self.val[pos]=1
        self.display()
        return self.evaluate_end_game()

    def op_move(self,pos):
        self.val[pos]=-1
        self.display()
        return self.evaluate_end_game()

    def display(self):
        for x in range(0,3):
            for y in range(0,3):
                if (y<2): endchar="|"
                else: endchar=""
                if (self.val[3*x+y]==0): print(' ',end=endchar)
                else:
                    if (self.val[3*x+y]==-1): print('O',end=endchar)
                    else: print('X',end=endchar)
            print()


t=tictactoe()
while ( not t.op_move(int(input("Your move: "))) and not t.make_move()): print("Continue") 
