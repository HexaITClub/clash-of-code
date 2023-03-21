fn valid_nep_name(name: &mut String) -> i32
{
    let mut spaces = 0;
    let ant = name.trim();
    for c in ant.chars()
    {
        if c == ' '
        {
            spaces += 1;
        }
    }
    if spaces == 0
    {
        return -1;
    }
    return spaces + 1;
}

fn main()
{
    let mut name = String::from(" Ramesh");
    println!("{}", valid_nep_name(&mut name));


    let mut name2 = String::from(" Ramesh Poudel");
    println!("{}", valid_nep_name(&mut name2));

    
    let mut name3 = String::from(" Ramesh Prasad Poudel  ");
    println!("{}", valid_nep_name(&mut name3));
}
