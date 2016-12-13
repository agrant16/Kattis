//Symmetric Order

import java.util.*;

public class SymmetricOrder{

     public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int num = input.nextInt();
        int set = 1;
        while (num != 0){
            System.out.println("SET " + set);
            int control = num;
            String[] names = new String[num];
            for (int i = 0; i < num / 2; i++){
                names[i] = input.next();
                names[control - 1] = input.next();
                control--;
            }
            if (num % 2 != 0) {
                names[(num / 2)]= input.next();
            }
            for (int i = 0; i < names.length; i++) {
                System.out.println(names[i]);
            }
            num = input.nextInt();
            set++;
        }
     }
}
