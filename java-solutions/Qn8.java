public class Qn8
{
    public static int validNepName(String name)
    {
        name = name.trim();
        String[] arr = name.split(" ");
        if(arr.length <= 1) return-1;

        int spaces = 0;
        for(String s: arr)
        {
            if(!s.equals(" ") && !s.equals(""))
                spaces++;
        }
        return spaces;
    }

    public static void main(String[] args)
    {
        String name1 = "Ramesh Poudel";
        String name2 = " Ramesh p Poudel";
        String name3 = "RameshPoudel";
        String name4 = "Ramesh Poudel ";
        System.out.println(validNepName(name1));
        System.out.println(validNepName(name2));
        System.out.println(validNepName(name3));
        System.out.println(validNepName(name4));
    }
}
