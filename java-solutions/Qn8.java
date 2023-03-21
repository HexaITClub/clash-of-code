public class Qn8
{
    public static int validNepName(String name)
    {
        name = name.trim();
        int spaces = 0;
        for(int i = 0; i < name.length(); i++)
        {
            if(name.charAt(i) == ' ')
                spaces++;
        }
        if(spaces == 0)
            return -1;
        return spaces + 1;
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
