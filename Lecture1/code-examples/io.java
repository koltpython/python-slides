import java.util.Scanner;

public class Example{ 
    public static void main(String[] args){
        // Create a scanner object 
        Scanner scanner = new Scanner(System.in);
        // Print descriptive text to console
        System.out.print("Enter your name: ");
        // Read user input and assign it to a variable
        String name = scanner.nextLine();
        // Greet user
        System.out.println("Hello from Java, " + name);
    }
}