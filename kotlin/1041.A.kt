fun main(){
    val n=readLine()!!.toInt()
    val s=readLine()!!.split(" ").map(String::toInt)
    print(s.maxOrNull()!!-s.minOrNull()!!-n+1)
}
