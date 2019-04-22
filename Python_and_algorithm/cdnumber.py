import sys
while(input = sys.stdin.readline()){
  lines = input.split(" ")
  n = parseInt(lines[0])
  s = parseInt(lines[1])
  L = parseInt(lines[2])  
  x=(L+1)/(s+1);#设每张CD收录x首歌
  x = Math.floor(x);  #求出x
  var ans = Math.ceil(n/x)  #求出非特殊条件下的结果
  if( x%13 == 0 ){
    x = x-1  #如果x是13倍数，那么每张CD都要少收录1首
    ans = Math.ceil(n/x)
  }
  if( n < x && n%13 == 0 ){
    ans = 2   #如果仅需要一张CD但是收录了13倍数的歌曲需要加一张，如“13 0”
  }
  if( (n-(ans-1)*x)%13 == 0 && x-(n-(ans-1)*x) == 1 ){
    '''如果最后一张CD是13的倍数【(n-(ans-1)*x)%13 == 0】
    可以把前一张拿过来一首，但是拿过来后前一张又可能会是13的倍数
    这时候也需要再加一张CD，比如这样的情况“14 14 13” “27 27 27 26”
    这样情况的条件是最后一个必须比前一个少1【x-(n-(ans-1)*x) == 1】
    所以满足上述两项条件的时候总CD需要加1
    '''
    ans += 1
  }
  print(ans)
}