/**
 * birthday_girl
 */
// This code takes in the person's name at runtime and returns an encryted version of a happy birthday
// A little work with bit manipulation

public class BirthdayGirl {

    public static void main(String[] args) throws java.io.IOException {
    /* TO A GREGARIOUS SOMEONE */
    /*TO START COMPILE CLASS FILE AS javac BirthdayGirl*/
        /*NEXT, RUN CLASS FILE AS java BirthdayGirl YoUr-FiRsTNaMe*/
        /*Yeah! your first name not "YoUr-FiRsTNaMe"*/

        String password = "temitayo";
        while (args[0].equals(password)) {
            System.out.println("Now enter your age: ");
        int key = System.in.read();
        System.out.println();
        System.out.print("Funny, you entered: ");
         int ch = key;
                for (int i = 512; i > 0; i=i/2) {
                    if (((byte)ch&i) !=0) {
                        System.out.print(1+" ");
                    } else {
                        System.out.print(0+" ");
                    }    
                }
                System.out.println();

        String enmsg="";
        String dcmsg="";
        int index = 0;
        String enchar ="";
        
    String msg = "Happy Birthday Temitayo Victoria Ikuerowo"; 
    // you can add whatever name you want

    if (args.length != 0) {
        for (int x=0;x!=msg.length();x++) {
            enmsg = enmsg + (int) (msg.charAt(x)^ args[0].charAt(index));
            enchar = enchar + (char) (msg.charAt(x)^ args[0].charAt(index));
        index++;
        if(index == 8) index =0;
        }
    }
    else{
        System.out.println(" you have not run the program properly");
    }
    System.out.println("\tJust  wanted to wish you "+enmsg);
    System.out.println("\n");
    index =0;
    if (args.length != 0 ) {
        for (int x=0;x!=msg.length();x++) {
            dcmsg = dcmsg + (char)(enchar.charAt(x)^ args[0].charAt(index));
        index++;
        if(index == 8) index =0;
        }
    }
    else{
        System.out.println(" you have not run the program properly");
    }
    System.out.println("\tOops, "+dcmsg);
    System.out.println("\t\t--------------THE END------------\t\t");
    break;
        }

    
    }
}