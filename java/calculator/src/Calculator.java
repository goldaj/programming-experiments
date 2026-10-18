import java.util.Scanner;

/**
 * Calculator class
 * Created by Goldaj on 14/02/2017.
 */
public class Calculator {
    private static final char[] ops={'+','-','*','/'};

    /**
     * Evaluate the string expression
     * @param expr the string expression to evaluate
     * @return result of the operation
     * @throws Exception
     */
    public static double operation(String expr) throws Exception {

        char operator=' ';
        int index = -1;
        double left;
        double right;

        for(int i = 0; (i < ops.length) && (operator == ' '); i += 1) {
            index = expr.indexOf(ops[i]);
            if(index > 0) operator=ops[i];
        }

        /*
         * operator check
         */
        if(operator==' ') throw new Exception("syntax error\n +" +
            "Valide operators are: + - * /");

        /*
        * left expr check
        */
        try {
            left = Double.parseDouble(expr.substring(0, index).trim());
        } catch(Exception e) {
            throw new Exception("lexical error: first operand is not a" +
                "valid number:\nexpecting [O^9]");
        }

        /*
         * right expr check
         */
        try {
            right = Double.parseDouble(expr.substring(index + 1).trim());
        } catch(Exception e) {
            throw new Exception("lexical error: first operand is not a" +
                "valid number:\nexpecting [O^9]");
        }

        /*
         * using the good op
         */
        switch(operator) {
            case '+' : return left + right;
            case '-' : return left - right;
            case '*' : return left * right;
            case '/' :
                if(Math.abs(right) < Double.MIN_VALUE)
                    throw new Exception("Divided by zero");
                return left / right;
        }
        throw new Exception("unknown issue occurred");
    }

    /**
     * print the result
     * @param str the result of the expression
     */
    public static void print(double str) {
        System.out.println("equals: " + str);
    }

    public static void analyse(String expr) {
        try {
            print(operation(expr));
        } catch(Exception e) {
            System.out.println("Erreur : " + e.getMessage());
        }
    }

    /**
     * just the main method
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String expr;

        while(true) {
            if (args.length > 0) {
                Calculator.analyse(args[0]);
            } else {
                System.out.println("Enter valid expression (or \"end\" to exit): ");
                if ((expr = scanner.nextLine()).contains("end")) {
                    return;
                }
                Calculator.analyse(expr);
            }
        }
    }
}