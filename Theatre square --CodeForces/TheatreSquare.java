import java.util.Scanner;

public class TheatreSquare {
    
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);

        long m, n, a;

        m = sc.nextLong();
        n = sc.nextLong();
        a = sc.nextLong();
        sc.close();

        long x = (m / a);
        long y = n / a;

        if (m % a != 0)
            x++;
        if (n % a != 0)
            y++;

        System.out.print(x*y);



    }
}
