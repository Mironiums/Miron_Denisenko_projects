import java.util.Scanner;
public class Binary2Decimal {
  public static void main(String[] args) {
      Scanner input = new Scanner(System.in);
      System.out.print("Your binary number\n> ");
      int binar = input.nextInt();
      int decimal = converter(binar);
      System.out.print(binar+" after convertion to decimal is "+decimal);
  }
  public static int converter(int exp) {
    int result=0;
    for (int i=0; exp/Math.pow(10,i+1)>0; i++){
        result+=exp % Math.pow(10,i+1) * Math.pow(2, i);
      exp/=Math.pow(10,i+1);
}
    return result;
  }

}