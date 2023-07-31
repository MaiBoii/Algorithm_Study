use std::io;

fn main(){
    let mut input_a = String::new();
    io::stdin().read_line(&mut input_a).unwrap();

    let number_a: Vec<i32> = input_a
    .split_whitespace()
    .map(|x| -> i32 { x.parse().unwrap() })
    .collect();

    let mut v = Vec::new();

    for i in 1..=number_a[0]{
        v.push(i);
    }

    for i in 0..number_a[1]{
        let mut input_b = String::new();
        io::stdin().read_line(&mut input_b).unwrap();
        let number_b: Vec<i32> = input_b
        .split_whitespace()
        .map(|x| -> i32 { x.parse().unwrap() })
        .collect();

        let a_v = v[number_b[0] as usize - 1];
        let b_v = v[number_b[1] as usize - 1];
            v[number_b[0] as usize -1] = b_v; //러스트로 스와핑하는 법
            v[number_b[1] as usize -1] = a_v;
    }
    for i in v{
        print!("{:?} ",i);
    }
}