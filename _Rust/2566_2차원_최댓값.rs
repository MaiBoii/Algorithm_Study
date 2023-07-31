use std::io;

fn main(){
    let mut input_a = String::new();
    io::stdin().read_line(&mut input_a).unwrap();

    let number_a: Vec<i32> = input_a
    .split_ascii_whitespace()
    .map(|x| -> i32 { x.parse().unwrap() })
    .collect();

    
}