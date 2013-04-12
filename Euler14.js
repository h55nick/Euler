/*
The following iterative sequence is defined for the set of positive integers:
n  n/2 (n is even)
n  3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13  40  20  10  5  16  8  4  2  1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
*/

/*
Working version with recur
*/
var length,m,mlength =0;

function next_chain(s){
  length++;
   if (s == 1){
     return length;
   }else if(s%2===0){
      return next_chain(s/=2);
   }else{
      return next_chain(s = 3 * s + 1);
   }
}

for(var i=1000000; i > 0; i--) {
  length = 0;
  if (next_chain(i) > mlength){
    m = i;
    mlength = length;
  }
}
console.log(m)


/*
WORKING VERSION - Non-recur  (I do believe this is faster)
var sl = 0;
var lc = 0;

for (var start = 1000000; start > 0; start--)
{
    var s = start;
    var length = 1;

    while (s != 1)
    {
        if (s % 2 == 0)
            s /= 2;
        else
            s = 3 * s + 1;
        length++;
    }

    if (length < longestChain)
        continue;

    sl = start;
    lc = length;
}
console.log(lc)
*/