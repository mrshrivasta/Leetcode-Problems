var promiseAll = function(functions) {
    return new Promise((resolve, reject) => {
        const results = [];
        let count = 0;
        functions.forEach((fn, i) => {
            fn().then(val => {
                results[i] = val;
                if (++count === functions.length) resolve(results);
            }).catch(reject);
        });
    });
};