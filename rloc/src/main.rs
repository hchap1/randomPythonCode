use std::env::args;
use std::env::current_dir;
use std::io::Read;
use std::path::PathBuf;
use std::fs::File;
use std::fs::read_dir;
use regex::Regex;

fn lines_in_file(path: &PathBuf) -> Result<usize, ()> {
    let mut file = match File::open(path) {
        Ok(file) => file,
        Err(_) => return Err(())
    };

    let mut buf: String = String::new();
    match file.read_to_string(&mut buf) {
        Ok(_) => Ok(buf.chars().filter_map(|c| if c == '\n' { Some(1) } else { None }).sum()),
        Err(_) => return Err(())
    }
}

fn get_files(path: &PathBuf, pattern: &Option<Regex>) -> Result<Vec<PathBuf>, ()> {
    match read_dir(path) {
        Ok(contents) => Ok(contents.flat_map(|item| match item {
            Ok(item) => {
                if item.path().is_file() {
                    let path = item.path();
                    let path_str = path.to_str().unwrap();
                    match pattern {
                        Some(p) => if p.is_match(path_str) { Some(vec![path]) } else { None },
                        None => Some(vec![path])
                    }
                } else if item.path().is_dir() {
                    Some(get_files(&item.path().to_path_buf(), pattern).unwrap())
                } else {
                    None
                }
            }
            Err(_) => None
        }).flatten().collect::<Vec<PathBuf>>()),
        Err(_) => Err(())
    }
}

fn main() {

    // To use: rloc directory
    // ARGS: -r regex | includes only the items that fit the regex
    //       -e extension | includes only the items that fit the extension

    let args: Vec<String> = args().skip(1).map(|x| String::from(x)).collect();

    let directory = match args.get(0) {
        Some(argument) => PathBuf::from(argument),
        None => current_dir().unwrap()
    };

    let pattern = match args.get(1) {
        Some(argument) if args.len() > 2 => Some(
            match Regex::new(
                (if argument == "-r" { args.get(2).unwrap().to_string() }
                else if argument == "-e" { format!(r"^.*\.{}", args.get(2).unwrap())}
                else {
                    eprintln!("[ERROR] Invalid pattern flag {argument}");
                    return;
                }).as_str())
            {
                Ok(regex) => regex,
                Err(_) => {
                    eprintln!("[ERROR] Invalid regex pattern {}", args.get(2).unwrap());
                    return;
                }
            }
        ),

        Some(_) => {
            eprintln!("[ERROR] Cannot supply empty pattern");
            return;
        }

        None => None
    };

    let loc = if directory.is_dir() {
        let files = match get_files(&directory, &pattern) {
            Ok(files) => files,
            Err(_) => {
                eprintln!("[ERROR] Could not read directory {}", directory.to_str().unwrap());
                return;
            }
        };
        files.iter().filter_map(|path| match lines_in_file(path) {
            Ok(loc) => Some(loc),
            Err(_) => None
        }).sum()

    } else if directory.is_file() {
        match lines_in_file(&directory) {
            Ok(loc) => loc,
            Err(_) => {
                eprintln!("[ERROR] Unable to read file {}", directory.to_str().unwrap());
                return;
            }
        }
    } else {
        eprintln!("[ERROR] Invalid Directory");
        return;
    };

    println!("{loc} lines of code.");
}
