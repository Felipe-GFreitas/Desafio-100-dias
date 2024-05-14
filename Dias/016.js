/* Exercicio feito em Jscript 
https://www.hackerrank.com/challenges/migratory-birds/problem
*/

function migratoryBirds(arr) {
    let passarosCont = {};

    for (let i = 1; i <= 5; i++) {
        passarosCont[i] = 0;
    }

    for (let passaro of arr) {
        passarosCont[passaro]++;
    }

    let maisPassaro = 1;
    for (let i = 2; i <= 5; i++) {
        if (passarosCont[i] > passarosCont[maisPassaro]) {
            maisPassaro = i;
        }
    }

    return maisPassaro;
}

// Teste de usos para verificar se esta saindo corretamente
const arr = [1, 4, 4, 4, 5, 3];
console.log(migratoryBirds(arr)); 
