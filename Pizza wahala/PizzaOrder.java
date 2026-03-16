import java.util.Scanner;
public class PizzaOrder {
    public static void main(String[]args){

    Scanner input = new Scanner(System.in);
    
    displayMenu();

    System.out.print("Enter number of people: ");
    int numberOfPeople = input.nextInt();
    input.nextLine();
    
    System.out.print("Enter pizza type (Sapa Size, Small Money, Big Boys, Odogwu): ");
    String typeOfPizza = input.nextLine();

    int slices = getSlicesPerBox(typeOfPizza);
    int price = getPricePerBox(typeOfPizza);
    int boxes = calculateBoxes(numberOfPeople, slices);
    int leftover = calculateLeftover(numberOfPeople, slices, boxes);
    int total = calculateTotalPrice(boxes, price);

    displaySummary(boxes, leftover, total);
    }

    public static void displayMenu(){
    System.out.println("""
    Pizza type  Number of Slices     Price per Box
    Sapa Size            4               2000
    Small Money          6               2400
    Big Boys             8               3000
    Odogwu               12              4200
    """);
}
    public static int getPricePerBox(String type){
    switch(type){

        case "Sapa Size":
            return 2000;
        case "Small Money":
            return 2400;
        case "Big Boys":
            return 3000;
        case "Odogwu":
            return 4200;            
        default:
            return 0;
    }
}
    
     public static int getSlicesPerBox(String type) {
        switch (type) {
            case "Sapa Size": 
                return 4;
            case "Small Money": 
                return 6;
            case "Big Boys": 
                return 8;
            case "Odogwu": 
                return 12;
            default: 
                return 0;
    }
}

    public static int calculateBoxes(int people, int slices) {
        return (int) Math.ceil((double) people / slices);
    }

    public static int calculateLeftover(int people, int slices, int boxes) {
        int totalSlices = boxes * slices;
        return totalSlices - people;
    } 
    public static int calculateTotalPrice(int boxes, int price) {
        return boxes * price;
    }   
    
     public static void displaySummary(int boxes, int leftover, int total) {

        System.out.println("\n--- Order Summary ---");
        System.out.println("Number of boxes of pizza to buy = " + boxes + " boxes");
        System.out.println("Number of leftover slices after serving = " + leftover + " slices");
        System.out.printf("Total price = %d%n", total);
    }
}



    


