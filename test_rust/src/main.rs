extern crate espeak_sys;
extern crate libc;

use libc::{c_int, c_char, c_uchar, c_void, c_short, size_t, c_uint, wchar_t, FILE};
// use libc::types::common::c95::c_void;

fn main() {
    println!("Hello, world!");
    let text = "text";
    // let text_prt: *const *const c_void = text as *const c_void;
    let textmode = 1;
    let phonememode = 1;
    unsafe {
        espeak_sys::espeak_TextToPhonemes(*(text), textmode, phonememode);
    }
}
