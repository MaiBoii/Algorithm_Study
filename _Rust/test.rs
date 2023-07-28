use std::io;

fn main(){
    let mut number = String::new();
    io::stdin().read_line(&mut number).unwrap();
    if number.trim().parse::<i32>().is_ok(){
        println!("number is {}", number.trim());
    }
    else {
        println!("number is not number");
    }
}