public class Bai119 {

    // kiểm tra số nguyên tố
    public static boolean isPrime(int n) {
        if (n < 2)
            return false;

        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0)
                return false;
        }

        return true;
    }

    // xoay 180 độ
    public static String rotate180(String s) {

        String result = "";

        for (int i = s.length() - 1; i >= 0; i--) {

            char c = s.charAt(i);

            switch (c) {
                case '0':
                    result += '0';
                    break;

                case '1':
                    result += '1';
                    break;

                case '6':
                    result += '9';
                    break;

                case '8':
                    result += '8';
                    break;

                case '9':
                    result += '6';
                    break;

                default:
                    return "";
            }
        }

        return result;
    }

    // kiểm tra strobogrammatic
    public static boolean isStrobogrammatic(int n) {

        String s = String.valueOf(n);

        String rotated = rotate180(s);

        return s.equals(rotated);
    }

    // kiểm tra strobogrammatic mở rộng
    public static boolean isExtendedStrobogrammatic(int n) {

        String s = String.valueOf(n);

        String rotated = rotate180(s);

        if (rotated.equals(""))
            return false;

        return true;
    }

    public static void main(String[] args) {

        System.out.println("a. So strobogrammatic < 1,000,000:");
        for (int i = 0; i < 1000000; i++) {

            if (isStrobogrammatic(i)) {
                System.out.print(i + " ");
            }
        }

        System.out.println("\n\nb. So nguyen to strobogrammatic < 1,000,000:");
        for (int i = 0; i < 1000000; i++) {

            if (isPrime(i) && isStrobogrammatic(i)) {
                System.out.print(i + " ");
            }
        }

        System.out.println("\n\nc. So strobogrammatic mo rong < 1,000,000:");
        for (int i = 0; i < 1000000; i++) {

            if (isExtendedStrobogrammatic(i)) {
                System.out.print(i + " ");
            }
        }

        System.out.println("\n\nd. So nguyen to strobogrammatic mo rong < 1,000,000:");
        for (int i = 0; i < 1000000; i++) {

            if (isPrime(i) && isExtendedStrobogrammatic(i)) {
                System.out.print(i + " ");
            }
        }

        System.out.println("\n\ne. Khong phai strobogrammatic, khong phai nguyen to");
        System.out.println("nhung sau khi xoay 180 do lai la so nguyen to:");

        for (int i = 0; i < 1000000; i++) {

            String rotated = rotate180(String.valueOf(i));

            if (!rotated.equals("")) {

                int rotatedNum = Integer.parseInt(rotated);

                if (!isPrime(i)
&& !isStrobogrammatic(i)
                        && isPrime(rotatedNum)) {

                    System.out.print(i + " ");
                }
            }
        }
    }
}