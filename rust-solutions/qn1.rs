fn summer(arr: &[i32], number: i32) -> i32
{
    let mut sum: i32 = 0;
    for a in arr
    {
        sum += a;
    }
    if sum >= number
    {
        sum - number
    }
    else
    {
        sum + number
    }
}

fn main()
{
    let arr = [4, 5];
    println!("{}", summer(&arr, 10));
}
