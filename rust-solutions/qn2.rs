fn main()
{
    let age = 21;
    let current = 2023;

    if age < 0
    {
        println!("Not a valid age");
        std::process::exit(1);
    }

    println!("Year: {}", current - age);
}
