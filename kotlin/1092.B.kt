fun main(){
    val n=readLine()!!.toInt()
    var s=readLine()!!.split(" ").map(String::toInt)
    var d=0
    s=s.toList().sorted()
    var k= s.slice(0..s.size-1 step 2).zip(s.slice(1..s.size-1 step 2))
    for(i in k)
                d+=Math.abs(i.first-i.second)
    
    print(d)
}
