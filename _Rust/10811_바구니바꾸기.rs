use std::io;
use std::collections::HashMap;

fn main(){
    let mut input_a = String::new();
    io::stdin().read_line(&mut input_a).unwrap();

    let number_a: Vec<i32> = input_a
    .split_whitespace()
    .map(|x| -> i32 { x.parse().unwrap() })
    .collect();

    let mut baguni = Vec::new();

    for i in 1..=number_a[0]{
        baguni.push(i);
    }

    let mut map = HashMap::new();

    for i in 0..number_a[1]{
        let mut input_b = String::new();
        io::stdin().read_line(&mut input_b).unwrap();
        let number_b: Vec<i32> = input_b
        .split_whitespace()
        .map(|x| -> i32 { x.parse().unwrap() })
        .collect();

        let mut i = number_b[0];
        let mut j = number_b[1];

        //slice the vector
        let mut slice = &mut baguni[i as usize - 1..j as usize];
        slice.reverse();

        //insert into hashmap
        map.insert(i, j);
}

for i in 0..baguni.len(){
    print!("{} ",baguni[i]);
}
}