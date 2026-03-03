import scala.io.StdIn.readLine
import scala.math.BigInt

object Main extends App {
  val t = readLine().trim.toInt
  for (_ <- 1 to t) {
    val s = readLine().trim
    val n = BigInt(s)
    val power = BigInt(10).pow(s.length - 1)
    println(n - power)
  }
}
