import java.util.Scanner;
import java.math.BigInteger;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        sc.nextLine(); // consume the newline after the integer
        
        while (t-- > 0) {
            String s = sc.nextLine();               // read the number as a string
            BigInteger n = new BigInteger(s);        // convert to BigInteger
            int len = s.length();
            BigInteger power = BigInteger.TEN.pow(len - 1); // 10^(len-1)
            BigInteger result = n.subtract(power);   // n - 10^(len-1)
            System.out.println(result);
        }
        
        sc.close();
    }
}
