import java.math.BigInteger

fun main() {
    val t = readLine()!!.toInt()
    repeat(t) {
        val s = readLine()!!
        val n = BigInteger(s)
        val power = BigInteger.TEN.pow(s.length - 1)
        println(n - power)
    }
}
