use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut lines = stdin.lock().lines();
    
    // Read the number of test cases
    let t: usize = lines
        .next()
        .expect("no input")
        .unwrap()
        .trim()
        .parse()
        .expect("invalid t");
    
    for _ in 0..t {
        let line = lines.next().unwrap().unwrap();
        let s = line.trim();
        
        // Parse the number as i128 (handles up to 39 digits)
        let n: i128 = s.parse().expect("invalid number");
        
        // Compute 10^(len-1)
        let len = s.len() as u32;
        let power = 10_i128.pow(len - 1);
        
        // Result
        let result = n - power;
        println!("{}", result);
    }
}
