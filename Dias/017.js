/*
Basicamente uma verificação basica , resolvi realizar esse para praticar condicional em JSscript
https://www.hackerrank.com/challenges/cats-and-a-mouse/problem?isFullScreen=true
*/

function catAndMouse(x, y, z) {
    const dist_cat_a = Math.abs(z - x);
    const dist_cat_b = Math.abs(z - y);
    
    if (dist_cat_a < dist_cat_b) {
        return "Cat A";
    } else if (dist_cat_b < dist_cat_a) {
        return "Cat B";
    } else {
        return "Mouse C";
    }
}