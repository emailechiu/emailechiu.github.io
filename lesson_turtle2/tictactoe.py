class tictactoe():
    def __init__(self):
        self.state=[0,0,0,0,0,0,0,0,0]
        self.dict={0:[0,1,2],1:[3,4,5],2:[6,7,8],3:[0,3,6],4:[1,4,7],5:[2,5,8],6:[0,4,8],7:[2,4,6]}
        self.line={0:[1,2],1:[0,2]
        self.score=[3,2,3,2,4,2,3,2,3]
        self.result=[0,0,0,0,0,0,0,0]
        for x in range(0,9):
            self.state.append(0)
        for x in range(0,8):
            self.result.append(0)
    def check_line(index1,index2,index3):
        return self.state[index1]+self.state[index2]+self.state[index3]
    
    def check_state(self):
##        self.result[0]=self.state[0]+self.state[1]+self.state[2]
##        self.result[1]=self.state[3]+self.state[4]+self.state[5]
##        self.result[2]=self.state[6]+self.state[7]+self.state[8]
##        self.result[3]=self.state[0]+self.state[3]+self.state[6]
##        self.result[4]=self.state[1]+self.state[4]+self.state[7]
##        self.result[5]=self.state[2]+self.state[5]+self.state[8]
##        self.result[6]=self.state[0]+self.state[4]+self.state[8]
##        self.result[7]=self.state[2]+self.state[4]+self.state[6]
        for i in range(0,8):
            pos=self.dict(i)
            val=list(self.state[pos[0]],self.state[pos[1]],self.state[pos[2]])
            all3=val[0]+val[1]+val[2]
            same3=(val[0]==val[1] & val[1]==val[2])
            for k in range(0,3):
                if val[k]==0:
                   if (sum==2):
                       self.score[pos[k]]+=512
                   else if (sum==-2):
                       self.score[pos[k]]+=256
                   else if (sum==1):
                       self.score[pos[k]]+=128
                   else if (sum==-1):
                       self.score[pos[k]]+=64
                   else if (sum==0):
                       self.score[pos[k]]+same3*32
                else self.score[pos[k]]=-1024
            
    def my_move(self):
        max_sofar=0
        for i in range(0,9):
            if self.score[i]>self.score[max_sofar]:
                   max_sofar=i
        self.state[max_sofar]=1

    def op_move(pos):
        self.state[pos]=-1

    

        
            
            
        




