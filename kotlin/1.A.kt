fun main(){
    val (n,m,a)=readLine()!!.split(" ").map(String::toLong)
    val r= if (n%a==0L) n/a else n/a+1
    val k= if (m%a==0L) m/a else m/a+1
    print(r*k)
}
