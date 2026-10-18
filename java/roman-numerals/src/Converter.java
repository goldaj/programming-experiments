import java.util.Scanner;

/**
 * Created by Goldaj on 16/02/2017.
 * Convert a roman number to a decimal one
 */
public class Converter {

    /**
     * Does all the work
     * @param expr the expression to parse
     * @return the converted number
     */
    public static int parser(String expr) {
        int result = 0;
        boolean stop_m, stop_d, stop_c, stop_l, stop_x, stop_v, stop_i;
        int nb_m, nb_d, nb_c, nb_l, nb_x, nb_v, nb_i;

        nb_m = nb_d = nb_c = nb_l = nb_x = nb_v = nb_i = 0;
        stop_m = stop_d = stop_c = stop_l = stop_x = stop_v = stop_i = false;

        for(int i = 0; i < expr.length(); i += 1) {
            if((!stop_m) && (nb_m < 4) && expr.substring(i, i+1).equals("M")) {
                result += 1000;
                nb_m += 1;
            } else if((!stop_d) && (nb_d < 4) && expr.substring(i, i+1).equals("D")) {
                stop_d = true;
                result += 500;
                nb_d += 1;
            } else if((!stop_c) && (nb_c < 4) && expr.substring(i, i+1).equals("C")) {
                stop_d = stop_m = true;
                result += 100;
                nb_c += 1;
            } else if((!stop_l) && (nb_l < 4) && expr.substring(i, i+1).equals("L")) {
                stop_d = stop_m = stop_c = true;
                result += 50;
                nb_l += 1;
            } else if((!stop_x) && (nb_x < 4) && expr.substring(i, i+1).equals("X")) {
                stop_d = stop_m = stop_c = stop_l = true;
                result += 10;
                nb_x += 1;
            } else if((!stop_v) && (nb_v < 4) && expr.substring(i, i+1).equals("V")) {
                stop_d = stop_m = stop_c = stop_l = stop_x = true;
                result += 5;
                nb_v += 1;
            } else if((!stop_i) && (nb_i < 4) && expr.substring(i, i+1).equals("I")) {
                stop_d = stop_m = stop_c = stop_l = stop_x = stop_v = true;
                result += 1;
                nb_i += 1;
            } else {
                return -1;
            }

        }

        return result;
    }

    /**
     * Main method to test
     * @param args unused here
     */
    public static void main(String args[]) {
        String expr;
        int result;
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter a valid Roman expression: ");
        expr = scanner.nextLine();

        if((result = Converter.parser(expr)) <= 0) {
            System.out.println("The number you entered ("
                                + expr + ") is invalid");
        }

        System.out.println("returned " + result);
    }
}
