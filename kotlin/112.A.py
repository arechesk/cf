@kotlin.ExperimentalStdlibApi
fun main(){
   val a=readLine()!!.uppercase()
   val b=readLine()!!.uppercase()
   if (a<b)
   print("-1")
   else if(a>b)
   print("1")
   else print("0")
}
