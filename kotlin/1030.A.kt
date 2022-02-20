fun main(){
    val n=readLine()!!.toInt()
    val s=readLine()!!.split(" ").map(String::toInt)
    val ans= if (s.reduce({x,y-> x or y})==1) "HARD" else "EASY"
    print(ans)
}
