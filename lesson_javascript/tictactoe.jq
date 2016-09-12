<style>
.button {border:1px solid #4CAF50;height:30;width:30;float:left}
</style>
<button id=x0 class=button></button>
<button id=x1 class=button></button>
<button id=x2 class=button></button>
<p style="clear:both">
<button id=x3 class=button></button>
<button id=x4 class=button></button>
<button id=x5 class=button></button>
<p style="clear:both">
<button id=x6 class=button></button>
<button id=x7 class=button></button>
<button id=x8 class=button></button>
<p style="clear:both">
<p id=result></p>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
<script>
var val=[0,0,0,0,0,0,0,0,0]
var ops={h1:[0,1,2],h2:[3,4,5],h3:[6,7,8],v1:[0,3,6],v2:[1,4,7],v3:[2,5,8],d1:[0,4,8],d2:[2,4,6]}
$(".button").click(function() {nextmove($(this))})
var you_first1=[$("#x4"),$("#x8"),$("#x1"),$("#x3"),$("#x6")] //rescue -2 positions


function metric(a,b,c) {
var i=a+b+c //sum
var j=(Math.abs(a)+Math.abs(b)+Math.abs(c))/2  //how many non-zero, so -1,+1, 1 is not as good as 0, 0,1
var k=1-Math.sign(i) //if negative, make it impossible to compensate with equal positives
var result=(i-k)*(Math.pow(10,Math.abs(i)))
return result
}

function test_you_first() {
//scenario 1 start in the middle: x4->y0->x8->y2->x1->y7?-
for (var i=0;i<scenario1.length;i++) nextmove(you_second1[i])
}

function test_I_first() {
var mymove=find_best()
make_move(0,1)
$($(".button")[0]).html("O")
for (var i=0;i<scenario1.length;i++) nextmove(I_first1[i])
}

function nextmove(elem) { 
	var x=$(".button")
	x.each(function(i,item) {
		if (item==elem[0]) { //your move, invalid move, or you win
		    if (val[i]==0) { //valid move
				elem.html("X")
				if (make_move(i,-1)==0) {//not game end
					//my move, game ends in draw before move, game ends in draw after move, I win
					var mymove=find_best()
					if (mymove>=0) { //can find a valid move
						$(x[mymove]).html("O")
						if (make_move(mymove,1)>0) $("#result").append("I win after my turn")
					}
					else $("#result").append("game ends in draw after your turn")
				}
				else $("#result").append("you win after your turn!")
			}
			else $("#result").append("Invalid Square<br>")
		}	
	})
}

function make_move(pos,value) {//returns 1 for game end, 0 for continue 
 	val[pos]=value
	console.log(val)
	if ((Math.abs(score_move(pos,value)))>2000) return 1; //end game after move
	else return 0 //can be a draw to be found out later
}

function find_best() {
    best_score=-999999
	best_pos=-1
	var current
	console.log(val)
	for (var i=0;i<val.length;i++) {
	    if (val[i]==0 ){
			current=score_move(i,1)
			console.log(i,current)
			if (current>best_score) {
				best_pos=i
				best_score=current
			}
		}
    }

	return best_pos;
}

function score_move(pos,value) {
	var new_val=val.slice()
	new_val[pos]=value
	var score=0
	for (var i in ops) {
	    score+=metric(new_val[ops[i][0]],new_val[ops[i][1]],new_val[ops[i][2]]) }
	return score
}

</script>
