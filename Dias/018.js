function average(arr) {
    const uniqueElements = new Set(arr);
    const sum = [...uniqueElements].reduce((acc, curr) => acc + curr, 0);
    const avg = sum / uniqueElements.size;
    return avg;
}
