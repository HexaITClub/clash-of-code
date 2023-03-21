public class Qn15 {
    public static void main(String[] args) {
        for (int i = 1; i <= 100; i++) {
            if (i % 3 == 0 && i % 5 == 0) {
                System.out.println("BCA");
            } else if (i % 3 == 0) {
                System.out.println("Patan");
            } else if (i % 5 == 0) {
                System.out.println("Campus");
            } else {
                System.out.println(i);
            }
        }
    }
}
