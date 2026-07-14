var cancellable = function(generator) {
    let cancel;
    const promise = new Promise((resolve, reject) => {
        cancel = () => step(null, true);

        function step(value, cancelled = false, isError = false) {
            try {
                const result = cancelled 
                    ? generator.throw("Cancelled")
                    : isError 
                        ? generator.throw(value)
                        : generator.next(value);
                
                if (result.done) {
                    resolve(result.value);
                } else {
                    result.value.then(
                        val => step(val),
                        err => step(err, false, true)
                    );
                }
            } catch(e) {
                reject(e);
            }
        }
        step();
    });

    return [cancel, promise];
};