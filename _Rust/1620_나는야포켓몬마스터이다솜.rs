use std::io;
use std::collections::HashMap;

fn main(){
    let mut numbers_arry = String::new();
    io::stdin().read_line(&mut numbers_arry).unwrap();
    let numbers: Vec<&str> = numbers_arry.split_whitespace().collect();

    let n: i32 = numbers[0].parse::<i32>().unwrap();
    let m: i32 = numbers[1].parse::<i32>().unwrap();

    let mut pokemon_name = HashMap::new();
    for _i in 1..n+1{
        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();
        pokemon_name.insert(input.trim().to_string(), _i.to_string());
        pokemon_name.insert(_i.to_string(),input.trim().to_string());
    }
    for _j in 0..m{
        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();
        if input.trim().parse::<i32>().is_ok(){
            let index:i32= input.trim().parse().unwrap();
            println!("{}",pokemon_name[&(index).to_string()])
        }
        else{
            println!("{}",pokemon_name[&input.trim().to_string()])
        }
    }
}