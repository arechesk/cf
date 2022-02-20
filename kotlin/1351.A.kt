fun main(){
    val n=readLine()!!.toInt()
    for(i in 1..n){
    val (a,b)= readLine()!!.split(" ").map(String::toInt)
    print(a+b)
    }
}
