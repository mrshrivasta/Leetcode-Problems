Array.prototype.groupBy = function(fn) {
    return this.reduce((result, item) => {
        const key = fn(item);
        (result[key] ??= []).push(item);
        return result;
    }, {});
};