use std::io;
use std::fs;
use std::path::Path;

fn main() {
    list_directory();
}

fn list_directory() -> io::Result<()> {
    let dir = Path::new("/home/ec2-user/environment");
    for entry in fs::read_dir(dir)? {
        let entry = entry?;
        let path = entry.path();
        println!("{}", path.display());
    }
    Ok(())
}